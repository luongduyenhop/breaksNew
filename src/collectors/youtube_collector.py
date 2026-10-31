import feedparser
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_comment_downloader import YoutubeCommentDownloader
from typing import List, Dict
from src.models.raw_item import RawItem, CommentItem

class YouTubeCollector:
    def __init__(self, channels: List[Dict[str, str]]):
        self.channels = channels
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
                for entry in feed.entries[:3]:
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
                            summary_text=content[:1500],
                            region=region,
                            metrics={
                                "views": 0,
                                "comments": len(top_comments)
                            },
                            top_comments=top_comments
                        )
                    )
            except Exception:
                continue
        return items

    def _get_transcript(self, video_id: str) -> str:
        if not video_id:
            return ""
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["vi", "en"])
            segments = [seg["text"] for seg in transcript_list[:120]]
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
                    votes_int = int(str(votes).replace(",", "").replace(".", ""))
                except Exception:
                    votes_int = 0
                if text and len(text) > 10:
                    comments.append(
                        CommentItem(
                            author=raw_comment.get("author", "User"),
                            text=text[:350],
                            votes=votes_int
                        )
                    )
                if len(comments) >= limit:
                    break
        except Exception:
            return comments
        return comments
