import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from src.models.raw_item import CommentItem, RawItem


def _parse_ts(value: str) -> float:
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except (TypeError, ValueError):
        return 0.0


class FacebookCollector:
    """Facebook group posts, read from the synced data file.

    GitHub Actions cannot read Facebook, so scripts/
    sync_facebook_groups.py runs on Muse's side (where the account
    is connected) and writes data/facebook_posts.json into the repo.
    This collector only reads that file — no network, no credentials.
    Admission into the briefing is the community lane's job (see
    community_quality_score in src/filters/relevance.py): raw group
    posts rarely match the topic keywords, so length + engagement
    act as the quality gate instead.
    """

    def __init__(self, data_file: str = "data/facebook_posts.json",
                 max_age_days: int = 3, limit: int = 30):
        self.data_file = data_file
        self.max_age_days = max_age_days
        self.limit = limit

    def fetch_items(self) -> List[RawItem]:
        path = Path(self.data_file)
        if not path.exists():
            print(f"Facebook data file missing ({self.data_file}) — skipped.")
            return []
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            print(f"Facebook data file unreadable ({self.data_file}): {error}")
            return []

        records = payload.get("items", []) if isinstance(payload, dict) else []
        cutoff = time.time() - self.max_age_days * 24 * 3600
        by_id = {}
        for record in records if isinstance(records, list) else []:
            if not isinstance(record, dict):
                continue
            post_id = str(record.get("id", "")).strip()
            if not post_id or post_id in by_id:
                continue
            published = record.get("published_at", "")
            published_ts = _parse_ts(published)
            if published_ts and published_ts < cutoff:
                continue
            group_name = record.get("group_name") or record.get("group_id", "")
            comments = [
                CommentItem(
                    author=str(c.get("author", "")),
                    text=str(c.get("text", "")),
                    votes=int(c.get("votes", 0) or 0),
                )
                for c in record.get("top_comments", [])
                if isinstance(c, dict) and (c.get("text") or "").strip()
            ]
            by_id[post_id] = RawItem(
                id=f"fb_{post_id}",
                title=record.get("title", ""),
                source_name=f"Facebook · {group_name}",
                source_type="facebook",
                url=record.get("url", ""),
                published_at=published,
                summary_text=(record.get("content") or "")[:3000],
                region="VN",
                metrics={
                    "reactions": int(record.get("reactions", 0) or 0),
                    "comments": int(record.get("comments_count", 0) or 0),
                },
                top_comments=comments,
            )
        items = list(by_id.values())[: self.limit]
        print(f"Facebook collector: {len(items)} posts from {self.data_file}")
        return items
