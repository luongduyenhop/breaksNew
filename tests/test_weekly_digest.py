"""Weekly digest builder: merge, dedupe, recurrence counting."""
import os
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.digest.weekly_digest import build_digest, collect_signals, write_digest

REPORT_A = """# BÁO CÁO

## 1. HƯỚNG ĐI
- AI Agent đang thay thế việc viết code thuần túy trong doanh nghiệp
- Thị trường tuyển dụng junior bị siết chặt vì layoff diện rộng

## 2. CẦN HỌC GÌ
- Kỹ năng hiểu business và toàn bộ hệ thống thay vì làm theo task

## 4. BÌNH LUẬN HAY NHẤT

1. **Bình luận từ `@senior_dev`** (YouTube - Kênh X)
   > Dev nên tập trung hiểu nghiệp vụ và hệ thống, code chỉ là phần nhỏ.
"""

REPORT_B = """# BÁO CÁO

## 1. HƯỚNG ĐI
- AI Agent đang thay thế việc viết code thuần túy trong doanh nghiệp
- Xu hướng AI local và bảo mật dữ liệu nội bộ tăng mạnh

## 2. CẦN HỌC GÌ
- Vector Databases và RAG cho hệ thống tri thức nội bộ doanh nghiệp

## 4. BÌNH LUẬN HAY NHẤT

1. **Bình luận từ `@techlead`** (YouTube - Kênh Y)
   > Khi làm lead tôi thấy kỹ năng giao tiếp quan trọng hơn kỹ năng code.
"""


class WeeklyDigestTests(unittest.TestCase):
    def test_repeated_signal_counted_across_days(self):
        signals = collect_signals([("2026-10-30", REPORT_A), ("2026-10-31", REPORT_B)])
        repeated = [s for s in signals if len(s["days"]) >= 2]
        self.assertTrue(any("AI Agent" in s["text"] for s in repeated))
        self.assertEqual(signals[0], repeated[0])  # repeated sorts first

    def test_digest_contains_all_sections(self):
        digest = build_digest(
            [("2026-10-30", REPORT_A), ("2026-10-31", REPORT_B)],
            generated_on=date(2026, 11, 2),
        )
        self.assertIn("## A. TÍN HIỆU LẶP LẠI", digest)
        self.assertIn("(2 ngày)", digest)
        self.assertIn("@senior_dev", digest)
        self.assertIn("@techlead", digest)
        self.assertIn("2026-10-30 → 2026-10-31", digest)

    def test_write_digest_creates_latest_and_dated(self):
        with tempfile.TemporaryDirectory() as tmp:
            reports_dir = Path(tmp) / "reports"
            reports_dir.mkdir()
            (reports_dir / "IT_Briefing_2026-10-31.md").write_text(REPORT_A, encoding="utf-8")
            (reports_dir / "IT_Briefing_2026-10-30.md").write_text(REPORT_B, encoding="utf-8")
            out_dir = reports_dir / "digests"
            written = write_digest(reports_dir, out_dir, today=date(2026, 11, 2))
            names = sorted(p.name for p in written)
            self.assertEqual(names, ["LATEST.md", "ROADMAP_DIGEST_2026-W45.md"])
            self.assertTrue((out_dir / "LATEST.md").exists())

    def test_no_reports_no_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            written = write_digest(Path(tmp), Path(tmp) / "digests", today=date(2026, 11, 2))
            self.assertEqual(written, [])


if __name__ == "__main__":
    unittest.main()
