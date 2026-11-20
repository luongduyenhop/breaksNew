📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.7qxqeei0qjkg)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
*   **Sự sụp đổ của "Junior Coder" truyền thống & sự trỗi dậy của "System Thinker"**: Thị trường VN đang loại bỏ hẳn vai trò "nhận task -> code xong -> nộp". Bình luận có `insight_score` cao nhất (12 điểm) khẳng định: **AI đã làm được 95-98% việc code, test (performance, security, e2e, UI/UX)**. Lập trình viên VN buộc phải chuyển sang **hiểu Business (nghiệp vụ), hiểu toàn bộ Hệ thống (System Design), và Kỹ năng làm việc với con người**. Việc "chia task + chia role" quen thuộc đã thành gánh nặng (`@phutran-z6h`, Tips JS "No Code").
*   **Công ty VN đang "lay hoay chuyển hướng"**: Nhiều công ty chưa kịp thích nghi với AI Agent, dẫn đến tuyển dụng đóng băng hoặc yêu cầu khủng khiếp cho Fresher/Junior (`@thong9564`, Tôi Đi Code Dạo). Tuy nhiên, **làm tự do (Freelance/Remote) vẫn là lối thoát sống sinh** với thu nhập ổn định (>25 triệu/tháng) nếu có kỹ năng tự quản trị và kinh doanh bản thân (`@NguyênNguyễnVăn-m6e3o`, Tips JS "No Code").
*   **Chuyển dịch công nghệ cốt lõi: Từ Backend thuần -> AI Engineering (RAG, Vector DB, Local LLM)**: Kênh Tips Javascript (Anonystick - tiếng nói uy tín Backend VN) tập trung mạnh vào **Vector Databases, RAG, Local AI Agents**. Đây là tín hiệu rõ ràng: Backend Dev VN *phải* nắm vững stack AI để không bị lỗi thời (`@duythanh1602`, `@giappham3462`, Tips JS "Vector DB").

### Trên thế giới (Và ý nghĩa với Dev Việt Nam)
*   **Cuộc "đóng băng tuyển dụng Junior" là có thật, có số liệu**: Stanford Digital Economy Lab (tháng 8/2026) xác nhận: Nhóm 22-25 tuổi ở nghề dễ bị AI thay thế **thụt lùi 19% so với xu hướng** (tăng từ 15% năm 2025). Nhóm 41-49 tuổi **tăng 20%**. Chỉ **4.5% vị trí là Entry-level**, **69% là Senior** (Complexity Compiled, AI Fallout, Kilobrief).
    *   *Ý nghĩa VN:* Không thể chỉ "học code" để xin việc. Dev VN (dù Junior) phải xây dựng hồ sơ thể hiện **tác động production (production impact), tư duy hệ thống, và khả năng dùng AI an toàn** ngay từ đầu.
*   **Nhu cầu bùng nổ cho Senior/Staff chuyên Reliability, Infra, AI Safety**: Coinbase tuyển Senior Core Reliability ($186k-$218k/base) yêu cầu: **Own reliability projects, T0/T1 services, scalable configs/secrets, canary deployments, giảm toil** (Expert Voice Score: 6 - Recruiter chuyên ngành).
    *   *Ý nghĩa VN:* Kỹ năng **SRE/Platform Engineering (K8s, Observability, Deployment Safety, System Hardening)** là "vé vàng" cho Dev Java/Spring Boot muốn lên lương cao hoặc làm Remote cho quốc tế.
*   **AI Agent Reliability là mảng mới nổi (High Value)**: Bài viết Dev.to (`katul1512`) chỉ ra bài toán **"Agent hoàn thành 4/5 bước rồi fail -> Ai chịu trách nhiệm?"**. Cần **Failure Recovery, Compensating Transactions, Reliable Execution Guarantees** cho Multi-agent workflows.
    *   *Ý nghĩa VN:* Dev biết xây dựng **hệ thống điều phối AI agent bền vững (Orchestration, State Management, Rollback)** sẽ cực kỳ khan hiếm và đắt giá.
*   **AI viết code nhưng nợ kỹ thuật (Tech Debt) tăng gấp bội**: Kushal Vijay (Expert 3) và AI Fallout nhấn mạnh: AI sinh code nhanh -> Chi phí **review, debug, maintain, secure** tăng vọt. Vai trò Dev chuyển sang **Code Reviewer, Architect, Guardian of Quality**.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cứng (Hard Skills) - Ưu tiên theo thứ tự
| Kỹ năng | Tại sao quan trọng (Nguồn) | Mức độ ưu tiên |
| :--- | :--- | :--- |
| **Thiết kế & Triển khai RAG / Vector Search / Local LLM** | Tips JS "Vector DB" (Expert 1.5), Cmt `@vantran_devopsinfra` (Insight 2): RAG là xương sống mọi AI App doanh nghiệp. `@giappham3462` (Insight 2): Local AI cho Security/Privacy + Codebase Awareness. | **CRITICAL** |
| **System Design / Architecture (End-to-end)** | `@phutran-z6h` (Insight 12): "Tìm hiểu nghiệp vụ của cả hệ thống". Coinbase JD: "Understand architecture, improve scalability". Tôi Đi Code Dạo: AI chưa làm được架构设计. | **CRITICAL** |
| **Reliability Engineering / SRE Mindset (Observability, Canary, Circuit Breaker, Chaos Eng)** | Coinbase JD (Expert 6): Core Reliability là role hot nhất. Kushal Vijay: Chi phí maintain/scale là thách thức lớn. | **HIGH** |
| **AI Agent Orchestration & Safety (Workflow, State, Rollback, Guardrails)** | Dev.to `katul1512`: "Multi-agent workflows need failure recovery, compensating transactions". | **HIGH** |
| **Network Security / AppSec (OWASP, Zero Trust, Secure Code Review)** | Persona mục tiêu + `@giappham3462` (Local AI for security) + Coinbase (Secrets Management, Config Security). | **HIGH** (Phù hợp persona) |
| **Python (FastAPI/Flask) + AI Libraries (LangChain, LlamaIndex, Ollama, HuggingFace)** | Cần thiết để triển khai PoC AI/RAG từ nền Java Spring Boot. | **MEDIUM** |

### Công nghệ cụ thể (Stack nên nắm vững Q4/2026)
1.  **Vector DB:** PostgreSQL (pgvector), MongoDB Atlas Vector Search, Qdrant, Milvus.
2.  **Local LLM Runtime:** Ollama, LM Studio, vLLM (chạy Qwen, Llama 3, Phi-3 local).
3.  **Orchestration:** LangGraph, Temporal.io (cho reliable workflows), hoặc custom state machine.
4.  **Infra/Deploy:** Docker, Kubernetes (EKS/GKE), ArgoCD/Flux (GitOps), Prometheus/Grafana/Loki (Observability).
5.  **Java/Spring Boot 3.x:** Virtual Threads, GraalVM Native Image (giảm cold start cho AI services), Spring AI (module mới chính thức).

### Phân biệt Xu hướng thật vs Hype
*   **Thật (Real Demand):** RAG Productionizing, Local LLM Deployment, System Reliability, Secure AI/Code Review, Business Analysis.
*   **Hype / Đã bão hòa:** "Prompt Engineering" đơn thuần (đã thành kỹ năng cơ bản như Googling), Viết CRUD thuần túy bằng Copilot/Cursor (AI làm 95-98% - `@phutran-z6h`), Train model từ đầu (quá đắt/không cần cho 99% dev VN).

---

## 3. TƯ DUY & CÁCH ÁP DỤNG (CHO DEV JAVA/SPRING BOOT ĐANG HỌC PYTHON + NETWORK SECURITY)

### Thay đổi tư duy cốt lõi (Từ cộng đồng nhắc nhiều nhất)
1.  **Từ "Task Completer" -> "Business Problem Solver"**: Đừng hỏi "Task này code như nào?". Hãy hỏi "Task này giải quyết bài toán kinh doanh gì? Luồng dữ liệu đi đâu? Rủi ro bảo mật/performance ở đâu?" (`@phutran-z6h`, Insight 12).
2.  **Từ "Viết code" -> "Kiến trúc & Review code AI"**: Chấp nhận AI viết 80-90% boilerplate. Nhiệm vụ của bạn: **Kiến trúc hệ thống (Architecture), Định nghĩa Interface/Contract, Review an ninh/chất lượng, Xử lý Edge cases AI bỏ lỡ**.
3.  **Tư duy "Local-First & Privacy-First"**: Với Network Security background, hãy định vị mình là người **triển khai AI On-premise/Private Cloud** cho doanh nghiệp VN (Ngân hàng, Y tế, Chính phủ) - nơi dữ liệu không được ra ngoài API OpenAI/Anthropic (`@giappham3462`, Insight 2).
4.  **Tư duy "Reliability by Default"**: Mọi feature (kể cả AI feature) phải có: Health check, Metrics, Logs có cấu trúc, Rollback plan, Canary deploy. Đây là chuẩn Coinbase/Big Tech (Expert Voice 6).

### Kế hoạch hành động TUẦN NÀY (Cụ thể cho Persona)
| Ngày | Hành động cụ thể | Mục tiêu |
| :--- | :--- | :--- |
| **Thứ 2-3** | **Xây dựng PoC RAG Local cho codebase Java cũ:** Dùng **Python (FastAPI) + Ollama (Qwen2.5-Coder/CodeLlama) + ChromaDB/pgvector**. Index toàn bộ source code Spring Boot project. Cho AI trả lời: "Service X gọi DB bảng nào?", "Luồng authentication như nào?". | Biến thế mạnh Java + Security thành lợi thế: **Codebase Awareness AI**. Học Python实战, Vector DB, Local LLM. |
| **Thứ 4** | **Hardening Spring Boot App:** Cấu hình **Spring Security 6 + OAuth2 Resource Server + Testcontainers**. Viết test case tấn công (SQLi, XSS, Path Traversal) trên local. Tích hợp **OWASP Dependency Check / SpotBugs** vào CI/CD (GitHub Actions/GitLab CI). | Chứng minh kỹ năng **AppSec + DevSecOps** - thứ nhà tuyển VN/Remote cực kỳ cần. |
| **Thứ 5** | **Triển khai Observability Stack local:** Docker compose: **Prometheus + Grafana + Loki + Tempo (hoặc Zipkin)**. Instrument Spring Boot app (Micrometer) + Python AI Service (OpenTelemetry). Tạo Dashboard: Latency, Error Rate, Token Usage/Cost (AI), JVM Metrics. | Học **SRE/Observability** - kỹ năng "Senior/Staff" theo chuẩn Coinbase. |
| **Thứ 6** | **Vibe Coding an toàn với Git (Workflow):** Thực hành series "Hỏi Dân IT": Tạo feature branch -> Dùng Cursor/Claude Code sinh code -> **Commit từng bước logic nhỏ** -> Chạy test/security scan -> Merge Request -> Review bằng checklist (Security, Performance, AI Hallucination check). | Biến "Vibe Coding" từ nguy hiểm thành **Quy trình chuyên nghiệp**. Tránh "mất code/hỏng code". |
| **Thứ 7-CN** | **Viết 1 bài Blog/LinkedIn (Tiếng Anh/VN):** "How I built a Local Code Assistant for Legacy Java Systems with RAG & Ollama" hoặc "Securing Spring Boot Apps in the Age of AI Code Generation". | **Personal Branding** - Quan trọng để phá vỡ "Junior Freeze", thu hút Freelance/Remote (theo `@NguyênNguyễnVăn-m6e3o`). |

### TRÁNH TUẦN NÀY
*   ❌ Học lý thuyết ML thuần (Backprop, Gradient Descent) - Không ROI cho Dev ứng dụng.
*   ❌ Chỉ code LeetCode/DSA thuần - Không giải quyết bài toán "Production Impact" nhà tuyển đang đòi.
*   ❌ Đăng ký khóa học "AI Agent" đắt tiền chỉ dạy kéo API OpenAI - Hãy tự build Local RAG (miễn phí, học sâu hơn, an toàn hơn).

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT (TOP INSIGHT SCORE)

### 1. `@phutran-z6h` — **Insight Score: 12.0** (Cao nhất toàn bộ dữ liệu)
*   **Nguồn:** Video "No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?" (Tips Javascript) — [Link](https://www.youtube.com/watch?v=gxIKlsOzq70)
*   **Votes:** 14
*   **Nội dung đầy đủ:**
    > "Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó, kĩ năng đó hình thành từ nhiều năm đi làm chứ ko phải một sớm 1 chiều, mà ngay cả khi ae muốn tìm hiểu thì cũng chưa chắc có cơ hội. Chuyện AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi, tuy ko đc 100% nhưng nó cũng làm dc 95-98% tùy vào cách ae setup + research. Chuyện lập trình viên ko cần code là chuyện trước mặt rồi, ko phải tương lai nữa, thế nên ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh. Với tình trạng mất não ko thể đọc tài liệu quá 100 dòng hiện nay thì thị"
*   **Tại sao đọc:** Đây là **cảnh báo thực tế nhất** từ người trong nghề VN. Nó bóp chết quan niệm "học code tốt là đủ". Chỉ ra 3 trụ cột sống còn: **Business, System, Soft Skills**. Con số "AI làm 95-98% coding/testing" là tham chiếu rất cụcreto cho việc lên kế hoạch học tập.

> English reference: "The problem is everyone is used to splitting tasks/roles... AI designing, running tests (perf, sec, e2e, uiux) is now very professional... does 95-98%... programmers not needing to code is happening now, not the future... focus on business + system + people skills."

---

### 2. `@NguyênNguyễnVăn-m6e3o` — **Insight Score: 4.5**
*   **Nguồn:** Video "No Code..." (Tips Javascript) — [Link](https://www.youtube.com/watch?v=gxIKlsOzq70)
*   **Votes:** 4
*   **Nội dung đầy đủ:**
    > "E nói thật chứ có kinh nghiệm kĩ thuật, năng lực,... Ở đâu cũng sống đc, chứ tại sao cứ phải suy nghĩ phải lm cho tư bản mới đc, như e làm tự do tháng đều đều trung bình cũng hơn 25 củ vưà lm vừa chơi, chưa kể sống ở nhà nông thôn nên chi phí sống vẫn dư giả chán, thấy nhiều người thất bại chỉ biết lắc đầu cười, ko phải cười họ thất bại, mà cười họ ko biết mình thất bại ở đâu rồi lấy cái lý do nào đó để tự nhủ cho cái thất bại của mình😅"
*   **Tại sao đọc:** Góc nhìn **Freelance/Remote/Location Independent** - lối thoát rất thực tế cho Dev VN khi thị trường tuyển dụng thu hẹp. Nhấn mạnh **tự nhận trách nhiệm** thay vì đổ lỗi thị trường/AI.

> English reference: "With technical skills/experience you can survive anywhere... why think you must work for capital? I freelance avg >25M VND/month... low cost of living in rural area... people fail because they don't know why they failed, just make excuses."

---

### 3. `@duythanh1602` — **Insight Score: 3.5**
*   **Nguồn:** Video "Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI" (Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)
*   **Votes:** 1
*   **Nội dung đầy đủ:**
    > "Đại ca ơi, giờ backend 5 năm kinh nghiệm có nên chuyển hướng sang AI engineering ko hay tập trung ôn tiếp BE vậy, vì em nộp thử CV thì thấy toàn AI nhiều"
*   **Tại sao đọc:** Đại diện cho **nhóm Backend Senior (5 năm) đang hoang mang trước wave AI**. Câu hỏi này xác nhận xu hướng: JDs đang yêu cầu AI skills ngay cả cho role Backend. Cần hướng dẫn lộ trình chuyển đổi cụ thể (Backend -> AI Engineer).

> English reference: "Bro, backend 5 years exp, should I pivot to AI engineering or keep grinding BE? I applied test CVs and see AI requirements everywhere."

---

### 4. `@vantran_devopsinfra` — **Insight Score: 2.0**
*   **Nguồn:** Video "Vector Databases..." (Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)
*   **Votes:** 8
*   **Nội dung đầy đủ:**
    > "Xưa em từng làm dự án sinh viên, nôm na là tự build 1 con AI để có thể trả lời 1 số chủ đề cụ thể trong 1 file tài liệu lớn, lúc đó em có suy nghĩ không thể đưa cho AI 1 file lớn như vậy và rồi chỉ để hỏi 1 số chủ đề trong đó, vì vậy cần 1 giải pháp tối ưu đó là RAG. Trước tiên cắt tài liệu thành các Chunks, dùng 1 model BGE (BGE-m3) để embedding các Chunks tài liệu, rồi đẩy vào Mongo Vector Search, sau đó embedding câu hỏi và truy vấn trong MongoDB Vector Search để lấy top K số Chunks liên quan, và rồi đẩy câu hỏi text kèm top K Chunks text vào LLM (Qwen2.5-3B) để trả lời. Cảm ơn video của anh làm em nhớ lại kỉ niệm sinh viên. Điểm thú vị đó là tìm ra điểm chưa tối ưu và tìm cách để tối ưu"
*   **Tại sao đọc:** **Case study thực tế, chi tiết kỹ thuật** (Chunking -> BGE-m3 Embedding -> Mongo Vector Search -> Qwen2.5-3B). Đây là **blueprint mẫu** cho Dev VN muốn build RAG production-ready. Nhấn mạnh việc "tìm ra điểm chưa tối ưu và tối ưu" - tư duy Engineer.

> English reference: "Built a student project: AI answering specific topics in large doc -> needed RAG. Chunk docs -> BGE-m3 embedding -> Mongo Vector Search -> embed query -> retrieve top K -> feed to Qwen2.5-3B. Interesting part: finding unoptimized parts and optimizing them."

---

### 5. `@giappham3462` — **Insight Score: 2.0**
*   **Nguồn:** Video "Vector Databases..." (Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)
*   **Votes:** 1
*   **Nội dung đầy đủ:**
    > "em có suy nghĩ như này:Giờ các AI aigent nhiều,toàn kéo API,tức là vấn đề bảo mật lộ ra ngoài á.Rồi sẽ có 1 lúc,các công ty sẽ cần những AI local,và code chay.Vì thế em nảy ra 1 ý tưởng,train AI local,theo phong các code của em,.. hiện tại,trên lý thuyết,em cũng nghĩ đến phương vector databases kết hợp chunking,để nó hiểu code em đang code là gì,để nó gợi ý tiếp theo,hoặc nó gen ra code,mà em mô tả cho nó (đương nhiên em sẽ viết skill,cho llm hiểu được ạ)"
*   **Tại sao đọc:** **Đoán trúng xu hướng "Local AI / Private AI"** cho Enterprise (Security/Privacy). Kết hợp **Vector DB + Codebase Chunking + Local LLM (Skill/Function Calling)**. Đây chính là hướng đi **"AI Engineer chuyên bảo mật/Code Assistant nội bộ"** - cực kỳ phù hợp với Persona Java + Network Security.

> English reference: "Many AI agents pull external APIs -> security/privacy leak risk. Companies will need Local AI running on-prem. Idea: Train local AI on my codebase style using Vector DB + chunking, so it understands my code, suggests next steps, generates code from description (with skills for LLM understanding)."

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY (ƯU TIÊN EXPERT VOICE & VN)

| # | Nguồn | Loại / Khu vực | Luận điểm chính / Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[VN] Tips Javascript: "No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?"** | Video (Expert Voice: 1.5 - Anonystick) | **Thực trạng VN thô nhất:** AI làm 95-98% code/test. Junior/Fresher chết sinh. Phải học Business + System + Soft Skills. Cmt `@phutran-z6h` (Insight 12) là "kinh thánh" định hướng. | **Bắt buộc xem.** Tóm gọn toàn bộ nỗi đau & cơ hội dev VN hiện nay. Expert voice uy tín cộng đồng Backend VN. |
| **2** | **[Global] Coinbase Hiring: Senior Software Engineer, Core Reliability** | Video/Shorts (Expert Voice: 6.0 - Recruiter Agency) | **Chuẩn mực Senior/Staff Global:** Lương $186-$218k. Yêu cầu: Reliability, Scalability, T0/T1 Services, Config/Secrets Management, Canary Deploy, Reduce Toil. Không hề nhắc "code giỏi", chỉ nhắc "hệ thống bền vững". | **Benchmark kỹ năng cao nhất.** Cho thấy Big Tech trả tiền cho **Reliability/Infra**, không phải CRUD. Dev VN muốn Remote/High-pay phải đánh vào mảng này. |
| **3** | **[VN] Tôi Đi Code Dạo: "Ngành lập trình và IT năm 2026 ảm đạm ra sao??"** | Video (Relevance 56, High Engagement) | **Tổng quan vĩ mô VN:** AI Agent bùng nổ. Junior/Fresher bi kịch ("qua cầu rút ván"). AI code đã "xịn". Khuyên: Đừng ghét AI, hãy dùng nó để làm việc nhàn hơn, lương cao hơn. Cmt `@hirunguyen4522` (180 votes): Thực tế thu nhập Junior thấp hơn xây dựng. | **Góc nhìn người dẫn đường cộng đồng VN.** Cập nhật tâm lý thị trường, cảnh báo "bi kịch Junior" rõ ràng. |
| **4** | **[VN] Tips Javascript: "Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI"** | Video (Expert Voice: 1.5) | **Lộ trình công nghệ cụ thể:** Vector DB là cầu nối từ Backend -> AI Engineer. RAG, Embedding, Chunking, Local LLM. Cmt `@vantran_devopsinfra` (Insight 2) cho full stack kỹ thuật; `@giappham3462` (Insight 2) chỉ hướng Local AI/Security. | **Hướng dẫn kỹ thuật "Taylor-made" cho Backend Dev VN.** Không hype, có code, có kiến trúc. |
| **5** | **[Global] Complexity Compiled / AI Fallout / Kilobrief: "The Real Reason It's So Hard To Get a Junior Dev Job Now" / "AI Isn't Firing People..."** | Video/Shorts (Relevance 48-63) | **Dữ liệu cứng (Stanford, Goldman, Indeed, JOLTS):** Junior roles 4.5%, Senior 69%. Tuổi 22-25 giảm 19% việc làm. AI không sa thải, AI **không tuyển**. Lương Junior stagnate, Senior tăng. | **Bằng chứng khoa học cho "Junior Freeze".** Giúp Dev VN chấp nhận thực tế, bỏ qua hy vọng vô lý, tập trung xây profile "Senior-like" ngay lập tức. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào với `is_major_incident = true`. Bỏ qua mục này.*