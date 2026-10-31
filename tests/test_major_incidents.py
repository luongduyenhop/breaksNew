"""Major-incident group: severity gate, scoring, selection cap, fallback."""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analyzers.summarizer import MarketBriefingSynthesizer
from src.filters.relevance import (
    INCIDENT_GATE_MIN,
    RelevanceScorer,
    incident_severity_score,
    is_major_incident,
)
from src.models.raw_item import RawItem


def make_item(title, summary="", region="GLOBAL", score=0.0, topics=None):
    item = RawItem(
        id=f"item-{abs(hash(title))}",
        title=title,
        source_name="Test",
        source_type="article",
        url=f"https://example.com/{abs(hash(title))}",
        published_at="",
        summary_text=summary,
        region=region,
        metrics={"score": 10, "comments": 0},
        top_comments=[],
    )
    item.relevance_score = score
    item.matched_topics = topics or []
    return item


# The REAL CMC Cyber Security headline/summary from 23/10/2026 — kept
# verbatim on purpose: it contains no neat keyword phrase ("Lỗ hổng 9,2
# điểm phơi bày điểm mù bảo mật..."), which is exactly why the incident
# keywords are broad and the severity gate does the admitting.
PHP2SHELL_TITLE = "PHP2Shell: Lỗ hổng 9,2 điểm phơi bày “điểm mù” bảo mật doanh nghiệp"
PHP2SHELL_SUMMARY = (
    "Hai lỗ hổng CVE-2026-109618 và CVE-2026-109619 trong lõi PHP, CVSS 9.2, "
    "cho phép thực thi mã từ xa không cần đăng nhập. Amazon ghi nhận khai "
    "thác thực tế từ 17/10, CISA đưa vào KEV. Hơn 22,6 triệu điểm triển "
    "khai có khả năng bị ảnh hưởng; doanh nghiệp cần vá khẩn cấp và kiểm "
    "kê hệ thống PHP."
)


class SeverityGateTests(unittest.TestCase):
    def setUp(self):
        self.scorer = RelevanceScorer()

    def test_php2shell_like_item_passes_gate(self):
        item = make_item(PHP2SHELL_TITLE, PHP2SHELL_SUMMARY)
        self.assertGreaterEqual(incident_severity_score(item), INCIDENT_GATE_MIN)
        self.scorer.score_item(item)
        self.assertIn("su_co_lon", item.matched_topics)
        self.assertTrue(is_major_incident(item))
        self.assertGreaterEqual(item.relevance_score, 25)

    def test_routine_vulnerability_gated_out(self):
        item = make_item(
            "Lỗ hổng bảo mật trong plugin WordPress X được phát hiện",
            "Nhà phát triển đã phát hành bản sửa lỗi, người dùng nên cập nhật plugin.",
        )
        self.assertLess(incident_severity_score(item), INCIDENT_GATE_MIN)
        self.scorer.score_item(item)
        self.assertNotIn("su_co_lon", item.matched_topics)
        self.assertFalse(is_major_incident(item))

    def test_bare_cve_alone_below_gate(self):
        item = make_item(
            "Critical vulnerability CVE-2026-12345 disclosed in library foo",
            "A vulnerability was disclosed in a small JavaScript library.",
        )
        self.assertEqual(incident_severity_score(item), 5.0)  # CVE only
        self.scorer.score_item(item)
        self.assertNotIn("su_co_lon", item.matched_topics)


class SelectionCapTests(unittest.TestCase):
    def test_incidents_capped_at_three_in_prompt_selection(self):
        synth = MarketBriefingSynthesizer(api_key=None)
        incidents = [
            make_item(f"Major incident {n} CVE-2026-1000{n}", region="VN",
                      score=90 - n, topics=["su_co_lon"])
            for n in range(6)
        ]
        normals = [
            make_item(f"Career item {n}", region="VN",
                      score=80 - n, topics=["career_survival"])
            for n in range(20)
        ]
        ranked = sorted(incidents + normals,
                        key=lambda i: i.relevance_score, reverse=True)
        selected = synth._select_for_prompt(ranked)
        self.assertLessEqual(
            sum(1 for i in selected if is_major_incident(i)), 3
        )
        self.assertEqual(len(selected), 20)


class FallbackSectionTests(unittest.TestCase):
    def test_fallback_report_includes_incident_section(self):
        synth = MarketBriefingSynthesizer(api_key=None)
        scorer = RelevanceScorer()
        incident = scorer.score_item(make_item(PHP2SHELL_TITLE, PHP2SHELL_SUMMARY))
        report = synth._build_fallback_report([incident])
        self.assertIn("## SỰ CỐ CÔNG NGHỆ LỚN HÔM NAY", report)
        self.assertIn("PHP2Shell", report)

    def test_fallback_report_omits_section_without_incidents(self):
        synth = MarketBriefingSynthesizer(api_key=None)
        normal = make_item("Senior engineer career advice", topics=["career_survival"])
        normal.relevance_score = 40
        report = synth._build_fallback_report([normal])
        self.assertNotIn("SỰ CỐ CÔNG NGHỆ LỚN", report)


if __name__ == "__main__":
    unittest.main()
