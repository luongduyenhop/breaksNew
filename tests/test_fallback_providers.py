"""Fallback providers: OpenRouter (full prompt) + Groq (compact prompt)."""
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analyzers import summarizer as summarizer_module
from src.analyzers.summarizer import (
    GROQ_DEFAULT_MODELS,
    OPENROUTER_DEFAULT_MODELS,
    MarketBriefingSynthesizer,
)
from src.models.raw_item import CommentItem, RawItem

OR_KEY = "OPENROUTER_" + "API_KEY"
GROQ_KEY = "GROQ_" + "API_KEY"


def _big_item(idx=0):
    return RawItem(
        id=f"x{idx}", title="AI layoff discussion thi truong tuyen dung",
        source_name="HN", source_type="article", url="https://example.com/x",
        published_at="", summary_text="S" * 2000,
        region="VN", metrics={},
        top_comments=[CommentItem(author="a", text="C" * 700, votes=3) for _ in range(4)],
        relevance_score=40.0,
    )


def _synth(client=None):
    synth = MarketBriefingSynthesizer.__new__(MarketBriefingSynthesizer)
    synth.client = client
    synth.used_fallback = False
    return synth


class _Resp:
    def __init__(self, status, payload=None, text=""):
        self.status_code = status
        self._payload = payload or {}
        self.text = text

    def json(self):
        return self._payload


_OK = _Resp(200, {"choices": [{"message": {"content": "BAO CAO"}}]})


class OpenRouterChainTests(unittest.TestCase):
    def test_no_key_skips_without_http(self):
        synth = _synth()
        with patch.dict(os.environ, {}, clear=True), \
             patch.object(summarizer_module.requests, "post") as post:
            self.assertIsNone(synth._try_openrouter_chain("prompt"))
        post.assert_not_called()

    def test_success_uses_first_default_model(self):
        synth = _synth()
        with patch.dict(os.environ, {OR_KEY: "k"}, clear=True), \
             patch.object(summarizer_module.requests, "post", return_value=_OK) as post:
            self.assertEqual(synth._try_openrouter_chain("prompt"), "BAO CAO")
        self.assertIn(OPENROUTER_DEFAULT_MODELS[0], str(post.call_args))
        self.assertIn("openrouter.ai", str(post.call_args))

    def test_roster_override(self):
        synth = _synth()
        env = {OR_KEY: "k", "OPENROUTER_MODELS": "a:free, b:free"}
        with patch.dict(os.environ, env, clear=True), \
             patch.object(summarizer_module.requests, "post", return_value=_OK) as post:
            synth._try_openrouter_chain("prompt")
        self.assertIn("a:free", str(post.call_args))


class GroqChainTests(unittest.TestCase):
    def test_no_key_skips_without_http(self):
        synth = _synth()
        with patch.dict(os.environ, {}, clear=True), \
             patch.object(summarizer_module.requests, "post") as post:
            self.assertIsNone(synth._try_groq_chain("prompt"))
        post.assert_not_called()

    def test_success_uses_llama_70b_default(self):
        synth = _synth()
        self.assertEqual(GROQ_DEFAULT_MODELS, ["llama-3.3-70b-versatile"])
        with patch.dict(os.environ, {GROQ_KEY: "k"}, clear=True), \
             patch.object(summarizer_module.requests, "post", return_value=_OK) as post:
            self.assertEqual(synth._try_groq_chain("prompt"), "BAO CAO")
        self.assertIn("llama-3.3-70b-versatile", str(post.call_args))
        self.assertIn("api.groq.com", str(post.call_args))


class CompactPayloadTests(unittest.TestCase):
    def test_compact_trims_items_previews_and_comments(self):
        synth = _synth()
        items = [_big_item(i) for i in range(15)]
        ranked = synth._ranked(items)
        full = synth._build_payload(ranked)
        compact = synth._build_payload(ranked, compact=True)
        self.assertEqual(len(full[0]["top_comments"]), 4)
        self.assertEqual(len(full[0]["content_preview"]), 1000)
        self.assertEqual(len(full[0]["top_comments"][0]["text"]), 700)
        self.assertLessEqual(len(compact), 10)
        self.assertEqual(len(compact[0]["content_preview"]), 400)
        self.assertEqual(len(compact[0]["top_comments"]), 2)
        self.assertEqual(len(compact[0]["top_comments"][0]["text"]), 350)


class ChainOrderTests(unittest.TestCase):
    def _synth_gemini_dead(self):
        synth = _synth(client=object())
        synth._try_model = lambda model, prompt: None
        return synth

    def test_openrouter_wins_before_groq(self):
        synth = self._synth_gemini_dead()
        synth._try_openrouter_chain = lambda prompt: "OR REPORT"
        synth._try_groq_chain = lambda prompt: self.fail("Groq must not run")
        synth._try_opencode_chain = lambda prompt: self.fail("Zen must not run")
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(synth.analyze_and_synthesize([_big_item()]), "OR REPORT")

    def test_groq_gets_shorter_prompt_than_openrouter(self):
        synth = self._synth_gemini_dead()
        seen = {}

        def _record(name, result):
            def _fn(prompt):
                seen[name] = prompt
                return result
            return _fn

        synth._try_openrouter_chain = _record("or", None)
        synth._try_groq_chain = _record("groq", "GROQ REPORT")
        synth._try_opencode_chain = lambda prompt: self.fail("Zen must not run")
        items = [_big_item(i) for i in range(15)]
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(synth.analyze_and_synthesize(items), "GROQ REPORT")
        self.assertLess(len(seen["groq"]), len(seen["or"]))

    def test_no_gemini_client_still_tries_providers(self):
        synth = _synth(client=None)
        synth._try_openrouter_chain = lambda prompt: "OR REPORT"
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(synth.analyze_and_synthesize([_big_item()]), "OR REPORT")
        self.assertFalse(synth.used_fallback)


if __name__ == "__main__":
    unittest.main()
