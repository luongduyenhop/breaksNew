from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class CommentItem:
    author: str
    text: str
    votes: int

@dataclass
class RawItem:
    id: str
    title: str
    source_name: str
    source_type: str
    url: str
    published_at: str
    summary_text: str
    region: str
    metrics: Dict[str, int]
    top_comments: List[CommentItem] = field(default_factory=list)
