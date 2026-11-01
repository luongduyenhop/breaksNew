"""Facebook groups: data-file collector, community lane gate, prompt cap."""
import json
import os
import sys
import tempfile
import time
import unittest
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analyzers.summarizer import COMMUNITY_PROMPT_MAX, MarketBriefingSynthesizer
from src.collectors.facebook_collector import FacebookCollector
from src.filters.relevance import (
    COMMUNITY_TOPIC,
    RelevanceScorer,
    community_gate_passed,
    community_quality_score,
    is_community_only,
)
from src.models.raw_item import CommentItem, RawItem


def iso_now(offset_seconds: float = 0) -> str:
    # No fractional seconds: the scorer's published_at parser (shared
    # with every other collector) does not accept them.
    return datetime.fromtimestamp(
        time.time() + offset_seconds, tz=timezone.utc
    ).replace(microsecond=0).isoformat()


def make_fb_item(summary="", title="Bài viết cộng đồng", reactions=0,
                 comments=0, published_at="", top_comments=None):
    return RawItem(
        id="fb-test",
        title=title,
        source_name="Facebook · Vietnam Java User Group",
        source_type="facebook",
        url="https://facebook.com/groups/vnjug/permalink/1/",
        published_at=published_at,
        summary_text=summary,
        region="VN",
        metrics={"reactions": reactions, "comments": comments},
        top_comments=top_comments or [],
    )


def filler(chars: int) -> str:
    """Neutral filler text with no topic keywords."""
    return ("noi dung bai viet " * (chars // 18 + 1))[:chars]


class CollectorTests(unittest.TestCase):
    def _write_data_file(self, payload) -> str:
        handle = tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        )
        if isinstance(payload, str):
            handle.write(payload)
        else:
            json.dump(payload, handle, ensure_ascii=False)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def _record(self, post_id, published_at, content="x" * 900, **overrides):
        record = {
            "id": post_id,
            "group_id": "vnjug",
            "group_name": "Vietnam Java User Group",
            "title": "Tiêu đề bài viết",
            "content": content,
            "url": f"https://facebook.com/groups/vnjug/permalink/{post_id}/",
            "published_at": published_at,
            "reactions": 42,
            "comments_count": 3,
            "top_comments": [
                {"author": "Facebook user", "text": "Bình luận hay", "votes": 0}
            ],
        }
        record.update(overrides)
        return record

    def test_parses_dedupes_and_filters_age(self):
        fresh = iso_now(-3600)
        old = iso_now(-10 * 24 * 3600)
        path = self._write_data_file({"generated_at": fresh, "items": [
            self._record("111", fresh, content="y" * 3500),
            self._record("111", fresh),  # duplicate id — dropped
            self._record("222", old),    # older than max_age_days — dropped
            self._record("333", fresh),
        ]})
        collector = FacebookCollector(data_file=path, max_age_days=3)
        items = collector.fetch_items()
        self.assertEqual([i.id for i in items], ["fb_111", "fb_333"])
        item = items[0]
        self.assertEqual(item.source_name, "Facebook · Vietnam Java User Group")
        self.assertEqual(item.source_type, "facebook")
        self.assertEqual(item.region, "VN")
        self.assertEqual(len(item.summary_text), 3000)  # truncated
        self.assertEqual(item.metrics, {"reactions": 42, "comments": 3})
        self.assertEqual(len(item.top_comments), 1)
        self.assertIsInstance(item.top_comments[0], CommentItem)
        self.assertEqual(item.top_comments[0].text, "Bình luận hay")

    def test_missing_file_returns_empty(self):
        collector = FacebookCollector(
            data_file="/tmp/definitely-not-here-fb.json", max_age_days=3
        )
        self.assertEqual(collector.fetch_items(), [])

    def test_corrupt_file_returns_empty(self):
        path = self._write_data_file("{not valid json")
        collector = FacebookCollector(data_file=path, max_age_days=3)
        self.assertEqual(collector.fetch_items(), [])


class CommunityGateTests(unittest.TestCase):
    def test_spring_ai_style_long_post_passes(self):
        # The real VNJUG Spring AI post: ~23k chars (3000 after the
        # collector's truncation), moderate engagement.
        item = make_fb_item(summary=filler(3000), reactions=35, comments=3)
        self.assertEqual(community_quality_score(item), 11.0)  # 8 + 3
        self.assertTrue(community_gate_passed(item))

    def test_system_design_style_long_low_engagement_passes(self):
        # Slow group: very long substance, almost no reactions — the
        # len >= 1200 branch of the gate exists for exactly this case.
        item = make_fb_item(summary=filler(1300), reactions=6, comments=2)
        self.assertEqual(community_quality_score(item), 5.0)  # 4 + 1
        self.assertTrue(community_gate_passed(item))

    def test_meme_fails_gate(self):
        item = make_fb_item(summary="Thật là kì lạ 🧐!", reactions=55, comments=6)
        self.assertFalse(community_gate_passed(item))

    def test_empty_post_fails_gate(self):
        item = make_fb_item(summary="", reactions=100, comments=10)
        self.assertFalse(community_gate_passed(item))

    def test_short_tip_fails_gate(self):
        item = make_fb_item(summary=filler(490), reactions=19, comments=0)
        self.assertEqual(community_quality_score(item), 2.0)  # 1 + 1
        self.assertFalse(community_gate_passed(item))

    def test_lane_only_applies_to_facebook(self):
        item = make_fb_item(summary=filler(3000), reactions=100, comments=10)
        item.source_type = "article"
        self.assertEqual(community_quality_score(item), 0.0)
        self.assertFalse(community_gate_passed(item))


class ScorerIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.scorer = RelevanceScorer()

    def test_gate_passing_item_clears_threshold(self):
        item = make_fb_item(
            summary=filler(3000), reactions=35, comments=3,
            published_at=iso_now(-600),
        )
        kept, dropped = self.scorer.score_and_filter([item])
        self.assertIn(COMMUNITY_TOPIC, item.matched_topics)
        self.assertGreaterEqual(item.relevance_score, 25)
        self.assertEqual(kept, [item])
        self.assertEqual(dropped, [])

    def test_gate_and_topic_can_stack(self):
        summary = filler(2000) + " lời khuyên cho junior mới vào nghề"
        item = make_fb_item(
            summary=summary, reactions=40, comments=2, published_at=iso_now(-600)
        )
        self.scorer.score_item(item)
        self.assertIn(COMMUNITY_TOPIC, item.matched_topics)
        self.assertIn("career_survival", item.matched_topics)
        self.assertFalse(is_community_only(item))

    def test_meme_dropped_despite_engagement(self):
        item = make_fb_item(
            summary="Thật là kì lạ 🧐!", reactions=55, comments=6,
            published_at=iso_now(-600),
        )
        kept, dropped = self.scorer.score_and_filter([item])
        self.assertNotIn(COMMUNITY_TOPIC, item.matched_topics)
        self.assertEqual(kept, [])
        self.assertEqual(dropped, [item])


def make_scored_item(title, score, topics, region="VN"):
    item = RawItem(
        id=f"item-{abs(hash(title))}",
        title=title,
        source_name="Test",
        source_type="facebook" if topics == [COMMUNITY_TOPIC] else "article",
        url=f"https://example.com/{abs(hash(title))}",
        published_at="",
        summary_text="",
        region=region,
        metrics={"reactions": 10, "comments": 0},
        top_comments=[],
    )
    item.relevance_score = score
    item.matched_topics = topics
    return item


class CommunityCapTests(unittest.TestCase):
    def test_community_only_items_capped_in_prompt_selection(self):
        synth = MarketBriefingSynthesizer(api_key=None)
        community = [
            make_scored_item(f"Community post {n}", 90 - n, [COMMUNITY_TOPIC])
            for n in range(6)
        ]
        normals = [
            make_scored_item(f"Career item {n}", 80 - n, ["career_survival"])
            for n in range(20)
        ]
        ranked = sorted(community + normals,
                        key=lambda i: i.relevance_score, reverse=True)
        selected = synth._select_for_prompt(ranked)
        self.assertLessEqual(
            sum(1 for i in selected if is_community_only(i)),
            COMMUNITY_PROMPT_MAX,
        )
        self.assertEqual(len(selected), 20)

    def test_mixed_topic_items_are_not_community_only(self):
        item = make_scored_item(
            "Mixed", 50, [COMMUNITY_TOPIC, "career_survival"]
        )
        self.assertFalse(is_community_only(item))


if __name__ == "__main__":
    unittest.main()
