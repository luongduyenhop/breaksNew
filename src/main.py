import os
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import json
import argparse
from datetime import datetime
from dotenv import load_dotenv

from src.collectors.youtube_collector import YouTubeCollector
from src.collectors.reddit_collector import RedditCollector
from src.collectors.hackernews_collector import HackerNewsCollector
from src.collectors.rss_collector import RssCollector
from src.normalizers.data_normalizer import DataNormalizer
from src.filters.relevance import RelevanceScorer, DEFAULT_TOPIC_GROUPS
from src.analyzers.summarizer import MarketBriefingSynthesizer
from src.publishers.markdown_publisher import MarkdownPublisher
from src.publishers.google_docs_publisher import GoogleDocsPublisher
from src.publishers.gmail_publisher import GmailPublisher

load_dotenv()


def load_sources_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        return {}
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_pipeline(dry_run: bool = False):
    config_file = PROJECT_ROOT / "config" / "sources.json"
    sources = load_sources_config(str(config_file))
    relevance_cfg = sources.get("relevance", {})
    max_age_days = int(relevance_cfg.get("max_age_days", 7))

    collected_items = []

    youtube_channels = sources.get("youtube_channels", [])
    youtube_search_queries = sources.get("youtube_search_queries", [])
    if youtube_channels or youtube_search_queries:
        youtube_collector = YouTubeCollector(
            youtube_channels, search_queries=youtube_search_queries
        )
        collected_items.extend(youtube_collector.fetch_items())

    flat_keywords = sources.get("keywords", [])
    subreddits = sources.get("subreddits", [])
    reddit_search_queries = sources.get("reddit_search_queries", [])
    if subreddits or reddit_search_queries:
        reddit_collector = RedditCollector(
            subreddits, keywords=flat_keywords, max_age_days=max_age_days,
            search_queries=reddit_search_queries,
        )
        collected_items.extend(reddit_collector.fetch_items())

    hn_queries = sources.get("hackernews_queries") or None
    hn_collector = HackerNewsCollector(limit=30, queries=hn_queries, max_age_days=max_age_days)
    collected_items.extend(hn_collector.fetch_items())

    rss_feeds = sources.get("rss_feeds", [])
    if rss_feeds:
        # VN blogs publish market reports infrequently — wider window,
        # the relevance scorer still guards topicality.
        rss_max_age = int(relevance_cfg.get("rss_max_age_days", max_age_days))
        rss_collector = RssCollector(rss_feeds, max_age_days=rss_max_age)
        collected_items.extend(rss_collector.fetch_items())

    normalizer = DataNormalizer()
    normalized_items = normalizer.deduplicate_and_normalize(collected_items)

    # Editorial filter: keep only items that are actually about the IT
    # market / new directions / career survival, ranked by relevance.
    topic_groups = sources.get("topic_groups") or DEFAULT_TOPIC_GROUPS
    scorer = RelevanceScorer(
        topic_groups=topic_groups,
        min_score=float(relevance_cfg.get("min_score", 25)),
        per_source_cap=int(relevance_cfg.get("per_source_cap", 6)),
        total_cap=int(relevance_cfg.get("total_cap", 40)),
        max_age_days=max_age_days,
    )
    filtered_items, dropped_items = scorer.score_and_filter(normalized_items)

    total_comments = sum(len(item.top_comments) for item in filtered_items)
    print(f"Collected total: {len(collected_items)} items")
    print(f"Normalized total: {len(normalized_items)} items")
    print(
        f"Relevance filter: kept {len(filtered_items)} items "
        f"(dropped {len(dropped_items)} off-topic/low-score), "
        f"{total_comments} top community comments in kept items"
    )
    for item in filtered_items[:10]:
        print(f"  [{item.relevance_score:5.1f}] {item.source_name}: {item.title[:80]}")

    synthesizer = MarketBriefingSynthesizer()
    # analyze_and_synthesize handles the no-key case itself and marks the
    # report with a visible fallback warning when Gemini cannot run.
    report_content = synthesizer.analyze_and_synthesize(filtered_items)

    today_str = datetime.now().strftime("%Y-%m-%d")
    report_title = f"IT Market & Career Briefing - {today_str}"

    # Publish to Google Docs FIRST so the Docs link can be embedded at the
    # top of every delivered copy (committed markdown + email). Previously
    # the markdown was saved before Docs existed, so no copy the reader
    # opened ever contained the link. A Docs failure is now visible in the
    # report itself instead of only in CI logs.
    google_docs_url = ""
    if not dry_run:
        docs_pub = GoogleDocsPublisher()
        google_docs_url = docs_pub.publish_document(today_str, report_content)
        if google_docs_url:
            print(f"Google Docs published: {google_docs_url}")
        else:
            print("Google Docs publishing produced no URL.")

    if dry_run:
        final_content = report_content
    elif google_docs_url:
        final_content = (
            f"📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** "
            f"[Mở Google Docs hôm nay]({google_docs_url})\n\n---\n\n"
            + report_content
        )
    else:
        final_content = (
            "> ⚠️ **Chưa tạo được Google Docs trong lần chạy này** — kiểm tra "
            "GOOGLE_DOCS_WEBHOOK_URL / GOOGLE_SERVICE_ACCOUNT_JSON và quyền "
            "truy cập của bản deploy Apps Script (phải là Anyone).\n\n"
            + report_content
        )

    reports_dir = str(PROJECT_ROOT / "reports")
    markdown_pub = MarkdownPublisher(output_dir=reports_dir)
    saved_markdown_path = markdown_pub.publish(final_content, today_str)
    print(f"Markdown report generated: {saved_markdown_path}")

    email_sent = False
    if not dry_run:
        gmail_pub = GmailPublisher()
        email_sent = gmail_pub.send_briefing_email(
            subject=f"[Daily Briefing] {report_title}",
            markdown_content=final_content,
            google_docs_url=google_docs_url,
        )
        print(f"Email sent status: {email_sent}")

    return {
        "items_count": len(filtered_items),
        "dropped_count": len(dropped_items),
        "comments_count": total_comments,
        "used_fallback": synthesizer.used_fallback,
        "markdown_path": saved_markdown_path,
        "google_docs_url": google_docs_url,
        "email_sent": email_sent,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    result = run_pipeline(dry_run=args.dry_run)
    sys.exit(0)
