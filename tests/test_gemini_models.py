"""Gemini model candidates + Interactions API fallback path."""
import os
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analyzers.summarizer import DEFAULT_MODELS, MarketBriefingSynthesizer
from src.models.raw_item import CommentItem, RawItem


def _item():
    return RawItem(
        id="x1",
        title="AI layoff discussion thi truong tuyen dung",
        source_name="HN",
        source_type="article",
        url="https://example.com/x",
        published_at="",
        summary_text="Noi dung ve thi truong tuyen dung IT va AI.",
        region="global",
        metrics={},
        top_comments=[CommentItem(author="a", text="nen hoc business", votes=3)],
        relevance_score=40.0,
    )


class _FailingModels:
    def generate_content(self, model, contents):
        raise RuntimeError("model unavailable on generateContent")


class _OkInteractions:
    def __init__(self, payload):
        self._payload = payload

    def create(self, model, input):
        return self._payload


class GeminiModelTests(unittest.TestCase):
    def test_default_models_start_with_current_flash(self):
        self.assertEqual(DEFAULT_MODELS[0], "gemini-3.8-flash")
        self.assertIn("gemini-3.6-flash", DEFAULT_MODELS)
        self.assertNotIn("gemini-2.0-flash", DEFAULT_MODELS)

    def test_extract_interaction_text_variants(self):
        extract = MarketBriefingSynthesizer._extract_interaction_text
        self.assertEqual(extract(SimpleNamespace(output_text="hello")), "hello")
        self.assertEqual(
            extract(SimpleNamespace(output_text=None, outputs=[SimpleNamespace(text="abc")])),
            "abc",
        )
        self.assertIsNone(extract(SimpleNamespace(output_text=None, outputs=[])))
        self.assertIsNone(extract(None))

    def test_interactions_fallback_produces_report(self):
        with patch.dict(os.environ, {}, clear=True):
            synth = MarketBriefingSynthesizer.__new__(MarketBriefingSynthesizer)
        synth.client = SimpleNamespace(
            models=_FailingModels(),
            interactions=_OkInteractions(SimpleNamespace(output_text="BAO CAO TU INTERACTIONS")),
        )
        synth.used_fallback = True
        with patch.dict(os.environ, {}, clear=True):
            report = synth.analyze_and_synthesize([_item()])
        self.assertEqual(report, "BAO CAO TU INTERACTIONS")
        self.assertFalse(synth.used_fallback)


if __name__ == "__main__":
    unittest.main()
