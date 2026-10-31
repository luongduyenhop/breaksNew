import time
import requests
from typing import List
from src.models.raw_item import RawItem, CommentItem

class RedditCollector:
    def __init__(self, subreddits: List[str]):
        self.subreddits = subreddits
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ITMarketTracker/1.0"}

    def fetch_items(self) -> List[RawItem]:
        items: List[RawItem] = []
        one_day_ago = time.time() - (24 * 3600)
        for sub in self.subreddits:
            url = f"https://www.reddit.com/r/{sub}/hot.json?limit=15"
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                if response.status_code != 200:
                    continue
                data = response.json()
                children = data.get("data", {}).get("children", [])
                for child in children:
                    post = child.get("data", {})
                    created_utc = post.get("created_utc", 0)
                    if created_utc < one_day_ago or post.get("stickied", False):
                        continue
                    post_id = post.get("id", "")
                    permalink = post.get("permalink", "")
                    top_comments = self._get_top_comments(permalink)
                    items.append(
                        RawItem(
                            id=f"reddit_{post_id}",
                            title=post.get("title", ""),
                            source_name=f"Reddit r/{sub}",
                            source_type="forum",
                            url=f"https://www.reddit.com{permalink}",
                            published_at=str(created_utc),
                            summary_text=post.get("selftext", "")[:1200],
                            region="GLOBAL",
                            metrics={
                                "score": post.get("score", 0),
                                "comments": post.get("num_comments", 0)
                            },
                            top_comments=top_comments
                        )
                    )
            except Exception:
                continue
        return items

    def _get_top_comments(self, permalink: str, limit: int = 4) -> List[CommentItem]:
        comments: List[CommentItem] = []
        if not permalink:
            return comments
        url = f"https://www.reddit.com{permalink}.json?sort=top&limit=5"
        try:
            res = requests.get(url, headers=self.headers, timeout=6)
            if res.status_code == 200:
                payload = res.json()
                if isinstance(payload, list) and len(payload) > 1:
                    children = payload[1].get("data", {}).get("children", [])
                    for child in children:
                        c_data = child.get("data", {})
                        body = c_data.get("body", "").strip()
                        score = c_data.get("score", 0)
                        author = c_data.get("author", "User")
                        if body and len(body) > 15 and not body.startswith("[deleted]"):
                            comments.append(CommentItem(author=author, text=body[:350], votes=score))
                        if len(comments) >= limit:
                            break
        except Exception:
            return comments
        return comments
