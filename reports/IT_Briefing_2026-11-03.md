📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.r7xxpqrhjlqf)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

---

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Cực hóa mạnh giữa "Senior chuyên sâu có domain" và "Junior/Fresher"**: Tin tuyển **Lead Architect (CAD Solutions)** lương **$4.000/tháng** yêu cầu **10 năm kinh nghiệm, 5 năm domain xây dựng/thép, tiếng Anh kỹ thuật fluency** và *kinh nghiệm công cụ AI* (Nguồn: System Design Vietnam, `expert_voice_score: 7.5`). Ngược lại, phân tích **3.469 tin tuyển dụng VN (phiên bản 2026)** cho thấy **hầu như không tuyển Junior** (Nguồn: "Học Lập Trình cùng Phát", `relevance: 57`). Bình luận top: *"Thị trường nát thật sự, ko tuyển Junior mới thì sau này lấy đâu ra Senior"* (@macobuzi, 7 votes).
- **Nhu cầu tuyển dụng tổng thể vẫn tăng nhưng "chất lượng" thay đổi**: Báo VnEconomy/VnReview xác nhận *số lượng tin tuyển tăng dù có AI*, nhưng bản chất là tìm người **có thể điều khiển AI/Agent**, không phải viết code thuần (Nguồn: Google News VN, `relevance: 34`).
- **Layoff lan sang Big Tech tại VN**: Microsoft Việt Nam đang sa thải nhân sự (Nguồn: VnExpress, `relevance: 34`). Dấu hiệu thị trường "an toàn" trước đây cũng bị tác động bởi tái cấu trúc toàn cầu.

### Trên thế giới (và ý nghĩa với Việt Nam)
- **AI Agents & Tool Calling đang trở thành chuẩn múc kỹ thuật cốt lõi**: Spring AI 2.1 buộc phải **giữ nguyên `reasoning/thinking blocks`** khi gọi tool (Anthropic, Gemini, OpenAI Responses API đều yêu cầu bắt buộc) (Nguồn: VN Java User Group, `relevance: 37.2`, `is_community_lane: true`). **Ý nghĩa VN**: Dev Java/Spring Boot **bắt buộc** nắm luồng *Stateful AI API (Responses API)* và *Message Parts* để build agent production, không chỉ chat single-turn.
- **Senior/Experienced devs đang bị "đè bẹp" bởi LeetCode + Ageism + AI**: Video "20-Year Developers Can't Find Work" (`expert_voice_score: 4.5`) ghi lại senior 20 năm kinh nghiệm thất nghiệp 2 năm, bị ép LeetCode, thay thế bởi AI coding. Bình luận: *"16yr freelance swe here. no prospect in 2 years. NO PROSPECT OR CALL!"* (@Bonomax85). **Ý nghĩa VN**: Kinh nghiệm năm tháng **không còn là khiên**. Cần chuyển sang **System Design, Architecture, Domain Expertise, AI Orchestration** — những thứ AI chưa thay thế được hẳn.
- **Restructuring mang vết sẹo dài hạn (Goldman Sachs)**: AI layoffs tạo "long-lasting scar" giống các cuộc khủng hoảng 40 năm qua, ảnh hưởng nặng đến worker lớn tuổi (Nguồn: Hacker News/ Fortune, `relevance: 37.1`). **Ý nghĩa VN**: Thị trường VN theo sát chu kỳ toàn cầu 6-12 tháng. Chuẩn bị *resilience* (tài chính, kỹ năng di động) là bắt buộc.
- **Mentorship & "Less AI at work" cho deep work**: Senior engineer từ shipper chuyển nghề khuyên: **giảm dùng AI khi cần hiểu sâu logic**, tìm mentor, tập trung *business context* (Nguồn: Beyond Coding with Ola, `expert_voice_score: 6.0`). **Ý nghĩa VN**: Junior/VN dev thường lạm dụng Copilot → mất tư duy thiết kế. Cần cân bằng: dùng AI để *thi triển*, tự suy nghĩ để *thiết kế*.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

| Kỹ năng / Công nghệ | Cấp độ ưu tiên | Vì sao (Dẫn chứng dữ liệu) | Thật hay Hype? |
| :--- | :--- | :--- | :--- |
| **System Design & Architecture** | **Bắt buộc (P0)** | Job Architect $4k yêu cầu "thiết kế từ đầu, chọn tech stack, dẫn dắt team" (System Design VN). Video System Design Interview 2027 (Dev.to) là chuẩn bị cứng. | **Thật** — Kỹ năng "khó thay thế bởi AI" nhất hiện nay. |
| **Tiếng Anh kỹ thuật (Fluency)** | **Bắt buộc (P0)** | Job Architect yêu cầu "Anh văn kỹ thuật xuất sắc để cộng tác Úc/Mỹ". Global remote/outsourcing VN đều yêu cầu. | **Thật** — Rào cản vào high-pay roles. |
| **Domain Knowledge (Ngành nghiệp cụ thể)** | **Rất cao (P1)** | Job Architect ưu tiên **5 năm domain Xây dựng/Thép/Kết cấu**. Senior dev 20 năm thất nghiệp vì thiếu domain depth khi bị so sánh với AI. | **Thật** — "Moat" bảo vệ career. |
| **AI Agent Orchestration (Tool Calling, RAG, Evaluation, Reasoning Preservation)** | **Rất cao (P1)** | Spring AI 2.1 bắt buộc preserve `thinking blocks`/`thought_signature` cho Anthropic/Gemini/OpenAI Responses API (VN Java UG, insight 4.5). Docker tặng $250 credit chạy agent (J2Team). | **Thật** — Từ "prompt engineering" chuyển sang "agent engineering" có state, eval, observability. |
| **Spring AI / Python (LangChain/LlamaIndex/FastAPI)** | **Cao (P1)** | Spring AI 2.1-RC1 là bắt buộc cho stack Java (VN Java UG). Python vẫn là lingua franca AI. | **Thật** — Cần hands-on build agent pipeline, không chỉ gọi API. |
| **Network Security / System Hardening** | **Trung bình - Cao (P2)** | Bối cảnh layoff, supply chain attack, AI-generated code rủi ro. Dev Java học Security có lợi thế niche (DevSecOps, Secure SDLC). | **Thật** — Nhu cầu an ninh tăng khi code sinh ra nhanh hơn review. |
| **LeetCode / Algo Grind** | **Thấp (P3) — Chỉ cho interview Big Tech** | Senior 20 năm vẫn bị ép LeetCode (Francesco Andreoli). Nhưng Job Architect $4k **không nhắc LeetCode**, chỉ hỏi kinh nghiệm thực chiến. | **Hype cho Senior** — Tập trung vào *System Design case study* thay vì grind algo. |
| **Prompt Engineering đơn thuần** | **Thấp (P3) — Đã commoditize** | Ai cũng prompt được. Giá trị ở *orchestration, eval, guardrails, tool integration*. | **Hype** — Đừng bỏ thời gian học "prompt template". |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy cốt lõi (từ cộng đồng & chuyên gia)
1.  **Từ "Task Executor" → "System Owner + Business Partner"**: Job Architect yêu cầu "toàn quyền lựa chọn công nghệ, dẫn dắt đội ngũ, lộ trình thăng tiến lâu dài". Senior dev thất nghiệp vì chỉ biết *làm ticket*, không biết *thiết kế giải pháp cho business* (Francesco Andreoli, Beyond Coding).
2.  **Từ "Viết code" → "Điều phối & Đánh giá Agent (Orchestration & Eval)"**: Spring AI 2.1 thay đổi core message structure để giữ `reasoning` cho tool calling. **Bài học**: Bạn không viết logic `if-else` cho agent, bạn **thiết kế schema, guardrails, evaluation harness** (Momentic HN discussion: "LLMs reinforce own assumptions, bad at visual understanding").
3.  **Từ "Học công nghệ mới" → "Tái đầu tư vào Foundation (Mạng, OS, DB, Distributed Systems)"**: Network Security bạn đang học chính là *foundation* không lỗi thời. AI agent chạy trên infra — hiểu network/security giúp bạn *harden* agent env, debug timeout, MITM, data exfil.
4.  **Tư duy "Portfolio > CV"**: Video "Food Delivery to Senior" nhấn mạnh **project thực tế + mentor review**. Phân tích 3.469 job VN: employer xem *github/project* hơn degree.

### Áp dụng cụ thể cho **Dev Java/Spring Boot đang học Python + Network Security** (Tuần này làm gì)

| Thứ | Hoạt động cụ thể | Mục tiêu định hướng |
| :--- | :--- | :--- |
| **2-3** | **Hands-on Spring AI 2.1-RC1**: Tạo project demo *Tool Calling* gọi hàm Java (vd: query DB, call API nội bộ), **bắt buộc log/inspect `MessagePart` reasoning blocks** (theo bài VN Java UG). | Nắm luồng **Stateful Agent** trên stack Java — kỹ năng hiếm, lương cao. |
| **4** | **Python FastAPI + LangGraph**: Build một *multi-agent workflow* đơn giản (Planner -> Executor -> Critic). Dùng **Docker SBX $250 credit** (J2Team) để chạy sandbox agent tách biệt. | Bilingual stack (Java + Python) cho AI Engineering. Hiểu *agent state machine*. |
| **5** | **Network Security Lab**: Setup **mitmproxy** intercept traffic giữa Agent <-> LLM API / Tool endpoints. Thử *prompt injection* qua tool input, viết rule chặn. | Kết hợp **Security + AI** → Niche **AI Safety/Red Teaming** rất hot. |
| **6-7** | **System Design Case Study**: Lấy yêu cầu Job Architect (CAD Solutions): *Thiết kế hệ thống quản lý bản vẽ thép 3D, sync real-time Úc-VN, xử lý file lớn, RBAC phức tạp*. Vẽ diagram, viết ADR (Architecture Decision Record). | Chuẩn bị cho **Staff/Architect interview**. Tăng tư duy "Business + System". |
| **Hàng ngày** | **Đọc 1 paper/blog về AI Agent Evaluation** (vd: "Evaluating LLM Systems" - Hamel Husain, hoặc blog Momentic/Codex). Không đọc tin tức AI. | Xây **mental model** về *đo lường chất lượng agent* — skill định giá cao. |

**Tránh tuyệt đối tuần này:**
- Grind LeetCode (trừ khi interview Big Tech tuần sau).
- Xem tutorial "100 prompt hay cho ChatGPT".
- Apply mass CV không tailor cho role Senior/Lead.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

### 1. Giải thích chuyên sâu **Stateless vs Stateful AI API** — *Key để build Agent production*
> **Tác giả**: Facebook user (VN Java User Group) | **Insight**: 4.5 | **Bài**: [Spring AI 2.1 Tool Calling](https://facebook.com/groups/vnjug/permalink/2576853536073284/)
> **Nội dung**:
> "Thêm context cho các anh em về Stateless trong AI. Khi nhắc đến AI API thì nhiều người thường hay nghĩ đến Stateless có nghĩa là AI không có trí nhớ, bạn gửi câu hỏi 1 bạn nhận về câu trả lời 1 sau đó bạn gửi tiếp câu hỏi 2, thì lúc này AI xem câu hỏi 2 ý như câu hỏi mới, nó hoàn toàn không có thông tin về bộ câu hỏi và câu trả lời 1. Đó là stateless, đó là lý do tại sao bạn phải thiết kế để hệ thống gửi kèm cả bộ câu hỏi và câu trả lời 1 khi hỏi thêm câu hỏi 2. Hầu như các AI Provider đều cung cấp AI dạng đó hay gọi theo chuẩn của OpenAI là ChatCompletion API, nhưng cũng có ngoại lệ và đó cũng là từ OpenAI gọi là Responses API, api này có thể giữ state phía server và bạn khi gửi câu hỏi 2 thì chỉ cần gửi conversation_id..."
> **Tại sao đọc**: Đây là **kiến thức cốt lõi** để hiểu sao Spring AI 2.1 phải redesign `Message Parts`. Dev Java muốn build agent **bắt buộc** phân biệt được `ChatCompletion` (stateless, tự manage history) vs `Responses API` (stateful, server-side state) để chọn architecture đúng, tránh bug context loss, token waste.

> **English reference**: *Stateless AI API means the model has no memory. You send Q1, get A1. Send Q2, model treats it as brand new, zero context of Q1/A1. That's why you must send full history every turn. Most providers follow OpenAI ChatCompletion (stateless). Exception: OpenAI Responses API — server-side state, just send conversation_id.*

---

### 2. Thực trạng **Junior Freeze → Senior Shortage trong 3-5 năm tới**
> **Tác giả**: @macobuzi | **Votes**: 7 | **Insight**: 0 (raw signal) | **Bài**: [Phân tích 3.469 việc làm IT 2026](https://www.youtube.com/watch?v=OommS5HRX3U)
> **Nội dung**: *"Thị trường nát thật sự, ko tuyển Junior mới thì sau này lấy đâu ra Senior."*
> **Tại sao đọc**: Dữ liệu 3.469 job + comment này khẳng định **cung cầu bị đứt gãy ở entry-level**. Người học IT *bây giờ* nếu không có chiến lược "nhảy cấp" (bootcamp chất lượng + project thật + mentor + English) sẽ rơi vào hố "0 năm kinh nghiệm sau 1 năm học". Doanh nghiệp VN đang ăn mòn pipeline nhân sự.

---

### 3. Thực tế khắc nghiệt: **Senior 16 năm Freelance không có prospect 2 năm**
> **Tác giả**: @Bonomax85 | **Votes**: 0 | **Insight**: 0 (raw signal) | **Bài**: [20-Year Developers Can't Find Work](https://www.youtube.com/watch?v=xjahkZUXdZg)
> **Nội dung**: *"16ye freelance swe here. no prospect in 2 years. NO PROSPECT OR CALL!"*
> **Tại sao đọc**: Phá vỡ thần thoại "kinh nghiệm = an toàn". Freelance/gig chỉ mạnh khi thị trường hype. Khi recession + AI, client thu hẹp vendor, giữ core team. **Lời khuyên**: Build *internal career capital* (domain, architecture, leadership) thay vì chỉ bán giờ code.

---

### 4. Spring AI 2.1 **bắt buộc upgrade** do thiếu sót architecture hiện tại
> **Tác giả**: Facebook user (VN Java User Group) | **Insight**: 1.0 | **Bài**: [Spring AI 2.1 Tool Calling](https://facebook.com/groups/vnjug/permalink/2576853536073284/)
> **Nội dung**: *"Spring AI hiện tại vẫn đang là 2.0 GA, nhưng việc lên 2.1 gần như là bắt buộc với những thiếu sót hiện tại. Hiện tại Spring AI 2.1 vẫn chưa GA, nhưng bạn có thể sử dụng thử Spring AI 2.1-RC1 mới được released vài ngày trước."*
> **Tại sao đọc**: Xác nhận **window of opportunity**: Sớm làm quen RC1 → thành early adopter → dẫn dắt team migration khi GA. Skill "Migration/Upgrade framework core" cực giá cho Staff/Architect.

---

### 5. Senior Engineer khuyên: **Dùng ít AI khi cần hiểu sâu, tìm Mentor**
> **Tác giả**: Shola (Senior Engineer) | **Nguồn**: Video Beyond Coding with Ola (`expert_voice_score: 6.0`) | **Link**: [From Food Delivery to Senior Engineer](https://www.youtube.com/watch?v=E5ZJUvbnMRY) (phút 22:16)
> **Nội dung tóm tắt**: Anh ấy giảm dùng AI ở công việc hiện tại vì nhận ra AI che lấp việc *không hiểu rõ luồng data, edge case*. Nhấn mạnh mentorship giúp rút ngắn 3-5 năm mò mẫm.
> **Tại sao đọc**: Cân bằng tâm lý "AI làm hết". **Tư duy**: Dùng AI *thi triển* (boilerplate, test, doc), tự *thiết kế & debug* core logic. Tìm mentor review code/design — ROI cao hơn học thêm 10 framework.

> **English reference**: *Shola reduced AI usage at work because it masked gaps in deep understanding of data flows and edge cases. Mentorship compressed 3-5 years of trial-and-error. Use AI for implementation velocity, not for architectural thinking.*

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| # | Nguồn | Loại / Vùng | Luận điểm chính & Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[HỒ CHÍ MINH] TUYỂN DỤNG LEAD SOFTWARE ARCHITECT (CAD SOLUTIONS) - $4,000 USD** | Job Post **[VN]** `expert_voice: 7.5` | **Benchmark đỉnh cao** cho Dev VN: Yêu cầu **Domain (Construction/Steel) + English + System Design + AI Tools**. Không hỏi LeetCode. Phúc lợi BHXH full, WLB tốt. | Xác định **mục tiêu career 3-5 năm**: Kỹ năng gì thì lương $4k. Domain knowledge là "moat" lớn nhất. |
| **2** | **Phân tích 3.469 việc làm IT ở VN (2026) \| Liệu còn cơ hội cho người mới?** | Video **[VN]** `relevance: 57` (Kênh: Học Lập Trình cùng Phát) | Dữ liệu thực: **Hà Nội/HCM chiếm 90%**, Backend/Java/SpringBoot top 1, **Junior ~0%**, AI/ML nhóm riêng nhỏ. Code crawler + dataset open source. | **Real data** thay vì "cảm giác". Biết chính xác stack, location, level đang hot. Tác giả share code → có thể tự re-run phân tích niche. |
| **3** | **[Spring AI 2.1] Vì sao tool calling cần giữ nguyên reasoning từ response đến database?** | Technical Deep-dive **[VN]** `is_community_lane: true` `insight_comment: 4.5` | Giải thích **kiến trúc Message Parts** mới: `Reasoning`/`Thinking blocks`/`Tool Call`/`Result` phải round-trip nguyên vẹn cho Anthropic/Gemini/OpenAI Responses API. | **Kiến thức cứng** cho Java dev build Agent. Bình luận giải thích Stateless vs Stateful API cực hay (xem mục 4). |
| **4** | **From Food Delivery to Senior Engineer** | Video **[GLOBAL]** `expert_voice: 6.0` | Hành trình 5 năm: Shipper → Self-study → Bootcamp → Mentor → Junior → Senior. **Less AI usage now**, focus deep understanding, business context. | **Role model** cho career switcher / junior. Tư duy "Mentorship > Course", "Deep work > AI shortcut". |
| **5** | **Nhu cầu tuyển dụng lập trình viên vẫn tăng dù đã có AI** / **AI đang tự động hóa... tại sao tin tuyển lại tăng?** | News **[VN]** `relevance: 34` (VnEconomy, VnReview) | Giải thích nghịch lý: AI tự động hóa *coding* → tăng năng suất → doanh nghiệp **mở rộng scope dự án, tuyển người kiểm soát/điều phối AI (Senior/Lead)**, không phải coder thuần. | Cập nhật **bối cảnh macro VN**: Không "tuyển ít hơn", mà "tuyển khác profile". Junior phải định vị thành "AI-augmented Junior". |
| **6** | **The 2027 System Design Interview Playbook** | Article **[GLOBAL]** `relevance: 36.9` (Dev.to) | Framework chuẩn bị System Design cho năm 2027: Requirements → Constraints → API → Data Model → High-level → Deep dive (Sharding, Cache, Consistency) → AI/ML infra considerations. | **Chuẩn bị interview Architect/Staff**. Có yếu tố AI Infra (vector DB, RAG, Agent scaling) — phù hợp xu hướng mới. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào với `is_major_incident = true` trong batch này. Bỏ qua mục 6.*