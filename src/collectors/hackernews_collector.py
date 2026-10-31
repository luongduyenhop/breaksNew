import time
import requests
from typing import List
from src.models.raw_item import RawItem, CommentItem

DEFAULT_QUERIES = [
    "developer layoffs",
    "tech hiring",
    "programmer job market",
    "AI replacing developers",
    "software engineer career",
]


class HackerNewsCollector:
    """Hacker News via keyword search (Algolia) instead of top stories.

    The old implementation took HN's global top stories, which let in
    anything trending (health policy, retro-gaming hacks...). With queries
    configured it searches Algolia's HN index for market/career topics in
    the last `max_age_days` days. Without queries it falls back to the
    Firebase top-stories behaviour.

    Note on comment votes: HN does not expose per-comment scores, so
    comments are ranked by substance (length) and carry votes=0 rather
    than the fabricated votes=1 the old code used.
    """

    def __init__(self, limit: int = 25, queries: List[str] = None, max_age_days: int = 7):
        self.limit = limit
        self.queries = queries
        self.max_age_days = max_age_days
        self.base_url = "https://hacker-news.firebaseio.com/v0"
        self.algolia_url = "https://hn.algolia.com/api/v1"

    def fetch_items(self) -> List[RawItem]:
        if self.queries:
            return self._fetch_by_search()
        return self._fetch_top_stories()

    # -- Algolia keyword search -------------------------------------------
    def _fetch_by_search(self) -> List[RawItem]:
        cutoff = int(time.time() - self.max_age_days * 24 * 3600)
        per_query = max(3, min(10, self.limit // max(1, len(self.queries)) + 2))
        by_id = {}
        for query in self.queries:
            try:
                response = requests.get(
                    f"{self.algolia_url}/search_by_date",
                    params={
                        "query": query,
                        "tags": "story",
                        "hitsPerPage": per_query,
                        "numericFilters": f"created_at_i>{cutoff}",
                    },
                    timeout=10,
                )
                if response.status_code != 200:
                    continue
                for hit in response.json().get("hits", []):
                    object_id = hit.get("objectID", "")
                    if not object_id or not hit.get("title"):
                        continue
                    existing = by_id.get(object_id)
                    if existing and existing.metrics.get("score", 0) >= hit.get("points", 0):
                        continue
                    by_id[object_id] = RawItem(
                        id=f"hn_{object_id}",
                        title=hit.get("title", ""),
                        source_name="Hacker News",
                        source_type="forum",
                        url=hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}",
                        published_at=str(hit.get("created_at_i", "")),
                        summary_text=(hit.get("story_text") or hit.get("title", ""))[:1200],
                        region="GLOBAL",
                        metrics={
                            "score": hit.get("points", 0) or 0,
                            "comments": hit.get("num_comments", 0) or 0,
                        },
                        top_comments=self._get_top_comments_algolia(object_id),
                    )
            except Exception:
                continue
        items = sorted(by_id.values(), key=lambda i: i.metrics.get("score", 0), reverse=True)
        return items[: self.limit]

    def _get_top_comments_algolia(self, story_id: str, limit: int = 4) -> List[CommentItem]:
        comments: List[CommentItem] = []
        try:
            res = requests.get(f"{self.algolia_url}/items/{story_id}", timeout=6)
            if res.status_code != 200:
                return comments
            children = res.json().get("children", []) or []
            candidates = []
            for child in children:
                text = (child.get("text") or "").strip()
                author = child.get("author") or "HN User"
                if text and len(text) > 15:
                    candidates.append(CommentItem(author=author, text=text[:350], votes=0))
            candidates.sort(key=lambda c: len(c.text), reverse=True)
            comments = candidates[:limit]
        except Exception:
            return comments
        return comments

    # -- Firebase top stories (fallback, no queries configured) ------------
    def _fetch_top_stories(self) -> List[RawItem]:
        items: List[RawItem] = []
        try:
            response = requests.get(f"{self.base_url}/topstories.json", timeout=10)
            if response.status_code != 200:
                return items
            story_ids = response.json()[: self.limit]
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
                top_comments = self._get_top_comments_firebase(kids)
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
                            "comments": data.get("descendants", 0),
                        },
                        top_comments=top_comments,
                    )
                )
        except Exception:
            return items
        return items

    def _get_top_comments_firebase(self, kids: list, limit: int = 4) -> List[CommentItem]:
        candidates: List[CommentItem] = []
        if not kids:
            return candidates
        for kid_id in kids[:10]:
            try:
                kid_res = requests.get(f"{self.base_url}/item/{kid_id}.json", timeout=4)
                if kid_res.status_code == 200:
                    c_data = kid_res.json()
                    if c_data and c_data.get("type") == "comment" and not c_data.get("deleted", False):
                        text = c_data.get("text", "")
                        author = c_data.get("by", "HN User")
                        if text and len(text) > 15:
                            candidates.append(CommentItem(author=author, text=text[:350], votes=0))
            except Exception:
                continue
        candidates.sort(key=lambda c: len(c.text), reverse=True)
        return candidates[:limit]
