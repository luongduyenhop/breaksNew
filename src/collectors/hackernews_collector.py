import time
import requests
from typing import List
from src.models.raw_item import RawItem, CommentItem

class HackerNewsCollector:
    def __init__(self, limit: int = 25):
        self.limit = limit
        self.base_url = "https://hacker-news.firebaseio.com/v0"

    def fetch_items(self) -> List[RawItem]:
        items: List[RawItem] = []
        try:
            response = requests.get(f"{self.base_url}/topstories.json", timeout=10)
            if response.status_code != 200:
                return items
            story_ids = response.json()[:self.limit]
            one_day_ago = time.time() - (24 * 3600)
            for story_id in story_ids:
                item_response = requests.get(f"{self.base_url}/item/{story_id}.json", timeout=5)
                if item_response.status_code != 200:
                    continue
                data = item_response.json()
                if not data or data.get("type") != "story":
                    continue
                if data.get("time", 0) < one_day_ago:
                    continue
                url = data.get("url") or f"https://news.ycombinator.com/item?id={story_id}"
                kids = data.get("kids", [])
                top_comments = self._get_top_comments(kids)
                items.append(
                    RawItem(
                        id=f"hn_{story_id}",
                        title=data.get("title", ""),
                        source_name="Hacker News",
                        source_type="forum",
                        url=url,
                        published_at=str(data.get("time", "")),
                        summary_text=data.get("text", "") or data.get("title", ""),
                        region="GLOBAL",
                        metrics={
                            "score": data.get("score", 0),
                            "comments": data.get("descendants", 0)
                        },
                        top_comments=top_comments
                    )
                )
        except Exception:
            return items
        return items

    def _get_top_comments(self, kids: list, limit: int = 3) -> List[CommentItem]:
        comments: List[CommentItem] = []
        if not kids:
            return comments
        for kid_id in kids[:limit]:
            try:
                kid_res = requests.get(f"{self.base_url}/item/{kid_id}.json", timeout=4)
                if kid_res.status_code == 200:
                    c_data = kid_res.json()
                    if c_data and c_data.get("type") == "comment" and not c_data.get("deleted", False):
                        text = c_data.get("text", "")
                        author = c_data.get("by", "HN User")
                        if text and len(text) > 15:
                            comments.append(CommentItem(author=author, text=text[:350], votes=1))
            except Exception:
                continue
        return comments
