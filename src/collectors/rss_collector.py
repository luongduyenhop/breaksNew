import calendar
import time
from typing import List, Dict
import feedparser
from src.models.raw_item import RawItem


class RssCollector:
    """RSS articles with a real publication-date window.

    The old version took the 8 newest entries of each feed regardless of
    age. Now entries older than `max_age_days` (when the feed provides a
    parseable date) are skipped, and a larger pool is collected so the
    relevance scorer has something to choose from.
    """

    def __init__(self, feeds: List[Dict[str, str]], pool_per_feed: int = 12,
                 max_age_days: int = 7):
        self.feeds = feeds
        self.pool_per_feed = pool_per_feed
        self.max_age_days = max_age_days

    def _is_fresh_enough(self, entry) -> bool:
        published_parsed = getattr(entry, "published_parsed", None)
        # Only trust a real struct_time (feedparser) — anything else
        # (missing dates, test doubles) is kept rather than dropped.
        if not isinstance(published_parsed, time.struct_time):
            return True
        published_ts = calendar.timegm(published_parsed)
        return published_ts >= time.time() - self.max_age_days * 24 * 3600

    def fetch_items(self) -> List[RawItem]:
        items: List[RawItem] = []
        for feed_config in self.feeds:
            feed_url = feed_config.get("url", "")
            feed_name = feed_config.get("name", "RSS")
            region = feed_config.get("region", "GLOBAL")
            try:
                parsed = feedparser.parse(feed_url)
                for entry in parsed.entries[: self.pool_per_feed]:
                    if not self._is_fresh_enough(entry):
                        continue
                    entry_id = getattr(entry, "id", entry.link)
                    title = getattr(entry, "title", "")
                    link = getattr(entry, "link", "")
                    summary = getattr(entry, "summary", "")
                    published = getattr(entry, "published", "")
                    items.append(
                        RawItem(
                            id=f"rss_{entry_id}",
                            title=title,
                            source_name=feed_name,
                            source_type="article",
                            url=link,
                            published_at=published,
                            summary_text=summary[:1500],
                            region=region,
                            metrics={
                                "score": 0,
                                "comments": 0,
                            },
                        )
                    )
            except Exception:
                continue
        return items
