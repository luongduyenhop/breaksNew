import unittest
from types import SimpleNamespace
from unittest.mock import patch, MagicMock

from src.collectors.youtube_collector import YouTubeCollector
from src.filters.relevance import (
    RelevanceScorer,
    comment_insight_score,
    rank_comments,
)
from src.models.raw_item import RawItem, CommentItem
from src.normalizers.data_normalizer import DataNormalizer

LONG_DIRECTION_COMMENT = (
    "Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae "
    "tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó, kĩ năng đó hình thành từ "
    "nhiều năm đi làm. Chuyện lập trình viên không cần code là chuyện trước mặt "
    "rồi, không phải tương lai nữa, thế nên ae nên tập trung vào việc hiểu "
    "business + hệ thống + kĩ năng làm việc với mọi người xung quanh, tranh thủ "
    "thời gian tự nâng cấp bản thân đi."
)


def make_item(title, comments=None, summary=""):
    return RawItem(
        id="x1", title=title, source_name="YouTube (Test)", source_type="video",
        url="https://youtube.com/watch?v=x1", published_at="", summary_text=summary,
        region="VN", metrics={"views": 0, "comments": len(comments or [])},
        top_comments=comments or [],
    )


class TestYouTubeDataApiComments(unittest.TestCase):
    def _api_response(self, payload):
        resp = MagicMock()
        resp.status_code = 200
        resp.json.return_value = payload
        return resp

    @patch("src.collectors.youtube_collector.requests.get")
    def test_comments_via_api_sorted_by_likes(self, mock_get):
        mock_get.return_value = self._api_response({
            "items": [
                {"snippet": {"topLevelComment": {"snippet": {
                    "authorDisplayName": "dev A",
                    "textDisplay": "Bình luận ít like nhưng cũng dài vừa đủ",
                    "likeCount": 3,
                }}}},
                {"snippet": {"topLevelComment": {"snippet": {
                    "authorDisplayName": "dev B",
                    "textDisplay": LONG_DIRECTION_COMMENT,
                    "likeCount": 250,
                }}}},
            ]
        })
        collector = YouTubeCollector([], api_key="test-key")
        comments = collector._get_comments_via_api("abc123", limit=5)
        self.assertEqual(len(comments), 2)
        self.assertEqual(comments[0].author, "dev B")
        self.assertEqual(comments[0].votes, 250)
        self.assertGreater(len(comments[0].text), 300)  # not truncated at 300

    @patch("src.collectors.youtube_collector.requests.get")
    def test_video_stats_via_api(self, mock_get):
        mock_get.return_value = self._api_response({
            "items": [{"statistics": {"viewCount": "12345", "likeCount": "678", "commentCount": "90"}}]
        })
        collector = YouTubeCollector([], api_key="test-key")
        stats = collector._get_video_stats("abc123")
        self.assertEqual(stats, {"views": 12345, "likes": 678, "comments": 90})

    @patch("src.collectors.youtube_collector.YouTubeCollector._get_transcript", return_value="")
    @patch("src.collectors.youtube_collector.feedparser.parse")
    @patch("src.collectors.youtube_collector.requests.get")
    def test_fetch_items_uses_api_when_key_present(self, mock_get, mock_parse, _mock_tr):
        entry = SimpleNamespace(
            yt_videoid="vid1", title="Dev có mất việc vì AI không?",
            summary="desc", published="Sat, 31 Oct 2026 10:00:00 GMT",
            link="https://youtube.com/watch?v=vid1",
        )
        mock_parse.return_value = SimpleNamespace(entries=[entry])

        comments_resp = self._api_response({
            "items": [{"snippet": {"topLevelComment": {"snippet": {
                "authorDisplayName": "senior dev",
                "textDisplay": LONG_DIRECTION_COMMENT,
                "likeCount": 99,
            }}}}]
        })
        stats_resp = self._api_response({
            "items": [{"statistics": {"viewCount": "1000", "likeCount": "50", "commentCount": "7"}}]
        })
        mock_get.side_effect = [comments_resp, stats_resp]

        collector = YouTubeCollector(
            [{"id": "chan1", "name": "Tips", "region": "VN"}], api_key="test-key"
        )
        items = collector.fetch_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(len(items[0].top_comments), 1)
        self.assertEqual(items[0].top_comments[0].votes, 99)
        self.assertEqual(items[0].metrics["views"], 1000)


class TestInsightScoring(unittest.TestCase):
    def test_directional_comment_scores_high(self):
        self.assertGreaterEqual(comment_insight_score(LONG_DIRECTION_COMMENT), 8)

    def test_reaction_comment_scores_low(self):
        self.assertLess(comment_insight_score("Hay quá anh ơi, cảm ơn anh nhiều nhé"), 3)

    def test_rank_comments_prefers_insight_over_raw_votes(self):
        punchy = CommentItem(author="a", text=LONG_DIRECTION_COMMENT, votes=10)
        popular = CommentItem(author="b", text="Video hay quá, cảm ơn kênh rất nhiều", votes=500)
        ranked = rank_comments([popular, punchy])
        self.assertEqual(ranked[0].author, "a")

    def test_insight_comment_boosts_item_score(self):
        scorer = RelevanceScorer()
        plain = make_item("Lập trình viên có mất việc vì AI không?")
        with_insight = make_item(
            "Lập trình viên có mất việc vì AI không?",
            comments=[CommentItem(author="s", text=LONG_DIRECTION_COMMENT, votes=42)],
        )
        scorer.score_item(plain)
        scorer.score_item(with_insight)
        self.assertGreater(with_insight.relevance_score, plain.relevance_score)


class TestLongCommentNormalization(unittest.TestCase):
    def test_comment_kept_up_to_700_chars(self):
        normalizer = DataNormalizer()
        item = make_item(
            "Video về thị trường",
            comments=[CommentItem(author="s", text="x" * 650, votes=1)],
        )
        result = normalizer.deduplicate_and_normalize([item])
        self.assertEqual(len(result[0].top_comments[0].text), 650)


class TestFallbackDirectionReport(unittest.TestCase):
    def test_fallback_leads_with_directional_comments(self):
        import os
        from src.analyzers.summarizer import MarketBriefingSynthesizer

        with patch.dict(os.environ, {}, clear=True):
            synth = MarketBriefingSynthesizer()
        item = make_item(
            "Lập trình viên có mất việc vì AI không?",
            comments=[CommentItem(author="senior", text=LONG_DIRECTION_COMMENT, votes=88)],
            summary="Thảo luận về tương lai nghề dev",
        )
        item.relevance_score = 60
        item.matched_topics = ["ai_va_huong_di_moi"]
        item.score_reason = "test"
        report = synth.analyze_and_synthesize([item])
        self.assertIn("BÌNH LUẬN ĐỊNH HƯỚNG NỔI BẬT", report)
        self.assertIn("hiểu", report)
        # Directional comments section appears before the source listing
        self.assertLess(
            report.index("BÌNH LUẬN ĐỊNH HƯỚNG NỔI BẬT"),
            report.index("NGUỒN ĐÃ LỌC"),
        )


if __name__ == "__main__":
    unittest.main()
