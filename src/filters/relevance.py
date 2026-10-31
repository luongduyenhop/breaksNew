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
    # Major technology/security incidents (a Log4Shell/PHP2Shell-class
    # event, a mass breach, a hyperscaler outage). The keywords here are
    # deliberately BROAD candidate generators ("lỗ hổng", "vulnerability")
    # — admission is decided by the severity gate in score_item: without
    # hard severity evidence (CVE/CVSS/KEV/exploitation...) the match is
    # discarded, so routine "a vulnerability was found" items cannot ride
    # this group into the briefing. (Verified against the real CMC
    # PHP2Shell headline, which contains no neat keyword phrase.)
    "su_co_lon": [
        "lỗ hổng", "lỗ hổng bảo mật", "lỗ hổng nghiêm trọng", "zero-day",
        "zero day", "ransomware", "mã độc tống tiền", "data breach",
        "breach", "rò rỉ dữ liệu", "sự cố an ninh mạng", "sự cố bảo mật",
        "an ninh mạng", "tấn công mạng", "critical vulnerability",
        "vulnerability", "exploit", "security breach", "mass outage",
        "sập hệ thống", "khai thác lỗ hổng",
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
INSIGHT_BONUS_CAP = 12.0

# Phrases that mark a comment as *directional insight* — a practitioner
# explaining what the industry shift means, what to learn, which mindset to
# adopt — as opposed to reactions/jokes. Written unfolded; they are folded
# before matching, like topic keywords.
INSIGHT_PHRASES = [
    "nên học", "cần học", "học những gì", "kỹ năng", "ky nang", "nghiệp vụ",
    "business", "tư duy", "mindset", "kinh nghiệm", "hệ thống", "toàn hệ thống",
    "làm việc với mọi người", "kỹ năng mềm", "soft skill", "áp dụng",
    "thực tế là", "trước mặt rồi", "không phải tương lai", "nâng cấp bản thân",
    "tự học", "định hướng", "lời khuyên", "should learn", "focus on",
    "instead of", "what matters", "in the future", "adapt", "upskill",
    "understand the business", "communication skill",
]


EXPERT_BONUS_CAP = 10.0
VN_REGION_BOOST = 4.0

# --- Major-incident severity gate -------------------------------------
# An item may *mention* a vulnerability and still be routine noise. It
# only counts as a major incident when independent severity evidence is
# present: a CVE id, a critical CVSS score, CISA KEV listing, confirmed
# in-the-wild exploitation, emergency patching, or mass scale. The gate
# is deliberately evidence-based rather than keyword-based.
INCIDENT_TOPIC = "su_co_lon"
INCIDENT_GATE_MIN = 6.0
INCIDENT_BONUS_CAP = 12.0

_CVE_RE = re.compile(r"cve-\d{4}-\d{4,}")
_CVSS_CRITICAL_RE = re.compile(r"cvss[^0-9]{0,16}(9\.\d|10(?:\.0)?)")
_EXPLOITATION_PHRASES = [
    "exploited in the wild", "actively exploited", "known exploited",
    "dang bi khai thac", "khai thac thuc te", "khai thac trong thuc te",
    "da bi khai thac",
]
_EMERGENCY_PATCH_PHRASES = [
    "emergency patch", "emergency security release", "out-of-cycle",
    "va khan cap", "ban va khan", "cap nhat ngay lap tuc", "patch now",
]
_SCALE_PHRASES = [
    "million", "trieu", "dien rong", "nationwide", "toan cau",
    "global outage", "worldwide", "hang trieu", "hang chuc trieu",
]


def incident_severity_score(item: RawItem) -> float:
    """Evidence-based severity of a suspected major incident (0..~19).

    Signals stack: a bare CVE id (5) is not enough to pass the gate on
    its own; CVE + exploitation, KEV + CVSS, exploitation + emergency
    patching, etc. are. Matching runs on folded title + body + comments.
    """
    haystack = fold_text(
        f"{item.title} {item.summary_text} "
        + " ".join(c.text for c in item.top_comments)
    )
    score = 0.0
    if _CVE_RE.search(haystack):
        score += 5.0
    if _CVSS_CRITICAL_RE.search(haystack):
        score += 4.0
    if "kev" in haystack or "known exploited vulnerabilities" in haystack:
        score += 4.0
    if any(phrase in haystack for phrase in _EXPLOITATION_PHRASES):
        score += 4.0
    if any(phrase in haystack for phrase in _EMERGENCY_PATCH_PHRASES):
        score += 2.0
    scale_hits = sum(1 for phrase in _SCALE_PHRASES if phrase in haystack)
    score += min(4.0, scale_hits * 2.0)
    return score


def is_major_incident(item: RawItem) -> bool:
    """True when the scorer kept the incident topic (gate passed)."""
    return INCIDENT_TOPIC in (item.matched_topics or [])

# Signals that the author/speaker is a seasoned practitioner — a senior,
# tech lead, PM or engineering manager — rather than a beginner or a news
# aggregator. The reader explicitly wants advice from people in those
# seats. Written unfolded; folded before matching.
EXPERT_ROLE_TERMS = [
    "senior engineer", "senior developer", "senior software",
    "tech lead", "team lead", "engineering manager", "project manager",
    "product manager", "staff engineer", "principal engineer",
    "principal software", "software architect", "solutions architect",
    "cto", "chief technology officer", "head of engineering",
    "vp of engineering", "trưởng nhóm", "trưởng phòng kỹ thuật",
    "quản lý dự án", "quản lý sản phẩm", "giám đốc công nghệ",
    "kiến trúc sư phần mềm", "techlead",
]

EXPERIENCE_PHRASES = [
    "years of experience", "in my experience", "my team", "our team",
    "when i led", "i have worked", "i've worked", "after years",
    "năm kinh nghiệm", "kinh nghiệm của tôi", "team của tôi",
    "đội của tôi", "khi tôi làm lead", "tôi từng làm", "sau nhiều năm đi làm",
    "nhiều năm đi làm",
]


def expert_voice_score(item: RawItem) -> float:
    """How strongly an item reads as a seasoned practitioner's voice (0-10).

    Role terms in the title are the strongest signal; role terms in the
    body and first-person experience phrases in body/comments add less.
    """
    title = fold_text(item.title)
    body = fold_text(item.summary_text)
    comments_text = fold_text(" ".join(c.text for c in item.top_comments))
    score = 0.0
    if any(_contains(title, fold_text(term)) for term in EXPERT_ROLE_TERMS):
        score += 6.0
    elif any(_contains(body, fold_text(term)) for term in EXPERT_ROLE_TERMS):
        score += 3.0
    haystack = f"{body} {comments_text}"
    exp_hits = sum(
        1 for phrase in EXPERIENCE_PHRASES if _contains(haystack, fold_text(phrase))
    )
    score += min(3.0, exp_hits * 1.5)
    return min(EXPERT_BONUS_CAP, score)


def comment_insight_score(text: str) -> float:
    """Score one comment's directional-insight value (0..~12).

    Phrase hits dominate; a small bonus for substantive length (a real
    argument rarely fits in one line). Votes are handled by the caller —
    a high-insight comment with few votes can still be the best one.
    """
    folded = fold_text(text or "")
    if not folded:
        return 0.0
    hits = sum(1 for phrase in INSIGHT_PHRASES if _contains(folded, fold_text(phrase)))
    score = min(10.0, hits * 2.5)
    if len(folded) >= 280:
        score += 2.0
    elif len(folded) >= 150:
        score += 1.0
    return score


def rank_comments(comments, limit: int = None):
    """Order comments by insight first, then community votes."""
    ranked = sorted(
        comments,
        key=lambda c: (comment_insight_score(c.text), c.votes),
        reverse=True,
    )
    return ranked[:limit] if limit else ranked


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



# Freshness gradient (PR #10): the old flat "+5 if <=2 days" treated a
# 1-hour-old and a 47-hour-old item as equally fresh, so re-running the
# pipeline later the same day resurfaced the same stories. The bonus now
# decays by AGE IN HOURS, so whatever was published most recently at run
# time floats to the top of every run.
FRESHNESS_TIERS_HOURS = [
    (3, 12.0), (6, 10.0), (12, 8.0), (24, 6.0),
    (48, 4.0), (72, 2.0), (168, 1.0),
]
STALE_PENALTY_DAYS = 30
STALE_PENALTY = -10.0


def freshness_bonus(age_hours: float) -> float:
    """Recency bonus for an item's age in hours (negative if ancient)."""
    if age_hours is None:
        return 0.0
    if age_hours > STALE_PENALTY_DAYS * 24:
        return STALE_PENALTY
    for limit_hours, bonus in FRESHNESS_TIERS_HOURS:
        if age_hours <= limit_hours:
            return bonus
    return 0.0


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
            if topic_points and topic == INCIDENT_TOPIC:
                severity = incident_severity_score(item)
                if severity < INCIDENT_GATE_MIN:
                    reasons.append(
                        f"su_co_lon: khớp '{hit}' nhưng không đạt cổng "
                        f"nghiêm trọng (severity {severity:.0f} < "
                        f"{INCIDENT_GATE_MIN:.0f}) — không tính điểm"
                    )
                    continue
                severity_bonus = min(INCIDENT_BONUS_CAP, severity)
                score += severity_bonus
                reasons.append(
                    f"sự cố lớn đạt cổng nghiêm trọng "
                    f"(severity {severity:.0f}, +{severity_bonus:.0f})"
                )
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

            insight_bonus = min(
                INSIGHT_BONUS_CAP,
                sum(comment_insight_score(c.text) for c in item.top_comments),
            )
            if insight_bonus > 0:
                score += insight_bonus
                reasons.append(f"bình luận có giá trị định hướng (+{insight_bonus:.0f})")

        expert_bonus = expert_voice_score(item)
        if expert_bonus > 0:
            score += expert_bonus
            reasons.append(f"tiếng nói chuyên gia/thâm niên (+{expert_bonus:.0f})")

        if item.region == "VN":
            score += VN_REGION_BOOST
            reasons.append(f"ưu tiên thị trường VN (+{VN_REGION_BOOST:.0f})")

        published_ts = _parse_published_ts(item.published_at)
        if published_ts:
            age_hours = max(0.0, (now_ts - published_ts) / 3600)
            bonus = freshness_bonus(age_hours)
            if bonus > 0:
                score += bonus
                reasons.append(f"độ mới {age_hours:.0f}h (+{bonus:.0f})")
            elif bonus < 0:
                score += bonus
                reasons.append(f"cũ >{STALE_PENALTY_DAYS} ngày ({bonus:.0f})")

        item.relevance_score = round(score, 1)
        item.matched_topics = matched_topics
        item.score_reason = "; ".join(reasons) if reasons else "không khớp chủ đề nào"
        return item

    def score_and_filter(self, items: List[RawItem]) -> Tuple[List[RawItem], List[RawItem]]:
        """Score everything, return (kept sorted by score, dropped)."""
        scored = [self.score_item(item) for item in items]
        scored.sort(
            key=lambda i: (i.relevance_score, _parse_published_ts(i.published_at)),
            reverse=True,
        )

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
