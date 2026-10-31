import os
import feedparser
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_comment_downloader import YoutubeCommentDownloader
from typing import List, Dict
from src.models.raw_item import RawItem, CommentItem

API_BASE = "https://www.googleapis.com/youtube/v3"
COMMENT_TEXT_CAP = 1000


class YouTubeCollector:
    """Collect recent videos from the configured channels.

    This collector gathers a *pool* (6 latest per channel); deciding which
    videos are actually about the IT market/direction is the job of
    src.filters.relevance.RelevanceScorer in the pipeline.

    Comments — the most valuable part of a video for this briefing — are
    fetched via the official YouTube Data API v3 when YOUTUBE_API_KEY is
    set (reliable from CI/datacenter IPs, real like counts, ~1 quota unit
    per video). Without a key it falls back to the scraper library, whose
    parameter is `sort_by` — the old code called it with `sort=`, which
    raised a TypeError that was silently swallowed, so YouTube comments
    were ALWAYS empty before this fix.
    """

    # The scraper fallback can block for tens of seconds per video when
    # YouTube throttles datacenter IPs, so it gets a small global budget
    # per run. The Data API path has no such problem and is unlimited.
    SCRAPER_BUDGET = 6

    # Search-discovered videos that get API comments per run (bounds the
    # runtime; the rest still compete on title/topic/engagement).
    SEARCH_COMMENT_BUDGET = 12

    def __init__(self, channels: List[Dict[str, str]], pool_per_channel: int = 6,
                 api_key: str = None, search_queries: List[Dict[str, str]] = None):
        self.channels = channels
        self.pool_per_channel = pool_per_channel
        self.api_key = api_key if api_key is not None else os.environ.get("YOUTUBE_API_KEY", "")
        self.search_queries = search_queries or []
        self.comment_downloader = YoutubeCommentDownloader()
        self._scraper_budget = self.SCRAPER_BUDGET

    def fetch_items(self) -> List[RawItem]:
        items: List[RawItem] = []
        seen_video_ids = set()
        for channel in self.channels:
            channel_id = channel.get("id", "")
            channel_name = channel.get("name", "YouTube")
            region = channel.get("region", "GLOBAL")
            feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[: self.pool_per_channel]:
                    video_id = getattr(entry, "yt_videoid", "")
                    if video_id:
                        seen_video_ids.add(video_id)
                    transcript = self._get_transcript(video_id)
                    description = getattr(entry, "summary", "")
                    content = transcript if transcript else description
                    published = getattr(entry, "published", "")
                    video_url = entry.link
                    top_comments = self._get_top_comments(video_id, video_url)
                    stats = self._get_video_stats(video_id) if self.api_key else {}
                    items.append(
                        RawItem(
                            id=f"yt_{video_id}",
                            title=entry.title,
                            source_name=f"YouTube ({channel_name})",
                            source_type="video",
                            url=video_url,
                            published_at=published,
                            summary_text=content[:4000],
                            region=region,
                            metrics={
                                "views": stats.get("views", 0),
                                "likes": stats.get("likes", 0),
                                "comments": stats.get("comments", len(top_comments)),
                            },
                            top_comments=top_comments,
                        )
                    )
            except Exception:
                continue
        if self.api_key and self.search_queries:
            items.extend(self._fetch_search_items(seen_video_ids))
        return items

    # -- Search discovery (escapes the fixed channel list) -------------------
    def _fetch_search_items(self, seen_video_ids: set) -> List[RawItem]:
        """YouTube Data API search by topic/role queries (last 72h).

        Each search.list call costs 100 quota units; ~8 queries/day is
        well inside the 10,000-unit daily quota. Results are enriched in
        one batched videos.list call, ranked by views, and the top few
        also get API comments — the practitioner discussion is the point.
        """
        from datetime import datetime, timedelta, timezone

        published_after = (
            datetime.now(timezone.utc) - timedelta(hours=72)
        ).strftime("%Y-%m-%dT%H:%M:%SZ")

        region_by_video: Dict[str, str] = {}
        # Two passes per query (PR #10): order=date surfaces what was
        # published in the last few hours; order=viewCount keeps the
        # proven popular hits. Date results are inserted first so the
        # freshest videos survive the videos.list cap below. Cost:
        # 2 calls x 100 units x ~10 queries = ~2,000 units/run of the
        # 10,000/day quota; if the quota is exhausted the search calls
        # fail soft and channel feeds still run.
        for order in ("date", "viewCount"):
            for query_cfg in self.search_queries:
                try:
                    response = requests.get(
                        f"{API_BASE}/search",
                        params={
                            "part": "snippet",
                            "type": "video",
                            "q": query_cfg.get("query", ""),
                            "order": order,
                            "publishedAfter": published_after,
                            "maxResults": 10,
                            "regionCode": query_cfg.get("region", "VN")
                            if query_cfg.get("region") in ("VN", "US")
                            else "VN",
                            "relevanceLanguage": query_cfg.get("language", "vi"),
                            "key": self.api_key,
                        },
                        timeout=15,
                    )
                    if response.status_code != 200:
                        print(f"YouTube search failed for '{query_cfg.get('query', '')[:40]}': HTTP {response.status_code}")
                        continue
                    for entry in response.json().get("items", []):
                        video_id = entry.get("id", {}).get("videoId", "")
                        if video_id and video_id not in seen_video_ids:
                            region_by_video.setdefault(video_id, query_cfg.get("region", "GLOBAL"))
                except Exception as error:
                    print(f"YouTube search error: {error}")
                    continue

        if not region_by_video:
            return []

        details: Dict[str, dict] = {}
        video_ids = list(region_by_video.keys())[:50]
        try:
            response = requests.get(
                f"{API_BASE}/videos",
                params={
                    "part": "snippet,statistics",
                    "id": ",".join(video_ids),
                    "key": self.api_key,
                },
                timeout=15,
            )
            if response.status_code == 200:
                for entry in response.json().get("items", []):
                    details[entry.get("id", "")] = entry
        except Exception as error:
            print(f"YouTube videos.list error: {error}")
            return []

        candidates = []
        for video_id, region in region_by_video.items():
            entry = details.get(video_id)
            if not entry:
                continue
            snippet = entry.get("snippet", {})
            stats = entry.get("statistics", {})
            candidates.append((video_id, region, snippet, stats))
        candidates.sort(key=lambda c: int(c[3].get("viewCount", 0) or 0), reverse=True)

        items: List[RawItem] = []
        for rank, (video_id, region, snippet, stats) in enumerate(candidates):
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            top_comments = (
                self._get_comments_via_api(video_id, limit=5)
                if rank < self.SEARCH_COMMENT_BUDGET
                else []
            )
            items.append(
                RawItem(
                    id=f"yt_{video_id}",
                    title=snippet.get("title", ""),
                    source_name=f"YouTube ({snippet.get('channelTitle', 'Search')})",
                    source_type="video",
                    url=video_url,
                    published_at=snippet.get("publishedAt", ""),
                    summary_text=(snippet.get("description", "") or "")[:4000],
                    region=region,
                    metrics={
                        "views": int(stats.get("viewCount", 0) or 0),
                        "likes": int(stats.get("likeCount", 0) or 0),
                        "comments": int(stats.get("commentCount", 0) or 0),
                    },
                    top_comments=top_comments,
                )
            )
        return items

    def _get_transcript(self, video_id: str) -> str:
        if not video_id:
            return ""
        # youtube-transcript-api >= 1.0 exposes an instance API; older
        # versions expose a classmethod. Support both.
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(
                video_id, languages=["vi", "en"]
            )
            segments = [seg["text"] for seg in transcript_list[:200]]
            return " ".join(segments)
        except Exception:
            pass
        try:
            api = YouTubeTranscriptApi()
            fetched = api.fetch(video_id, languages=["vi", "en"])
            segments = [seg.text for seg in list(fetched)[:200]]
            return " ".join(segments)
        except Exception:
            return ""

    # -- Comments ------------------------------------------------------------
    def _get_top_comments(self, video_id: str, video_url: str, limit: int = 5) -> List[CommentItem]:
        if self.api_key and video_id:
            comments = self._get_comments_via_api(video_id, limit=limit)
            if comments:
                return comments
        if self._scraper_budget <= 0:
            return []
        self._scraper_budget -= 1
        return self._get_comments_via_scraper(video_url, limit=limit)

    def _get_comments_via_api(self, video_id: str, limit: int = 5) -> List[CommentItem]:
        comments: List[CommentItem] = []
        try:
            response = requests.get(
                f"{API_BASE}/commentThreads",
                params={
                    "part": "snippet",
                    "videoId": video_id,
                    "order": "relevance",
                    "maxResults": 25,
                    "textFormat": "plainText",
                    "key": self.api_key,
                },
                timeout=10,
            )
            if response.status_code != 200:
                print(f"YouTube Data API comments failed for {video_id}: HTTP {response.status_code}")
                return comments
            for thread in response.json().get("items", []):
                snippet = (
                    thread.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
                )
                text = (snippet.get("textDisplay") or "").strip()
                if text and len(text) > 10:
                    comments.append(
                        CommentItem(
                            author=snippet.get("authorDisplayName", "User"),
                            text=text[:COMMENT_TEXT_CAP],
                            votes=int(snippet.get("likeCount", 0) or 0),
                        )
                    )
        except Exception as error:
            print(f"YouTube Data API comments error for {video_id}: {error}")
            return comments
        comments.sort(key=lambda c: c.votes, reverse=True)
        return comments[:limit]

    def _get_video_stats(self, video_id: str) -> Dict[str, int]:
        try:
            response = requests.get(
                f"{API_BASE}/videos",
                params={"part": "statistics", "id": video_id, "key": self.api_key},
                timeout=10,
            )
            if response.status_code != 200:
                return {}
            items = response.json().get("items", [])
            if not items:
                return {}
            stats = items[0].get("statistics", {})
            return {
                "views": int(stats.get("viewCount", 0) or 0),
                "likes": int(stats.get("likeCount", 0) or 0),
                "comments": int(stats.get("commentCount", 0) or 0),
            }
        except Exception:
            return {}

    def _get_comments_via_scraper(self, video_url: str, limit: int = 5) -> List[CommentItem]:
        comments: List[CommentItem] = []
        try:
            # NOTE: the parameter is `sort_by` (0 = top comments). Calling
            # it with `sort=` raises TypeError — that bug, hidden by the
            # old blanket try/except, zeroed all YouTube comments.
            generator = self.comment_downloader.get_comments_from_url(video_url, sort_by=0)
            for raw_comment in generator:
                text = (raw_comment.get("text") or "").strip()
                votes = raw_comment.get("votes", 0)
                try:
                    votes_int = int(
                        str(votes).replace(",", "").replace(".", "").replace("K", "000")
                    )
                except Exception:
                    votes_int = 0
                if text and len(text) > 10:
                    comments.append(
                        CommentItem(
                            author=raw_comment.get("author", "User"),
                            text=text[:COMMENT_TEXT_CAP],
                            votes=votes_int,
                        )
                    )
                if len(comments) >= limit * 3:
                    break
        except Exception:
            pass
        comments.sort(key=lambda c: c.votes, reverse=True)
        return comments[:limit]
