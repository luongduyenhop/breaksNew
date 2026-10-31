import feedparser
from typing import List, Dict
from src.models.raw_item import RawItem

class RssCollector:
    def __init__(self, feeds: List[Dict[str, str]]):
        self.feeds = feeds

    def fetch_items(self) -> List[RawItem]:
        items: List[RawItem] = []
        for feed_config in self.feeds:
            feed_url = feed_config.get("url", "")
            feed_name = feed_config.get("name", "RSS")
            region = feed_config.get("region", "GLOBAL")
            try:
                parsed = feedparser.parse(feed_url)
                for entry in parsed.entries[:8]:
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
                                "comments": 0
                            }
                        )
                    )
            except Exception:
                continue
        return items
