📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.r8env2qfocbv)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
1. **AI Agent đang thay đổi cốt lõi quy trình dev: từ "viết code" sang "quản trị chất lượng & thiết kế hệ thống".**  
   - Video *Tôi Đi Code Dạo* (VN, relevance 56) nhấn mạnh AI Agent giờ code "xịn cỡ nào", Junior bị đào thải nhanh vì AI làm được 95-98% việc code thuần túy.  
   - Bài chia sẻ VGU Tech Alumni (VN, relevance 38.9) từ Quân IT: team 6-7 người dùng AI chạy 5-6 project song song, productivity tăng 30-40%. Bài toán chuyển sang **nâng mức tin cậy (low→high trust), giữ chặt System Design, chuyển từ *know the how* sang *know the what***.  
   - Bình luận top @phutran-z6h (video Tips JS, insight 12): *"AI tự thiết kế, tự chạy test performance, security, e2e, uiux... lập trình viên ko cần code là chuyện trước mặt rồi... ae nên tập trung vào việc hiểu business + hệ thống + kĩ năng làm việc với mọi người"*.

2. **Thị trường tuyển dụng극 độ phân hóa: Senior lên, Junior/Fresher gần như "chết".**  
   - Video *AI Fallout* (GLOBAL, relevance 61) trích Stanford/Indeed: job posting senior tăng, dev 22-25 tuổi giảm ~19% sau ChatGPT, dev 41-49 tăng ~20%.  
   - Video *Complexity Compiled* (GLOBAL, relevance 45.8): chỉ 4.5% role entry-level năm 2026, senior chiếm 69%. AI làm việc junior, layoff tràn dev giàu kinh nghiệm xuống争 junior slot.  
   - Áp dụng VN: Công ty VN outsource/product đều siết chặt headcount junior, yêu cầu fresher phải "production-ready" ngay (biết CI/CD, test, Docker, hiểu business logic) — yếu tố lọc CV khắt khe hơn hẳn 2 năm trước.

3. **Kỹ năng "soft" trở thành hard skill: hiểu nghiệp vụ, giao tiếp, quản trị rủi ro AI.**  
   - Nhiều bình luận VN (insight cao) đồng thanh: dev kiểu "nhận task code xong nộp" sẽ bị thay thế. Cần **hiểu end-to-end system, biết nói chuyện với stakeholder, review code do AI sinh ra (security, performance, maintainability)**.  
   - Nghiên cứu Harvard (VGU Alumni, relevance 50.8): AI giúp viết code nhanh 30%, commit nhiều 20%, PR nhiều 23% — **NHƯNG ticket done KHÔNG TĂNG** vì bottlenecks dời sang code review (dài 49%), sửa code gấp đôi, comment tăng 35%. → Dev senior giá trị nằm ở **gating quality & architectural decisions**, không phải gõ phím.

### Trên thế giới (ý nghĩa với dev Việt Nam)
1. **Khoảng cách "Junior trap" toàn cầu đang lan sang VN nhanh hơn dự kiến.**  
   - Dữ liệu US (Hacker News, 15 YOE unemployed 2 năm, relevance 57.8) cho thấy ngay senior 15 năm kinh nghiệm C#/.NET/AWS cũng thất nghiệp dài hạn do gap CV + AI screening.  
   - **Ý nghĩa VN:** Đừng tin "lâu năm = an toàn". Dev VN 5-8 YOE nếu chỉ biết code feature, không có portfolio system design/public speaking/mentoring sẽ rơi vào bẫy tương tự khi market điều chỉnh.

2. **Chi phí chạy AI agent chênh lệch 5x tùy "harness" (tooling/workflow) — cơ hội niche cho VN.**  
   - Bài J2TEAM (VN, relevance 40.7): cùng model DeepSeek V4.1, Cline CLI tốn gấp 5 lần OpenCode. Harness đắt không đồng nghĩa hiệu quả cao.  
   - **Ý nghĩa VN:** Công ty VN đang tìm người **"tối ưu chi phí inference + build internal AI workflow"**. Kiến thức về *prompt engineering, agent orchestration (LangGraph, CrewAI), eval harness, RAG tuning* giá trị hơn biết dùng Cursor/Copilot cơ bản.

3. **Xu hướng "Vibe Coding" (code bằng tự nhiên + AI) đang chuẩn hóa — nhưng an toàn chỉ khi có Git/guardrails chặt.**  
   - Series *Hỏi Dân IT* (VN, relevance 51.9, 51.5, 33) dạy vibe coding với Git hooks, Antigravity IDE, Gemini/Claude Code.  
   - **Ý nghĩa VN:** Fresher/Junior học vibe coding **PHẢI** kèm quy trình: plan → approve → step-by-step exec → test evidence → commit. Không guardrail = technical debt nổ sau 2 tuần.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

| Kỹ năng / Công nghệ | Cấp độ ưu tiên | Tại sao (nguồn/bình luận) | Ghi chú: Xu hướng thật vs Hype |
|---|---|---|---|
| **System Design & Architecture (distributed, event-driven, data modeling)** | 🔥 Critical | Quân IT (VGU Alumni): "giữ chặt System Design"; @phutran-z6h: "hiểu business + hệ thống"; Harvard study: bottlenecks ở design/review. | **Thật** — AI chưa thay thế được trade-off kiến trúc, capacity planning, migration strategy. |
| **AI Agent Engineering: RAG, Vector DB, Prompt/Chain orchestration, Eval harness** | 🔥 Critical | Video Tips JS "Vector Databases" (relevance 56); J2TEAM harness study (relevance 40.7); comment @duythanh1602 hỏi chuyển BE→AI Eng. | **Thật** — Enterprise đang productionize GenAI, cần người build pipeline đáng tin cậy, không chỉ gọi API. |
| **Code Review & Quality Gating cho code do AI sinh (security, perf, maintainability)** | 🔥 Critical | Harvard study: PR review lâu 49%, sửa code gấp đôi; @phutran-z6h: AI làm 95-98% nhưng cần setup/research. | **Thật** — Đây là "moat" của dev senior: biết nhìn ra bug tiềm ẩn, hallucination, over-engineering của AI. |
| **Business Domain Knowledge + Stakeholder Communication** | 🔥 Critical | @phutran-z6h: "tập trung hiểu business + kĩ năng làm việc với mọi người"; Tôi Đi Code Dạo: "biết chọn đúng việc nên làm". | **Thật** — AI không hiểu context doanh nghiệp, rủi ro pháp lý, UX thực tế. |
| **Git/GitHub Advanced: Conventional Commits, Stacked PRs, CI/CD Guardrails, Hooks** | 🔥 Critical | Series Hỏi Dân IT (relevance 51.9, 51.5): "vibe coding an toàn với Git hooks, slash commands /task /resume /learn". | **Thật** — Workflow chuẩn mới cho dev-AI collaboration. |
| **Python (Data/AI stack) + Network Security fundamentals** | 🔥 Critical (cho profile Java/Spring Boot) | Profile người đọc: đang học Python + NetSec. Market cần **AI Security, API Security, LLM Red-teaming** — giao điểm 2 mảng này. | **Thật** — OWASP Top 10 for LLM, Prompt Injection, Data Poisoning là kỹ năng hiếm, lương cao. |
| **Cloud Native Observability (OpenTelemetry, eBPF, Distributed Tracing)** | ⭐ High | AI agent sinh ra nhiều service nhỏ, cần observability để debug production. | **Thật** — Kết hợp tốt với background Java/Spring Boot (Micrometer, Spring Cloud Sleuth). |
| **Kubernetes / Platform Engineering (Internal Developer Platform)** | ⭐ High | Công ty VN scale đều cần self-serve infra cho dev team. | **Thật** — Từ "DevOps" chuyển sang "Platform Eng". |
| **React/Next.js (Fullstack)** | ⭐ Medium | Series Hỏi Dân IT React Fresher Test (relevance 42.8) — vẫn là baseline hiring cho FE/BE-fullstack. | **Cơ bản** — Yêu cầu tối thiểu để tự build demo/portfolio AI app. |
| **No-code/Low-code (Retool, n8n, Windmill)** | 🧪 Niche | Video "No Code" Tips JS (relevance 63.5): dev cần hiểu business, no-code cho internal tools nhanh. | **Thật nhưng niche** — Hữu ích cho internal tooling, không thay thế core backend. |
| **Blockchain / Web3 / Crypto** | ❌ Hype (trừ chuyên ngành) | Không xuất hiện trong dữ liệu định hướng career survival. | **Hype** — Tránh trừ khi target chuyên ngành. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy cốt lõi (từ cộng đồng VN/Global)
1. **Từ "Task Executor" → "Problem Owner & System Thinker"**  
   - Không hỏi "task này code như nào?" mà hỏi "task này giải quyết business problem gì? Rủi ro gì? Làm sao đo lường thành công? Tác động hệ thống khác ra sao?".
2. **Từ "Code Owner" → "AI Supervisor & Quality Gatekeeper"**  
   - Chấp nhận AI viết 80-90% boilerplate. Nhiệm vụ bạn: **architect prompt/context, review output, thiết lập test/guardrails, refactor cho maintainability**.
3. **Từ "Specialist Silo" → "T-shaped + Business Fluency"**  
   - Senior BE Java phải hiểu FE cơ bản, DB tuning, Infra, **và nhất là domain knowledge** (fintech, e-com, logistics...).
4. **Từ "Học công nghệ mới" → "Học cách học &.eval công nghệ mới"**  
   - Harness study (J2TEAM): tool thay đổi hàng tháng. Kỹ năng bền: **thiết lập benchmark, eval harness, cost/quality trade-off**.

### Áp dụng cụ thể cho Dev Java/Spring Boot đang học Python + Network Security (Tuần này)
| Ngày | Hành động cụ thể | Mục tiêu |
|---|---|---|
| **Thứ 2-3** | **Python:** Xây dựng mini RAG pipeline local: `LangChain/LlamaIndex` + `ChromaDB/Qdrant` + `Ollama (llama3.1:8b)` + `FastAPI` expose `/query`. Viết unit test + integration test cho pipeline. | Hiểu end-to-end AI app, không chỉ gọi API OpenAI. Portfolio concrete. |
| **Thứ 4** | **Security:** Thực hành **Prompt Injection** lab (OWASP LLM Top 10). Dùng `LangChain` + `Guardrails AI` hoặc `Llama Guard` để detect injection. Viết blog note 500 từ: "Cách bảo vệ RAG pipeline khỏi prompt injection". | Kết hợp Python + NetSec → AI Security niche. Có artifact cho CV/LinkedIn. |
| **Thứ 5** | **System Design:** Vẽ diagram (Mermaid/Excalidraw) cho RAG pipeline trên: data ingestion, embedding, vector store, retrieval, generation, guardrails, observability (OpenTelemetry → Jaeger). Đánh giá trade-off: latency vs accuracy, cost vs quality. | Tư duy System Design + AI. Chuẩn bị cho phỏng vấn Senior/AI Eng. |
| **Thứ 6** | **Workflow:** Setup repo GitHub với: Conventional Commits, Husky pre-commit (lint, test), GitHub Actions CI (test, build docker, Trivy scan), Dependabot. Thử **vibe coding** một feature nhỏ với **Claude Code / Cursor** theo quy trình `/plan → /approve → /execute → /test → /commit` (tham khảo template Hỏi Dân IT). | Làm chủ AI-assisted workflow an toàn. Đây là skill ngay lập tức áp dụng được ở công ty. |
| **Thứ 7-Chủ Nhật** | **Network/NetSec:** Lab **mTLS giữa các service** trong RAG pipeline (Spring Boot gateway → Python RAG service) dùng `Istio`/`Linkerd` hoặc `Cilium`. Ghi chép config, troubleshoot cert rotation. | Kết hợp Java (gateway) + Python (AI) + NetSec (mTLS, zero trust). Full-stack security profile. |

**Tránh tuyệt đối:**  
- Chỉ đọc tutorial không code.  
- Học lướt qua 10 framework (LangGraph, CrewAI, AutoGen, Semantic Kernel...) không sâu cái nào.  
- Bỏ qua Git/Testing/Observability khi vibe coding — đó là đường tắt đến technical debt.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

| # | Bình luận (trích dài) | Tác giả / Votes / Insight | Nguồn (Link) | Tại sao đáng đọc |
|---|---|---|---|---|
| 1 | **"Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó, kĩ năng đó hình thành từ nhiều năm đi làm chứ ko phải một sớm 1 chiều, mà ngay cả khi ae muốn tìm hiểu thì cũng chưa chắc có cơ hội. Chuyện AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi, tuy ko đc 100% nhưng nó cũng làm dc 95-98% tùy vào cách ae setup + research. Chuyện lập trình viên ko cần code là chuyện trước mặt rồi, ko phải tương lai nữa, thế nên ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh. Với tình trạng mất não ko thể đọc tài liệu quá 100 dòng hiện nay thì thị"** | @phutran-z6h · 14 votes · **Insight 12.0** | [Video Tips JS "No Code"](https://www.youtube.com/watch?v=gxIKlsOzq70) | **Nói trúng "nỗi đau" dev VN:** task-based mindset là rào cản lớn nhất. Khẳng định AI đã làm 95-98% code/test — dev phải chuyển sang business+system+people skills. Cảnh báo "mất não đọc tài liệu >100 dòng" — thách thức học tập thực tế. |
| 2 | **"E nói thật chứ có kinh nghiệm kĩ thuật, năng lực,... Ở đâu cũng sống đc, chứ tại sao cứ phải suy nghĩ phải lm cho tư bản mới đc, như e làm tự do tháng đều đều trung bình cũng hơn 25 củ vưà lm vừa chơi, chưa kể sống ở nhà nông thôn nên chi phí sống vẫn dư giả chán, thấy nhiều người thất bại chỉ biết lắc đầu cười, ko phải cười họ thất bại, mà cười họ ko biết mình thất bại ở đâu rồi lấy cái lý do nào đó để tự nhủ cho cái thất bại của mình😅"** | @NguyênNguyễnVăn-m6e3o · 4 votes · **Insight 4.5** | [Video Tips JS "No Code"](https://www.youtube.com/watch?v=gxIKlsOzq70) | **Góc nhìn phi truyền thống:** Freelance/remote + geo-arbitrage (sống nông thôn) cho income 25tr+/tháng. Nhấn mạnh **tự nhận thức lỗi lặp lại** thay vì đổ lỗi market. Hữu ích cho dev muốn thoát कुएn "cố định văn phòng". |
| 3 | **"Antigravity được thiết kế kỹ phết mà lại bị mang tiếng xấu. Điểm yếu chắc là cache tệ, search tool như đb ko support native multi-agent, với độ sâu customization kém thôi. Chứ experience dạo này cực tốt. Quả brain lưu memory chuẩn xác vl, gần như ko cần refer context mấy. Có mấy cái internal plugin sát với workflow. Console response cực gọn, dễ inspect. Ko bao giờ thấy chơi A/B testing hay sụt performance. Nói chung là cực kỳ tốt với beginner hoặc dân business/research."** | Facebook user · 0 votes · **Insight 4.5** | [Bài J2TEAM "Harness chi phí lệch 5 lần"](https://facebook.com/groups/j2team.community/permalink/3254565451542219/) | **Review kỹ thuật sâu về IDE agent (Antigravity):** chỉ ra memory management, plugin ecosystem, console UX — yếu tố quyết định productivity thực tế khi vibe coding. Giúp lựa chọn tooling hợp lý. |
| 4 | **"từ blog của langchain về harness engineering, t bt sự thật là model tiến hoá theo harness (gpt-codex, gemini-antigravity,...), vì vậy model hoạt động tốt nhất khi đi kèm với harness nhà trồng (có vài trg hợp như thg qwen 3.8 train bằng opus distill nên claude code rất tốt đối với nó) check terminal bench 4.0 là rõ nhất"** | Facebook user · 0 votes · **Insight 2.0** | [Bài J2TEAM "Harness chi phí lệch 5 lần"](https://facebook.com/groups/j2team.community/permalink/3254565451542219/) | **Insight quan trọng về co-evolution Model ↔ Harness:** Không chỉ chọn model tốt, phải chọn **cặp model+harness đồng bộ**. Terminal Bench 4.0 là benchmark tham chiếu. |
| 5 | **"anh lead cũ của con nói với con là \" thời này rồi nó cũng qua thôi, bám trụ đi em, không thiệt thòi đâu, ngành mình lương vẫn cao hơn rất nhiều so với các ngành khác, cơ mà phải update bản thân nhiều hơn để không bị đào thải \""** | @iuNgocDuong · 21 votes · **Insight 1.0** | [Video Tips JS "No Code"](https://www.youtube.com/watch?v=gxIKlsOzq70) | **Lời khuyên từ Lead thực tế:** Market cyclical, lương IT vẫn cao so với ngành khác, **điều kiện** là "update bản thân nhiều hơn". Cân bằng giữa optimism và urgency. |

> English reference: "The issue is everyone works in task-split/role-split mode, now asking them to understand the whole business system is hard — that skill takes years, not one morning... AI can now design, run perf/security/e2e/uiux tests... 95-98% done... so devs must focus on business + system + people skills." — @phutran-z6h

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| # | Nguồn | Loại / Region | Luận điểm chính | Góc nhìn nổi bật từ bình luận | Lý do chọn |
|---|---|---|---|---|---|
| 1 | **[Khi ai cũng viết code nhanh nhờ AI, anh em kỹ sư cần đứng ở đâu?](https://facebook.com/groups/vgu.tech.alumni/permalink/1510513554318487/)** | Facebook · VN | Team nhỏ (6-7 người) dùng AI chạy 5-6 project, productivity +30-40%. Bài toán cốt lõi: **nâng trust level, giữ System Design, chuyển know-how → know-what**. | Không có comment deep, nhưng tóm tắt video Quân IT rất chính xác — là **manifest của xu hướng VN 2025-2026**. | Expert voice (Quân IT - Tech Lead/CTO cấp), region VN, relevance 38.9, gói gọn strategic shift. |
| 2 | **[Nghiên cứu Harvard 300M data points: AI viết code nhanh hơn nhưng việc done không tăng](https://facebook.com/groups/vgu.tech.alumni/permalink/1510335027669673/)** | Facebook · VN | 718 công ty, 5 năm: code +30%, commit +20%, PR +23% → **ticket done 0%**. Bottleneck dời sang PR review (+49% time), sửa code (x2), comment (+35%). Layoff dùng cớ AI ép người còn lại gánh hơn. | Comment: "đó là Amazon, có mấy Amazon, thực tế chung ngành thì không phải vậy" — **cảnh báo generalize từ big tech**. | Dữ liệu thực tế lớn, định lượng bottleneck chuyển từ coding → review/quality. Cảnh báo "AI productivity theater". |
| 3 | **[Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI](https://www.youtube.com/watch?v=kRXoK02KJow)** | YouTube (Tips JS) · VN | Hướng dẫn kỹ thuật Vector DB, Embedding, RAG — nền tảng cho AI Engineer. | @duythanh1602 (1 vote, insight 3.5): *"Backend 5 năm kinh nghiệm có nên chuyển sang AI Engineering không? Em nộp CV thấy toàn AI nhiều"* — **câu hỏi thực tế của nhiều senior BE VN**. | Expert voice (AnonyViet/Backend lead), relevance 56, kỹ thuật sâu, gắn liền career pivot BE→AI Eng. |
| 4 | **[Don't Choose the Wrong Tech Career in 2026](https://www.youtube.com/watch?v=INy9de3U9m0)** | YouTube (Tech Easylearn) · GLOBAL | 149k layoffs 2026, junior jobs giảm, AI viết code hơn. Phân tích job growth: AI/ML, Security, Data, Platform Eng. New roles: AI Product Manager, Prompt Engineer, AI Safety. | Không có comment. | Global macro view, relevance 69.1 (cao nhất dataset), mapping job growth → skill map. Áp dụng VN: Security & Platform Eng đang hire mạnh ở VN. |
| 5 | **[The Real Reason It's So Hard To Get a Junior Dev Job Now](https://www.youtube.com/watch?v=XcyZ7bJabvI)** | YouTube (Complexity Compiled) · GLOBAL | 4.5% entry-level roles 2026. Senior 69%. AI làm junior work, layoff tràn senior xuống. Hiring manager screen: **production impact ngay, không còn high-volume apply**. | Không có comment. | Giải thích cơ chế "rung đầu thang" biến mất. Dev VN fresher phải hiểu để điều chỉnh chiến lược (portfolio > degree, internship > course cert). |
| 6 | **[Cùng một mô hình AI, chi phí lập trình lệch tới 5 lần tùy harness](https://facebook.com/groups/j2team.community/permalink/3254565451542219/)** | Facebook (J2TEAM) · VN | FrontierHarness Eval: 22 harness, 5 models, 83B tokens. Harness quyết định cost variance 1.8-5x. Rank đảo lộn khi đổi model. Harness đắt ≠ hiệu quả cao. | 3 comment insight 4.5, 2.0, 1.0: **Antigravity memory/plugin tốt, model-harness co-evolution, terminal bench 4.0**. | Dữ liệu benchmark thực tế, community VN chuyên sâu (J2TEAM), relevance 40.7. Giúp chọn tooling tiết kiệm chi phí enterprise. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào với `is_major_incident = true` trong bộ dữ liệu cung cấp. Bỏ qua mục này.*