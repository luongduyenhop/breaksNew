import feedparser
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_comment_downloader import YoutubeCommentDownloader
from typing import List, Dict
from src.models.raw_item import RawItem, CommentItem


class YouTubeCollector:
    """Collect recent videos from the configured channels.

    This collector intentionally gathers a *pool* (6 latest per channel);
    deciding which videos are actually about the IT market is the job of
    src.filters.relevance.RelevanceScorer in the pipeline. What this class
    does guarantee: transcript-first content and comments sorted by real
    vote counts, highest first.
    """

    def __init__(self, channels: List[Dict[str, str]], pool_per_channel: int = 6):
        self.channels = channels
        self.pool_per_channel = pool_per_channel
        self.comment_downloader = YoutubeCommentDownloader()

    def fetch_items(self) -> List[RawItem]:
        items: List[RawItem] = []
        for channel in self.channels:
            channel_id = channel.get("id", "")
            channel_name = channel.get("name", "YouTube")
            region = channel.get("region", "GLOBAL")
            feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[: self.pool_per_channel]:
                    video_id = getattr(entry, "yt_videoid", "")
                    transcript = self._get_transcript(video_id)
                    description = getattr(entry, "summary", "")
                    content = transcript if transcript else description
                    published = getattr(entry, "published", "")
                    video_url = entry.link
                    top_comments = self._get_top_comments(video_url)
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
                                "views": 0,
                                "comments": len(top_comments),
                            },
                            top_comments=top_comments,
                        )
                    )
            except Exception:
                continue
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

    def _get_top_comments(self, video_url: str, limit: int = 5) -> List[CommentItem]:
        comments: List[CommentItem] = []
        try:
            generator = self.comment_downloader.get_comments_from_url(video_url, sort=0)
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
                            text=text[:350],
                            votes=votes_int,
                        )
                    )
                # Gather a candidate pool, then keep the highest-voted —
                # the downloader's ordering is not guaranteed to be by votes.
                if len(comments) >= limit * 3:
                    break
        except Exception:
            return sorted(comments, key=lambda c: c.votes, reverse=True)[:limit]
        comments.sort(key=lambda c: c.votes, reverse=True)
        return comments[:limit]
