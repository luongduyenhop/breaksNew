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

    collected_items = []

    youtube_channels = sources.get("youtube_channels", [])
    if youtube_channels:
        youtube_collector = YouTubeCollector(youtube_channels)
        collected_items.extend(youtube_collector.fetch_items())

    subreddits = sources.get("subreddits", [])
    if subreddits:
        reddit_collector = RedditCollector(subreddits)
        collected_items.extend(reddit_collector.fetch_items())

    hn_collector = HackerNewsCollector(limit=20)
    collected_items.extend(hn_collector.fetch_items())

    rss_feeds = sources.get("rss_feeds", [])
    if rss_feeds:
        rss_collector = RssCollector(rss_feeds)
        collected_items.extend(rss_collector.fetch_items())

    normalizer = DataNormalizer()
    normalized_items = normalizer.deduplicate_and_normalize(collected_items)

    total_comments = sum(len(item.top_comments) for item in normalized_items)
    print(f"Collected total: {len(collected_items)} items")
    print(f"Normalized total: {len(normalized_items)} items (with {total_comments} top community comments)")

    synthesizer = MarketBriefingSynthesizer()
    if dry_run and not os.environ.get("GEMINI_API_KEY"):
        report_content = synthesizer._build_fallback_report(normalized_items)
    else:
        report_content = synthesizer.analyze_and_synthesize(normalized_items)

    today_str = datetime.now().strftime("%Y-%m-%d")
    report_title = f"IT Market & Career Briefing - {today_str}"

    reports_dir = str(PROJECT_ROOT / "reports")
    markdown_pub = MarkdownPublisher(output_dir=reports_dir)
    saved_markdown_path = markdown_pub.publish(report_content, today_str)
    print(f"Markdown report generated: {saved_markdown_path}")

    google_docs_url = ""
    if not dry_run:
        docs_pub = GoogleDocsPublisher()
        google_docs_url = docs_pub.publish_document(today_str, report_content)
        if google_docs_url:
            print(f"Google Docs published: {google_docs_url}")

    email_sent = False
    if not dry_run:
        gmail_pub = GmailPublisher()
        email_sent = gmail_pub.send_briefing_email(
            subject=f"[Daily Briefing] {report_title}",
            markdown_content=report_content,
            google_docs_url=google_docs_url
        )
        print(f"Email sent status: {email_sent}")

    return {
        "items_count": len(normalized_items),
        "comments_count": total_comments,
        "markdown_path": saved_markdown_path,
        "google_docs_url": google_docs_url,
        "email_sent": email_sent
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    result = run_pipeline(dry_run=args.dry_run)
    sys.exit(0)
