import os
import unittest
from unittest.mock import patch, MagicMock

from src.filters.relevance import RelevanceScorer, fold_text
from src.models.raw_item import RawItem, CommentItem
from src.normalizers.data_normalizer import DataNormalizer
from src.publishers.markdown_to_docs import parse_markdown_blocks, build_docs_requests
from src.collectors.hackernews_collector import HackerNewsCollector


def make_item(title, summary="", source="Test", comments=None, score=0, published=""):
    return RawItem(
        id=f"item-{title[:10]}",
        title=title,
        source_name=source,
        source_type="article",
        url=f"https://example.com/{abs(hash(title))}",
        published_at=published,
        summary_text=summary,
        region="GLOBAL",
        metrics={"score": score, "comments": len(comments or [])},
        top_comments=comments or [],
    )


class TestFoldText(unittest.TestCase):
    def test_vietnamese_accents_folded(self):
        self.assertEqual(fold_text("Tuyển Dụng Thị Trường"), "tuyen dung thi truong")
        self.assertEqual(fold_text("Đào tạo"), "dao tao")


class TestRelevanceScorer(unittest.TestCase):
    def setUp(self):
        self.scorer = RelevanceScorer()

    def test_market_video_is_kept(self):
        item = make_item(
            "Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm sau?",
            summary="Thảo luận về thị trường việc làm IT và AI",
            comments=[CommentItem(author="dev1", text="Junior giờ khó xin việc lắm", votes=120)],
        )
        kept, dropped = self.scorer.score_and_filter([item])
        self.assertEqual(len(kept), 1)
        self.assertIn("thi_truong_tuyen_dung", kept[0].matched_topics)
        self.assertTrue(kept[0].score_reason)

    def test_pure_tutorial_is_dropped(self):
        item = make_item("Kafka (10): KAFKA 4.0 QUEUES & SHARE GROUPS",
                         summary="Kafka tutorial part 10")
        kept, dropped = self.scorer.score_and_filter([item])
        self.assertEqual(len(kept), 0)
        self.assertEqual(len(dropped), 1)

    def test_off_topic_news_is_dropped(self):
        item = make_item("Medicare Will Pay $50k for Your Heart Attack",
                         summary="US healthcare policy opinion")
        kept, _ = self.scorer.score_and_filter([item])
        self.assertEqual(len(kept), 0)

    def test_ai_direction_article_is_kept(self):
        item = make_item("AI isn't replacing SREs, it's deskilling them",
                         summary="How AI agents change the future of programming work",
                         score=180)
        kept, _ = self.scorer.score_and_filter([item])
        self.assertEqual(len(kept), 1)
        self.assertIn("ai_va_huong_di_moi", kept[0].matched_topics)

    def test_series_tutorial_with_weak_topic_is_dropped(self):
        # Title matches 'vibe coding' but it is a course-series episode,
        # not a market viewpoint — the series penalty pushes it out.
        item = make_item("Vibe Coding Course | Series Gemini AI For Beginners",
                         summary="lesson content")
        kept, _ = self.scorer.score_and_filter([item])
        self.assertEqual(len(kept), 0)

    def test_singular_tech_job_title_is_kept(self):
        item = make_item("Looking for a tech job is a helpless data-entry nightmare",
                         summary="The job market for developers right now", score=120)
        kept, _ = self.scorer.score_and_filter([item])
        self.assertEqual(len(kept), 1)

    def test_salary_keyword_does_not_match_luong_flow(self):
        # 'lương' (salary) folded is 'luong', which also matches 'luồng'
        # (workflow) — the scorer must not treat workflow text as salary.
        item = make_item("Quy trình làm việc hiệu quả",
                         summary="Cách tổ chức luồng công việc cho team")
        kept, _ = self.scorer.score_and_filter([item])
        self.assertEqual(len(kept), 0)

    def test_per_source_cap_applies(self):
        items = [
            make_item(f"Tech layoff wave part {i}", source="SameSource", score=50)
            for i in range(8)
        ]
        kept, dropped = self.scorer.score_and_filter(items)
        self.assertEqual(len(kept), 6)  # default per_source_cap
        self.assertEqual(len(dropped), 2)

    def test_kept_items_sorted_by_score(self):
        low = make_item("Junior dev notes", summary="career advice")
        high = make_item(
            "Massive tech layoff and hiring freeze in the job market",
            summary="layoff hiring salary job market",
            comments=[CommentItem(author="a", text="layoff everywhere", votes=10)],
            score=500,
        )
        kept, _ = self.scorer.score_and_filter([low, high])
        self.assertEqual(kept[0].title, high.title)


class TestBoilerplateStrip(unittest.TestCase):
    def test_youtube_description_boilerplate_removed(self):
        normalizer = DataNormalizer()
        raw = (
            "Thị trường IT đang thay đổi vì AI agent.\n"
            "👉 Link Discord: https://discord.gg/abc\n"
            "HOT HOT Link Member backend NESTJS: Tham gia làm hội viên\n"
            "Nhiều junior mất việc vì đóng băng tuyển dụng."
        )
        cleaned = normalizer.strip_boilerplate(raw)
        self.assertIn("Thị trường IT", cleaned)
        self.assertIn("mất việc", cleaned)
        self.assertNotIn("Discord", cleaned)
        self.assertNotIn("hội viên", cleaned)


class TestMarkdownToDocs(unittest.TestCase):
    MD = "# Title\n\n## Section\n\n- **Bold point** and [a link](https://example.com)\n\n> quoted line\n\nPlain text."

    def test_blocks_parsed_with_styles(self):
        blocks = parse_markdown_blocks(self.MD)
        self.assertEqual(blocks[0]["named_style"], "TITLE")
        self.assertEqual(blocks[1]["named_style"], "HEADING_1")
        self.assertTrue(blocks[2]["bullet"])
        self.assertEqual(blocks[2]["text"], "Bold point and a link")
        span_kinds = {("bold" in s, "link_url" in s) for s in blocks[2]["spans"]}
        self.assertIn((True, False), span_kinds)
        self.assertIn((False, True), span_kinds)
        self.assertEqual(blocks[3]["text"], "quoted line")

    def test_requests_cover_full_text(self):
        built = build_docs_requests(self.MD, start_index=1)
        insert = built["requests"][0]["insertText"]
        self.assertEqual(insert["text"], built["full_text"])
        self.assertNotIn("#", built["full_text"])
        self.assertNotIn("**", built["full_text"])
        style_requests = [r for r in built["requests"] if "updateParagraphStyle" in r]
        self.assertEqual(len(style_requests), 2)  # TITLE + HEADING_1
        bullet_requests = [r for r in built["requests"] if "createParagraphBullets" in r]
        self.assertEqual(len(bullet_requests), 1)
        text_styles = [r for r in built["requests"] if "updateTextStyle" in r]
        # bold span + link span + quote italic span
        self.assertEqual(len(text_styles), 3)
        for r in text_styles:
            rng = r["updateTextStyle"]["range"]
            self.assertLess(rng["startIndex"], rng["endIndex"])
            self.assertLessEqual(rng["endIndex"], 1 + len(built["full_text"]))


class TestHackerNewsSearch(unittest.TestCase):
    @patch("requests.get")
    def test_algolia_search_parses_hits_and_comments(self, mock_get):
        search_resp = MagicMock()
        search_resp.status_code = 200
        search_resp.json.return_value = {
            "hits": [{
                "objectID": "777",
                "title": "Tech layoff trends in 2026",
                "url": "https://example.com/layoffs",
                "points": 210,
                "num_comments": 95,
                "created_at_i": 9999999999,
                "story_text": "Hiring freeze discussion",
            }]
        }
        item_resp = MagicMock()
        item_resp.status_code = 200
        item_resp.json.return_value = {
            "children": [
                {"author": "pg_fan", "text": "Short"},
                {"author": "senior_dev", "text": "A much longer substantive comment about the hiring market"},
            ]
        }
        mock_get.side_effect = [search_resp, item_resp]

        collector = HackerNewsCollector(limit=10, queries=["tech layoff"])
        items = collector.fetch_items()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "Tech layoff trends in 2026")
        self.assertEqual(items[0].metrics["score"], 210)
        # Longest (most substantive) comment ranked first; "Short" (<15 chars body rule) excluded
        self.assertEqual(len(items[0].top_comments), 1)
        self.assertEqual(items[0].top_comments[0].author, "senior_dev")
        self.assertEqual(items[0].top_comments[0].votes, 0)  # HN exposes no comment votes


class TestSummarizerFallback(unittest.TestCase):
    def test_fallback_warns_and_ranks_by_score(self):
        from src.analyzers.summarizer import MarketBriefingSynthesizer

        with patch.dict(os.environ, {}, clear=True):
            synth = MarketBriefingSynthesizer()
        low = make_item("Junior career advice", summary="career")
        low.relevance_score = 30
        low.matched_topics = ["career_survival"]
        low.score_reason = "test"
        high = make_item("Big layoff analysis", summary="layoff")
        high.relevance_score = 90
        high.matched_topics = ["thi_truong_tuyen_dung"]
        high.score_reason = "test"

        report = synth.analyze_and_synthesize([low, high])
        self.assertTrue(synth.used_fallback)
        self.assertIn("Cảnh báo", report)
        self.assertLess(report.index("Big layoff analysis"), report.index("Junior career advice"))


if __name__ == "__main__":
    unittest.main()
