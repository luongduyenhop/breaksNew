import unittest
from src.normalizers.data_normalizer import DataNormalizer
from src.models.raw_item import RawItem, CommentItem

class TestDataNormalizer(unittest.TestCase):
    def setUp(self):
        self.normalizer = DataNormalizer()

    def test_clean_text_removes_html_and_spaces(self):
        raw = "<p>Hello <b>World</b>!   Line break \n\t test</p>"
        cleaned = self.normalizer.clean_text(raw)
        self.assertEqual(cleaned, "Hello World! Line break test")

    def test_clean_url_strips_tracking_params(self):
        url = "https://example.com/post?utm_source=facebook&utm_medium=cpc&id=123&fbclid=abcdef"
        cleaned = self.normalizer.clean_url(url)
        self.assertEqual(cleaned, "https://example.com/post?id=123")

    def test_deduplicate_and_normalize(self):
        items = [
            RawItem(
                id="item1",
                title="AI In 2026",
                source_name="Dev.to",
                source_type="article",
                url="https://example.com/article1?utm_source=rss",
                published_at="2026-10-30",
                summary_text="<p>Summary with <b>tags</b></p>",
                region="GLOBAL",
                metrics={"score": 10, "comments": 2},
                top_comments=[CommentItem(author="Alex", text="<p>Great insight!</p>", votes=50)]
            ),
            RawItem(
                id="item2",
                title="ai in 2026",
                source_name="Dev.to",
                source_type="article",
                url="https://example.com/article1",
                published_at="2026-10-30",
                summary_text="Duplicate title and url",
                region="GLOBAL",
                metrics={"score": 5, "comments": 1}
            )
        ]
        result = self.normalizer.deduplicate_and_normalize(items)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "AI In 2026")
        self.assertEqual(result[0].summary_text, "Summary with tags")
        self.assertEqual(result[0].url, "https://example.com/article1")
        self.assertEqual(len(result[0].top_comments), 1)
        self.assertEqual(result[0].top_comments[0].text, "Great insight!")

if __name__ == "__main__":
    unittest.main()
