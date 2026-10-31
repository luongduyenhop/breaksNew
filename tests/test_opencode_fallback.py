"""OpenCode Zen fallback chain: runs only after Gemini fails."""
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analyzers import summarizer as summarizer_module
from src.analyzers.summarizer import MarketBriefingSynthesizer
from src.models.raw_item import CommentItem, RawItem


def _item():
    return RawItem(
        id="x1", title="AI layoff discussion thi truong tuyen dung",
        source_name="HN", source_type="article", url="https://example.com/x",
        published_at="", summary_text="Noi dung ve thi truong IT va AI.",
        region="global", metrics={},
        top_comments=[CommentItem(author="a", text="nen hoc business", votes=3)],
        relevance_score=40.0,
    )


class _Resp:
    def __init__(self, status, payload=None, text=""):
        self.status_code = status
        self._payload = payload or {}
        self.text = text

    def json(self):
        return self._payload


def _synth_without_gemini():
    synth = MarketBriefingSynthesizer.__new__(MarketBriefingSynthesizer)
    synth.client = None
    synth.used_fallback = False
    return synth


class OpenCodeFallbackTests(unittest.TestCase):
    def test_no_key_skips_chain(self):
        synth = _synth_without_gemini()
        with patch.dict(os.environ, {}, clear=True):
            self.assertIsNone(synth._try_opencode_chain("prompt"))

    def test_zen_success_returns_report(self):
        synth = _synth_without_gemini()
        ok = _Resp(200, {"choices": [{"message": {"content": "BAO CAO TU ZEN"}}]})
        env = {"OPENCODE_" + "API_KEY": "k"}
        with patch.dict(os.environ, env, clear=True), \
             patch.object(summarizer_module.requests, "post", return_value=ok) as post:
            report = synth._try_opencode_chain("prompt")
        self.assertEqual(report, "BAO CAO TU ZEN")
        self.assertIn("deepseek-v4.1-flash-free", str(post.call_args))

    def test_zen_gate_error_falls_through_to_local_fallback(self):
        synth = _synth_without_gemini()
        gated = _Resp(403, text='{"error":"FreeTierError"}')
        env = {"OPENCODE_" + "API_KEY": "k"}
        with patch.dict(os.environ, env, clear=True), \
             patch.object(summarizer_module.requests, "post", return_value=gated):
            report = synth.analyze_and_synthesize([_item()])
        self.assertTrue(synth.used_fallback)
        self.assertIn("Cảnh báo", report)

    def test_model_roster_override(self):
        synth = _synth_without_gemini()
        with patch.dict(os.environ, {"OPENCODE_MODELS": "a-free, b-free"}, clear=True):
            self.assertEqual(synth._opencode_models(), ["a-free", "b-free"])


if __name__ == "__main__":
    unittest.main()
