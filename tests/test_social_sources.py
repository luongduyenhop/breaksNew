"""PR #11: Lobsters, Lemmy, Mastodon, dev.to collectors + config wiring."""
import json
import os
import sys
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.collectors.devto_collector import DevToCollector
from src.collectors.lemmy_collector import LemmyCollector
from src.collectors.lobsters_collector import LobstersCollector
from src.collectors.mastodon_collector import MastodonCollector


def _iso_age_hours(hours):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - hours * 3600))


class _Resp:
    def __init__(self, status=200, payload=None):
        self.status_code = status
        self._payload = payload if payload is not None else {}

    def json(self):
        return self._payload


class LobstersTests(unittest.TestCase):
    def test_parse_and_age_filter(self):
        payload = [
            {"short_id": "a1", "title": "AI developer tools discussion",
             "url": "https://example.com/a", "created_at": _iso_age_hours(2),
             "score": 12, "comment_count": 30, "description_plain": "body",
             "submitter_user": {"username": "dev1"}},
            {"short_id": "a2", "title": "Old post",
             "url": "https://example.com/b", "created_at": _iso_age_hours(24 * 9),
             "score": 99, "comment_count": 99, "description_plain": "",
             "submitter_user": {"username": "dev2"}},
        ]
        with patch("src.collectors.lobsters_collector.requests.get",
                   return_value=_Resp(200, payload)):
            items = LobstersCollector(max_age_days=3).fetch_items()
        self.assertEqual(len(items), 1)  # two feeds dedupe + old dropped
        self.assertEqual(items[0].source_name, "Lobsters")
        self.assertEqual(items[0].metrics["comments"], 30)

    def test_fail_soft_on_http_error(self):
        with patch("src.collectors.lobsters_collector.requests.get",
                   return_value=_Resp(503)):
            self.assertEqual(LobstersCollector().fetch_items(), [])


class LemmyTests(unittest.TestCase):
    def test_parse_search_results(self):
        payload = {"posts": [{
            "post": {"id": 7, "name": "AI layoffs hit developer hiring",
                     "url": "https://example.com/post", "body": "discussion body",
                     "published": _iso_age_hours(5)},
            "counts": {"score": 42, "comments": 13},
        }]}
        with patch("src.collectors.lemmy_collector.requests.get",
                   return_value=_Resp(200, payload)):
            items = LemmyCollector(queries=["AI layoffs"], max_age_days=3).fetch_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].metrics["score"], 42)
        self.assertIn("programming.dev", items[0].source_name)

    def test_no_queries_no_calls(self):
        with patch("src.collectors.lemmy_collector.requests.get") as get:
            self.assertEqual(LemmyCollector(queries=[]).fetch_items(), [])
        get.assert_not_called()


class MastodonTests(unittest.TestCase):
    def test_html_stripped_and_reblogs_skipped(self):
        payload = [
            {"id": "1", "content": "<p>Senior devs on AI replacing junior hiring pipelines</p>",
             "created_at": _iso_age_hours(1), "language": "en", "reblog": None,
             "url": "https://hachyderm.io/@a/1", "favourites_count": 9,
             "reblogs_count": 2, "replies_count": 4,
             "account": {"display_name": "A", "username": "a"}},
            {"id": "2", "content": "<p>boosted</p>", "created_at": _iso_age_hours(1),
             "language": "en", "reblog": {"id": "x"}, "url": "https://hachyderm.io/@b/2",
             "favourites_count": 1, "reblogs_count": 0, "replies_count": 0,
             "account": {"display_name": "B", "username": "b"}},
        ]
        with patch("src.collectors.mastodon_collector.requests.get",
                   return_value=_Resp(200, payload)):
            items = MastodonCollector(hashtags=["ai"], max_age_days=3).fetch_items()
        self.assertEqual(len(items), 1)
        self.assertNotIn("<p>", items[0].summary_text)
        self.assertEqual(items[0].source_type, "post")


class DevToTests(unittest.TestCase):
    def test_parse_articles(self):
        payload = [{
            "id": 5, "title": "Career advice for developers in the AI era",
            "description": "desc", "url": "https://dev.to/x",
            "published_at": _iso_age_hours(3),
            "public_reactions_count": 120, "comments_count": 18,
        }]
        with patch("src.collectors.devto_collector.requests.get",
                   return_value=_Resp(200, payload)):
            items = DevToCollector(tags=["career"], max_age_days=3).fetch_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].metrics["reactions"], 120)


class ConfigTests(unittest.TestCase):
    def test_sources_config_has_new_sources(self):
        cfg = json.load(open(os.path.join(
            os.path.dirname(__file__), "..", "config", "sources.json")))
        urls = {f["name"]: f["url"] for f in cfg["rss_feeds"] if "url" in f}
        self.assertEqual(urls["Viblo"], "https://viblo.asia/rss")
        self.assertIn("Tuổi Trẻ · Công nghệ", urls)
        self.assertTrue(cfg["mastodon_hashtags"])
        self.assertTrue(cfg["devto_tags"])


if __name__ == "__main__":
    unittest.main()
