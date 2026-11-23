📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.pt789rtesni1)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Thị trường tuyển dụng "bóng ma" (Silent Attrition) và "qua cầu rút ván"**: Kênh *Tôi Đi Code Dạo* (Item 4) và bình luận cộng đồng xác nhận năm 2026 kinh tế "dễ thở" hơn nhưng ngành IT **không hồi phục tuyết rơi**. Công ty ít tuyển mới (backfill), ép KPI năng suất nhờ AI, Junior/Fresher bị "dao cạo" nặng nề nhất. Bình luận `@hirunguyen4522` (180 votes) thẳng thắn: *"Dev tầm 2022 trở về trước thì đúng là sướng thật. Bây giờ thì chỉ còn anh em dev cũ có vốn lớn vài tỷ thì sẽ có khả năng nhìn nhận AI lợi hơn hại. Còn không vốn phải đi làm thuê thì đói kém lắm."*
- **Yêu cầu "Senior hóa" ngay từ vị trí Dev cơ bản**: Video *Tips Javascript* (Item 2) và bình luận top `@phutran-z6h` (insight 12.0) chỉ ra sự chuyển dịch quyết liệt: **AI làm 95-98% việc code/task-level**. Lập trình viên Việt Nam **bắt buộc** phải hiểu **nghiệp vụ (business), kiến trúc toàn hệ thống (system), và kỹ năng làm việc với con người**. Kỹ năng "chia task, chia role" kiểu nhàm chán đã hết giá trị.
- **Chuyển dịch stack thực chiến cho Fresher/Junior**: Series *Hỏi Dân IT* (Items 13, 15, 16, 17) cho thấy doanh nghiệp VN hiện nay yêu cầu **React 18 + TypeScript + Ant Design Pro + JWT/VNPAY/Google Login** làm chuẩn mực cho người mới. Không còn chỗ cho JS thuần hay CSS thủ công.

### Trên thế giới (và ý nghĩa với Việt Nam)
- **AI Agent tự chủ tìm và khai thác Zero-day trong 11 phút** (Item 1 - Amazon Report, `is_major_incident=true`, CVSS 9.8): **Đây là điểm uốn lxsl**. AI không chỉ viết code, nó **tự động hóa quy trình tấn công toàn chuỗi (recon -> exploit -> persistence)**. *Ý nghĩa VN:* An ninh ứng dụng (AppSec) và bảo mật hạ tầng (NetSec) bỗng trở thành **kỹ năng "sống còn" đắt giá nhất**, vượt xa khả năng code feature. Công ty outsourcing/sản phẩm tại VN sẽ bị ép buộc phải có quy trình hardening/detection tự động.
- **"Silent Attrition" - Tuyển dụng đóng băng thay vì sa thải công khai** (Item 5 - Jim Stroud, Item 9 - Mostly Untangled): Các công ty lớn (Google, Microsoft, Block...) **ngưng tuyển backfill**, để AI Agent hấp thụ workload. *Ý nghĩa VN:* Mô hình "thuê người làm task" của nhiều công ty VN phục vụ khách hàng nước ngoài sẽ co lại. Dev VN phải chuyển sang vai trò **kiểm soát/chỉ huy AI Agent (AI Orchestration) hoặc giải quyết vấn đề AI không làm được (Architecture, Security, Business Logic phức tạp)**.
- **Thực trạng khủng hoảng Senior/Experienced** (Item 6 - Ask HN, 15y exp, 2y unemployed): Dù là Senior 15 năm, gap CV 2 năm là "chết chắc" do ATS/AI filter. *Ý nghĩa VN:* **Không được ngừng code/xây dự án thực tế** (dù thất nghiệp hay đang học). Portfolio GitHub hoạt động, contribution open-source, side-project có user thật là "giấy thông hành" duy nhất khi ATS chặn CV.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cốt lõi (Must-have) — có bằng chứng từ dữ liệu
| Kỹ năng | Tại sao quan trọng (Nguồn) | Mức độ ưu tiên |
| :--- | :--- | :--- |
| **Hiểu Business & Kiến trúc hệ thống (System Design)** | `@phutran-z6h` (Item 2, Insight 12): "AE nên tập trung vào việc hiểu business + hệ thống... AI tự thiết kế, tự chạy test... 95-98%". Item 12 (Dev.to): "Changing what 'senior' means". | **CAO NHẤT** |
| **An ninh mạng / AppSec / NetSec (Thực chiến)** | Item 1: AI Agent tìm Zero-day (Path Traversal -> RCE) trong **11 phút** trên MONAI Label (CVE-2026-133968, CVSS 9.8). Kỹ năng: Secure coding, Input validation, Hardening, Detection Engineering, Incident Response. | **CAO NHẤT** |
| **AI Engineering / RAG / Vector DB / Agent Orchestration** | Item 3 (Tips JS): Video định hướng "Backend -> AI Engineer". Bình luận `@vantran_devopsinfra` (Insight 2.0) demo chi tiết RAG pipeline (Chunking -> BGE-m3 Embedding -> Mongo Vector Search -> Qwen2.5). `@giappham3462` nhắc AI Local cho bảo mật code. | **CAO** |
| **Python (Automation, Security Tooling, AI/ML Glue)** | Item 1: Attacker dùng Python reverse shell. Item 3: RAG pipeline dùng Python. Item 6 (HN): OP học Python/AI nhưng vẫn thất nghiệp vì gap CV -> **Phải dùng Python để build tool/security automation thực tế**. | **CAO** |
| **TypeScript + React Ecosystem (Ant Design Pro, React Query, Vite)** | Series *Hỏi Dân IT* (Items 13, 15, 16, 17): Chuẩn mực tuyển dụng Fresher/Junior tại VN hiện nay. 100% TS, Ant Design Pro cho Admin, VNPAY/JWT/Google Auth. | **TRUNG BÌNH** (Để có việc làm ngay) |

### Công nghệ: Xu hướng thật vs Hype
- **Thật (Real Trend):**
    - **Vector Database (Mongo Vector Search, pgvector, Qdrant, Milvus)**: Cốt lõi của RAG, Agent Memory (Item 3, 11).
    - **Local LLM / On-premise AI (Ollama, LM Studio, vLLM)**: `@giappham3462` (Item 3) và xu hướng bảo mật dữ liệu (Item 1) đẩy mạnh nhu cầu deploy AI nội bộ.
    - **Infrastructure as Code / GitOps / Platform Engineering**: Để vận hành hệ thống an toàn khi AI tự sinh code/tấn công.
- **Hype (Cảnh giác):**
    - **"No-code/Vibe Coding" cho người không biết code** (Item 8): Chỉ phù hợp PM/Designer/Founder MVP. Dev chuyên nghiệp dùng **Agentic Workflow (Claude Code, Cursor, Aider)** — có quy trình, review, test, context management — chứ không "vibe" ngẫu hứng.
    - **Prompt Engineering đơn lẻ**: Đã bị nhúng vào model reasoning (o1, Sonnet 3.5+). Kỹ năng thay thế: **Context Engineering** (cung cấp đúng context/codebase/docs cho Agent).

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy cốt lõi (Từ cộng đồng)
1.  **Từ "Task Executor" -> "System Owner / Business Partner"**: `@phutran-z6h` (Item 2) nhấn mạnh: *"Kĩ năng [hiểu nghiệp vụ] hình thành từ nhiều năm đi làm... AE nên tập trung vào việc hiểu business + hệ thống + kĩ năng làm việc với mọi người xung quanh."*
2.  **Từ "Viết code sạch" -> "Thiết kế an toàn & Kiểm soát AI"**: Item 1 chứng minh AI viết exploit tốt hơn dev viết fix. Tư duy mới: **Assume breach**. Code phải có validation chặt, logging đầy đủ, least privilege. Review code của AI như review code của Junior hay External Contributor.
3.  **Từ "Học framework mới" -> "Học nguyên lý không đổi"**: Network Security (TCP/IP, TLS, AuthN/AuthZ), Distributed Systems, Data Modeling, Cryptography. AI thay đổi tool hàng tháng, nguyên lý thì không.

### Kế hoạch hành động TUẦN NÀY (Cho Dev Java/Spring Boot đang học Python + NetSec)
> **Mục tiêu:** Biến thế mạnh Java (Enterprise, Type Safety, Spring Security) thành lợi thế cho Security & AI Engineering.

| Ngày | Hành động cụ thể (Actionable) | Lý do / Nguồn gợi ý |
| :--- | :--- | :--- |
| **Thứ 2-3** | **Lab: Tái hiện CVE-2026-133968 (Path Traversal -> RCE) trên local.** Dùng Python script để fuzz/scan lỗi upload file. Viết patch fix trong Spring Boot (`MultipartFile` validation, `Path.normalize()`, `SecurityContextHolder`). | Item 1: Hiểu luồng tấn công của AI Agent (11 phút). Học **Secure Coding** thực tế ngay trên stack Java mạnh của bạn. |
| **Thứ 4** | **Build Mini RAG Local cho Codebase Java của chính bạn.** Stack: Python (LangChain/LlamaIndex) + `sentence-transformers` (BGE-m3) + `ChromaDB`/`pgvector` + Ollama (CodeLlama/Qwen2.5-Coder). Index toàn bộ source Spring Boot -> Hỏi Agent: "Service nào xử lý thanh toán VNPAY?", "Config security ở đâu?". | Item 3 (Video Vector DB, `@vantran_devopsinfra`): Kỹ năng **AI Engineering/RAG** áp dụng ngay cho daily job. Hiểu codebase sâu hơn AI. |
| **Thứ 5** | **Viết 1 Script Python tự động hóa Security Checklist:** Quét `pom.xml`/`build.gradle` tìm dependency cũ (OWASP Dependency Check CLI), check `application.yml` hardcoded secret, check Spring Security config missing `frameOptions/CSRF`. Chạy qua GitHub Actions. | Item 1 & 5: **Automation/Platform Engineering**. Biến NetSec thành tooling dev dùng hàng ngày. Portfolio GitHub Action "xanh" là bằng chứng kỹ năng. |
| **Thứ 6** | **Viết 1 Blog Post / LinkedIn Technical Note (Tiếng Việt):** *"Từ CVE-2026-133968: Tại sao Spring Boot Dev phải biết Path Traversal & Cách fix an toàn"* hoặc *"Xây RAG Local để 'chat' với Legacy Java Monolith"*. Tag #Java #Security #AIEngineering #VietnamDev. | Item 6 (HN): **Personal Branding** phá vỡ "Gap CV". Viết bằng tiếng Việt để hiểu được business VN (yêu cầu Item 2). |
| **Cuối tuần** | **Học React/TS cơ bản qua Series Hỏi Dân IT (Video #15, #16).** Chỉ làm đủ: Component, Hook, TypeScript Interface, Call API Spring Boot (JWT). Không cần sâu CSS. | Items 13, 15, 16, 17: **Fullstack Versatility** — yêu cầu bắt buộc của 90% JD Fresher/Junior VN hiện nay. |

### TRÁNH TUẦN NÀY
- ❌ Học lý thuyết Network Security suông (OSI model, port scanning theory) mà **không lab exploit/fix thực tế**.
- ❌ Ngồi "vibe coding" hỏi ChatGPT/Claude web UI mà **không setup Agent trong IDE (Cursor/Claude Code/Aider) với context project**.
- ❌ Nộp CV hàng loạt (spray & pray) mà **không có side-project/security tool/RAG demo trên GitHub public**.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

### 1. `@phutran-z6h` — **Insight Score: 12.0** (Cao nhất toàn bộ dataset)
> **Nguồn:** Video *"No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?"* (Item 2, Tips Javascript) — [Link](https://www.youtube.com/watch?v=gxIKlsOzq70)
> **Votes:** 14
> **Nội dung đầy đủ:**
> "Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó, kĩ năng đó hình thành từ nhiều năm đi làm chứ ko phải một sớm 1 chiều, mà ngay cả khi ae muốn tìm hiểu thì cũng chưa chắc có cơ hội. Chuyện AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi, tuy ko đc 100% nhưng nó cũng làm dc 95-98% tùy vào cách ae setup + research. Chuyện lập trình viên ko cần code là chuyện trước mặt rồi, ko phải tương lai nữa, thế nên ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh. Với tình trạng mất não ko thể đọc tài liệu quá 100 dòng hiện nay thì thị"
> **Tại sao đọc:** Đây là **cảnh báo cụ thể nhất** về "chết hạn" của kỹ năng code thuần túy tại VN. Con số "95-98%" từ người trong nghề setup AI Agent là mốc tham chiếu thực tế. Nhấn mạnh **Business + System + Soft Skills** là "bộ 3 sống còn".

### 2. `@vantran_devopsinfra` — **Insight Score: 2.0** (Chi tiết kỹ thuật cao nhất về RAG)
> **Nguồn:** Video *"Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI"* (Item 3, Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)
> **Votes:** 8
> **Nội dung đầy đủ:**
> "Xưa em từng làm dự án sinh viên, nôm na là tự build 1 con AI để có thể trả lời 1 số chủ đề cụ thể trong 1 file tài liệu lớn, lúc đó em có suy nghĩ không thể đưa cho AI 1 file lớn như vậy và rồi chỉ để hỏi 1 số chủ đề trong đó, vì vậy cần 1 giải pháp tối ưu đó là RAG. Trước tiên cắt tài liệu thành các Chunks, dùng 1 model BGE (BGE-m3) để embedding các Chunks tài liệu, rồi đẩy vào Mongo Vector Search, sau đó embedding câu hỏi và truy vấn trong MongoDB Vector Search để lấy top K số Chunks liên quan, và rồi đẩy câu hỏi text kèm top K Chunks text vào LLM (Qwen2.5-3B) để trả lời. Cảm ơn video của anh làm em nhớ lại kỉ niệm sinh viên. Điểm thú vị đó là tìm ra điểm chưa tối ưu và tìm cách để tối ưu"
> **Tại sao đọc:** Đây là **case study thực tế** (không phải theory) triển khai RAG production-like: **Chunking -> BGE-m3 Embedding -> Mongo Vector Search -> Qwen2.5**. Rất phù hợp cho Dev Java muốn chuyển sang AI Engineer: stack mở, có thể chạy local, áp dụng ngay cho internal docs/codebase.

### 3. `@hirunguyen4522` — **Votes: 180** (Tâm lý thị trường VN thực tế nhất)
> **Nguồn:** Video *"Ngành lập trình và IT năm 2026 ảm đạm ra sao??"* (Item 4, Tôi Đi Code Dạo) — [Link](https://www.youtube.com/watch?v=mOaakWt7txY)
> **Insight Score:** 2.0
> **Nội dung đầy đủ:**
> "Dev tầm 2022 trở về trước thì đúng là sướng thật. bây giờ thì chỉ còn anh em dev cũ có vốn lớn vài tỷ thì sẽ có khả năng nhìn nhận AI lợi hơn hại. Còn không vốn phải đi làm thuê thì đói kém lắm. tầm này nhà nước đẩy mạnh bơm tiền cho xây dựng, nhiều khi làm về tay chân lương cao hơn dev mới đó."
> **Tại sao đọc:** Góc nhìn "khó nghe nhưng thật" về **thu nhập thực tế & cơ hội thoát nghề** tại VN. Cảnh báo về "illusion" lương cao IT so với thực tế thị trường 2026. Giúp bạn định vị kỳ vọng lương & kế hoạch tài chính thực tế.

### 4. `@noprocrastedaga` & `@ramesh31` (Hacker News) — **Insight Score: 2.0** (Thực trạng Global Senior)
> **Nguồn:** *"Ask HN: I have been unemployed for 2y. 15 years of experience, US."* (Item 6) — [Link](https://news.ycombinator.com/item?id=50583761)
> **Nội dung đại diện:**
> - `@noprocrastedaga`: *"What should you do? Lie. I’ve been on both sides... opening a position got me a thousand of applications per day, all ChatGPT’d resumes from monkeys who likely couldn’t engineer their way out of a wet paper bag."*
> - `@ramesh31`: *"I think increasingly the answer is to accept that the game is up. We are Detroit auto workers in 1985. The old world is gone and it’s not coming back. You will probably never again make what you used to."*
> **Tại sao đọc:** **Cảnh báo cực đoan nhưng cần thiết** về ATS/AI Filter chặn CV Senior, và sự sụp đổ mô hình "kinh nghiệm = an toàn". Khuyên Dev VN: **Portfolio > CV**, **Side-project > Certificate**, **Adaptability > Loyalty**.

### 5. `@duythanh1602` — **Insight Score: 3.5** (Câu hỏi điển hình Backend 5 năm VN)
> **Nguồn:** Video *"Vector Databases..."* (Item 3, Tips Javascript) — [Link](https://www.youtube.com/watch?v=kRXoK02KJow)
> **Votes:** 1
> **Nội dung:** *"Đại ca ơi, giờ backend 5 năm kinh nghiệm có nên chuyển hướng sang AI engineering ko hay tập trung ôn tiếp BE vậy, vì em nộp thử CV thì thấy toàn AI nhiều"*
> **Tại sao đọc:** Biểu tượng cho **nỗi lo của hàng nghìn Backend Dev VN trung cấp**. Câu trả lời ngầm từ dữ liệu: **Không phải chọn MỘT trong hai**. Hãy làm **Backend AI-Ready** (Spring Boot expose API cho Agent, RAG internal knowledge, Secure by default). Đó là niche ít cạnh tranh nhất.

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| # | Nguồn | Loại / Khu vực | Luận điểm chính / Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[VIDEO] AI Agents Found a Zero-Day in 11 Minutes — Amazon Report** (Item 1) | [Quốc tế] **Sự cố lớn (Major Incident)** | AI Agent tự chủ (Cairn framework) tìm & exploit Zero-day (Path Traversal -> RCE) trên MONAI Label trong 11 phút. CVE-2026-133968, CVSS 9.8. | **Bắt buộc xem.** Điểm uốn lxsl: AI tấn công tự động hóa cấp độ Nation-state. Dev NetSec/Java phải hiểu luồng tấn công này để defend. |
| **2** | **[VIDEO] No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?** (Item 2) | [VN] **Expert Voice (Tech Lead/Anonystick)** | AI làm 95-98% coding/task. Kỹ năng sống còn: Hiểu Business, Hệ thống, Soft skills. Bình luận `@phutran-z6h` (Insight 12) là "kinh thánh" định hướng. | Nói đúng "tiếng VN", đúng bối cảnh VN, có expert_voice_score cao (1.5), comment community chất lượng nhất dataset. |
| **3** | **[VIDEO] Vector Databases - Nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI** (Item 3) | [VN] **Expert Voice (Tech Lead/Anonystick)** | Hướng dẫn kỹ thuật sâu: Vector DB, Embedding (BGE-m3), RAG, Chunking. Chuyển dịch Backend -> AI Engineer. Comment `@vantran_devopsinfra` demo pipeline thực tế. | Cụ thể hóa **"Học gì"** cho Dev Java muốn sang AI Engineering. Stack mở (Mongo, BGE, Qwen) dễ áp dụng tại VN. |
| **4** | **[FORUM] Ask HN: Unemployed 2y, 15yoe, US** (Item 6) | [Quốc tế] **Community Lane (Senior/Expert)** | Thực trạng khủng hoảng Senior: ATS filter, Gap CV, Ageism, 1000 CV/position (AI-generated). Lời khuyên gay gắt: Lie, Pivot, Accept lower pay, Build real things. | **Đèn đỏ cảnh báo** cho Dev VN 5-10 năm kinh nghiệm. Hiểu rõ "kẻ thù" là ATS/AI Filter, không phải thiếu kỹ năng. |
| **5** | **[SERIES] React.js Thực Chiến - Luyện Tập Bài Test Fresher React** (Items 13, 15, 16, 17 - Hỏi Dân IT) | [VN] **Training / Practical** | Chuẩn mực stack tuyển dụng VN 2026: React 18 + TS + Ant Design Pro + JWT/VNPAY/Google Auth + Vite. 100% TypeScript. | **Curriculum thực chiến** cho người đang học thêm Frontend để Fullstack. Không lý thuyết, chỉ code JD yêu cầu. |

> **English reference (Item 1 - Amazon Report):** *"The agents ran on an open-source framework called Cairn. Over about 48 hours... the agents mapped the application's interface and, in about 11 minutes, went from mapping the API to arbitrarily writing files on the server through a path traversal flaw... In a later session they planted a Python reverse shell in a file Python runs at startup, triggered a training feature, and came back with a root shell."*
> **English reference (Item 5 - Jim Stroud):** *"Most discussions around AI and the future of work focus on mass layoffs. But the real shift might be much quieter: 'silent attrition.' Instead of pink slips, companies simply stop backfilling open roles, letting automated tools and AI agents quietly absorb the workload."*
> **English reference (Item 12 - Dev.to):** *"'Will AI replace developers?' is the wrong question. The better one is: which of your skills just got commoditized, and which just became leverage?"*

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP

### Sự cố: **AI Agent tự chủ khai thác Zero-day (CVE-2026-133968) trên MONAI Label Medical Server**
- **Chi tiết:** Nhóm đe dọa liên quan Trung Quốc sử dụng AI Agent tự chủ (framework **Cairn**) tấn công các trường đại học Đông Á. Từ việc mapping API, trong **~11 phút** Agent phát hiện và khai thác **Path Traversal trong tính năng upload file** (Path Traversal -> Arbitrary File Write -> RCE). Sau đó Agent plant **Python reverse shell** vào file khởi động Python, trigger tính năng training, đạt **Root Shell**.
- **Chỉ số:** **CVE-2026-133968**, **CVSS 9.8 (Critical)**, Authentication **OFF by default**. Phiên bản ảnh hưởng: MONAI Label 0.8.5 trở xuống. Fix đã merge 19/10/2026.
- **Nguồn:** Item 1 (YouTube: AI Automation and Agentic Blueprint / Amazon Threat Intelligence Report). `is_major_incident: true`, `incident_severity: 9.0`.

### BÀI HỌC NGHỀ NGHIỆP & HÀNH ĐỘNG TUẦN NÀY (Cho Dev Java/Spring Boot + Python/NetSec)

| Lĩnh vực | Kỹ năng bỗng trở nên "đắt giá" (High Leverage) | Hành động cụ thể tuần này |
| :--- | :--- | :--- |
| **Secure Coding / AppSec** | **Input Validation & Path Sanitization** tại tầng Controller/Service. Không tin tưởng client-side check. Hiểu `Path.normalize()`, `Path.resolve()`, `Files.isSameFile()` trong Java NIO. | **Lab Thứ 2-3:** Viết unit test cho `MultipartFile` upload trong Spring Boot: test path traversal (`../../etc/passwd`), null byte injection, filename length. Implement `StorageService` an toàn (whitelist extension, random filename, lưu ngoài webroot). |
| **Detection Engineering / Blue Team** | **Log Source Coverage & Alert Rule**. AI Agent tạo noise pattern: mapping API nhanh -> lỗi 400/500 spike -> file write anomaly -> process execution (python reverse shell). | **Lab Thứ 4:** Viết script Python (Elastic/OpenSearch DSL hoặc Sigma Rule) detect: 1) Burst request tới endpoint upload. 2) Process creation `python`/`bash` từ user `tomcat`/`springboot`. 3) File modification trong `/tmp`, `/var/www`, `user.home`. |
| **Infrastructure Hardening** | **Least Privilege & Immutable Infrastructure**. Container chạy app **không được chạy as root**, **read-only root filesystem**, **drop ALL capabilities**, **no shell**. | **Lab Thứ 5:** Harden `Dockerfile` Spring Boot: `USER 1000:1000`, `RUN chown -R 1000:1000 /app`, `securityContext: {readOnlyRootFilesystem: true, runAsNonRoot: true, capabilities: {drop: ["ALL"]}}`. Test deploy K8s local (Kind/K3d). |
| **AI/Agent Security (Emerging)** | **Agent Observability & Guardrails**. Nếu công ty dùng AI Agent nội bộ (CodeGen, Ops), cần monitor: Tool calls, File system access, Network egress. | **Research Thứ 6:** Tìm hiểu **OpenTelemetry for LLM Agents** (Trace tool calls), **Guardrails AI / NeMo Guardrails**. Viết note: "Cách sandbox Agent chạy code Python/Java an toàn trong K8s Job". |
| **Career Positioning** | **Profile: "Security-Aware Backend Engineer / DevSecOps Practitioner"**. Không phải "Security Analyst" thuần túy. Bán được: "Tôi viết Spring Boot an toàn, tự động hóa security check trong CI/CD, hiểu AI Agent attack vector". | **Cuối tuần:** Cập nhật GitHub Profile README & LinkedIn Headline. Push 3 repo tuần này: `spring-secure-upload`, `rag-java-codebase`, `security-sigma-rules`. Viết 1 bài LinkedIn tiếng Việt tóm tắt bài học CVE-2026-133968 cho Dev Java. |

> **English reference (Item 1):** *"The flaw is now CVE-2026-133968, rated 9.8 out of 10 critical, affecting MONAI Label 0.8.5 and earlier, with authentication off by default. The maintainers merged a fix on October 19, 2026, but there is no evidence the fix has been widely deployed."* — **Bài học:** Patching speed < Exploit speed (11 phút). **Defense phải là Pre-deploy (Code/Infra), không phải Post-deploy (Patch).**