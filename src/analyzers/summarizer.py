import os
import json
from google import genai
from typing import List
from src.filters.relevance import comment_insight_score, rank_comments
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
                {
                    "author": c.author,
                    "votes": c.votes,
                    "insight_score": round(comment_insight_score(c.text), 1),
                    "text": c.text,
                }
                for c in rank_comments(item.top_comments, limit=4)
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
        Bạn là chuyên gia phân tích định hướng nghề nghiệp IT cho lập trình viên Việt Nam.
        Dưới đây là các bài viết / video / thảo luận ĐÃ ĐƯỢC LỌC theo điểm liên quan,
        kèm BÌNH LUẬN của cộng đồng. Mỗi bình luận có `insight_score` — điểm giá trị
        định hướng do hệ thống chấm (bình luận của người trong nghề giải thích ngành
        đang đi về đâu, cần học gì, tư duy thế nào sẽ có điểm cao):

        {context_json}

        NGƯỜI ĐỌC THỰC SỰ MUỐN GÌ — đây là trọng tâm của bản tin:
        - Không phải tin tức IT nói chung. Người đọc muốn ĐỊNH HƯỚNG: ngành IT hiện
          nay đang đi theo hướng nào, người học IT bây giờ cần học NHỮNG GÌ (kỹ năng
          và CÔNG NGHỆ cụ thể), áp dụng như thế nào vào học tập/công việc, và cần
          thay đổi TƯ DUY ra sao.
        - Nguồn giá trị nhất là các bình luận dài của người trong nghề (insight_score
          cao): họ nói thẳng điều bài viết/video không nói. Ưu tiên khai thác chúng.
        - Mọi nhận định phải bám dữ liệu: nguồn/bình luận nào nói. Không bịa số liệu,
          không viết sáo rỗng kiểu "AI đang phát triển mạnh mẽ".

        QUY TẮC SONG NGỮ:
        - Phân tích, nhận định, lời khuyên: TIẾNG VIỆT trước, rõ ràng, thực chiến.
        - Trích dẫn nguyên văn tiếng Anh đắt giá: đặt ngay bên dưới dạng
          `> English reference: ...`.

        CẤU TRÚC BÁO CÁO BẮT BUỘC (đúng 5 mục):

        # BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

        ## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY
        - 3-5 dịch chuyển quan trọng nhất (AI thay đổi cách làm việc ra sao, tuyển
          dụng/layoff, vai trò dev đang biến đổi thế nào), mỗi ý kèm nguồn dẫn chứng.

        ## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ
        - Kỹ năng cần học: liệt kê cụ thể, kèm vì sao và nguồn/bình luận nào nhắc tới.
        - Công nghệ cần học: liệt kê cụ thể (ngôn ngữ, framework, mảng AI/security/
          system...), phân biệt "đang là xu hướng thật" vs "chỉ là hype" nếu dữ liệu
          cho phép nhận định.

        ## 3. TƯ DUY & CÁCH ÁP DỤNG
        - Những thay đổi tư duy được cộng đồng nhắc nhiều nhất (vd: từ làm theo task
          sang hiểu business + cả hệ thống, kỹ năng làm việc với con người...).
        - Cách áp dụng cụ thể cho một dev nền Java/Spring Boot đang học thêm Python
          và network security: tuần này nên làm gì, tránh gì.

        ## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT
        - Chọn 3-5 bình luận có insight_score cao nhất. Trích DÀI, giữ trọn ý chính
          (không cắt còn 1 dòng), kèm tác giả, số votes, thuộc video/bài nào (kèm link),
          và 1-2 câu vì sao bình luận này đáng đọc.

        ## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY
        - Các nguồn điểm liên quan cao nhất: tiêu đề + link, 2-3 câu tóm tắt luận
          điểm chính, góc nhìn nổi bật nhất từ bình luận, lý do được chọn.
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

    def _top_insight_comments(self, items: List[RawItem], limit: int = 5):
        """Best directional comments across all items: (item, comment, insight)."""
        pool = []
        for item in items:
            for comment in item.top_comments:
                pool.append((item, comment, comment_insight_score(comment.text)))
        pool.sort(key=lambda entry: (entry[2], entry[1].votes), reverse=True)
        return pool[:limit]

    def _build_fallback_report(self, items: List[RawItem]) -> str:
        """Structured listing of the *filtered* items, direction-first.

        Leads with the best directional community comments (full text, up
        to the normalizer's 700-char cap) — for this briefing those
        comments ARE the product — then the ranked source list.
        """
        ranked = self._ranked(items)
        lines = [
            "# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT (BẢN LỌC TỰ ĐỘNG)",
            "",
        ]
        if not ranked:
            lines.append("Hôm nay không có nguồn nào đạt ngưỡng liên quan tối thiểu.")
            return "\n".join(lines)

        lines.append("## BÌNH LUẬN ĐỊNH HƯỚNG NỔI BẬT")
        lines.append("")
        top_comments = self._top_insight_comments(ranked)
        if top_comments:
            for item, comment, insight in top_comments:
                votes_label = f"{comment.votes} votes" if comment.votes else "HN comment"
                lines.append(
                    f"### Từ [{item.title}]({item.url}) ({item.source_name})"
                )
                lines.append(f"*{comment.author}* ({votes_label}, insight {insight:.0f}):")
                lines.append(f"> {comment.text}")
                lines.append("")
        else:
            lines.append("Chưa thu được bình luận cộng đồng nào trong lần chạy này.")
            lines.append("")

        lines.append("## NGUỒN ĐÃ LỌC THEO ĐIỂM LIÊN QUAN")
        lines.append("")
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
                for c in rank_comments(item.top_comments, limit=3):
                    votes_label = f"{c.votes} votes" if c.votes else "HN comment"
                    lines.append(f"- *{c.author}* ({votes_label}): \"{c.text}\"")
            lines.append("")
        return "\n".join(lines)
