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
    # Filled in by src.filters.relevance.RelevanceScorer during the pipeline.
    # Defaults keep collectors and older tests working without the scorer.
    relevance_score: float = 0.0
    matched_topics: List[str] = field(default_factory=list)
    score_reason: str = ""
