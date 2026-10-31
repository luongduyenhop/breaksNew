📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/open?id=10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
1.  **AI Agent & RAG trở thành kỹ năng "bắt buộc" cho Backend/Senior, không còn là "đặc thù AI Engineer"**
    *   Video **Vector Databases** (Tips Javascript) định vị rõ: việc hiểu Vector DB, Embedding, Chunking, RAG là mốc nâng cấp từ *Kỹ sư lập trình* sang *Kỹ sư AI*. Bình luận của `@duythanh1602` (Backend 5 năm) và `@giappham3462` cho thấy áp lực chuyển hướng thực tế: CV không có từ khóa AI/RAG khó pass screening.
    *   *Nguồn:* [Video Vector Databases](https://www.youtube.com/watch?v=kRXoK02KJow) (expert_voice_score: 1.5), bình luận `@duythanh1602` (insight 3.5), `@giappham3462` (insight 2.0).

2.  **Tiêu chuẩn tuyển dụng dịch chuyển từ "Code tay" sang "Hiểu Business + Hệ thống + Làm việc với AI"**
    *   Bình luận top nhất video **No Code** (`@phutran-z6h`, insight 12.0, 14 votes) khẳng định: AI đã làm được 95-98% coding/testing. Lập trình viên sống sót là người hiểu *business logic*, *kiến trúc hệ thống* và *soft skills*. Video **Tôi Đi Code Dạo năm 2026** đồng tình: Junior bị "qua cầu rút ván" vì AI làm code cơ bản tốt hơn họ.
    *   *Nguồn:* [Video No Code](https://www.youtube.com/watch?v=gxIKlsOzq70), bình luận `@phutran-z6h`; [Video Năm 2026](https://www.youtube.com/watch?v=mOaakWt7txY).

3.  **Thị trường tuyển dụng "ảo" và kiệt sức: Quy trình ATS/AI screening khiến dev giỏi cũng nộp hàng trăm form không hồi âm**
    *   Dù bài báo VnEconomy/VnReview nói "nhu cầu tăng", thực tế từ Hacker News (`Tech market feels like a data entry job`, `Looking for a tech job...`) và tin Microsoft sa thải VN cho thấy: quy trình tuyển dụng đã vỡ. Dev 5+ năm kinh nghiệm, làm SV remote vẫn phải nộp form thủ công hàng giờ, cạnh tranh toàn cầu.
    *   *Nguồn:* [HN: Tech market feels like data entry](https://news.ycombinator.com/item?id=50254751), [HN: Helpless data-entry nightmare](https://news.ycombinator.com/item?id=50254873), [Tin Microsoft sa thải VN](https://news.google.com/rss/articles/CBMifkFVX3lxTE1JdmtaZWxyTnktS3hHeUZ6OUQ2Y2hZQmpzTDlSenJIYXpxdDhYMmg1YlB1ZklZRnQ1U21DdFhGZDBuSGE2VHJNZnZaem9LRko4TGx0SVVucl9vYmI4WlVlQ3B2eGdlRldpSXV0dUYtNldtTmUyeFRXc0w3TTUwZw?oc=5).

### Trên thế giới (Ý nghĩa với Việt Nam)
1.  **LeetCode/Algo interview đang "chết" → Được thay thế bằng đánh giá thực chiến với AI (System Design, Debugging, Agent Workflow)**
    *   *The Pragmatic Engineer* báo Anthropic đã bỏ hẳn coding interview kiểu LeetCode. Microsoft voluntary exit (60k nhân sự) cho thấy Big Tech tái cấu trúc về *hiệu suất* chứ không phải cắt giảm headcount đơn thuần.
    *   **Ý nghĩa VN:** Công ty VN (outsourcing & product) thường theo đuổi trend chậm 6-12 tháng. Nên chuẩn bị *portfolios thực tế dùng AI build sản phẩm* thay vì grinding LeetCode.
    *   *Nguồn:* [The Pulse: Anthropic kills coding interview](https://newsletter.pragmaticengineer.com/p/the-pulse-anthropic-kills-the-coding), [Video Microsoft Layoffs](https://www.youtube.com/watch?v=KRDyv-wVKkU).

2.  **Goldman Sachs: AI Layoffs để lại "sẹo lâu dài" 40 năm → Dev trung niên/cập nhật chậm sẽ bị đào thải vĩnh viễn**
    *   Báo cáo Goldman (Fortune) so sánh sốc AI với các cuộc cách mạng công nghiệp trước: người bị vạch ra rất khó quay lại ngang ngửa.
    *   **Ý nghĩa VN:** Lương IT VN cao so với trung bình khu vực → Áp lực tự động hóa/tối ưu chi phí ở đây *mạnh hơn* nhiều nước. Dev 30+ tuổi không nắm AI/Architecture rất nguy hiểm.
    *   *Nguồn:* [Goldman says AI layoffs leaving lasting scar](https://fortune.com/2026/10/30/goldman-sachs-ai-layoffs-displaced-workers-older-workers-past-tech-disruptions/).

3.  **Chạy LLM Local (On-premise) là xu hướng bảo mật/Khách hàng Enterprise → Cần kỹ năng Infra/MLOps/Hardware**
    *   Video **Build PC chạy AI Local** (Tôi Đi Code Dạo) demo cấu hình RTX 5080/Ultra 9 chạy Agent, ComfyUI offline. Bình luận `@giappham3462` (video Vector DB) dự đoán: "Công ty sẽ cần AI local do bảo mật".
    *   **Ý nghĩa VN:** Nhiều dự án Outsourcing/Enterprise VN (Banking, Gov) *bắt buộc* data không ra khỏi VPN. Kỹ năng deploy LLMs local (Ollama, vLLM, TensorRT-LLM, GPU optimization) là "mỏ vàng" niche.
    *   *Nguồn:* [Video Build PC AI Local](https://www.youtube.com/watch?v=nFj7IlNYZMg), bình luận `@giappham3462` (Video Vector DB).

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cứng (Hard Skills) - Ưu tiên theo thứ tự
| Kỹ năng/Công nghệ | Tại sao quan trọng (Từ dữ liệu) | Mức độ ưu tiên |
| :--- | :--- | :--- |
| **RAG Pipeline & Vector DB** (Chunking, Embedding BGE-m3, MongoDB Vector Search/Pinecone/pgvector) | Core của mọi AI App hiện nay. Backend 5 năm hỏi "có nên chuyển sang AI Eng?" -> Trả lời: Học RAG trước. (`@duythanh1602`, `@vantran_devopsinfra`) | **CRITICAL** |
| **Agentic Workflow / Function Calling / Tool Use** (LangGraph, CrewAI, Antigravity/Claude Code) | "Vibe Coding" chuyên nghiệp = điều khiển Agent làm task phức tạp (code, test, deploy, browse). Series Hỏi Dân IT dạy Antigravity/Gemini CLI là minh chứng. | **CRITICAL** |
| **System Design & Architecture** (Scalability, Caching, Message Queue, DB Sharding) | AI code được logic cục bộ, *không* thiết kế được hệ thống phân tán, trade-off CAP, cost optimization. `@phutran-z6h` nhấn mạnh "hiểu hệ thống". Video Tips JS System Design (relevance 40) vẫn hot. | **HIGH** |
| **Local LLM Deployment & Optimization** (Ollama, vLLM, quantization GGUF/AWQ, GPU VRAM management) | Yêu cầu Enterprise/Banking VN: Data sovereignty. Video build PC AI local (Tôi Đi Code Dạo) chứng minh nhu cầu thực tế. | **HIGH (Niche)** |
| **Git & Version Control trong quy trình AI** (Branch strategy, revert AI mess, commit convention) | Series "Git siêu dễ cho Vibe Coding" (Hỏi Dân IT) nhấn mạnh: không sợ AI hỏng code nếu biết Git. Kỹ năng "an toàn" khi pair với AI. | **MEDIUM** |
| **Python Ecosystem cho AI/Data** (FastAPI, Pydantic, AsyncIO, Polars, UV package manager) | Java/Spring Boot dev *phải* biết Python để chạy inference, build API wrapper cho model, data preprocessing. | **HIGH** |

### Kỹ năng mềm / Tư duy (Soft Skills/Mindset) - Bắt buộc
1.  **Product Mindset / Business Understanding:** Hiểu *tại sao* làm feature, ROI là gì, user pain point là gì. (`@phutran-z6h`: "tìm hiểu nghiệp vụ của cả hệ thống").
2.  **AI Orchestration / Prompt Engineering nâng cao:** Không chỉ viết prompt, mà thiết kế *workflow*, *evaluation loop*, *guardrails* cho Agent.
3.  **Communication & Stakeholder Management:** Khi AI làm 95% code, giá trị dev là dịch business requirement -> technical spec cho AI, review output, negotiate scope.

---

## 3. TƯ DUY & CÁCH ÁP DỤNG (CHO DEV JAVA/SPRING BOOT ĐANG HỌC PYTHON + NETWORK SECURITY)

### Thay đổi tư duy cốt lõi
*   **TỪ:** "Tôi viết code Java/Spring Boot để implement ticket JIRA." -> **SANG:** "Tôi thiết kế giải pháp (dùng Java/Python/AI) giải quyết business problem, tôi orchestrate AI agents để generate 80% boilerplate, tôi focus 20%: Architecture, Security, Edge cases, Performance."
*   **TỪ:** "Học xong Python xong học Network Security." -> **SANG:** "Dùng Python *ngay* để build tool security automation / RAG cho knowledge base security / AI Agent phân tích log anomaly."

### Kế hoạch hành động TUẦN NÀY (Cụ thể,可执行)
| Thứ | Hoạt động chính | Mục tiêu đầu ra | Công cụ/Tham chiếu |
| :--- | :--- | :--- | :--- |
| **2-3** | **Build Mini RAG System cho Security Knowledge:** Dùng Python (FastAPI/LangChain/LlamaIndex) + Vector DB (Chroma/pgvector) + Embedding model (BGE-m3 local). Nạp các RFC, CVE reports, hardening guide. | Hiểu luồng RAG end-to-end; Có project demo cho CV (Backend + AI + Security). | `@vantran_devopsinfra` workflow; Video Vector DB. |
| **4** | **Thử nghiệm Local LLM cho Security Task:** Cài Ollama/vLLM trên máy cá nhân (hoặc GPU cloud free tier). Chạy model `llama3.1:8b` hoặc `qwen2.5-coder:7b`. Prompt: "Phân tích file nginx log này tìm dấu hiệu brute force / SQLi". | Biết chạy AI offline (yêu cầu Enterprise); Hiểu limit của local model vs API. | Video Build PC AI Local; `@giappham3462` idea. |
| **5** | **Vibe Coding 1 Tool Security nhỏ với AI Agent:** Dùng Antigravity IDE / Cursor / Claude Code. Yêu cầu: "Viết Python script scan subdomain, check takeover, output JSON". Yêu cầu AI viết test, Git commit từng bước. | Thói quen: Spec -> AI Code -> Review -> Test -> Commit. Không copy-paste mù. | Series Hỏi Dân IT (Antigravity, Git cho Vibe Coding). |
| **6-7** | **Ôn System Design một bài liên quan Security/Scale:** VD: "Thiết kế hệ thống Rate Limiting/WAF phân tán cho 10k RPS". Vẽ diagram, giải thích trade-off (Redis vs In-memory, Consistency vs Latency). Ghi âm nói tiếng Việt 15p. | Chuẩn bị phỏng vấn Senior/Lead; Chứng minh "hiểu hệ thống" - kỹ năng AI chưa thay thế. | Video Tips JS System Design; `@phutran-z6h` advice. |

### TRÁNH TUẦN NÀY
*   ❌ Grinding LeetCode Medium/Hard (trừ khi target FAIR/BigTech có vòng algo bắt buộc).
*   ❌ Học lý thuyết Network Security sâu (OSI model, TCP/IP handshake) *mà không code demo*.
*   ❌ Nộp CV hàng loạt qua LinkedIn/TopCV mà không customize cho JD (ATS sẽ filter out).
*   ❌ Học framework JS mới (Next.js, Svelte...) nếu mục tiêu là Backend/Platform/Infra.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT (TOP INSIGHT SCORE)

### 1. `@phutran-z6h` — **Insight Score: 12.0** (Video: *No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?*)
> **Nội dung:** "Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó, kĩ năng đó hình thành từ nhiều năm đi làm chứ ko phải một sớm 1 chiều, mà ngay cả khi ae muốn tìm hiểu thì cũng chưa chắc có cơ hội. Chuyện AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi, tùy vào cách ae setup + research. Chuyện lập trình viên ko cần code là chuyện trước mặt rồi, ko phải tương lại nữa, thế nên ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh. Với tình trạng mất não ko thể đọc tài liệu quá 100 dòng hiện nay thì thị"
> **Link:** [Xem bình luận](https://www.youtube.com/watch?v=gxIKlsOzq70&lc=Ug...)
> **Tại sao đọc:** **Bản chất thực tế nhất về "Junior/Fresher死路一条" (dead end).** Người này đã trải qua, nhìn thấy AI làm 95-98% việc code/test. Ông chỉ ra *bottleneck* chính: Dev Việt Nam quen "chia task" (ticket-driven) nên thiếu tư duy hệ thống/business. Lời khuyên "hiểu business + hệ thống + soft skills" là *survival kit* duy nhất.

### 2. `@vantran_devopsinfra` — **Insight Score: 2.0** (Video: *Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI*)
> **Nội dung:** "Xưa em từng làm dự án sinh viên, nôm na là tự build 1 con AI để có thể trả lời 1 số chủ đề cụ thể trong 1 file tài liệu lớn... cần 1 giải pháp tối ưu đó là RAG. Trước tiên cắt tài liệu thành các Chunks, dùng 1 model BGE (BGE-m3) để embedding các Chunks tài liệu, rồi đẩy vào Mongo Vector Search, sau đó embedding câu hỏi và truy vấn trong MongoDB Vector Search để lấy top K số Chunks liên quan, và rồi đẩy câu hỏi text kèm top K Chunks text vào LLM (Qwen2.5-3B) để trả lời."
> **Link:** [Xem bình luận](https://www.youtube.com/watch?v=kRXoK02KJow&lc=Ug...)
> **Tại sao đọc:** **Blueprint kỹ thuật chuẩn chỉnh cho RAG Pipeline.** Không phải lý thuyết, là *kinh nghiệm thực chiến* (student project nhưng stack production: BGE-m3, Mongo Vector Search, Qwen2.5). Dev Java muốn sang AI *phải* biết luồng này thành thạo.

### 3. `@duythanh1602` — **Insight Score: 3.5** (Video: *Vector Databases...*)
> **Nội dung:** "Đại ca ơi, giờ backend 5 năm kinh nghiệm có nên chuyển hướng sang AI engineering ko hay tập trung ôn tiếp BE vậy, vì em nộp thử CV thì thấy toàn AI nhiều"
> **Link:** [Xem bình luận](https://www.youtube.com/watch?v=kRXoK02KJow&lc=Ug...)
> **Tại sao đọc:** **Giọng nói của thị trường tuyển dụng thực tế.** Backend 5 năm (senior level) nộp CV *thử* và thấy "toàn AI nhiều". Tín hiệu rõ ràng: JD Backend thuần túy đang khan hiếm, yêu cầu "AI-aware" là mặc định.

### 4. `anilgulecha` (Hacker News) — **Insight Score: 4.5** (Bài: *Tech market feels like a data entry job*)
> **Nội dung:** "A friend of mine put this to me: Ai can do everything needed for a business currently, outside of anticipating future business needs constantly. Which means the job market will currently benefit those with this skill. Traditionally what EMs/PMs,leaders would do. I'm not sure where this will land, but the above rings true - Juniors are"
> **English reference:** > "AI can do everything needed for a business currently, outside of anticipating future business needs constantly. Which means the job market will currently benefit those with this skill. Traditionally what EMs/PMs, leaders would do."
> **Tại sao đọc:** **Định vị lại giá trị của Developer.** AI làm *execution* (cái "gì" và "như thế nào"), Human phải làm *strategy/foresight* (cái "tại sao" và "gì tiếp theo"). Đây là tư duy EM/PM/Architect — kỹ năng "đắt giá" nhất hiện nay.

### 5. `@NguyênNguyễnVăn-m6e3o` — **Insight Score: 4.5** (Video: *No Code...*)
> **Nội dung:** "E nói thật chứ có kinh nghiệm kĩ thuật, năng lực,... Ở đâu cũng sống đc, chứ tại sao cứ phải suy nghĩ phải lm cho tư bản mới đc, như e làm tự do tháng đều đều trung bình cũng hơn 25 củ vưà lm vừa chơi, chưa kể sống ở nhà nông thôn nên chi phí sống vẫn dư giả chán..."
> **Tại sao đọc:** **Lối thoát "Plan B" thực tế cho dev VN.** Freelance/Remote/Outsource cho khách nước ngoài (đặc biệt là US/EU) cho thu nhập cao, tự chủ thời gian, ít phụ thuộc tuyển dụng VN. Yêu cầu: English tốt + Portfolio mạnh + Soft skill bán hàng/dự án.

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY (ƯU TIÊN EXPERT VOICE & RELEVANCE)

| # | Nguồn | Loại | Vùng | Luận điểm chính / Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **[Vector Databases - Tips Javascript](https://www.youtube.com/watch?v=kRXoK02KJow)** | Video | **[VN]** | **Tech Lead/Architect दृष्टिकोण (expert_voice_score: 1.5).** Giải thích rõ *tại sao* Vector DB là cầu nối từ Backend -> AI Engineer. Demo code RAG pipeline thực tế. | **Định hướng kỹ thuật cốt lõi.** Bắt buộc xem để hiểu stack AI App hiện nay. Bình luận chất lượng cao. |
| **2** | **[No Code - Tips Javascript](https://www.youtube.com/watch?v=gxIKlsOzq70)** | Video | **[VN]** | **Senior Dev दृष्टिकोণ (expert_voice_score: 1.5).** Phân tích "Vibe Coding" thực tế: AI làm 95% code, dev làm 5% quyết định kiến trúc/business. Cảnh báo Junior chỉ biết code tay sẽ chết. | **Định hướng tư duy & sống còn.** Bình luận `@phutran-z6h` (insight 12) là "kinh thánh" survival. |
| **3** | **[The Pulse: Anthropic kills the coding interview](https://newsletter.pragmaticengineer.com/p/the-pulse-anthropic-kills-the-coding)** | Article | **[Quốc tế]** | **Engineering Manager/Recruiter दृष्टिकोण (Pragmatic Engineer - Gergely Orosz).** Anthropic bỏ LeetCode, thay bằng "coding with AI tools", "system design", "debugging". Microsoft voluntary exit details. | **Dự báo xu hướng phỏng vấn VN 6-12 tháng tới.** Chuẩn bị portfolio/AI workflow thay vì grinding algo. |
| **4** | **[Tech market feels like a data entry job (Hacker News)](https://news.ycombinator.com/item?id=50254751)** | Forum | **[Quốc tế]** | **Senior Dev (5+ yrs, ex-SV) thực tế.** Kêu cứu quy trình tuyển dụng vỡ: nộp form tay hàng giờ, ATS/AI filter vô lý, fake jobs, malware take-home. | **Kiểm thực thị trường.** Đừng tin báo chí "nhu cầu tăng". Hiểu rõ "khoảng cách" giữa CV và Offer. |
| **5** | **[Năm 2026 ảm đạm ra sao? - Tôi Đi Code Dạo](https://www.youtube.com/watch?v=mOaakWt7txY)** | Video | **[VN]** | **Industry Observer/Veteran दृष्टिकोण.** Tổng hợp: Layoff BigTech -> Fresher VN bão hòa, AI Agent bùng nổ, StackOverflow chết, Junior bị ép KPI. Khuyên: "Đừng ghét AI, hãy dùng nó". | **Tổng quan makro VN.** Góc nhìn "người trong nghề" quan sát thị trường VN cụ thể (lương, fresher, outsourcing). |
| **6** | **[Build PC chạy AI Local - Tôi Đi Code Dạo](https://www.youtube.com/watch?v=nFj7IlNYZMg)** | Video | **[VN]** | **Practitioner दृष्टिकोण.** Demo chạy Agent, ComfyUI, Hybrid Cloud/Local trên RTX 5080. Chứng minh local AI đã sẵn sàng cho production/enterprise. | **Kỹ năng Niche đắt giá (Local LLM/Infra).** Phù hợp background Network Security/Java backend (cần hiểu HW/OS/Deploy). |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào có `is_major_incident = true` hoặc CVE/CVSS/KEV cụ thể trong batch này. Bỏ qua mục 6.*