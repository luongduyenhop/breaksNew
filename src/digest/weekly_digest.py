"""Weekly digest builder for the career-roadmap workflow.

The daily briefing is written for a human skimming over coffee. A roadmap
advisor (ChatGPT, in Luong's setup) needs something else: a *compressed,
deduplicated* view of the whole week where a signal that repeats on
several days is visibly stronger than a one-day headline. This module
builds exactly that from the committed daily reports — deterministically,
with no extra AI call:

- market/direction bullets from sections 1-2 of each daily report,
  deduplicated across days and annotated with how many days they appeared;
- the best practitioner comments from section 4 of each report;
- written to reports/digests/ROADMAP_DIGEST_<iso-week>.md plus a stable
  reports/digests/LATEST.md — the fixed URL the ChatGPT scheduled task
  fetches every week.
"""
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List, Tuple

from src.filters.relevance import fold_text

REPORT_NAME_RE = re.compile(r"IT_Briefing_(\d{4}-\d{2}-\d{2})\.md$")
MAX_SIGNAL_LINES = 40
MAX_COMMENT_BLOCKS = 10


def _sections(markdown: str) -> Dict[str, List[str]]:
    """Split a daily report into {section-number: lines} by '## N.' headers."""
    sections: Dict[str, List[str]] = {}
    current = None
    for line in markdown.splitlines():
        header = re.match(r"^##\s+(\d+)\.", line)
        if header:
            current = header.group(1)
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return sections


def _bullets(lines: List[str]) -> List[str]:
    """Top-level bullet texts (markdown stripped of the leading '- ')."""
    out = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            out.append(stripped[2:].strip())
        elif re.match(r"^###\s", stripped):
            out.append(stripped.lstrip("# ").strip())
    return [b for b in out if len(b) > 25]


def _dedupe_key(text: str) -> str:
    folded = fold_text(text)
    folded = re.sub(r"[^a-z0-9 ]+", " ", folded)
    return re.sub(r"\s+", " ", folded).strip()[:110]


def collect_signals(reports: List[Tuple[str, str]]) -> List[dict]:
    """Merge sections 1+2 bullets across (date, markdown) reports.

    Returns entries {text, days: set[date-str], latest} sorted by how many
    days they appeared on, then recency — repetition is the trend signal.
    """
    merged: Dict[str, dict] = {}
    for day, markdown in reports:
        sections = _sections(markdown)
        for section_no in ("1", "2"):
            for bullet in _bullets(sections.get(section_no, [])):
                key = _dedupe_key(bullet)
                if not key:
                    continue
                entry = merged.setdefault(
                    key, {"text": bullet, "days": set(), "latest": day}
                )
                entry["days"].add(day)
                if day >= entry["latest"]:
                    entry["latest"] = day
                    entry["text"] = bullet
    signals = sorted(
        merged.values(),
        key=lambda e: (len(e["days"]), e["latest"]),
        reverse=True,
    )
    return signals[:MAX_SIGNAL_LINES]


def collect_comments(reports: List[Tuple[str, str]]) -> List[str]:
    """Best-comment blocks from section 4 of each report, deduped."""
    blocks: List[str] = []
    seen = set()
    for day, markdown in reversed(reports):  # newest first
        lines = _sections(markdown).get("4", [])
        current: List[str] = []
        entries: List[List[str]] = []
        for line in lines:
            if re.match(r"^\d+\.\s", line.strip()):
                if current:
                    entries.append(current)
                current = [line]
            elif current:
                current.append(line)
        if current:
            entries.append(current)
        for entry_lines in entries:
            text = "\n".join(entry_lines).strip()
            key = _dedupe_key(text)[:60]
            if text and key not in seen:
                seen.add(key)
                blocks.append(f"_(ngày {day})_\n\n{text}")
        if len(blocks) >= MAX_COMMENT_BLOCKS:
            break
    return blocks[:MAX_COMMENT_BLOCKS]


def build_digest(reports: List[Tuple[str, str]], generated_on: date) -> str:
    """reports: list of (YYYY-MM-DD, markdown). Returns digest markdown."""
    reports = sorted(reports)
    days = [d for d, _ in reports]
    signals = collect_signals(reports)
    comments = collect_comments(reports)
    repeated = [s for s in signals if len(s["days"]) >= 2]
    one_off = [s for s in signals if len(s["days"]) < 2]

    lines = [
        "# DIGEST TUẦN — TÍN HIỆU THỊ TRƯỜNG IT CHO LỘ TRÌNH NGHỀ NGHIỆP",
        "",
        f"- Giai đoạn dữ liệu: {days[0]} → {days[-1]} ({len(reports)} bản tin ngày)",
        f"- Ngày sinh digest: {generated_on.isoformat()}",
        "- Nguồn: bản tin định hướng ngành IT hằng ngày (đã lọc theo chủ đề thị trường/"
        "hướng đi/sự nghiệp, ưu tiên bình luận của senior/tech lead/PM).",
        "- Cách đọc: tín hiệu xuất hiện nhiều ngày = xu hướng đáng tin; tín hiệu 1 ngày"
        " = tham khảo, chờ xác nhận thêm.",
        "",
        "## A. TÍN HIỆU LẶP LẠI NHIỀU NGÀY (xu hướng)",
        "",
    ]
    if repeated:
        for s in repeated:
            lines.append(f"- ({len(s['days'])} ngày) {s['text']}")
    else:
        lines.append("- (Chưa có tín hiệu nào lặp lại — dữ liệu mới tích lũy vài ngày đầu.)")
    lines += ["", "## B. TÍN HIỆU ĐÁNG CHÚ Ý KHÁC TRONG TUẦN", ""]
    for s in one_off[:25]:
        lines.append(f"- ({s['latest']}) {s['text']}")
    lines += ["", "## C. LỜI KHUYÊN / BÌNH LUẬN ĐỊNH HƯỚNG NỔI BẬT", ""]
    if comments:
        for block in comments:
            lines.append(block)
            lines.append("")
    else:
        lines.append("- (Chưa có bình luận nổi bật trong kỳ.)")
    lines += [
        "",
        "---",
        "Digest được sinh tự động từ các bản tin ngày trong repo breaksNew "
        "(reports/digests/LATEST.md luôn là bản mới nhất).",
    ]
    return "\n".join(lines) + "\n"


def load_recent_reports(reports_dir: Path, days: int = 7) -> List[Tuple[str, str]]:
    found: List[Tuple[str, str]] = []
    for path in sorted(reports_dir.glob("IT_Briefing_*.md")):
        match = REPORT_NAME_RE.search(path.name)
        if match:
            found.append((match.group(1), path.read_text(encoding="utf-8")))
    return found[-days:]


def write_digest(reports_dir: Path, out_dir: Path, today: date = None) -> List[Path]:
    today = today or date.today()
    reports = load_recent_reports(reports_dir)
    if not reports:
        return []
    content = build_digest(reports, generated_on=today)
    iso_year, iso_week, _ = today.isocalendar()
    dated = out_dir / f"ROADMAP_DIGEST_{iso_year}-W{iso_week:02d}.md"
    latest = out_dir / "LATEST.md"
    out_dir.mkdir(parents=True, exist_ok=True)
    dated.write_text(content, encoding="utf-8")
    latest.write_text(content, encoding="utf-8")
    return [dated, latest]


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    written = write_digest(root / "reports", root / "reports" / "digests")
    for path in written:
        print(f"Wrote {path}")
