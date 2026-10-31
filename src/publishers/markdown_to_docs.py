"""Convert report markdown into Google Docs formatting requests.

Previously the publisher inserted raw markdown into the document, so the
Doc showed literal '#', '**' and '[]()' characters — the opposite of the
'standardized, easy to read' output the briefing needs. This module parses
markdown into plain-text blocks (headings, bullets, quotes, paragraphs)
with inline spans (bold, italic, links), then builds Docs API batchUpdate
requests: one insertText for the whole plain text, followed by
updateParagraphStyle / createParagraphBullets / updateTextStyle requests
with exact character ranges.
"""
import re
from typing import List, Optional

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_QUOTE_RE = re.compile(r"^>\s?(.*)$")
_BULLET_RE = re.compile(r"^[-*+]\s+(.*)$")
_NUMBERED_RE = re.compile(r"^\d+[.)]\s+(.*)$")
_HR_RE = re.compile(r"^(\*\*\*|---|___)\s*$")
_INLINE_RE = re.compile(
    r"(\*\*.+?\*\*|\*[^*\n]+?\*|`[^`\n]+?`|\[[^\]\n]+\]\([^)\n]+\))"
)
_LINK_RE = re.compile(r"^\[([^\]]+)\]\(([^)]+)\)$")

_HEADING_STYLES = {
    1: "TITLE",
    2: "HEADING_1",
    3: "HEADING_2",
    4: "HEADING_3",
    5: "HEADING_4",
    6: "HEADING_5",
}


def _parse_inline(text: str):
    """Return (plain_text, spans) with markdown markers removed.

    Spans are dicts: {start, length, bold, italic, link_url} with offsets
    relative to the start of the plain text.
    """
    plain_parts: List[str] = []
    spans = []
    pos = 0
    cursor = 0
    for match in _INLINE_RE.finditer(text):
        if match.start() > pos:
            chunk = text[pos:match.start()]
            plain_parts.append(chunk)
            cursor += len(chunk)
        token = match.group(0)
        link_match = _LINK_RE.match(token)
        if token.startswith("**") and token.endswith("**"):
            inner = token[2:-2]
            spans.append({"start": cursor, "length": len(inner), "bold": True})
            plain_parts.append(inner)
            cursor += len(inner)
        elif link_match:
            inner, url = link_match.group(1), link_match.group(2)
            spans.append({"start": cursor, "length": len(inner), "link_url": url})
            plain_parts.append(inner)
            cursor += len(inner)
        elif token.startswith("`"):
            inner = token[1:-1]
            plain_parts.append(inner)
            cursor += len(inner)
        else:  # *italic*
            inner = token[1:-1]
            spans.append({"start": cursor, "length": len(inner), "italic": True})
            plain_parts.append(inner)
            cursor += len(inner)
        pos = match.end()
    if pos < len(text):
        plain_parts.append(text[pos:])
    return "".join(plain_parts), spans


def parse_markdown_blocks(markdown: str) -> List[dict]:
    """Split markdown into styled blocks with plain (marker-free) text."""
    blocks: List[dict] = []
    for raw_line in (markdown or "").splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if _HR_RE.match(line.strip()):
            continue

        named_style = "NORMAL_TEXT"
        bullet = False
        quote = False
        content = line.strip()

        heading = _HEADING_RE.match(content)
        quote_match = _QUOTE_RE.match(content)
        bullet_match = _BULLET_RE.match(content) or _NUMBERED_RE.match(content)
        if heading:
            level = len(heading.group(1))
            named_style = _HEADING_STYLES.get(level, "HEADING_5")
            content = heading.group(2)
        elif quote_match:
            quote = True
            content = quote_match.group(1)
        elif bullet_match:
            bullet = True
            content = bullet_match.group(1)

        plain, spans = _parse_inline(content)
        if quote and plain:
            spans.append({"start": 0, "length": len(plain), "italic": True})
        if plain:
            blocks.append({
                "text": plain,
                "named_style": named_style,
                "bullet": bullet,
                "spans": spans,
            })
    return blocks


def build_docs_requests(markdown: str, start_index: int = 1,
                        tab_id: Optional[str] = None) -> dict:
    """Build {full_text, requests} for a Docs batchUpdate call.

    Character ranges follow the Docs API convention: indices are 1-based
    positions in the document body (or tab), and each block's range covers
    its text plus the trailing newline.
    """
    blocks = parse_markdown_blocks(markdown)
    full_text = "".join(block["text"] + "\n" for block in blocks)

    location = {"index": start_index}
    if tab_id:
        location["tabId"] = tab_id
    requests = [{
        "insertText": {"location": location, "text": full_text}
    }]

    offset = start_index
    for block in blocks:
        block_start = offset
        block_end = offset + len(block["text"]) + 1  # include newline

        style_location = {"startIndex": block_start, "endIndex": block_end}
        if tab_id:
            style_location["tabId"] = tab_id

        if block["named_style"] != "NORMAL_TEXT":
            requests.append({
                "updateParagraphStyle": {
                    "range": dict(style_location),
                    "paragraphStyle": {"namedStyleType": block["named_style"]},
                    "fields": "namedStyleType",
                }
            })
        if block["bullet"]:
            requests.append({
                "createParagraphBullets": {
                    "range": dict(style_location),
                    "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
                }
            })
        for span in block["spans"]:
            span_range = {
                "startIndex": block_start + span["start"],
                "endIndex": block_start + span["start"] + span["length"],
            }
            if tab_id:
                span_range["tabId"] = tab_id
            text_style = {}
            fields = []
            if span.get("bold"):
                text_style["bold"] = True
                fields.append("bold")
            if span.get("italic"):
                text_style["italic"] = True
                fields.append("italic")
            if span.get("link_url"):
                text_style["link"] = {"url": span["link_url"]}
                fields.append("link")
            if text_style:
                requests.append({
                    "updateTextStyle": {
                        "range": span_range,
                        "textStyle": text_style,
                        "fields": ",".join(fields),
                    }
                })
        offset = block_end

    return {"full_text": full_text, "requests": requests}
