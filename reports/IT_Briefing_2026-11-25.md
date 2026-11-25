📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.lpz0exh7f4lx)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

---

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Thị trường "co lại im lặng" (Silent Attrition)**: Không phải là lày off hàng loạt, mà là **đóng băng tuyển dụng, không backfill vị trí rיק**, khiến Junior/Fresher gần như không có chỗ đứng. Video *Tôi Đi Code Dạo* (2026) và *Jim Stroud (Global)* cùng chỉ ra công ty "qua cầu rút ván": ép KPI cao hơn, AI làm 95-98% việc code tay, người ở lại phải gánh volume work lớn hơn.
- **Khoảng cách Senior - Junior bị xóa bằng AI**: Theo *VGU Tech Alumni* (Quân IT - 20 năm kinh nghiệm), 10-15 năm kinh nghiệm code truyền thống giờ chỉ còn giá trị **6 tháng - 1 năm** vì cả hai phải học lại từ đầu (AI Agent, MCP, Fine-tuning). Junior bỏ tư duy "nạn nhân" (victim mentality), chuyển sang **"học nền tảng + build sản phẩm chạy thật bằng AI → đào sâu nguyên lý sau"**.
- **Yêu cầu "Full-cycle + Business" bắt buộc**: Bình luận top @phutran-z6h (Video Tips JS "No Code") nêu rõ: *Chia task/role kiểu cũ đã chết. Dev phải hiểu nghiệp vụ cả hệ thống, biết setup AI chạy test perf/security/e2e/uiux.* Kỹ năng "code tay" không còn là core value.
- **Con đường "tự do/freelance" thực tế hơn lương thuê**: @NguyênNguyễnVăn (cùng video) sống nông thôn, tự do thu trung bình **>25 triệu/tháng**, nhấn mạnh: *Đừng gắn bó tư duy "phải làm cho tư bản", hãy xây dựng sản phẩm/kỹ năng bán được ra ngoài.*

> English reference: *"AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi... lập trình viên ko cần code là chuyện trước mặt rồi... ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh."* — @phutran-z6h (insight 12.0)

### Trên thế giới (và ý nghĩa với Việt Nam)
- **Ấn Độ: Layoff Senior nhưng tuyển Freshers hàng chục ngàn** (*Decode Bharat*): TCS cắt 23k người nhưng tuyển 44k+ freshers. Google: **75% code mới do AI viết**. Nghĩa cho VN: Công ty Outsourcing/Enterprise VN (FPT, CMC, v.v.) sẽ theo mô hình này — **giảm headcount Senior đắt, tăng Freshers rẻ + AI tooling**. Dev VN cấp 3-5 năm (Mid-level) là nhóm rủi ro nhất bị "kẹp".
- **Cloud/Infra/Support/Networking VẪN THIẾU NGƯỜI** (*Learning Partner, comment @mohdyasir1645 insight 2.0*): Dù AI hype thay thế, các role **Linux Admin, K8s, AWS/Azure Admin, L1/L2 Prod Support** vẫn boom. Ý nghĩa VN: **DevOps/Platform Engineer/Infra** là "bến đỗ an toàn" hơn thuần Dev feature.
- **Rust & System Programming: Niche cao, lương cực khủng** (*KaiPov, expert_voice 3.0*): Staff/Principal Rust Engineer **$200k+**. VN ít có vị trí nhưng remote cho US/EU hoàn toàn khả thi nếu thành thạo *memory safety, concurrency, FFI* — kỹ năng AI khó thay thế hoàn toàn.
- **Recruiter kém chất lượng làm chậm việc tìm người** (*Hacker News, comment Peroni insight 4.5*): Internal recruiter thường đánh giá sai skill, ưu tiên "bureaucratic tenure" hơn "exceptional talent". Dev VN cần **bypass HR: build public profile (GitHub, blog, product), liên hệ hiring manager trực tiếp**.

> English reference: *"Mostly Cloud Infrastructure and IT Support related roles... are getting boom even though these are the roles which are said to be replaced by AI."* — @mohdyasir1645 (insight 2.0)  
> English reference: *"Tech recruiters are the main obstacle to successful startups. Poorly trained, lazy, incompetent... they look for bureaucratic tenure that turns performance into slow boat to China."* — emilielder (HN) / *"Internal recruiters assessed on: time-to-fill, hiring manager satisfaction, diversity metrics, retention at 6/12 months."* — Peroni (insight 4.5)

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cốt lõi (Must-have) — có bằng chứng từ dữ liệu
| Kỹ năng | Tại sao quan trọng (Nguồn) | Mức độ ưu tiên |
|---------|----------------------------|----------------|
| **Thiết kế & vận hành AI Agent / Agentic Workflow (MCP, Tool Calling, RAG, Vector DB)** | Video *Ponytail* (Viblo), *Vector DB* (Tips JS), *Major Incident Amazon*: Agent tự tìm zero-day trong 11 phút. Dev phải biết **khiến Agent làm việc đúng, an toàn, không ẩu**. | 🔴 **Critical** |
| **Hiểu Business + System Design (End-to-end)** | @phutran-z6h (insight 12.0): *"AE tìm hiểu nghiệp vụ cả hệ thống... kĩ năng đó hình thành từ nhiều năm"*. Không còn chia task nhỏ. | 🔴 **Critical** |
| **Cloud Native / Infra / Linux / K8s / Observability** | @mohdyasir1645 (insight 2.0): Role Infra/Support **boom ngược dòng**. AI chưa thay thế được việc "giữ hệ thống sống". | 🟠 **High** |
| **Application Security (AppSec) & Secure Coding** | *Major Incident*: AI Agent khai thác path traversal (CVE-2026-133968, CVSS 9.8) tự động. Cần: **SAST/DAST, threat modeling, hardening, incident response**. | 🟠 **High** |
| **Python (AI/ML stack) + TypeScript/React (Fullstack thực tế)** | *Hỏi Dân IT* series Fresher React/TS + VNPAY/JWT/AntD: Yêu cầu tuyển dụng VN vẫn xoay quanh stack này. Python bắt buộc cho AI Engineering. | 🟠 **High** |
| **Rust / Go (System level, High performance)** | *KaiPov*: Rust career path $105k→$200k+. Go chuẩn cho Backend/Infra modern. AI sinh code Rust/Go vẫn kém an toàn → cơ hội cho con người. | 🟢 **Medium-High** (nếu định hướng remote/niche) |

### Công nghệ cần học — Tách "Xu hướng thật" vs "Hype"
| Công nghệ | Xu hướng thật (Real) | Chỉ là Hype / Không đủ |
|-----------|----------------------|------------------------|
| **Vector DB (PGVector, Milvus, Qdrant, MongoDB Vector)** | ✅ Bắt buộc cho RAG, Agent memory. Comment @vantran_devopsinfra đã triển khai thực tế sinh viên. | — |
| **MCP (Model Context Protocol) & Tool Calling** | ✅ Chuẩn hóa cách Agent dùng tool. *Ponytail*, *Dev.to "Tool Changed Overnight"* cảnh báo rủi ro schema thay đổi. | — |
| **Fine-tuning / LoRA / Small Language Models (SLM)** | ✅ *RevveAI (Hỷ - AI Engineer)* train F5-TTS 6000h tiếng Việt. Enterprise cần model riêng, on-premise, low-latency. | ❌ "Prompt Engineering" đơn thuần (khóa học 1-2 tuần) — không còn giá trị riêng. |
| **No-code / Low-code cho Dev** | ❌ Không thay thế Dev. *Video "No Code" Tips JS*: Dev vẫn cần hiểu code để review/debug AI. | ✅ Chỉ là tool hỗ trợ. |
| **Blockchain / Web3 / Crypto** | ❌ Không xuất hiện trong dữ liệu 2026 này. | ✅ Hype đã qua. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy được cộng đồng nhắc nhiều nhất
1.  **Từ "Làm task giao" → "Chủ sản phẩm/hệ thống"**: @phutran-z6h: *AI làm 95-98% code/test. Giá trị bạn = hiểu business, thiết kế hệ thống, setup pipeline AI, chịu trách nhiệm khi AI sai.*
2.  **Từ "Victim mentality (AI lấy việc)" → "Builder mentality (AI làm đòn bẩy)"**: *VGU Alumni / Quân IT*: *Khoảng cách Senior-Junior co lại 6-12 tháng. Junior có lợi thế: không gánh legacy mindset, học AI Agent từ con số 0 nhanh hơn.*
3.  **Từ "Ứng tuyển CV qua HR" → "Xây dựng bằng chứng công khai (Public Proof of Work)"**: *HN Peroni + @NguyênNguyễnVăn*: Recruiter lọc sai. Hãy làm **side project chạy thật, deploy production, viết blog post-mortem, đóng góp OSS**. Freelance/Remote pays better.
4.  **Security by default, không phải afterthought**: *Major Incident*: AI Agent tự hack zero-day. Dev phải code defensively: validate input, least privilege, immutable infra, monitoring anomaly.

### Kế hoạch hành động tuần này (Dành cho Dev Java/Spring Boot → học Python + Network Security)
| Ngày | Hành động cụ thể | Mục tiêu |
|------|------------------|----------|
| **Thứ 2-3** | **Setup Lab RAG cục bộ**: Spring Boot (API) + Python FastAPI (Embedding/LLM) + **PGVector (PostgreSQL extension)**. Index codebase Spring Boot cũ, cho Agent trả lời "Service nào xử lý X?", "Table nào lưu Y?". | Biết nối Java ↔ Python ↔ Vector DB — core skill AI Engineer. |
| **Thứ 4** | **Triển khai MCP Server đơn giản**: Expose function `search_code(query)` cho Agent. Test với Claude/Cursor: "Tìm bug tiềm ẩn trong module Payment". | Hiểu **MCP/Tool Calling** — chuẩn 산업 (Ponytail, Dev.to incident). |
| **Thứ 5** | **Thực hành khai thác CVE-2026-133968 (Path Traversal) trong Docker lab**: Viết script Python tự động scan/upload exploit → lấy shell. Sau đó **vá lỗi + viết test regression + config WAF rule**. | Network Security thực chiến: Recon → Exploit → Patch → Harden. |
| **Thứ 6** | **Viết 1 bài blog/LinkedIn (Tiếng Việt + Anh)**: *"Tự xây RAG cho codebase Java legacy + cho AI Agent tìm zero-day path traversal"*. Tag #SpringBoot #Python #AISecurity #MCP. | Bằng chứng công khai (Public Proof) — bypass recruiter, thu hút hiring manager. |
| **Cuối tuần** | **Ôn Linux/K8s basics**: `kubectl debug`, `nsenter`, `bpftrace`, `falco` detect shell spawn. Xem video *KaiPov Rust* để hiểu system programming mindset. | Mở đường DevOps/Platform/Infra — nhóm vẫn thiếu người (@mohdyasir1645). |

**Tránh tuyệt đối tuần này**: Chỉ đọc sách/khóa học lý thuyết mà không deploy gì; apply mass CV qua LinkedIn/TopCV không custom; học "Prompt Engineering" đơn lẻ.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT (Top 5 Insight Score)

| # | Tác giả / Nguồn | Insight | Votes | Nội dung trích dẫn (gốc) | Tại sao đáng đọc |
|---|-----------------|---------|-------|--------------------------|------------------|
| **1** | **@phutran-z6h**<br>Video: *No Code \| Không thể nào các lập trình viên kiểu này thực sự mất việc...*<br>[Link](https://www.youtube.com/watch?v=gxIKlsOzq70) | **12.0** | 14 | *"Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó... Chuyện AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi... Chuyện lập trình viên ko cần code là chuyện trước mặt rồi... ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh."* | **Nói trúng tim xu hướng:** Xác nhận AI đã thay thế 95-98% coding/testing. Chỉ ra skill gap thực: *Business/System thinking + AI Orchestration*. Là comment actionable nhất cho dev VN. |
| **2** | **@NguyênNguyễnVăn-m6e3o**<br>Cùng video trên | **4.5** | 4 | *"E nói thật chứ có kinh nghiệm kĩ thuật, năng lực,... Ở đâu cũng sống đc, chứ tại sao cứ phải suy nghĩ phải lm cho tư bản mới đc, như e làm tự do tháng đều đều trung bình cũng hơn 25 củ vưà lm vừa chơi... thấy nhiều người thất bại chỉ biết lắc đầu cười, ko phải cười họ thất bại, mà cười họ ko biết mình thất bại ở đâu..."* | **Mindset breaker:** Phá vỡ tư duy "phải có việc làm chính quy". Chứng minh Freelance/Remote VN hoàn toàn viable nếu có skill thật. Khuyến khích tự chủ thu nhập. |
| **3** | **Peroni**<br>Hacker News: *Ask HN: How are tech recruiters assessed...*<br>[Link](https://news.ycombinator.com/item?id=50609394) | **4.5** | 0 | *"Internal recruiters assessed on: time-to-fill, hiring manager satisfaction, diversity metrics, retention at 6/12 months, quality of hire (performance reviews)... Agency recruiters: revenue, commission, send-outs, interviews arranged."* | **Insider view:** Giải mã tại sao CV tốt vẫn bị lọc sai. Internal recruiter KPI ≠ "tìm người giỏi nhất" → Dev phải **bypass HR, trực tiếp Hiring Manager**. |
| **4** | **@duythanh1602**<br>Video: *Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI*<br>[Link](https://www.youtube.com/watch?v=kRXoK02KJow) | **3.5** | 1 | *"Đại ca ơi, giờ backend 5 năm kinh nghiệm có nên chuyển hướng sang AI engineering ko hay tập trung ôn tiếp BE vậy, vì em nộp thử CV thì thấy toàn AI nhiều"* | **Câu hỏi đau đáu của Mid-level:** Phản ánh áp lực chuyển型 thực tế. Cần phân tích: *Backend core vẫn cần, nhưng phải "AI-augmented Backend"*. |
| **5** | **@mohdyasir1645**<br>Video: *IT Job Market 2026: You Have NO IDEA How Bad...*<br>[Link](https://www.youtube.com/watch?v=o3eB6rzv08o) | **2.0** | 1 | *"Also I noticed one thing, mostly Cloud Infrastructure and IT Support related roles like Networking Operations, Linux Admin, Windows Admin, Azure/AWS Admin, L1/L2 Application Production Support jobs are getting boom even though these are the roles which are said to be replaced by AI are still in demand."* | **Data point ngược dòng:** Infra/Cloud/Support **không bị AI thay thế** mà còn thiếu người. Lựa chọn an toàn, lương ổn định cho dev muốn tránh "code feature" competition. |

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY (Ưu tiên Relevance + Expert Voice + Insight Comments)

| # | Nguồn | Nhãn | Luận điểm chính / Góc nhìn nổi bật | Lý do chọn |
|---|-------|------|-----------------------------------|------------|
| **1** | **AI Agents Found a Zero-Day in Medical Software in 11 Minutes — Amazon Report** (YouTube) | **[Quốc tế] 🚨 Major Incident** | AI Agent tự chủ (framework Cairn) tìm & khai thác zero-day (CVE-2026-133968, CVSS 9.8) trong 11 phút, lấy root shell. Maintainer fix sau 1 tháng. | **Sự cố định hướng nghề nghiệp lớn nhất**: Security + AI Agent = skill gap khổng lồ. Dev phải hiểu *Agentic Security* ngay. |
| **2** | **No Code \| Không thể nào các lập trình viên kiểu này thực sự mất việc...** (Tips Javascript) | **[VN] 💎 High Insight Comments** | AI đã làm 95-98% code/test. Dev thất nghiệp do *không hiểu business/hệ thống*, không setup được AI pipeline. Comment @phutran-z6h (insight 12.0) là "bí kíp" survival. | **Thực tế VN ra xương sống**: Nói rõ skill nào còn giá trị, skill nào chết. Comment chất lượng cao nhất dataset. |
| **3** | **Ngành lập trình và IT năm 2026 ảm đạm ra sao??** (Tôi Đi Code Dạo) | **[VN] Market Reality** | Thị trường "silent attrition", Junior bị đào thải, AI Agent bùng nổ. Lời khuyên: "Đừng ghét AI, hãy dùng nó để làm nhàn hơn, lương cao hơn". Comment @hirunguyen4522 (180 votes): Dev pre-2022 đã làm nền, nay mới khó. | **Góc nhìn người trong nghề VN uy tín**: Tổng hợp được cả macro (kinh tế) lẫn micro (kỹ năng hàng ngày). |
| **4** | **Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI (AI Engineer)** (Tips Javascript) | **[VN] Tech Deep-dive** | Hướng dẫn 구체 từ Dev → AI Engineer: Embedding, Chunking, Vector Search, RAG. Comment @vantran_devopsinfra chia sẻ architecture RAG production (Mongo Vector Search + BGE-m3 + Qwen). | **Learning path cụ thể**: Không hype, có code/architecture thực tế từ người VN đã làm. |
| **5** | **AI vs Developer Jobs in India: Layoffs, Hiring & the 3 Skills That Matter in 2026** (Decode Bharat) | **[Quốc tế] Data-driven** | Google 75% code by AI. TCS layoff 23k nhưng hire 44k freshers. 3 skills: **System Design, AI Tooling Mastery, Domain Expertise**. | **Dữ liệu quy mô lớn (Ấn Độ ≈ mô hình Outsourcing VN)**: Dự báo xu hướng tuyển dụng VN 6-12 tháng tới. |
| **6** | **Your Life At Every Level of Rust** (KaiPov) | **[Quốc tế] Expert Voice (3.0)** | Career path Rust: Junior $105k → Staff $200k+. Yêu cầu: Systems programming, Memory safety, Concurrency, Open Source contribution. | **Niche high-value**: Cho dev muốn remote US/EU, thoát red ocean Web CRUD. Rust skill khó bị AI thay thế. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP

> **Điều kiện kích hoạt**: Dữ liệu có mục `is_major_incident = true` (Item 0: Amazon Report, CVE-2026-133968, CVSS 9.8, exploited by AI Agent).

### Sự cố: AI Agent tự chủ tìm & khai thác Zero-Day (CVE-2026-133968) trong 11 phút
- **Chuyện gì xảy ra**: Nhóm đe dọa liên quan Trung Quốc dùng **AI Agent tự chủ (framework Cairn)** quét MONAI Label (medical imaging server). Agent **tự mapping API → tìm path traversal ở file upload → ghi file tùy ý → plant Python reverse shell tại startup hook → trigger training feature → lấy root shell**. Toàn bộ quá trình **11 phút** sau khi mapping xong. CVE-2026-133968 (CVSS 9.8 Critical), auth off by default. Fix merged 19/10/2026.
- **Quy mô ảnh hưởng**: Các trường đại học Đông Á (trừ Trung Quốc đại lục). Server y tế, dữ liệu nhạy cảm. Amazon Threat Intelligence phát hiện và báo cáo.

### BÀI HỌC NGHỀ NGHIỆP (Career-Driven Lessons)

| Lĩnh vực | Thay đổi nhu cầu nhân lực / Kỹ năng đắt giá | Hành động cụ thể tuần này (Dev Java/Spring Boot + Python/NetSec) |
|----------|---------------------------------------------|------------------------------------------------------------------|
| **Application Security (AppSec)** | **Kỹ năng "Secure Code Review cho code do AI sinh" + "Threat Modeling cho Agentic System"** trở thành yêu cầu bắt buộc. AI Agent viết code nhanh nhưng **không hiểu context bảo mật** (path traversal, deserialization, SSRF). Cần người **verify, hardening, viết rule SAST/DAST custom**. | **Thứ 2-3**: Cài **Semgrep/CodeQL** scan project Spring Boot. Viết 1 rule custom detect `Path Traversal` (pattern `java.io.File` + user input). Chạy trên code AI sinh (dùng Cursor/Copilot generate controller upload file). |
| **Security Operations / Incident Response** | **Săn dấu hiệu xâm nhập do AI Agent gây ra** (MCP server bị compromise, tool schema bị thay đổi — *xem Dev.to "Tool Changed Overnight"*). Cần: **eBPF/Falco detection**, **Immutable Infrastructure**, **Zero Trust Network**. | **Thứ 5**: Lab **Falco rule detect reverse shell spawn** (execve `/bin/bash` từ user `www-data`/`tomcat`). Deploy MONAI Label vulnerable version trong K8s kind, cho AI Agent attack, quan sát Falco alert. Viết runbook containment. |
| **AI/ML Engineering (AI Safety & Security)** | **Red-teaming AI Agent** (Prompt injection, Tool poisoning, MCP hijacking) thành chuyên môn mới: **AI Security Engineer**. Enterprise cần người **audit Agent workflow trước khi production**. | **Thứ 4**: Research **OWASP Top 10 for LLM/Agent** (LLM01 Prompt Injection, LLM05 Improper Output Handling, LLM07 Tool Poisoning). Viết checklist audit cho MCP Server tự build (Thứ 4 kế hoạch trên). |
| **Platform / Infra Engineering** | **Hardening mặc định (Secure by Default)**: Tắt auth off-by-default, drop capabilities, read-only rootfs, seccomp profile. **Platform Engineer phải build "Paved Road" an toàn** cho Dev/AI Agent deploy. | **Thứ 6**: Harden Dockerfile Spring Boot: `USER 1000`, `readOnlyRootFilesystem: true`, `drop: [ALL]`, `capabilities: []`. Test app vẫn chạy. Commit lên GitHub với README giải thích từng hardening step. |

**Tóm gọn: Tuần này hãy biến mình thành "Dev có thể bảo vệ hệ thống trước AI Agent đi hack"**. Đó là vị trí đắt giá nhất thị trường 2026.