import os
import json
from google import genai
from typing import List
from src.models.raw_item import RawItem

class MarketBriefingSynthesizer:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None

    def analyze_and_synthesize(self, items: List[RawItem]) -> str:
        if not self.client:
            print("Gemini API skipped: No GEMINI_API_KEY provided.")
            return self._build_fallback_report(items)

        payload = []
        for item in items[:35]:
            comments_data = [
                {"author": c.author, "votes": c.votes, "text": c.text}
                for c in item.top_comments
            ]
            payload.append({
                "title": item.title,
                "source": item.source_name,
                "region": item.region,
                "url": item.url,
                "content_preview": item.summary_text[:600],
                "top_comments": comments_data
            })

        context_json = json.dumps(payload, ensure_ascii=False, indent=2)

        prompt = f"""
        Bạn là một chuyên gia phân tích dữ liệu ngành công nghệ thông tin và cố vấn nghề nghiệp IT cấp cao.
        Dưới đây là dữ liệu các video phân tích, bài viết chuyên sâu và các BÌNH LUẬN ĐƯỢC NHIỀU LIKE NHẤT từ cộng đồng kỹ sư (Việt Nam và Quốc tế):

        {context_json}

        Nhiệm vụ: Biên soạn bản tin toàn diện "Báo Cáo Toàn Cảnh Thị Trường IT & Cẩm Nang Bám Trụ Nghề Nghiệp".

        YÊU CẦU ĐẶC BIỆT:
        1. PHÂN TÍCH BÌNH LUẬN CỘNG ĐỒNG: Tuyệt đối không chỉ đọc bài viết mà phải tổng hợp sâu các bình luận nhiều like (kinh nghiệm thực tế, tranh cãi, lời khuyên thật lòng của các dev trong nghề).
        2. TRÍCH NGUỒN CÓ TÓM TẮT CHI TIẾT: Với mỗi nguồn tin được chọn lọc, phải tóm tắt rõ luận điểm chính và nêu bật góc nhìn đắt giá nhất từ phần bình luận.
        3. QUY TẮC SONG NGỮ (VIỆT - ANH):
           - Toàn bộ nội dung phân tích, nhận định và lời khuyên phải viết bằng TIẾNG VIỆT rõ ràng, mạch lạc, thực chiến trước.
           - Với các trích dẫn hoặc thuật ngữ từ nguồn quốc tế, đặt ngay bên dưới khối Tiếng Việt bằng định dạng: `> English reference: ...`.

        CẤU TRÚC BÁO CÁO BẮT BUỘC:
        # BÁO CÁO CHIẾN LƯỢC THỊ TRƯỜNG IT & KINH NGHIỆM BÁM TRỤ NGHỀ NGHIỆP

        ## 1. TỔNG QUAN CHUYỂN DỊCH CÔNG NGHỆ & TÂM LÝ THỊ TRƯỜNG
        - Xu hướng công nghệ nổi bật trong ngày (AI Agent, Vibe Coding, Cloud/Infra...).
        - Đối chiếu thực tế giữa thảo luận quốc tế và thị trường Việt Nam (từ Hỏi Dân IT, Tips Javascript, Tôi Đi Code Dạo).

        ## 2. THỰC TẾ TUYỂN DỤNG & VIỆC LÀM (HIRING & LAYOFF REALITIES)
        - Đánh giá nhu cầu tuyển dụng theo cấp độ (Fresher, Junior, Middle, Senior).
        - Những thách thức thực tế và rào cản việc làm đang được nhắc tới nhiều nhất.

        ## 3. CẨM NANG BÁM TRỤ & NÂNG CẤP BẢN THÂN (SURVIVAL ADVICE)
        - Kinh nghiệm thực chiến rút ra từ các bình luận được like nhiều nhất của cộng đồng kỹ sư.
        - Kỹ năng cốt lõi cần rèn luyện ngay hôm nay để không bị đào thải.

        ## 4. CHI TIẾT CÁC NGUỒN CHẤT LƯỢNG NÊN XEM HÔM NAY (CURATED HIGHLIGHTS)
        - Trình bày thành các mục riêng cho từng nguồn nổi bật (Việt Nam & Quốc tế):
          - Tiêu đề & Link truy cập.
          - Tóm tắt nội dung chính của video / bài viết.
          - Bình luận / Góc nhìn nổi bật nhất của cộng đồng (kèm số upvote/like nếu có).
          - Lời khuyên rút ra cho lập trình viên.
        """

        candidate_models = [
            os.environ.get("GEMINI_MODEL", "gemini-3.8-flash"),
            "gemini-2.0-flash",
            "gemini-2.5-flash",
            "gemini-1.5-flash"
        ]

        for model_candidate in candidate_models:
            try:
                response = self.client.models.generate_content(
                    model=model_candidate,
                    contents=prompt
                )
                if response and response.text:
                    return response.text
            except Exception as error:
                print(f"Gemini API attempt failed with model {model_candidate}: {error}")
                continue

        print("All Gemini models failed. Falling back to structured local report.")
        return self._build_fallback_report(items)

    def _build_fallback_report(self, items: List[RawItem]) -> str:
        lines = [
            "# BÁO CÁO THỊ TRƯỜNG IT & BÌNH LUẬN NỔI BẬT TRONG NGÀY",
            "",
            "## 1. NGUỒN CÔNG NGHỆ VIỆT NAM (BÀI VIẾT & BÌNH LUẬN TIÊU BIỂU)",
            ""
        ]
        vn_items = [i for i in items if i.region == "VN"]
        for item in vn_items[:8]:
            lines.append(f"### [{item.title}]({item.url}) ({item.source_name})")
            if item.summary_text:
                lines.append(f"**Tóm tắt nội dung:** {item.summary_text[:280]}...")
            if item.top_comments:
                lines.append("**Bình luận nổi bật từ cộng đồng:**")
                for c in item.top_comments[:3]:
                    lines.append(f"- *{c.author}* ({c.votes} upvotes/likes): \"{c.text}\"")
            lines.append("")

        lines.append("## 2. NGUỒN CÔNG NGHỆ QUỐC TẾ (GLOBAL TECH & EXPERT DISCUSSIONS)")
        lines.append("")
        global_items = [i for i in items if i.region == "GLOBAL"]
        for item in global_items[:8]:
            lines.append(f"### [{item.title}]({item.url}) ({item.source_name})")
            if item.summary_text:
                lines.append(f"**Tóm tắt nội dung:** {item.summary_text[:280]}...")
                lines.append(f"> English reference: {item.summary_text[:180]}...")
            if item.top_comments:
                lines.append("**Top Community Comments:**")
                for c in item.top_comments[:3]:
                    lines.append(f"- *{c.author}* ({c.votes} votes): \"{c.text}\"")
            lines.append("")

        return "\n".join(lines)
