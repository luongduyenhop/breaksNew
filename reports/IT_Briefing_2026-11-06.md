📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.9c6zelkrh96l)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

---

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
*   **Phân hóa cực rõ giữa "Senior/Architect" và "Fresher/Junior":** Các tập đoàn lớn (Microsoft VN) đang cắt giảm nhân sự (layoff) nhưng đồng thời market vẫn có tin tuyển **Solutions Architect** với yêu cầu khắt khe: **10+ năm kinh nghiệm, tiếng Anh lưu loát, am hiểu GenAI/RAG/Agents, System Design, K8s, Cloud (AWS/GCP), Backend Node.js/TypeScript/NestJS** – làm việc hybrid với đối tác Hong Kong [Nguồn: System Design Vietnam Group]. Điều này cho thấy nhu cầu **dời sang vai trò thiết kế hệ thống, dẫn dắt dự án AI thực chiến, giao tiếp quốc tế** thay vì chỉ code feature.
*   **Nhu cầu tuyển dụng vẫn có nhưng "nâng khung":** Báo chí VN (VnEconomy) xác nhận nhu cầu tuyển lập trình viên vẫn tăng dù có AI, tuy nhiên các bài phân tích (VnExpress) cho thấy các "đại gia" sa thải để **tái cấu trúc chi phí sang AI/Automation**. Kết luận: VN không thiếu việc, nhưng thiếu người *đáp ứng được tiêu chuẩn mới* (AI-augmented + System Design + Soft skills).
*   **Bảo mật thành yêu cầu bắt buộc (bắt nguồn từ thực tế VN):** Sự kiện Binance bị hack do **giả mạo tuyển dụng, dụ dev chạy mã độc cục bộ** [J2TEAM Community] và حملات OTP spam quy mô lớn hướng đến người già [J2TEAM] cho thấy: **Kỹ năng Secure Coding, Threat Modeling, Auth/OAuth hardening, Supply Chain Security** không còn là chuyên môn riêng mà là *kỹ năng sống còn* cho mọi dev.

> English reference: "🔥 TÌM KIẾM **SOLUTIONS ARCHITECT** ... 📌 Tối thiểu** 10 năm kinh nghiệm ... 📌 Có k**inh nghiệm thực chiến với GenAI, RAG, Agents**." (System Design Vietnam FB Group)

### Trên thế giới (và ý nghĩa với dev Việt Nam)
1.  **AI không sa thải dev – AI "ngưng tuyển" Fresher/Junior:** Nghiên cứu Stanford & BLS (Video *Under The Numbers*) chỉ ra cơ chế: AI làm tăng năng suất dev senior → công ty **cắt giảm "bậc thang thấp nhất" (entry-level rungs)**. **Ý nghĩa VN:** Sinh viên/newbie VN **không thể chỉ biết code LeetCode/CRUD**. Cần chứng minh được tư duy **Product Engineer** (hiểu business, viết PRD, thiết kế hệ thống) ngay từ portfolio.
2.  **Chuyển dịch "Vibe Coding" → "Spec-Driven Development":** Bài viết *Why PRD.md is Your Best Guardrail* (Dev.to) chỉ ra lỗi hiểm của Vibe Coding: **AI thiếu scope (bối cảnh), over-engineering, hallucination architecture**. Giải pháp: **Viết PRD/Spec chi tiết trước, dùng làm "bộ lưới an toàn" cho AI**. **Ý nghĩa VN:** Kỹ năng **viết tài liệu kỹ thuật (PRD, ADR, System Design Doc), prompt engineering có cấu trúc** trở thành core skill – dev VN thường yếu ở chỗ này.
3.  **Tư duy Architect/Systems > Coding speed:** Cuộc thảo luận *Ask HN: How to Keep the Edge?* (Hacker News) tập trung cao độ vào việc **chuyển từ Engineer → Architect mindset**: "Systems = Technology + People + Business Needs". **Ý nghĩa VN:** Dev VN muốn lên lương cao (Senior/Lead/Architect) **bắt buộc** bổ sung tư duy hệ thống, giao tiếp stakeholder, hiểu business – không chỉ 깊 stack.
4.  **Tốc độ khai thác Zero-day siêu nhanh (4 ngày trước khi public):** Sự cố PHP RCE (CVSS 9.2) bị exploit từ Oct 17 mà disclose Oct 21 [CyberTales]. **Ý nghĩa VN:** Quy trình **patch management, observability, incident response, dependency scanning (SBOM)** phải tự động hóa, không thể chờ vendor advisory. Dev backend (Java/Spring, Node, Python) phải tự build "khả năng phản ứng 0-day".
5.  **Chênh lệch lương khổng lồ cho cùng title:** Senior Engineer tại Reddit vs Lyft chênh **$62K/năm** [HUNT MARKET]. **Ý nghĩa VN:** Lương không theo title mà theo **độ phức tạp hệ thống, quy mô traffic, tác động business, và khả năng đàm phân**. Dev VN cần chọn môi trường "làm hệ thống phức tạp" hoặc remote cho công ty US/EU để tối ưu thu nhập.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cần học (Soft/Process/Core) – *Có nguồn dẫn chứng*
| Kỹ năng | Tại sao quan trọng | Nguồn/Bình luận nhắc tới |
| :--- | :--- | :--- |
| **Viết PRD / Spec / System Design Doc** | "Guardrail" duy nhất kiểm soát AI (Vibe Coding), ngăn over-engineering, hallucination. | *Dev.to: Why PRD.md is Your Best Guardrail* |
| **Tư duy Architect / Systems Thinking** | Chuyển từ "làm task" → "giải quyết business problem bằng tech + people + process". Yêu cầu bắt buộc cho role 10+ năm VN. | *HN Comment `talmr` (Insight 7.0)*; *JD Solutions Architect VN* |
| **GenAI/RAG/Agents thực chiến (không chỉ gọi API)** | JD Senior VN yêu cầu "kinh nghiệm thực chiến"; AI Engineer SF khuyên "excel at other critical aspects" (rag, eval, guardrails). | *JD System Design VN*; *YT Comment `@shivaraghav8184` (Insight 2.0)* |
| **Secure Coding / Auth Hardening / Supply Chain Security** | Hack Binance qua fake interview (chạy code local); OTP spam do lỗi logic auth; PHP 0-day exploit sớm. | *J2TEAM Binance Hack*; *J2TEAM OTP Spam*; *CyberTales PHP 0-day* |
| **Tiếng Anh giao tiếp chuyên nghiệp (Fluent)** | Điều kiện *bắt buộc* cho role Architect/Senior làm việc với HK/SG/US tại VN. | *JD System Design VN* |
| **Product Engineering Mindset** | "Figure out what your company should build next" – HN `greenowl`; Hiểu business để AI không thay thế. | *HN Comment `greenowl`*; *Video Under The Numbers* |

### Công nghệ cần học – *Phân biệt Xu hướng thật vs Hype*
| Công nghệ / Mảng | Trạng thái | Hành động cụ thể |
| :--- | :--- | :--- |
| **Python (FastAPI/LangChain/LlamaIndex) + RAG/Eval** | **Xu hướng thật** – Cần cho GenAI backend, Agentic workflow. | Học để build *một RAG system end-to-end có eval pipeline* (không chỉ prototype). |
| **Node.js / TypeScript / NestJS** | **Xu hướng thật** – Stack yêu cầu bắt buộc cho JD Architect VN (thay/văn song song Java/Spring). | Nắm vững DI, Module, Microservice pattern trong NestJS; so sánh với Spring Boot. |
| **Kubernetes (EKS/GKE) & Cloud Native (AWS/GCP)** | **Xu hướng thật** – Yêu cầu chuẩn cho Senior/Architect VN. | Học *thực chiến*: Deploy một hệ thống HA, setup CI/CD, Observability (Prometheus/Grafana/Loki). |
| **System Design (Distributed Systems, Event-Driven, CQRS)** | **Core skill vĩnh cửu** – Là rào cản lớn nhất để lên Architect. | Học qua *Designing Data-Intensive Applications (DDIA)* + luyện case study thực (Uber, TikTok architecture). |
| **Security: OWASP Top 10 for LLM/Apps, SBOM, Cosign/SBOM signing** | **Xu hướng thật & Bắt buộc** – Do chuỗi cung cấp & AI attack surface mở rộng. | Tham gia *OWASP Top 10 for LLM*; config `Syft`/`Grype`/`Cosign` trong pipeline. |
| **Prompt Engineering có cấu trúc (Structured Output, Few-shot, RAG prompting)** | **Xu hướng thật** – Kỹ năng "điều khiển" AI coding agent hiệu quả. | Áp dụng ngay trong daily coding: dùng Cursor/Copilot với *rule file* (`.cursorrules`), cung cấp PRD context. |
| **Rust/Go (cho infrastructure tooling)** | **Niche nhưng đắt giá** – Dùng cho high-perf sidecar, security tool, CLI. | Chỉ học nếu muốn chuyên Infrastructure/Security Engineering; không bắt buộc cho App Dev. |
| **Blockchain/Web3** | **Hype giảm / Niche** – Không xuất hiện trong JD Senior/Architect VN hay Global trend dữ liệu. | Không ưu tiên trừ khi muốn chuyên mảng này. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Những thay đổi tư duy cốt lõi (từ cộng đồng senior)
1.  **Từ "Code Writer" → "System Designer & PRD Author":** AI viết code nhanh hơn bạn. Giá trị của bạn là **xác định *cái gì* cần xây, *tại sao*, *ranh giới* đâu, *rủi ro* gì** – ghi thành PRD/Spec trước khi prompt AI. [Dev.to Article]
2.  **Từ "Task Executor" → "Business Problem Solver":** Hãy hỏi: "Feature này giải quyết vấn đề business nào? Metric nào? Nếu không làm thì sao?". Tư duy này giúp bạn **bất khả thay thế bởi AI** (AI chưa hiểu context business sâu). [HN `talmr`, `greenowl`]
3.  **Từ "Học framework mới" → "Nắm vững nguyên lý (Fundamentals)":** Network, OS, DB Internals, Distributed Consensus, Crypto basics. Các nguyên lý này **không đổi** khi framework thay đổi mỗi 6 tháng. [HN `vincent-uden` - lifelong learning bleeding edge]
4.  **Từ "Ứng tuyển qua HR/LinkedIn" → "Tiếp cận Founder/Hiring Manager trực tiếp":** Market khó, referral/internal hire chiếm đa số. AI Engineer SF khuyên: **"Target startups, reach out to founders directly"**. [YT `@shivaraghav8184`]
5.  **Security là trách nhiệm của *mọi dev*, không chỉ Sec Team:** Chạy code interview cục bộ (Binance hack), validate input OTP (Spam), patch dependency (PHP 0-day) – đều là daily job của dev.

### Áp dụng cụ thể cho Dev nền **Java/Spring Boot** đang học **Python + Network Security** (Tuần này làm gì?)

| Tuần này | Hành động cụ thể (Actionable) | Tránh gì (Anti-pattern) |
| :--- | :--- | :--- |
| **Python + AI** | 1. Viết **PRD 1 trang** cho bài toán: *"Hệ thống RAG tra cứu tài liệu nội bộ công ty"*.<br>2. Dùng **FastAPI + LangChain/LlamaIndex** implement RAG pipeline: Ingestion → Embedding (BGE-M3) → Vector DB (Qdrant/Milvus) → Retrieval (Hybrid Search) → Rerank → Generation.<br>3. **QUAN TRỌNG:** Viết **Eval Script** (Ragas/DeepEval) đo *Faithfulness, Answer Relevancy, Context Precision*. Commit lên GitHub. | Chỉ copy-paste tutorial "chat with PDF" 50 dòng code không có eval, không có chunking strategy, không có monitoring. |
| **Network Security** | 1. Lab **OWASP Top 10 for LLM** (LLM01: Prompt Injection, LLM06: Excessive Agency) trên local (Docker).<br>2. Setup **Dependency Scanning** cho project Spring Boot + Python: `OWASP Dependency Check` (Java) + `pip-audit`/`Grype` (Python) tích hợp vào GitHub Actions.<br>3. Tìm hiểu **mTLS (Istio/Linkerd)** hoặc **Zero Trust Network** cơ bản – liên quan đến Secure Service-to-Service comms. | Chỉ đọc lý thuyết CVE. Không chạy tool scan trên project thật. Không hiểu diff giữa Network Security truyền thống vs AI/LLM Security. |
| **System Design / Portfolio** | 1. Viết **ADR (Architecture Decision Record)** cho project RAG ở trên: Tại sao chọn Qdrant không phải Pinecone? Tại sao Hybrid Search? Trade-off cost/latency/accuracy.<br>2. Chuẩn bị **kịch bản giải thích** project cho Founder/Hiring Manager (theo tư duy Product Engineer): Business problem → Solution → Metric → Risk → Cost. | Chỉ đẩy code lên GitHub không có README, không có Architecture Diagram, không có ADR. |
| **Network/Outreach** | 1. Tìm 3-5 Founder/CTO tại VN/SG/US đang build AI product (LinkedIn, Twitter/X, TopDev, ITviec).<br>2. Gửi tin nhắn **cá nhân hóa**: "Em thấy anh/chị đang build X, em vừa làm project RAG/Eval giải quyết vấn đề Y tương tự, đây là link GitHub + ADR 1 trang. Em muốn xin 15p hỏi ý kiến kiến trúc." | Spam CV qua form "Apply Now". Chỉ connect LinkedIn không nhắn tin. |

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT (Top Insight Scores)

### 1. `talmr` (Hacker News – *Ask HN: How to Keep the Edge as an Engineer?*) — **Insight Score: 7.0**
> **Nguyên văn:** "I believe this is a good time for going from Engineer -> Architect mindset. You don't need to wait for a formal career progression. When I got into tech, as an engineer, I enjoyed learning as much as I could about building systems. Systems are comprised of technology, people, and business needs. How can we help our customers in the best way..."
> **Link:** [news.ycombinator.com/item?id=50362698](https://news.ycombinator.com/item?id=50362698)
> **Tại sao đáng đọc:** Đây là **bình luận có insight_score cao nhất toàn bộ dataset (7.0)**. Nó tóm gọn được *chuyển dịch tư duy cốt lõi* mà mọi senior/lead đều nhắc: ngừng tư duy "viết code xong task", bắt đầu tư duy "thiết kế hệ thống giải quyết vấn đề người + business". Đây là chìa khóa để không bị AI thay thế.

### 2. `@shivaraghav8184` (YouTube – *Suman Mpm: Why Is Getting an IT Job So Difficult in 2027?*) — **Insight Score: 2.0** (Founding AI Engineer, SF, CEG Alumni)
> **Nguyên văn:** "Hey guys, I am a founding AI engineer at a startup in San Francisco... the market here in the US is quite tough right now... My advice to anyone looking for a job right now is to **target startups and reach out to founders directly**. Also, AI is definitely here to stay, and while almost no one writes code from scratch nowadays, software development is about so much more than just coding. **Try to excel at the other critical aspects**."
> **Link:** [youtube.com/watch?v=8Xkx7lcInuQ](https://www.youtube.com/watch?v=8Xkx7lcInuQ) (Comment đầu tiên)
> **Tại sao đáng đọc:** Góc nhìn **thực tế từ "trận địa" AI Silicon Valley** (Founding Engineer). Khẳng định: (1) Market khó ở cả US, (2) Chiến thuật tìm việc hiệu quả là *direct outreach to founders* (bỏ qua HR/ATS), (3) "Critical aspects" ngoài coding (system design, eval, product sense, security) mới là giá trị cốt lõi.

### 3. `vincent-uden` (Hacker News – *Ask HN: How to Keep the Edge as an Engineer?*) — **Insight Score: 2.0**
> **Nguyên văn:** "As you mention in your post its more about keeping up with the moving bleeding edge rather than keeping what you have. The most important point/habit is to be invested in lifelong learning. The moment you stop learning, only doing rote work, is when you stagnate."
> **Link:** [news.ycombinator.com/item?id=50362698](https://news.ycombinator.com/item?id=50362698)
> **Tại sao đáng đọc:** Nhấn mạnh **tư duy "bleeding edge" & lifelong learning** là *thói quen*, không phải mục tiêu. Phù hợp với dev VN đang học Python/Security: đừng học xong coi là "xong", hãy xây quy trình cập nhật kiến thức liên tục (RSS, Newsletter, Paper reading).

### 4. `kypro` (Hacker News – *Ask HN: How to Keep the Edge as an Engineer?*) — **Insight Score: 2.0**
> **Nguyên văn:** "Realistically you can't [compete with AI]. People trying to compete with AIs at processing or manipulating data are going to fall short both in capability and in speed... 'Sure, AI can create a basic prototype, but you need real engineers to build something production ready' ... 'Maybe we just need to accept that the bar for 'production ready' is being raised'."
> **Link:** [news.ycombinator.com/item?id=50362698](https://news.ycombinator.com/item?id=50362698)
> **Tại sao đáng đọc:** Phá vỡ ảo tưởng "AI chỉ làm prototype, dev lo production". Thực tế: **Thanh bar "production ready" đang được nâng cao bởi chính AI** (AI viết test, AI setup CI/CD, AI config K8s). Dev phải nắm *chuẩn production* cao hơn AI (observability, resilience, cost opt, security hardening).

### 5. **Facebook User** (J2TEAM Community – *Cảnh báo OTP Spam*) — **Insight Score: 3.5**
> **Nguyên văn:** "bài viết này chỉ giúp lan truyền con bot spam OTP ra thêm thôi chứ ko giảm đc gì đâu bác ạ:v toàn cty các kiểu hệ thống nó dễ cho người dùng r giờ làm gắt là gắt thế nào đc"
> **Link:** [facebook.com/groups/j2team.community/permalink/3234026643596100/](https://facebook.com/groups/j2team.community/permalink/3234026643596100/)
> **Tại sao đáng đọc:** Góc nhìn **thực tế vận hành (DevOps/Security) tại VN**: Không thể chỉ patch lỗ hổng điểm (rate limit OTP), phải **thiết kế hệ thống auth resilient từ gốc** (device fingerprint, behavioral analysis, silent auth, passkey). Đây là tư duy Architect/Security Engineer mà dev VN cần học.

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY (Ưu tiên Expert Voice & VN Context)

| # | Nguồn | Loại / Region | Luận điểm chính / Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Ask HN: How to Keep the Edge as an Engineer?** | Forum / Global | Cuộc thảo luận chất lượng cao nhất về survival strategy: Architect mindset, Product Engineer, Lifelong learning, Accepting AI raises the bar. | **Insight_score cao nhất (7.0)**, tập trung tiếng nói Senior/Staff/EM toàn cầu. **Bắt đọc.** |
| **2** | **Why PRD.md is Your Best Guardrail in the Era of Vibe Coding** (Dev.to) | Article / Global | Phân tích sâu lỗi Vibe Coding (AI thiếu scope, over-engineering). Đề xuất quy trình **Spec/PRD-driven development** như guardrail. | **Expert voice cao** (tác giả là practitioner), hành động hóa ngay được cho daily coding với Cursor/Copilot. |
| **3** | **🔥 TÌM KIẾM SOLUTIONS ARCHITECT - System Design Vietnam** | Facebook (Group) / **VN** | **JD thực tế mercato VN cao cấp:** 10yrs, English fluent, Node/TS/NestJS, **GenAI/RAG/Agents thực chiến**, System Design, K8s, AWS/GCP, Hybrid HK/HCM. | **Expert Voice Score: 7.5** (Group chuyên System Design). **Bản đồ kỹ năng đích** cho dev VN muốn lên Architect. |
| **4** | **AI May Not Fire You. It May Stop Hiring You.** (Under The Numbers) | Video / Global | Dựa trên Stanford Research, BLS: AI không gây layoff mass mà **cắt bậc thang entry-level**. Cơ chế: Senior + AI = produtivity cao → ít thu junior. | **Dữ liệu thực (Data-driven)**, không dự đoán suông. Giải thích tại sao Fresher VN khó tìm việc & cách phá vỡ (Portfolio phải chứng minh senior-like thinking). |
| **5** | **Hackers Exploited This Zero-Day 4 DAYS Before Disclosure!** (CyberTales) | Video / Global | **Sự cố Major (is_major_incident=true):** PHP RCE (CVSS 9.2) exploit từ Oct 17, disclose Oct 21. Legacy server vẫn ở rủi ro. | **Bắt buộc xem cho mục 6**. Thay đổi tư duy security: "Patch ngay khi có PoC/Exploit trong tự nhiên" chứ không chờ CVE publish. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP

> **Điều kiện:** Dữ liệu có mục `is_major_incident: true` (PHP Zero-day exploit pre-disclosure).

### Sự cố: **PHP Zero-Day (PHP2Shell) – Remote Code Execution được khai thác 4 ngày trước khi công bố**
*   **Chi tiết kỹ thuật:** 2 lỗ hổng RCE nghiêm trọng trong PHP runtime memory management (fatal error handling). **CVSS 9.2 (Critical)**. Tên mã: *PHP2Shell*.
*   **Timeline:** Threat actors bắt đầu bắn exploit thực tế vào honeypot (Amazon MadPot) **ngày 17/10**. Coordinated embargo lift / Public disclosure **ngày 21/10**. Có bằng chứng embargo bị rò rỉ.
*   **Quy mô:** Hàng triệu server PHP legacy (EOL, unpatched) vĩnh viễn bị exposed. Không chỉ PHP core, cả các framework/app chạy trên PHP cũ đều bị ảnh hưởng.

### BÀI HỌC NGHỀ NGHIỆP (Career Lessons) – *Dev Java/Spring Boot + Python/NetSec làm gì tuần này?*

| Lĩnh vực | Bài học & Hành động cụ thể (Action Items) |
| :--- | :--- |
| **Dependency & Supply Chain Management** | 1. **Kiểm tra toàn bộ project (Java `pom.xml`/`build.gradle`, Python `requirements.txt`/`pyproject.toml`):** Có component nào dùng PHP không? (Rất hiếm nhưng có thể qua `exec()`, `shell_exec()`, sidecar container, CI/CD image base).<br>2. **Automate SBOM (Software Bill of Materials):** Cài `Syft` (Anchore) vào CI pipeline *hôm nay* để gen SBOM cho mọi build. Biết chính xác version transitive dependency. |
| **Vulnerability Management & Patching Speed** | 1. **Thiết lập "Zero-Day Response Playbook" cá nhân/team:** Khi exploit public (như PHP2Shell Oct 17) mà chưa có patch vendor -> **Mitigation ngay**: WAF rule (ModSecurity/Coraza), disable function危险 (`disable_functions` trong php.ini), network segmentation, egress filtering.<br>2. **Không chờ CVE/NVD.** Theo dõi **Exploit DB, GitHub Security Advisories, Vendor Security Mailing List, Honeypot feeds (GreyNoise, Shadowserver)**. |
| **Observability & Incident Response** | 1. **Log & Metric phải bắt được "Anomaly Execution":** Spike CPU/Memory lạ, process con lạ spawn (`/bin/sh`, `curl`, `wget`), outbound connection đến IP không whitelist. Setup alert rule cho các pattern này (Falco, Tetragon, hoặc đơn giản là Promtail/Loki + LogQL alert).<br>2. **Tabletop Exercise 15 phút:** Giả định server app bị RCE hôm nay -> Quy trình isolate, forensic, notify, rollback/rollforward là gì? Viết runbook 1 trang. |
| **Secure Coding & Hardening (Applied to Java/Python)** | 1. **Java:** Tắt `Java Deserialization` risk (ObjectInputFilter), kiểm tra `Runtime.exec()`/`ProcessBuilder` usage. Dùng `Spring Boot Actuator` + `Micrometer` để expose health/metric cho detection.<br>2. **Python:** **Cấm `eval()`, `exec()`, `pickle.load()`, `subprocess.shell=True`** trong code xử lý input user. Dùng `shlex.quote()` / `subprocess.run(args_list, shell=False)`.<br>3. **Container Hardening:** Chạy non-root, `readOnlyRootFilesystem: true`, `capabilities: drop: [ALL]`, `seccompProfile: RuntimeDefault` (hoặc custom block `execve` không cần thiết). |
| **Kỹ năng đắt giá bỗng nổi (High-Value Skills)** | 1. **Egress Filtering & Network Policy (Cilium/Calico/Kubernetes NetworkPolicy):** Chặn container/app kết nối ra ngoài trừ whitelist. Kỹ năng này vừa giải quyết RCE callback, vừa giải quyết Supply Chain attack (dependency gọi về server c2).<br>2. **Runtime Security (eBPF-based: Falco, Tetragon, Tracee):** Phát hiện anomaly *tại runtime* (syscall bất thường) – không phụ thuộc signature CVE. **Học setup Falco rules custom cho app Java/Python của bạn.**<br>3. **Patch Automation & Canary Deployment:** Khả năng rollout patch/security config đến 100% fleet trong < 1 giờ (ArgoCD/Flux + Progressive Delivery). |

> **Tóm gọn cho tuần này:** Hãy **setup Falco/Tetragon trên local Kind/K3d cluster**, viết 1 rule detect `execve` của `sh`/`bash`/`python`/`curl`/`wget` từ process Java/Python app. Chạy thử exploit proof-of-concept an toàn (ví dụ: một script test spawn shell) xem rule có trigger không. Đây là **kỹ năng security engineering thực chiến** mà JD Architect/Senior VN và Global đều săn.