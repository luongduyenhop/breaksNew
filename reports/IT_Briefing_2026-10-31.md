📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/open?id=10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

---

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
*   **Dịch chuyển cốt lõi: Từ "Viết code" sang "Kiến trúc & Điều phối AI + Hiểu Business".**  
    Bình luận có `insight_score` cao nhất (12.0) của **@phutran-z6h** (video "No Code" - Tips Javascript) khẳng định: AI đã làm được 95-98% việc code (test, security, UI/UX). Lập trình viên ở VN *bắt buộc* chuyển sang hiểu nghiệp vụ (business), hệ thống toàn cảnh (system) và kỹ năng làm việc với người. Việc chỉ nhận task và code là "chết chắc".
*   **Thị trường Junior/Fresher "đóng băng", Senior bị ép KPI nhờ AI.**  
    **Tôi Đi Code Dạo** (video 2026, relevance 54) và bình luận **@JavaOnly_** tóm gọn: Bigtech layoff + sinh viên ra trường hàng chục ngàn + AI tăng năng suất = cung vượt cầu cực lớn ở cấp độ Junior. Các công ty VN đang "lay hoay chuyển hướng" (**@thong9564**) nhưng chưa rõ đường lối.
*   **Xu hướng "AI Engineer" thực tế là RAG + Vector DB + Local LLM, không phải train model.**  
    Video **Vector Databases** (Tips Javascript, relevance 66, expert 1.5) và bình luận **@vantran_devopsinfra** (insight 2.0) minh họa quy trình production: Chunking -> Embedding (BGE-m3) -> Vector Search (Mongo/PGVector) -> LLM Local (Qwen). Đây là kỹ năng "hard" cần có ngay cho dev VN muốn chuyển dòng.
*   **Tesla tuyển dụng tại VN (5 vị trí đầu) báo hiệu nhu cầu Embedded/Automotive/High-performance computing.**  
    Tin Google News (relevance 36) cho thấy các tập đoàn lớn vào VN không chỉ thuê dev web thuần túy mà cần kỹ sư hệ thống sâu, an ninh mạng, hiệu năng cao.

### Trên thế giới (và ý nghĩa với Việt Nam)
*   **Anthropic (hãng AI hàng đầu) đã bỏ phỏng vấn LeetCode thuần túy.**  
    **The Pragmatic Engineer** / **Dev.to** (expert_voice_score 3.0) tiết lộ Engineering Manager Felix Rieseberg dừng việc yêu cầu algorithm coding. *Ý nghĩa VN:* Các công ty Outsourcing/Product lớn tại VN (FPT, VNG, TikTok VN, v.v.) sẽ theo kịp trong 6-12 tháng. Phỏng vấn sẽ xoay quanh **System Design, Debug thực tế, Prompt Engineering, RAG Pipeline**.
*   **Microsoft freiwillige Austritt (voluntary exit) & Goldman Sachs: AI layoff để lại sẹo lâu dài.**  
    Video Microsoft (relevance 72) & Hacker News Goldman (relevance 46). *Ý nghĩa VN:* Các nhà tuyển dụng VN (đặc biệt là nhánh của Bigtech hoặc công ty خدم AI) sẽ "giảm bớt headcount, tăng chất lượng". Một dev phải tạo ra giá trị gấp 2-3x lương cũ nhờ công cụ AI.
*   **Hiring 2026 yêu cầu "Full Stack + Cloud + AI Tooling" làm baseline.**  
    Video **Akash Tolanur** (relevance 48.7): JD lặp lại React, Node, TS, Cloud, Docker, CI/CD, **AI Tools**. *Ý nghĩa VN:* Dev Java/Spring Boot không thể chỉ biết Spring Boot. Phải container hóa (Docker/K8s), biết CI/CD, và biết nhúng AI vào pipeline (Spring AI, LangChain4j).

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

| Kỹ năng / Công nghệ | Trạng thái | Vì sao (Nguồn) | Cách học gợi ý cho Dev Java/Spring Boot |
| :--- | :--- | :--- | :--- |
| **RAG & Vector Database (PGVector, Mongo Atlas, Milvus, Qdrant)** | **Xu hướng thật, cần ngay** | Video Vector DB (Tips JS), Comment @vantran_devopsinfra (insight 2.0): Triển khai thực tế BGE-m3 + Qwen + Mongo Vector Search. | Dùng **Spring AI** tích hợp PGVector (PostgreSQL) hoặc Mongo. Viết 1 project: Chatbot tài liệu nội bộ công ty (PDF -> Chunk -> Embed -> Search -> Gen). |
| **AI Agent Workflow & Tooling (Claude Code, Cursor, Antigravity IDE, Git)** | **Xu hướng thật, kỹ năng "sống còn"** | Series Hỏi Dân IT (relevance 51, 43): Vibe Coding an toàn với Git. Comment @hoidanit (insight 2.0): Local multi-agent. | Học **Antigravity IDE** hoặc **Claude Code** (CLI). Bắt buộc: Quy trình Git (commit nhỏ, branch feature, revert khi AI hỏng). Đừng "vibe" mà không có version control. |
| **System Design & Kiến trúc phân tán** | **Cốt lõi, không thể thiếu** | Video System Design (Tips JS, relevance 40). Comment @phutran-z6h (insight 12): Hiểu cả hệ thống. | Học: Load Balancing, Cache (Redis), Message Queue (Kafka/RabbitMQ), DB Sharding/Replication. Luyện case study: Thiết kế hệ thống RAG serving 10k req/s. |
| **Cloud Native & DevOps cơ bản (Docker, K8s, CI/CD, Linux Network)** | **Baseline bắt buộc** | Video Akash Tolanur (relevance 48.7): JD lặp lại Cloud, Docker, CI/CD. | Container hóa Spring Boot app. Viết GitHub Actions/GitLab CI: Build -> Test -> Scan Security (Trivy) -> Deploy K8s (minikube/local). |
| **Python cho AI/NetSec (FastAPI, LangChain, Scapy, eBPF)** | **Mở rộng stack, đắt giá** | Bối cảnh người đọc + Comment @giappham3462 (Vector DB): Cần local AI, bảo mật code. | Viết **FastAPI service** phục vụ Embedding/Inference (vLLM/Ollama) gọi từ Spring Boot. Học eBPF/BPFtrace để observability/security kernel-level. |
| **LeetCode Hard / Thuật toán thuần** | **Hype / Giảm trọng số** | Anthropic bỏ coding interview (Pragmatic Engineer, expert 3.0). | Chỉ ôn **LeetCode Medium** (Pattern: Sliding Window, Two Pointers, BFS/DFS Tree/Graph). Dành thời gian cho System Design & AI Project. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG (CHO DEV JAVA/SPRING BOOT + PYTHON/NETSEC)

### Thay đổi tư duy cốt lõi (từ cộng đồng)
1.  **Từ "Task Executor" → "Business Problem Solver"**: Đừng chờ PM chia task. Hiểu *tại sao* feature này làm tiền/lưu user. (**@phutran-z6h**, insight 12).
2.  **Từ "Code Owner" → "AI Orchestrator / Reviewer"**: Code do AI gen, bạn đọc hiểu, review security/performance/architecture, tích hợp. (**@phutran-z6h**, **Hỏi Dân IT series**).
3.  **Từ "Stack đơn nhất" → "Polyglot Pragmatist"**: Java làm Backbone (Transaction, Stability), Python làm AI/Scripting/NetSec, Go/Rust làm Sidecar/High-perf. (**@vantran_devopsinfra** dùng Python/Go cho pipeline RAG).
4.  **Security by Design (Local First)**: Comment **@giappham3462** lo ngại data leak qua API AI Agent. Xu hướng **Local LLM / On-premise AI** sẽ nổ ở VN (Ngân hàng, Chính phủ, Doanh nghiệp lớn). Network Security skill giờ là "AI Security" (Prompt Injection, Data Exfiltration via RAG).

### Kế hoạch hành động TUẦN NÀY (Cụ thể)
| Ngày | Focus | Hành động cụ thể (Output) |
| :--- | :--- | :--- |
| **Thứ 2-3** | **RAG + Vector DB (Java Stack)** | Tạo project Spring Boot 3.3 + Spring AI + PostgreSQL (PGVector). Index 50 trang PDF tài liệu kỹ thuật. Viết API `/ask` trả lời có trích dẫn source chunk. |
| **Thứ 4** | **Python AI Serving + NetSec** | Setup **Ollama/vLLM** chạy Qwen2.5-Coder/BGE-m3 local. Viết **FastAPI** wrapper `/embed`, `/generate`. Cấu hình **mTLS** giữa Spring Boot và FastAPI (NetSec practice). |
| **Thứ 5** | **AI Agent Workflow + Git Safety** | Cài **Antigravity IDE** hoặc **Claude Code**. Dùng nó *chỉ* để: (1) Gen test case cho RAG service, (2) Refactor code, (3) Viết Dockerfile/K8s manifest. **Bắt buộc**: Commit từng step, viết commit message rõ ràng. |
| **Thứ 6** | **System Design & Security Review** | Vẽ sơ đồ kiến trúc hệ thống RAG vừa dựng (Draw.io/Excalidraw). Đánh giá threat model: PII leakage trong chunk? Prompt injection? DDoS embedding endpoint? Viết doc `SECURITY.md`. |
| **Thứ 7-CN** | **Portfolio & Network** | Push code lên GitHub (README chi tiết: Kiến trúc, Tech stack, Cách chạy, Kết quả benchmark). Viết 1 bài LinkedIn/Viblo tóm tắt bài học: *"Từ Spring Boot Dev xây RAG Local-First với AI Agent"*. Comment vào 3 bài viết của Tech Lead/Recruiter VN. |

**Tránh tuyệt đối:** Ngồi "vibe coding" mà không commit Git, không review code AI sinh ra, chỉ học theory không chạy được local, chỉ làm LeetCode.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT (TOP INSIGHT SCORE)

### 1. **@phutran-z6h** — *Insight: 12.0 | Votes: 14*  
**Nguồn:** Video **"No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?"** (Tips Javascript) — [Link](https://www.youtube.com/watch?v=gxIKlsOzq70)  
**Nội dung đầy đủ:**  
> "Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó, kĩ năng đó hình thành từ nhiều năm đi làm chứ ko phải một sớm 1 chiều, mà ngay cả khi ae muốn tìm hiểu thì cũng chưa chắc có cơ hội. Chuyện AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi, tùy ko đc 100% nhưng nó cũng làm dc 95-98% tùy vào cách ae setup + research. Chuyện lập trình viên ko cần code là chuyện trước mặt rồi, ko phải tương lại nữa, thế nên ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh. Với tình trạng mất não ko thể đọc tài liệu quá 100 dòng hiện nay thì thị"  
**Tại sao đọc:** Đây là **manifesto** thực tế nhất về vai trò dev mới. Nó bác bỏ hype "AI thay dev" và định nghĩa lại giá trị: *Business Acumen + System Thinking + Human Skills*. Người đọc nên in câu "hiểu bussiness + hệ thống" dán trước màn hình.

### 2. **@NguyênNguyễnVăn-m6e3o** — *Insight: 4.5 | Votes: 2*  
**Nguồn:** Video **"No Code..."** (Tips Javascript) — [Link](https://www.youtube.com/watch?v=gxIKlsOzq70)  
**Nội dung đầy đủ:**  
> "E nói thật chứ có kinh nghiệm kĩ thuật, năng lực,... Ở đâu cũng sống đc, chứ tại sao cứ phải suy nghĩ phải lm cho tư bản mới đc, như e làm tự do tháng đều đều trung bình cũng hơn 25 củ vưà lm vừa chơi, chưa kể sống ở nhà nông thôn nên chi phí sống vẫn dư giả chán, thấy nhiều người thất bại chỉ biết lắc đầu cười, ko phải cười họ thất bại, mà cười họ ko biết mình thất bại ở đâu rồi lấy cái lý do nào đó để tự nhủ cho cái thất bại của mình😅"  
**Tại sao đọc:** Góc nhìn **Freelance/Remote/Geo-arbitrage** tại VN. Khẳng định kỹ năng cứng (technical competence) cho phép thoát khỏi cuộn lương/thương lượng kém. Nhắc nhở trách nhiệm bản thân (accountability) thay vì đổ lỗi thị trường.

### 3. **@duythanh1602** — *Insight: 3.5 | Votes: 1*  
**Nguồn:** Video **"Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI (AI Engineer)."** (Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)  
**Nội dung đầy đủ:**  
> "Đại ca ơi, giờ backend 5 năm kinh nghiệm có nên chuyển hướng sang AI engineering ko hay tập trung ôn tiếp BE vậy, vì em nộp thử CV thì thấy toàn AI nhiều"  
**Tại sao đọc:** Câu hỏi đau đáu của **Senior Backend (5 năm)** đang bị ép buộc chuyển dòng. Phản ánh thực tế JD VN: "Toàn AI nhiều". Cần có roadmap chuyển đổi rõ (Backend -> RAG/System -> AI Engineer) thay vì bỏ BE học train model.

### 4. **@vantran_devopsinfra** — *Insight: 2.0 | Votes: 8*  
**Nguồn:** Video **"Vector Databases..."** (Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)  
**Nội dung đầy đủ:**  
> "Xưa em từng làm dự án sinh viên, nôm na là tự build 1 con AI để có thể trả lời 1 số chủ đề cụ thể trong 1 file tài liệu lớn, lúc đó em có suy nghĩ không thể đưa cho AI 1 file lớn như vậy và rồi chỉ để hỏi 1 số chủ đề trong đó, vì vậy cần 1 giải pháp tối ưu đó là RAG. Trước tiên cắt tài liệu thành các Chunks, dùng 1 model BGE (BGE-m3) để embedding các Chunks tài liệu, rồi đẩy vào Mongo Vector Search, sau đó embedding câu hỏi và truy vấn trong MongoDB Vector Search để lấy top K số Chunks liên quan, và rồi đẩy câu hỏi text kèm top K Chunks text vào LLM (Qwen2.5-3B) để trả lời. Cảm ơn video của anh làm em nhớ lại kỉ niệm sinh viên. Điểm thú vị đó là tìm ra điểm chưa tối ưu và tìm cách để tối ưu"  
**Tại sao đọc:** **Case study thực chiến** full pipeline RAG production-ready: Chunking -> BGE-m3 -> Mongo Vector Search -> Qwen2.5. Đây chính là "bài tập lớn" người đọc nên replicate ngay tuần này (thay Mongo bằng PGVector để tận dụng Java/Spring).

### 5. **@giappham3462** — *Insight: 2.0 | Votes: 1*  
**Nguồn:** Video **"Vector Databases..."** (Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)  
**Nội dung đầy đủ:**  
> "em có suy nghĩ như này:Giờ các AI aigent nhiều,toàn kéo API,tức là vấn đề bảo mật lộ ra ngoài á.Rồi sẽ có 1 lúc,các công ty sẽ cần những AI local,và code chay.Vì thế em nảy ra 1 ý tưởng,train AI local,theo phong các code của em,.. hiện tại,trên lý thuyết,em cũng nghĩ đến phương vector databases kết hợp chunking,để nó hiểu code em đang code là gì,để nó gợi ý tiếp theo,hoặc nó gen ra code,mà em mô tả cho nó (đương nhiên em sẽ viết skill,cho llm hiểu được ạ)"  
**Tại sao đọc:** Dự đoán xu hướng **Local AI / On-premise AI** driven by **Security/Privacy** (Data leak via API). Gợi ý niche cực hot: **Code Assistant Local (RAG on Codebase)**. Kết hợp hoàn hảo với background Network Security của người đọc.

> **English reference:**  
> > @phutran-z6h: "AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi... làm dc 95-98%... ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh."  
> > @vantran_devopsinfra: "Chunking -> BGE-m3 embedding -> Mongo Vector Search -> Qwen2.5-3B... tìm ra điểm chưa tối ưu và tìm cách để tối ưu."  
> > @giappham3462: "Các AI agent nhiều, toàn kéo API -> vấn đề bảo mật lộ ra ngoài -> công ty sẽ cần AI local."

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY (ƯU TIÊN THEO RELEVANCE & EXPERT VOICE)

| # | Nguồn | Loại / Khu vực | Luận điểm chính / Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Vector Databases - Kỹ sư lập trình đến Kỹ sư AI](https://www.youtube.com/watch?v=kRXoK02KJow)** (Tips Javascript) | **[VN] Video** (Relevance 66, Expert 1.5) | Định nghĩa rõ ràng lộ trình **Backend -> AI Engineer** qua Vector DB/RAG. Tech stack cụ thể: Embedding models, Vector DB, RAG Flow. | **Chuyên gia Backend (Anonystick) nói chuyện backend.** Comment chất lượng cao (@vantran_devopsinfra, @giappham3462) cho case study thực tế. Bắt buộc xem để xây project tuần này. |
| **2** | **[No Code | Lập trình viên mất việc?](https://www.youtube.com/watch?v=gxIKlsOzq70)** (Tips Javascript) | **[VN] Video** (Relevance 64.5, Expert 1.5) | AI đã làm 95% coding. Dev phải chuyển sang **Business + System + Soft Skills**. Phỏng vấn sẽ hỏi System Design, không hỏi syntax. | Comment **@phutran-z6h (Insight 12)** là "kim chỉ nam" tư duy. Video đánh trúng nỗi lo "chia task" của dev VN. |
| **3** | **[The Pulse: Anthropic kills the coding interview](https://newsletter.pragmaticengineer.com/p/the-pulse-anthropic-kills-the-coding)** (Pragmatic Engineer) | **[Quốc tế] Article** (Relevance 34, Expert 3.0) | **Engineering Manager Anthropic** bỏ LeetCode. Phỏng vấn mới: Hiểu codebase, Debug, Design, AI Collaboration. | **Expert voice score cao nhất (3.0)**. Dự báo chu chuân cho thị trường VN (Outsource/Product follow BigTech). Người đọc phải đổi cách ôn phỏng vấn *ngay*. |
| **4** | **[Ngành lập trình IT năm 2026 ảm đạm?](https://www.youtube.com/watch?v=mOaakWt7txY)** (Tôi Đi Code Dạo) | **[VN] Video** (Relevance 54) | Junior/Fresher crisis. AI Agent bùng nổ. Lời khuyên: **Đừng ghét AI, dùng nó làm "force multiplier"**. | Góc nhìn macro VN thực tế (Layoff, Kinh tế, Cung cầu). Cảnh báo "qua cầu rút ván" cho Junior. |
| **5** | **[Software Development Isn't Dead… But Hiring Has Changed in 2026](https://www.youtube.com/watch?v=L2Gi3iKRMC8)** (Akash Tolanur) | **[Quốc tế] Video** (Relevance 48.7) | Phân tích JD thực tế: **React, Node, TS, Cloud, Docker, CI/CD, AI Tools** là baseline. Không chỉ biết 1 language. | Dữ liệu JD thực tế. Map trực tiếp cho dev Java: Phải biết Cloud/Container/CI/CD/AI Tooling ngoài Spring Boot. |
| **6** | **[Vibe Coding An Toàn Với Git](https://www.youtube.com/watch?v=r_4pDELxZz8)** (Hỏi Dân IT) | **[VN] Video** (Relevance 51.6) | Quy trình **Git + AI Agent (Claude Code, Antigravity)** để không mất code/hỏng code. | Kỹ năng "vibe coding có trách nhiệm" - bắt buộc cho dev hiện đại. Series hands-on, dễ làm theo. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào có `is_major_incident: true` trong batch này. Bỏ qua mục này.*