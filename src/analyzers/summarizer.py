import os
import json
from google import genai
from typing import List
from src.models.raw_item import RawItem

# Verified Gemini model ids, most capable first. The previous default
# ("gemini-3.8-flash") does not exist, which silently forced every run
# into the fallback report. GEMINI_MODEL env still takes precedence.
DEFAULT_MODELS = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-2.5-flash-lite",
]

TOP_ITEMS_FOR_PROMPT = 20
FALLBACK_WARNING = (
    "> ⚠️ **Cảnh báo:** Bản tin hôm nay là bản tổng hợp tự động (fallback) vì "
    "Gemini không chạy được — nội dung dưới đây là danh sách nguồn đã lọc theo "
    "điểm liên quan, chưa có lớp phân tích sâu. Kiểm tra GEMINI_API_KEY / "
    "GEMINI_MODEL trong GitHub Secrets.\n\n"
)


class MarketBriefingSynthesizer:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None
        self.used_fallback = False

    def _ranked(self, items: List[RawItem]) -> List[RawItem]:
        """Highest relevance first — never raw collection order."""
        return sorted(items, key=lambda i: i.relevance_score, reverse=True)

    def analyze_and_synthesize(self, items: List[RawItem]) -> str:
        ranked = self._ranked(items)
        if not self.client:
            print("Gemini API skipped: No GEMINI_API_KEY provided.")
            self.used_fallback = True
            return FALLBACK_WARNING + self._build_fallback_report(ranked)

        payload = []
        for item in ranked[:TOP_ITEMS_FOR_PROMPT]:
            comments_data = [
                {"author": c.author, "votes": c.votes, "text": c.text}
                for c in sorted(item.top_comments, key=lambda c: c.votes, reverse=True)[:4]
            ]
            payload.append({
                "title": item.title,
                "source": item.source_name,
                "type": item.source_type,
                "region": item.region,
                "url": item.url,
                "relevance_score": item.relevance_score,
                "matched_topics": item.matched_topics,
                "content_preview": item.summary_text[:1000],
                "top_comments": comments_data,
            })

        context_json = json.dumps(payload, ensure_ascii=False, indent=2)

        prompt = f"""
        Bạn là chuyên gia phân tích thị trường IT và cố vấn nghề nghiệp cho lập trình viên Việt Nam.
        Dưới đây là các bài viết / video / thảo luận ĐÃ ĐƯỢC LỌC theo điểm liên quan
        (relevance_score) về thị trường IT hiện nay, kèm BÌNH LUẬN được cộng đồng
        ủng hộ nhất của từng nguồn:

        {context_json}

        MỤC TIÊU CỦA BẢN TIN — đọc kỹ, đây là điều người đọc thực sự muốn:
        - Không phải tin tức IT nói chung. Chỉ tập trung vào: thị trường IT đang
          dịch chuyển thế nào, cộng đồng đang NHÌN NHẬN ra sao (góc nhìn, tranh luận,
          kinh nghiệm thật trong phần bình luận), và HƯỚNG ĐI MỚI nào đang hình thành
          trong thời đại AI.
        - Mọi nhận định phải bám vào dữ liệu trên: nêu được nguồn nào nói, bình luận
          nào ủng hộ/phản đối. Không bịa số liệu, không viết chung chung kiểu
          "AI đang phát triển mạnh mẽ".

        QUY TẮC SONG NGỮ:
        - Phân tích, nhận định, lời khuyên: TIẾNG VIỆT trước, rõ ràng, thực chiến.
        - Trích dẫn nguyên văn tiếng Anh đắt giá: đặt ngay bên dưới dạng
          `> English reference: ...`.

        CẤU TRÚC BÁO CÁO BẮT BUỘC (đúng 5 mục):

        # BÁO CÁO THỊ TRƯỜNG IT & HƯỚNG ĐI MỚI

        ## 1. THỊ TRƯỜNG HÔM NAY ĐANG DỊCH CHUYỂN ĐI ĐÂU
        - 3-5 dịch chuyển quan trọng nhất rút ra từ dữ liệu (tuyển dụng, layoff,
          nhu cầu kỹ năng, AI...), mỗi ý kèm nguồn dẫn chứng cụ thể.

        ## 2. GÓC NHÌN & TRANH LUẬN CỦA CỘNG ĐỒNG
        - Cộng đồng đồng thuận ở điểm nào, trái chiều ở điểm nào.
        - Đối chiếu góc nhìn Việt Nam vs quốc tế nếu dữ liệu cho phép.

        ## 3. BÌNH LUẬN ĐẮT GIÁ NHẤT
        - 3-5 bình luận đáng đọc nhất: trích nguyên văn (rút gọn nếu quá dài),
          tác giả, số votes, thuộc nguồn nào, và 1 câu vì sao nó đáng giá.

        ## 4. HƯỚNG ĐI MỚI & VIỆC NÊN LÀM
        - Hướng đi/kỹ năng đang lên được nhắc tới nhiều nhất.
        - Hành động cụ thể cho một dev nền Java/Spring Boot đang học thêm
          Python và network security: tuần này nên học/làm gì, tránh gì.

        ## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY
        - Từng nguồn trong dữ liệu có điểm liên quan cao nhất: tiêu đề + link,
          2-3 câu tóm tắt luận điểm chính, góc nhìn nổi bật nhất từ bình luận,
          và lý do được chọn (dựa trên matched_topics).
        """

        candidate_models = []
        env_model = os.environ.get("GEMINI_MODEL")
        if env_model:
            candidate_models.append(env_model)
        candidate_models.extend(m for m in DEFAULT_MODELS if m not in candidate_models)

        for model_candidate in candidate_models:
            try:
                response = self.client.models.generate_content(
                    model=model_candidate,
                    contents=prompt,
                )
                if response and response.text:
                    self.used_fallback = False
                    return response.text
            except Exception as error:
                print(f"Gemini API attempt failed with model {model_candidate}: {error}")
                continue

        print("All Gemini models failed. Falling back to structured local report.")
        self.used_fallback = True
        return FALLBACK_WARNING + self._build_fallback_report(ranked)

    def _build_fallback_report(self, items: List[RawItem]) -> str:
        """Structured listing of the *filtered* items, grouped by topic.

        Unlike the old fallback this only receives relevance-filtered items
        (the pipeline filters before synthesizing) and explains why each
        item was selected, with its top community comments.
        """
        ranked = self._ranked(items)
        lines = [
            "# BÁO CÁO THỊ TRƯỜNG IT & HƯỚNG ĐI MỚI (BẢN LỌC TỰ ĐỘNG)",
            "",
            "## NGUỒN ĐÃ LỌC THEO ĐIỂM LIÊN QUAN",
            "",
        ]
        if not ranked:
            lines.append("Hôm nay không có nguồn nào đạt ngưỡng liên quan tối thiểu.")
            return "\n".join(lines)

        for item in ranked[:15]:
            topics = ", ".join(item.matched_topics) if item.matched_topics else "—"
            lines.append(
                f"### [{item.title}]({item.url}) ({item.source_name})"
            )
            lines.append(
                f"**Điểm liên quan:** {item.relevance_score:.0f} · "
                f"**Chủ đề:** {topics} · **Vì sao chọn:** {item.score_reason}"
            )
            if item.summary_text:
                lines.append(f"**Tóm tắt nội dung:** {item.summary_text[:280]}...")
                if item.region == "GLOBAL":
                    lines.append(f"> English reference: {item.summary_text[:180]}...")
            if item.top_comments:
                lines.append("**Bình luận nổi bật từ cộng đồng:**")
                for c in item.top_comments[:3]:
                    votes_label = f"{c.votes} votes" if c.votes else "HN comment"
                    lines.append(f"- *{c.author}* ({votes_label}): \"{c.text}\"")
            lines.append("")
        return "\n".join(lines)
