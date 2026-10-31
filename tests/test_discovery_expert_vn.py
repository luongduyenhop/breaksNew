"""PR #5: search-first discovery, expert voices, VN/global balance."""
import os
import sys
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analyzers.summarizer import MarketBriefingSynthesizer, TOP_ITEMS_FOR_PROMPT
from src.collectors.rss_collector import RssCollector
from src.collectors.reddit_collector import RedditCollector
from src.collectors.youtube_collector import YouTubeCollector
from src.filters.relevance import RelevanceScorer, expert_voice_score
from src.models.raw_item import CommentItem, RawItem


def _item(**overrides):
    base = dict(
        id="x1", title="Tin IT", source_name="Test", source_type="article",
        url="https://example.com/x", published_at="", summary_text="",
        region="GLOBAL", metrics={}, top_comments=[],
    )
    base.update(overrides)
    return RawItem(**base)


class _Resp:
    def __init__(self, status=200, payload=None):
        self.status_code = status
        self._payload = payload or {}

    def json(self):
        return self._payload


class YouTubeSearchTests(unittest.TestCase):
    def _dispatch(self, url, params=None, timeout=None):
        if url.endswith("/search"):
            return _Resp(200, {"items": [
                {"id": {"videoId": "v1"}}, {"id": {"videoId": "v2"}},
            ]})
        if url.endswith("/videos"):
            return _Resp(200, {"items": [
                {"id": "v1",
                 "snippet": {"title": "Senior dev chia sẻ thị trường IT Việt Nam",
                             "channelTitle": "Kênh Lạ Mới", "publishedAt": "2026-10-31T01:00:00Z",
                             "description": "Nội dung về tuyển dụng"},
                 "statistics": {"viewCount": "9000", "likeCount": "120", "commentCount": "30"}},
                {"id": "v2",
                 "snippet": {"title": "Video phụ", "channelTitle": "Kênh Khác",
                             "publishedAt": "2026-10-31T02:00:00Z", "description": "khác"},
                 "statistics": {"viewCount": "50", "likeCount": "1", "commentCount": "0"}},
            ]})
        if url.endswith("/commentThreads"):
            return _Resp(200, {"items": [
                {"snippet": {"topLevelComment": {"snippet": {
                    "textDisplay": "Bình luận định hướng rất dài và có ích cho dev",
                    "authorDisplayName": "@senior", "likeCount": 42}}}},
            ]})
        raise AssertionError(f"unexpected URL {url}")

    def test_search_discovers_videos_beyond_fixed_channels(self):
        collector = YouTubeCollector(
            [], api_key="k",
            search_queries=[{"query": "thị trường IT", "region": "VN", "language": "vi"}],
        )
        with patch("src.collectors.youtube_collector.requests.get", side_effect=self._dispatch):
            items = collector.fetch_items()
        self.assertEqual(len(items), 2)
        top = items[0]
        self.assertEqual(top.region, "VN")
        self.assertIn("Kênh Lạ Mới", top.source_name)
        self.assertEqual(top.metrics["views"], 9000)
        self.assertTrue(top.top_comments)  # comments fetched for top-viewed

    def test_search_skipped_without_api_key(self):
        collector = YouTubeCollector(
            [], api_key="",
            search_queries=[{"query": "x", "region": "VN", "language": "vi"}],
        )
        self.assertEqual(collector.fetch_items(), [])


class GoogleNewsRssTests(unittest.TestCase):
    def test_url_builder(self):
        url = RssCollector.google_news_url(
            {"google_news_query": "thị trường IT", "hl": "vi", "gl": "VN", "ceid": "VN:vi"}
        )
        self.assertTrue(url.startswith("https://news.google.com/rss/search?q="))
        self.assertIn("hl=vi", url)
        self.assertIn("ceid=VN:vi", url)

    def test_title_publisher_stripped(self):
        self.assertEqual(
            RssCollector.clean_title("Sa thải hàng loạt tại công ty X - VnExpress", True),
            "Sa thải hàng loạt tại công ty X",
        )
        self.assertEqual(RssCollector.clean_title("Bài gốc - giữ nguyên", False), "Bài gốc - giữ nguyên")


class RedditSearchTests(unittest.TestCase):
    def test_search_blocked_falls_through(self):
        collector = RedditCollector([], keywords=[], search_queries=["senior advice"])
        with patch("src.collectors.reddit_collector.requests.get",
                   return_value=_Resp(403, {})):
            self.assertEqual(collector.fetch_items(), [])

    def test_search_success_collects_post(self):
        now = time.time()
        post = {
            "id": "p1", "title": "Senior engineer career advice thread",
            "selftext": "body", "created_utc": now, "stickied": False,
            "permalink": "/r/ExperiencedDevs/comments/p1/x/", "score": 50,
            "num_comments": 3,
        }

        def dispatch(url, headers=None, timeout=None):
            if "search.json" in url:
                return _Resp(200, {"data": {"children": [{"data": post}]}})
            return _Resp(200, [{"data": {"children": []}},
                               {"data": {"children": [{"data": {
                                   "body": "Lời khuyên từ kinh nghiệm nhiều năm đi làm ở team tôi",
                                   "score": 9, "author": "lead1"}}]}}])

        collector = RedditCollector([], keywords=[], search_queries=["senior engineer advice"])
        with patch("src.collectors.reddit_collector.requests.get", side_effect=dispatch):
            items = collector.fetch_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].source_name, "Reddit (Tìm kiếm toàn site)")


class ExpertAndRegionScoringTests(unittest.TestCase):
    def test_expert_voice_title_role(self):
        item = _item(title="Tech Lead chia sẻ: dev nên học gì lúc này")
        self.assertGreaterEqual(expert_voice_score(item), 6.0)

    def test_expert_voice_experience_phrases(self):
        item = _item(
            title="Thị trường tuyển dụng IT",
            summary_text="Sau nhiều năm đi làm, team của tôi nhận ra điều quan trọng.",
        )
        self.assertGreater(expert_voice_score(item), 0.0)

    def test_expert_voice_plain_news_is_zero(self):
        item = _item(title="Công ty X ra mắt sản phẩm mới", summary_text="Thông cáo báo chí.")
        self.assertEqual(expert_voice_score(item), 0.0)

    def test_vn_region_boost(self):
        scorer = RelevanceScorer()
        vn = scorer.score_item(_item(title="Thị trường tuyển dụng IT hôm nay", region="VN"))
        gl = scorer.score_item(_item(title="Thị trường tuyển dụng IT hôm nay", region="GLOBAL"))
        self.assertAlmostEqual(vn.relevance_score - gl.relevance_score, 4.0, places=1)
        self.assertIn("thị trường VN", vn.score_reason)


class VnQuotaSelectionTests(unittest.TestCase):
    def test_quota_guarantees_vn_floor(self):
        ranked = []
        for i in range(20):
            ranked.append(_item(id=f"g{i}", region="GLOBAL"))
            ranked[-1].relevance_score = 100.0 - i
        for i in range(10):
            ranked.append(_item(id=f"v{i}", region="VN"))
            ranked[-1].relevance_score = 70.0 - i
        synth = MarketBriefingSynthesizer.__new__(MarketBriefingSynthesizer)
        selected = synth._select_for_prompt(ranked)
        self.assertEqual(len(selected), TOP_ITEMS_FOR_PROMPT)
        vn_count = sum(1 for i in selected if i.region == "VN")
        self.assertGreaterEqual(vn_count, 8)


if __name__ == "__main__":
    unittest.main()
