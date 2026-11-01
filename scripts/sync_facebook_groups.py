"""Sync Facebook group posts into the repo as a data file.

GitHub Actions cannot read Facebook (no public API for group posts,
and scraping from a datacenter IP hits the same bot walls as the old
YouTube comment scraper). This script therefore runs on Muse's side,
where Luong's Facebook account is connected through facebook-cli. It
pulls the newest posts from the configured groups, normalizes them and
writes ``data/facebook_posts.json``; the daily pipeline only reads
that file (see src/collectors/facebook_collector.py).

Run it before the daily briefing (a separate cron on Muse's side
will own the schedule — this script is just the worker):

    python scripts/sync_facebook_groups.py [--hours 24] [--limit 20]

The CLI path comes from the FB_CLI env var (default
/opt/hatch/bin/facebook-cli). Fail-soft per group: one group's failure
is logged and skipped, never fatal for the others.
"""
import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CLI = "/opt/hatch/bin/facebook-cli"

# Pre-filter for comment enrichment: long-form posts with at least
# some community reaction are the ones whose discussion is worth
# carrying into the briefing. Everything else ships without comments.
COMMENT_MIN_LENGTH = 800
COMMENT_MIN_REACTIONS = 20
COMMENT_MIN_COUNT = 3
COMMENTS_PER_POST = 5
TITLE_MAX_CHARS = 130
CONTENT_MAX_CHARS = 6000


def run_cli(cli: str, args: list) -> dict:
    """Run one facebook-cli command and parse its JSON stdout."""
    result = subprocess.run(
        [cli] + args, capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"facebook-cli {' '.join(args[:3])}... exited "
            f"{result.returncode}: {(result.stderr or '')[:300]}"
        )
    return json.loads(result.stdout)


def make_title(content: str) -> str:
    """First non-empty line of the post, lightly cleaned, capped."""
    for line in (content or "").splitlines():
        line = line.strip().strip("*# ").strip()
        if line:
            return line[:TITLE_MAX_CHARS]
    return ""


def fetch_top_comments(cli: str, post_id: str) -> list:
    """Best-effort comments for one post; [] on any failure.

    The CLI does not return comment author names, so author is a
    fixed placeholder; votes are unknown and stay 0 (the briefing's
    insight scoring works on text, not on Facebook reaction counts).
    """
    try:
        payload = run_cli(
            cli, ["post", "comments", "read", "--post-id", str(post_id),
                  "--limit", str(COMMENTS_PER_POST)]
        )
    except Exception as error:
        print(f"    comments for post {post_id} skipped: {error}")
        return []
    comments = []
    for entry in payload.get("data", []) if isinstance(payload, dict) else []:
        text = (entry.get("text") or "").strip()
        if not text:
            continue
        comments.append({"author": "Facebook user", "text": text, "votes": 0})
    return comments


def sync_group(cli: str, group: dict, min_ts: int, limit: int) -> list:
    group_id = group["id"]
    group_name = group.get("name", group_id)
    payload = run_cli(cli, [
        "groups", "posts", "--group-id", group_id,
        "--sort-by", "NEW_POSTS",
        "--min-timestamp", str(min_ts),
        "--limit", str(limit),
    ])
    posts = payload.get("data", []) if isinstance(payload, dict) else []
    records = []
    for post in posts:
        content = (post.get("content") or "")[:CONTENT_MAX_CHARS]
        created = int(post.get("creation_time") or 0)
        reactions = int(post.get("react_count", 0) or 0)
        comments_count = int(post.get("comment_count", 0) or 0)
        record = {
            "id": str(post.get("id", "")),
            "group_id": group_id,
            "group_name": group_name,
            "title": make_title(content),
            "content": content,
            "url": post.get("post_url") or "",
            "published_at": datetime.fromtimestamp(
                created, tz=timezone.utc
            ).isoformat() if created else "",
            "reactions": reactions,
            "comments_count": comments_count,
            "top_comments": [],
        }
        if (
            len(content) >= COMMENT_MIN_LENGTH
            and (reactions >= COMMENT_MIN_REACTIONS
                 or comments_count >= COMMENT_MIN_COUNT)
        ):
            record["top_comments"] = fetch_top_comments(cli, record["id"])
        records.append(record)
    print(
        f"Facebook group '{group_name}' ({group_id}): {len(records)} posts, "
        f"{sum(1 for r in records if r['top_comments'])} with comments"
    )
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hours", type=int, default=24,
                        help="only posts published within this many hours")
    parser.add_argument("--limit", type=int, default=20,
                        help="max posts per group")
    parser.add_argument("--config", default=str(PROJECT_ROOT / "config" / "sources.json"))
    parser.add_argument("--output", default=None,
                        help="default: the facebook_data_file from the config")
    args = parser.parse_args()

    cli = os.environ.get("FB_CLI", DEFAULT_CLI)
    with open(args.config, "r", encoding="utf-8") as file:
        config = json.load(file)
    groups = config.get("facebook_groups", [])
    if not groups:
        print("No facebook_groups configured — nothing to sync.")
        return 0

    output = args.output or str(
        PROJECT_ROOT / config.get("facebook_data_file", "data/facebook_posts.json")
    )
    min_ts = int(time.time()) - args.hours * 3600

    items = []
    for group in groups:
        try:
            items.extend(sync_group(cli, group, min_ts, args.limit))
        except Exception as error:
            print(f"Facebook group '{group.get('name', group.get('id'))}' "
                  f"failed, skipped: {error}")

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "items": items,
    }
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=1)
    print(f"Wrote {len(items)} Facebook posts to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
