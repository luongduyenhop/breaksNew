"""PR #10 freshness-first: hourly recency gradient, tie-breaks, dual-order YouTube search."""
import os
import sys
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.collectors.youtube_collector import YouTubeCollector
from src.filters.relevance import RelevanceScorer, freshness_bonus
from src.models.raw_item import RawItem

NOW = 1_800_000_000.0  # fixed reference instant


def _item(age_hours, item_id="x"):
    return RawItem(
        id=item_id, title="Thị trường IT Việt Nam tuyển dụng lập trình viên",
        source_name="Test", source_type="article", url="https://example.com/x",
        published_at=str(int(NOW - age_hours * 3600)),
        summary_text="Nội dung về thị trường IT và tuyển dụng.",
        region="GLOBAL", metrics={}, top_comments=[],
    )


class FreshnessBonusTests(unittest.TestCase):
    def test_tiers(self):
        self.assertEqual(freshness_bonus(1), 12.0)
        self.assertEqual(freshness_bonus(5), 10.0)
        self.assertEqual(freshness_bonus(10), 8.0)
        self.assertEqual(freshness_bonus(20), 6.0)
        self.assertEqual(freshness_bonus(40), 4.0)
        self.assertEqual(freshness_bonus(60), 2.0)
        self.assertEqual(freshness_bonus(100), 1.0)
        self.assertEqual(freshness_bonus(300), 0.0)
        self.assertEqual(freshness_bonus(800), -10.0)
        self.assertEqual(freshness_bonus(None), 0.0)

    def test_fresher_item_scores_higher_same_content(self):
        scorer = RelevanceScorer()
        fresh = scorer.score_item(_item(1, "fresh"), now_ts=NOW)
        day_old = scorer.score_item(_item(30, "day"), now_ts=NOW)
        week_old = scorer.score_item(_item(300, "week"), now_ts=NOW)
        self.assertGreater(fresh.relevance_score, day_old.relevance_score)
        self.assertGreater(day_old.relevance_score, week_old.relevance_score)
        self.assertAlmostEqual(
            fresh.relevance_score - day_old.relevance_score, 12.0 - 4.0, places=1
        )
        self.assertIn("độ mới", fresh.score_reason)

    def test_equal_scores_newer_first(self):
        scorer = RelevanceScorer()
        older = _item(100, "older")
        newer = _item(90, "newer")  # same freshness tier (+1) => equal score
        kept, _ = scorer.score_and_filter([older, newer])
        ids = [i.id for i in kept]
        self.assertLess(ids.index("newer"), ids.index("older"))


class _Resp:
    def __init__(self, status=200, payload=None):
        self.status_code = status
        self._payload = payload or {}

    def json(self):
        return self._payload


class YouTubeDualOrderTests(unittest.TestCase):
    def test_search_runs_date_and_viewcount_passes_and_dedupes(self):
        orders_seen = []

        def dispatch(url, params=None, timeout=None):
            if url.endswith("/search"):
                orders_seen.append(params.get("order"))
                return _Resp(200, {"items": [{"id": {"videoId": "v1"}}]})
            if url.endswith("/videos"):
                return _Resp(200, {"items": [{
                    "id": "v1",
                    "snippet": {"title": "Thị trường IT Việt Nam mới nhất",
                                "channelTitle": "Kênh Test",
                                "publishedAt": "2026-11-01T00:00:00Z",
                                "description": "mô tả"},
                    "statistics": {"viewCount": "100", "likeCount": "5"},
                }]})
            if url.endswith("/commentThreads"):
                return _Resp(200, {"items": []})
            raise AssertionError(f"unexpected URL {url}")

        collector = YouTubeCollector(
            [], api_key="k",
            search_queries=[{"query": "thị trường IT", "region": "VN", "language": "vi"}],
        )
        with patch("src.collectors.youtube_collector.requests.get", side_effect=dispatch):
            items = collector.fetch_items()
        self.assertEqual(orders_seen, ["date", "viewCount"])
        self.assertEqual(len(items), 1)  # same video from both passes, deduped


if __name__ == "__main__":
    unittest.main()
