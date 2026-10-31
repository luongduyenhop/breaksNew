import time
from datetime import datetime, timezone
from typing import List

import requests

from src.models.raw_item import RawItem


def _parse_ts(value: str) -> float:
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except (TypeError, ValueError):
        return 0.0


class DevToCollector:
    """dev.to via its public API, per tag — richer than the RSS feed.

    The single Dev.to RSS feed mixed every topic together; the API lets
    the pipeline pull the newest articles per professional tag with real
    reaction/comment counts for the engagement signal. No key needed.
    """

    def __init__(self, tags: List[str] = None, max_age_days: int = 3, limit: int = 30):
        self.tags = tags or []
        self.max_age_days = max_age_days
        self.limit = limit
        self.base_url = "https://dev.to/api/articles"

    def fetch_items(self) -> List[RawItem]:
        cutoff = time.time() - self.max_age_days * 24 * 3600
        by_id = {}
        for tag in self.tags:
            try:
                response = requests.get(
                    self.base_url,
                    params={"tag": tag, "per_page": 15, "state": "fresh"},
                    timeout=10,
                )
                if response.status_code != 200:
                    print(f"dev.to tag '{tag}' skipped: HTTP {response.status_code}")
                    continue
                articles = response.json()
            except Exception as error:
                print(f"dev.to tag '{tag}' error: {error}")
                continue
            for article in articles if isinstance(articles, list) else []:
                article_id = article.get("id")
                if not article_id or article_id in by_id:
                    continue
                published = article.get("published_at", "")
                if _parse_ts(published) and _parse_ts(published) < cutoff:
                    continue
                by_id[article_id] = RawItem(
                    id=f"devto_{article_id}",
                    title=article.get("title", ""),
                    source_name="Dev.to",
                    source_type="article",
                    url=article.get("url", ""),
                    published_at=published,
                    summary_text=(article.get("description") or "")[:1200],
                    region="GLOBAL",
                    metrics={
                        "reactions": int(article.get("public_reactions_count", 0) or 0),
                        "comments": int(article.get("comments_count", 0) or 0),
                    },
                )
        return list(by_id.values())[: self.limit]
