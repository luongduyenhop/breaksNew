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


class LobstersCollector:
    """Lobsters (lobste.rs) — a veteran, invite-only developer community.

    Its public JSON feeds need no key and carry exactly what the scorer
    wants: title, external URL, score, comment count and tags. Both the
    newest and hottest listings are read; duplicates are merged.
    """

    FEEDS = ("newest", "hottest")

    def __init__(self, max_age_days: int = 3, limit: int = 25):
        self.max_age_days = max_age_days
        self.limit = limit
        self.base_url = "https://lobste.rs"

    def fetch_items(self) -> List[RawItem]:
        cutoff = time.time() - self.max_age_days * 24 * 3600
        by_id = {}
        for feed in self.FEEDS:
            try:
                response = requests.get(f"{self.base_url}/{feed}.json", timeout=10)
                if response.status_code != 200:
                    print(f"Lobsters {feed} skipped: HTTP {response.status_code}")
                    continue
                entries = response.json()
            except Exception as error:
                print(f"Lobsters {feed} error: {error}")
                continue
            for entry in entries if isinstance(entries, list) else []:
                short_id = entry.get("short_id", "")
                if not short_id or short_id in by_id:
                    continue
                created = entry.get("created_at", "")
                if _parse_ts(created) and _parse_ts(created) < cutoff:
                    continue
                submitter = entry.get("submitter_user")
                author = (
                    submitter.get("username", "")
                    if isinstance(submitter, dict)
                    else str(submitter or "")
                )
                by_id[short_id] = RawItem(
                    id=f"lobsters_{short_id}",
                    title=entry.get("title", ""),
                    source_name="Lobsters",
                    source_type="article",
                    url=entry.get("url") or entry.get("comments_url", ""),
                    published_at=created,
                    summary_text=(entry.get("description_plain") or "")[:1200],
                    region="GLOBAL",
                    metrics={
                        "score": int(entry.get("score", 0) or 0),
                        "comments": int(entry.get("comment_count", 0) or 0),
                    },
                )
        return list(by_id.values())[: self.limit]
