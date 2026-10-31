import re
from typing import List
from urllib.parse import urlparse, parse_qs, urlunparse
from src.models.raw_item import RawItem, CommentItem

# Lines that are channel/description boilerplate rather than content:
# subscription pitches, course/member sales, social links, sponsor blocks.
_BOILERPLATE_MARKERS = (
    "subscribe", "đăng ký kênh", "nhớ subscribe", "follow me", "discord",
    "khóa học", "khoa hoc", "hội viên", "member", "tham gia làm",
    "mua sách", "ủng hộ mình", "link đăng ký", "hot hot", "tiktok",
    "try ", " for free", "sign in with", "get 20%", "get 10%", "% off",
    "newsletter:", "courses:", "sponsor",
)


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

    def strip_boilerplate(self, text: str) -> str:
        """Drop promotional/description boilerplate lines before cleaning.

        YouTube descriptions in particular are mostly sales copy; feeding
        them to the summarizer made reports quote course ads as 'content'.
        Works line-by-line, so it must run before clean_text collapses
        whitespace.
        """
        if not text:
            return ""
        kept_lines = []
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            lowered = line.lower()
            if "http" in lowered or "www." in lowered:
                continue
            if any(marker in lowered for marker in _BOILERPLATE_MARKERS):
                continue
            if line.count("👉") or line.count("🔥") or line.count("🎦"):
                continue
            kept_lines.append(line)
        # Fallback: if line-based filtering removed everything (single-line
        # transcripts etc.), keep the original text untouched.
        return " ".join(kept_lines) if kept_lines else text

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
            summary_source = item.summary_text
            if item.source_type == "video":
                summary_source = self.strip_boilerplate(summary_source)
            item.summary_text = self.clean_text(summary_source)[:1500]

            cleaned_comments = []
            for comment in item.top_comments:
                cleaned_comment_text = self.clean_text(comment.text)[:700]  # long practitioner comments carry the directional insight — do not truncate at 300
                if cleaned_comment_text and len(cleaned_comment_text) > 8:
                    cleaned_comments.append(
                        CommentItem(
                            author=comment.author,
                            text=cleaned_comment_text,
                            votes=comment.votes
                        )
                    )
            # Highest-voted community voices first — the summarizer and the
            # fallback report both rely on this ordering.
            cleaned_comments.sort(key=lambda c: c.votes, reverse=True)
            item.top_comments = cleaned_comments
            normalized_items.append(item)
        return normalized_items
