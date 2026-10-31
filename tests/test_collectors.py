import unittest
from unittest.mock import patch, MagicMock
from src.collectors.hackernews_collector import HackerNewsCollector
from src.collectors.reddit_collector import RedditCollector
from src.collectors.rss_collector import RssCollector

class TestCollectors(unittest.TestCase):
    @patch("requests.get")
    def test_hackernews_collector_parses_stories(self, mock_get):
        stories_response = MagicMock()
        stories_response.status_code = 200
        stories_response.json.return_value = [101]

        story_item_response = MagicMock()
        story_item_response.status_code = 200
        story_item_response.json.return_value = {
            "id": 101,
            "type": "story",
            "time": 9999999999,
            "title": "Tech Layoff Trends",
            "url": "https://news.ycombinator.com/item?id=101",
            "score": 150,
            "descendants": 45
        }

        mock_get.side_effect = [stories_response, story_item_response]

        collector = HackerNewsCollector(limit=1)
        items = collector.fetch_items()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "Tech Layoff Trends")
        self.assertEqual(items[0].source_name, "Hacker News")
        self.assertEqual(items[0].region, "GLOBAL")

    @patch("requests.get")
    def test_reddit_collector_parses_posts(self, mock_get):
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {
            "data": {
                "children": [
                    {
                        "data": {
                            "id": "abc12",
                            "title": "How to survive as senior engineer in 2026",
                            "permalink": "/r/ExperiencedDevs/comments/abc12",
                            "created_utc": 9999999999,
                            "stickied": False,
                            "selftext": "Key thoughts on survival",
                            "score": 300,
                            "num_comments": 80
                        }
                    }
                ]
            }
        }
        mock_get.return_value = response

        collector = RedditCollector(["ExperiencedDevs"])
        items = collector.fetch_items()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "How to survive as senior engineer in 2026")
        self.assertEqual(items[0].source_name, "Reddit r/ExperiencedDevs")

    @patch("feedparser.parse")
    def test_rss_collector_parses_feed(self, mock_parse):
        entry = MagicMock()
        entry.id = "post-99"
        entry.title = "Chia sẻ kinh nghiệm phỏng vấn IT"
        entry.link = "https://viblo.asia/p/chia-se"
        entry.summary = "Kinh nghiệm thực chiến"
        entry.published = "2026-10-30"

        feed_mock = MagicMock()
        feed_mock.entries = [entry]
        mock_parse.return_value = feed_mock

        collector = RssCollector([{"name": "Viblo", "url": "https://viblo.asia/feed.rss", "region": "VN"}])
        items = collector.fetch_items()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].region, "VN")
        self.assertEqual(items[0].title, "Chia sẻ kinh nghiệm phỏng vấn IT")

if __name__ == "__main__":
    unittest.main()
