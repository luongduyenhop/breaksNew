"""Gemini time budget: >2 min total on Gemini => switch to OpenCode Zen."""
import os
import sys
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analyzers.summarizer import GEMINI_TIME_BUDGET_SECS, MarketBriefingSynthesizer
from src.models.raw_item import CommentItem, RawItem


def _item():
    return RawItem(
        id="x1", title="AI layoff discussion thi truong tuyen dung",
        source_name="HN", source_type="article", url="https://example.com/x",
        published_at="", summary_text="Noi dung ve thi truong IT va AI.",
        region="VN", metrics={},
        top_comments=[CommentItem(author="a", text="nen hoc business", votes=3)],
        relevance_score=40.0,
    )


def _synth_with_client():
    synth = MarketBriefingSynthesizer.__new__(MarketBriefingSynthesizer)
    synth.client = object()  # truthy fake: enters the Gemini path
    synth.used_fallback = False
    return synth


class GeminiBudgetConfigTests(unittest.TestCase):
    def test_default_budget_is_120_seconds(self):
        self.assertEqual(GEMINI_TIME_BUDGET_SECS, 120)
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(MarketBriefingSynthesizer._gemini_budget_secs(), 120.0)

    def test_env_override_and_garbage_fallback(self):
        with patch.dict(os.environ, {"GEMINI_TIME_BUDGET_SECS": "45"}):
            self.assertEqual(MarketBriefingSynthesizer._gemini_budget_secs(), 45.0)
        with patch.dict(os.environ, {"GEMINI_TIME_BUDGET_SECS": "abc"}):
            self.assertEqual(MarketBriefingSynthesizer._gemini_budget_secs(), 120.0)


class GeminiBudgetBehaviorTests(unittest.TestCase):
    def test_slow_gemini_switches_to_zen_within_budget(self):
        synth = _synth_with_client()
        calls = []

        def slow_model(model, prompt):
            calls.append(model)
            time.sleep(5)
            return "LATE GEMINI REPORT"

        synth._try_model = slow_model
        synth._try_opencode_chain = lambda prompt: "ZEN REPORT"
        started = time.monotonic()
        with patch.dict(os.environ, {"GEMINI_TIME_BUDGET_SECS": "1"}, clear=True):
            result = synth.analyze_and_synthesize([_item()])
        elapsed = time.monotonic() - started
        self.assertEqual(result, "ZEN REPORT")
        self.assertLess(elapsed, 4.0)
        self.assertEqual(len(calls), 1)  # later candidates never attempted

    def test_fast_gemini_success_skips_zen(self):
        synth = _synth_with_client()
        synth._try_model = lambda model, prompt: "GEMINI OK"
        zen_calls = []
        synth._try_opencode_chain = lambda prompt: zen_calls.append(1) or "ZEN"
        with patch.dict(os.environ, {}, clear=True):
            result = synth.analyze_and_synthesize([_item()])
        self.assertEqual(result, "GEMINI OK")
        self.assertEqual(zen_calls, [])

    def test_all_gemini_fail_fast_still_reaches_zen(self):
        synth = _synth_with_client()
        calls = []
        synth._try_model = lambda model, prompt: calls.append(model) or None
        synth._try_opencode_chain = lambda prompt: "ZEN REPORT"
        with patch.dict(os.environ, {}, clear=True):
            result = synth.analyze_and_synthesize([_item()])
        self.assertEqual(result, "ZEN REPORT")
        self.assertEqual(len(calls), 4)  # all default candidates attempted


if __name__ == "__main__":
    unittest.main()
