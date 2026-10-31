import re
from typing import List
from urllib.parse import urlparse, parse_qs, urlunparse
from src.models.raw_item import RawItem, CommentItem

class DataNormalizer:
    def clean_text(self, text: str) -> str:
        if not text:
            return ""
        with_spaces = re.sub(r"<(?:p|div|br|li|h[1-6])[^>]*>", " ", text, flags=re.IGNORECASE)
        no_html = re.sub(r"<[^>]+>", "", with_spaces)
        no_links = re.sub(r"http\S+", "", no_html)
        no_duplicate_spaces = re.sub(r"\s+", " ", no_links).strip()
        cleaned = re.sub(r"\s+([.,!?:;])", r"\1", no_duplicate_spaces)
        return cleaned

    def clean_url(self, url: str) -> str:
        if not url:
            return ""
        parsed = urlparse(url)
        query_dict = parse_qs(parsed.query)
        filtered_query = {
            key: value for key, value in query_dict.items()
            if not key.startswith("utm_") and key not in {"fbclid", "ref", "source"}
        }
        rebuilt_query = "&".join(f"{k}={v[0]}" for k, v in filtered_query.items())
        return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, rebuilt_query, ""))

    def deduplicate_and_normalize(self, items: List[RawItem]) -> List[RawItem]:
        seen_urls = set()
        seen_titles = set()
        normalized_items = []
        for item in items:
            cleaned_url = self.clean_url(item.url)
            normalized_title = self.clean_text(item.title).lower()
            if not normalized_title or cleaned_url in seen_urls or normalized_title in seen_titles:
                continue
            seen_urls.add(cleaned_url)
            seen_titles.add(normalized_title)
            item.url = cleaned_url
            item.title = self.clean_text(item.title)
            item.summary_text = self.clean_text(item.summary_text)[:1500]

            cleaned_comments = []
            for comment in item.top_comments:
                cleaned_comment_text = self.clean_text(comment.text)[:300]
                if cleaned_comment_text and len(cleaned_comment_text) > 8:
                    cleaned_comments.append(
                        CommentItem(
                            author=comment.author,
                            text=cleaned_comment_text,
                            votes=comment.votes
                        )
                    )
            item.top_comments = cleaned_comments
            normalized_items.append(item)
        return normalized_items
