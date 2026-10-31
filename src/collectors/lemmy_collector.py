import re
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


class LemmyCollector:
    """Lemmy (programming.dev) — a federated, developer-heavy Reddit-like.

    The instance's public search API needs no key. Queries mirror the
    Hacker News topic queries, sorted newest-first; the scorer remains
    the editorial gate, exactly as with Reddit search.
    """

    def __init__(self, queries: List[str] = None, max_age_days: int = 3,
                 instance: str = "https://programming.dev", limit: int = 30):
        self.queries = queries or []
        self.max_age_days = max_age_days
        self.instance = instance.rstrip("/")
        self.limit = limit

    def fetch_items(self) -> List[RawItem]:
        if not self.queries:
            return []
        cutoff = time.time() - self.max_age_days * 24 * 3600
        by_id = {}
        for query in self.queries:
            try:
                response = requests.get(
                    f"{self.instance}/api/v3/search",
                    params={"q": query, "type_": "Posts", "sort": "New", "limit": 15},
                    timeout=10,
                )
                if response.status_code != 200:
                    print(f"Lemmy search skipped for '{query}': HTTP {response.status_code}")
                    continue
                posts = response.json().get("posts", [])
            except Exception as error:
                print(f"Lemmy search error for '{query}': {error}")
                continue
            for view in posts:
                post = view.get("post", {})
                counts = view.get("counts", {})
                post_id = post.get("id")
                if not post_id or post_id in by_id:
                    continue
                published = post.get("published", "")
                if _parse_ts(published) and _parse_ts(published) < cutoff:
                    continue
                body = re.sub(r"\s+", " ", post.get("body") or "").strip()
                by_id[post_id] = RawItem(
                    id=f"lemmy_{post_id}",
                    title=post.get("name", ""),
                    source_name="Lemmy (programming.dev)",
                    source_type="article",
                    url=post.get("url") or f"{self.instance}/post/{post_id}",
                    published_at=published,
                    summary_text=body[:1200],
                    region="GLOBAL",
                    metrics={
                        "score": int(counts.get("score", 0) or 0),
                        "comments": int(counts.get("comments", 0) or 0),
                    },
                )
        return list(by_id.values())[: self.limit]
