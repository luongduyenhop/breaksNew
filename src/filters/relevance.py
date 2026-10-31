"""Relevance scoring for the IT-market briefing.

The collectors gather *everything recent* from each source. This module is
the missing editorial layer: it scores every item against the topic groups
the briefing is actually about (the IT job market, AI-driven new directions,
and career survival), explains the score, and keeps only items that clear a
threshold. Matching is accent-insensitive so Vietnamese keywords match both
accented and unaccented text.
"""
import math
import re
import time
import unicodedata
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Dict, List, Tuple

from src.models.raw_item import RawItem

DEFAULT_TOPIC_GROUPS: Dict[str, List[str]] = {
    "thi_truong_tuyen_dung": [
        "layoff", "laid off", "sa thải", "cắt giảm nhân sự", "mất việc",
        "job market", "thị trường việc làm", "thị trường tuyển dụng",
        "tuyển dụng", "hiring", "đóng băng tuyển dụng", "mức lương", "lương dev",
        "lương it", "salary", "tech job", "tech market",
        "thị trường it", "it market", "nhu cầu tuyển dụng", "khó xin việc",
        "thất nghiệp", "unemployment", "tech jobs",
    ],
    "ai_va_huong_di_moi": [
        "ai agent", "ai thay thế", "thay thế lập trình viên",
        "replacing developers", "replacing programmers", "isn't replacing",
        "future of coding", "future of programming", "tương lai của lập trình",
        "hướng đi mới", "xu hướng mới", "vibe coding", "ai engineer",
        "kỹ sư ai", "deskilling", "ai bubble", "bong bóng ai",
        "prompt engineer", "llm engineer",
        "trí tuệ nhân tạo",
    ],
    "career_survival": [
        "junior", "fresher", "senior", "mới ra trường", "career advice",
        "lời khuyên nghề nghiệp", "bám trụ", "survive", "survival",
        "nên học gì", "học gì để", "chuyển ngành", "career change",
        "kinh nghiệm xin việc", "phỏng vấn", "interview", "experienced dev",
        "sự nghiệp", "career",
    ],
}

# Titles that look like pure tutorials / course episodes. They are only a
# problem when the item matches no briefing topic at all.
_TUTORIAL_PATTERNS = [
    r"\(\d+\)",            # "Kafka (10): ..." episode numbering
    r"\bepisode\s*\d+",
    r"\bseries\b",
    r"\btutorial\b",
    r"\bpart\s*\d+\b",
    r"hướng dẫn học",
    r"toàn tập",
]

TITLE_MATCH_POINTS = 30.0
BODY_MATCH_POINTS = 10.0
COMMENT_MATCH_POINTS = 6.0
COMMENT_MATCH_CAP = 12.0
NO_TOPIC_TUTORIAL_PENALTY = -25.0


def fold_text(text: str) -> str:
    """Lowercase and strip Vietnamese accents for keyword matching."""
    if not text:
        return ""
    decomposed = unicodedata.normalize("NFD", text.lower())
    folded = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    # đ/Đ are not decomposed by NFD
    return folded.replace("đ", "d")


def _contains(folded_text: str, folded_keyword: str) -> bool:
    if not folded_keyword:
        return False
    if len(folded_keyword) <= 3:
        return re.search(rf"\b{re.escape(folded_keyword)}\b", folded_text) is not None
    return folded_keyword in folded_text


def _parse_published_ts(published_at: str) -> float:
    """Best-effort parse of the collectors' published_at formats."""
    if not published_at:
        return 0.0
    raw = str(published_at).strip()
    try:
        return float(raw)  # epoch seconds (Reddit / Hacker News)
    except ValueError:
        pass
    try:
        dt = parsedate_to_datetime(raw)  # RFC 2822 (YouTube / RSS feeds)
        if dt is not None:
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.timestamp()
    except (TypeError, ValueError):
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.timestamp()
        except ValueError:
            continue
    return 0.0


class RelevanceScorer:
    def __init__(self, topic_groups: Dict[str, List[str]] = None,
                 min_score: float = 25.0, per_source_cap: int = 6,
                 total_cap: int = 40, max_age_days: int = 7):
        groups = topic_groups or DEFAULT_TOPIC_GROUPS
        self.topic_groups = {
            topic: [fold_text(kw) for kw in keywords]
            for topic, keywords in groups.items()
        }
        self.min_score = min_score
        self.per_source_cap = per_source_cap
        self.total_cap = total_cap
        self.max_age_days = max_age_days

    def score_item(self, item: RawItem, now_ts: float = None) -> RawItem:
        now_ts = now_ts or time.time()
        title = fold_text(item.title)
        body = fold_text(item.summary_text)
        comments_text = fold_text(" ".join(c.text for c in item.top_comments))

        score = 0.0
        matched_topics: List[str] = []
        reasons: List[str] = []

        for topic, keywords in self.topic_groups.items():
            topic_points = 0.0
            hit = ""
            # Title matches outrank body matches, so scan ALL keywords
            # against the title first, then all against the body.
            for kw in keywords:
                if _contains(title, kw):
                    topic_points += TITLE_MATCH_POINTS
                    hit = kw
                    break
            if not topic_points:
                for kw in keywords:
                    if _contains(body, kw):
                        topic_points += BODY_MATCH_POINTS
                        hit = kw
                        break
            if topic_points:
                comment_points = 0.0
                for kw in keywords:
                    if _contains(comments_text, kw):
                        comment_points = min(COMMENT_MATCH_POINTS, COMMENT_MATCH_CAP)
                        break
                score += topic_points + comment_points
                matched_topics.append(topic)
                reasons.append(f"{topic}: khớp '{hit}' (+{topic_points + comment_points:.0f})")

        if re.search(r"\bseries\b|#\d+|\bepisode\b", title):
            score -= 15
            reasons.append("tiêu đề dạng series/khóa học (-15)")

        if not matched_topics:
            if any(re.search(p, title) for p in _TUTORIAL_PATTERNS):
                score += NO_TOPIC_TUTORIAL_PENALTY
                reasons.append(f"trông giống tutorial/khóa học, không khớp chủ đề ({NO_TOPIC_TUTORIAL_PENALTY:.0f})")

        engagement = max(
            [int(v) for v in (item.metrics or {}).values() if isinstance(v, (int, float))]
            or [0]
        )
        if engagement > 0:
            bonus = min(10.0, math.log10(1 + engagement) * 3)
            score += bonus
            reasons.append(f"tương tác (+{bonus:.0f})")

        if item.top_comments:
            bonus = min(6.0, len(item.top_comments) * 1.5)
            score += bonus
            reasons.append(f"có {len(item.top_comments)} bình luận cộng đồng (+{bonus:.0f})")

        published_ts = _parse_published_ts(item.published_at)
        if published_ts:
            age_days = max(0.0, (now_ts - published_ts) / 86400)
            if age_days <= 2:
                score += 5
                reasons.append("mới <=2 ngày (+5)")
            elif age_days <= self.max_age_days:
                score += 2
                reasons.append("mới <=7 ngày (+2)")
            elif age_days > 30:
                score -= 10
                reasons.append("cũ >30 ngày (-10)")

        item.relevance_score = round(score, 1)
        item.matched_topics = matched_topics
        item.score_reason = "; ".join(reasons) if reasons else "không khớp chủ đề nào"
        return item

    def score_and_filter(self, items: List[RawItem]) -> Tuple[List[RawItem], List[RawItem]]:
        """Score everything, return (kept sorted by score, dropped)."""
        scored = [self.score_item(item) for item in items]
        scored.sort(key=lambda i: i.relevance_score, reverse=True)

        kept: List[RawItem] = []
        dropped: List[RawItem] = []
        per_source_count: Dict[str, int] = {}
        for item in scored:
            if item.relevance_score < self.min_score or not item.matched_topics:
                dropped.append(item)
                continue
            count = per_source_count.get(item.source_name, 0)
            if count >= self.per_source_cap or len(kept) >= self.total_cap:
                dropped.append(item)
                continue
            per_source_count[item.source_name] = count + 1
            kept.append(item)
        return kept, dropped
