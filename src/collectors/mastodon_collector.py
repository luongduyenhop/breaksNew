import html
import re
import time
from datetime import datetime, timezone
from typing import List

import requests

from src.models.raw_item import RawItem

_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(value: str) -> str:
    text = _TAG_RE.sub(" ", value or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def _parse_ts(value: str) -> float:
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except (TypeError, ValueError):
        return 0.0


class MastodonCollector:
    """Mastodon via hachyderm.io — an instance built for IT professionals.

    Instance search needs an account, but hashtag timelines are public
    and need no key, so this collector reads a small set of professional
    hashtags. Posts are short practitioner utterances: they enter the
    pool as `post` items whose text is both headline and body, and the
    relevance/insight scorers decide whether they carry signal. Boosts
    (reblogs) are skipped to avoid duplicates.
    """

    def __init__(self, hashtags: List[str] = None, max_age_days: int = 3,
                 instance: str = "https://hachyderm.io", limit: int = 30):
        self.hashtags = hashtags or []
        self.max_age_days = max_age_days
        self.instance = instance.rstrip("/")
        self.limit = limit

    def fetch_items(self) -> List[RawItem]:
        cutoff = time.time() - self.max_age_days * 24 * 3600
        by_id = {}
        for tag in self.hashtags:
            try:
                response = requests.get(
                    f"{self.instance}/api/v1/timelines/tag/{tag}",
                    params={"limit": 20},
                    timeout=10,
                )
                if response.status_code != 200:
                    print(f"Mastodon tag '{tag}' skipped: HTTP {response.status_code}")
                    continue
                statuses = response.json()
            except Exception as error:
                print(f"Mastodon tag '{tag}' error: {error}")
                continue
            for status in statuses if isinstance(statuses, list) else []:
                status_id = status.get("id")
                if not status_id or status_id in by_id or status.get("reblog"):
                    continue
                if status.get("language") not in (None, "en", "vi"):
                    continue
                created = status.get("created_at", "")
                if _parse_ts(created) and _parse_ts(created) < cutoff:
                    continue
                text = _strip_html(status.get("content", ""))
                if len(text) < 40:  # link-only or emoji-only posts carry no signal
                    continue
                account = status.get("account", {})
                author = account.get("display_name") or account.get("username", "")
                title = text[:90] + ("…" if len(text) > 90 else "")
                item = RawItem(
                    id=f"mastodon_{status_id}",
                    title=title,
                    source_name="Mastodon (Hachyderm)",
                    source_type="post",
                    url=status.get("url", ""),
                    published_at=created,
                    summary_text=text[:1000],
                    region="GLOBAL",
                    metrics={
                        "favourites": int(status.get("favourites_count", 0) or 0),
                        "reblogs": int(status.get("reblogs_count", 0) or 0),
                        "replies": int(status.get("replies_count", 0) or 0),
                    },
                )
                by_id[status_id] = item
        return list(by_id.values())[: self.limit]
