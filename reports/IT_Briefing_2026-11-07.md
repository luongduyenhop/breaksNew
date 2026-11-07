📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.4xtfetmcslkr)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

---

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Định phân cực thị trường: "Số liệu tăng" ≠ "Cơ hội tốt cho tất cả"**.  
  Tin tức VN liên tiếp báo "nhu cầu tuyển dụng tăng dù có AI" (VnEconomy, VnReview) nhưng song song đó **Microsoft sa thải nhân sự tại VN** (VnExpress). Theo góc nhìn của chuyên gia, đây là dấu hiệu thị trường **tách lớp**:  
  - *Lớp 1:* Vị trí outsourcing/ODC, maintenance, code thuần túy → bị AI nén chặt, lương stagnate, dễ bị cut.  
  - *Lớp 2:* Vị trí "Product Engineer", "AI/Harness Engineer", Security/Infra senior → khan hiếm, lương cao, được ưu tiên tuyển.  
  → **Dev VN không nên vui sướng trước con số tuyển dụng tăng**, mà phải hỏi: *tuyển vị trí nào, yêu cầu cấp độ nào?*

- **Đầu tư hạ tầng AI tại TP.HCM** (Trung tâm Xuất sắc AI ứng dụng đầu tiên Châu Á – Tuổi Trẻ).  
  Tín hiệu rõ ràng: **Chính sách quốc gia đẩy "ứng dụng AI" chứ không chỉ "train model"**.  
  → Cơ hội lớn cho dev biết **triển khai, vận hành, bảo mật hệ thống AI (Harness Engineering, RAG, Agent Ops)** hơn là chỉ biết fine-tune model.

### Trên thế giới (và ý nghĩa với_dev Việt Nam)
| Dịch chuyển toàn cầu | Ý nghĩa với dev VN |
| :--- | :--- |
| **Đường vào nghề Junior bị gãy** (Dev.to: "AI Isn't Killing Juniors, It's Breaking the Learning Path") | Các công ty ODC/Outsource tại VN thường tuyển Junior làm "cú pháp". AI làm phần này tốt hơn. **Junior VN phải tự xây "learning path" mới: hiểu hệ thống, review code AI, viết test/harness ngay từ đầu.** |
| **Sự trỗi dậy của Harness Engineering** (VGU Tech Alumni: "Agent = Model + Harness"; Dev.to: "Repo won't let you file it") | Không còn giá trị "prompt engineer". Giá trị nằm ở **kiến trúc vận hành Agent: Context window management, Tool calling, Evaluation loop, Safety guardrails**. Dev VN nên học **LangGraph, LangChain, AutoGen, evaluation frameworks (RAGAS, DeepEval)**. |
| **Tư duy Architect/Systems > Coder** (HN "Ask HN: How to Keep the Edge" – top comment insight 7.0) | "Engineer → Architect mindset: Systems = Technology + People + Business". **Dev VN ở cấp độ 3-5 năm kinh nghiệm bắt buộc chuyển sang tư duy này** để không bị thay thế bởi AI coder. |
| **Thị trường US/Ấn Độ cực kỳ khủng hoảng cho Fresher/Entry-level** (Suman Mpm video + comment founding AI engineer @shivaraghav8184) | Mô hình "đào tạo fresher 3-6 tháng ra làm việc" tại VN đang hết hạn. **Cần portfolio thực tế (side project có user, contrib open source, bug bounty) thay vì chỉ chứng chỉ/đồ án trường.** |

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cứng (Hard Skills) – Ưu tiên theo thứ tự "đắt giá nhất"
1.  **Harness Engineering / Agentic Workflow Architecture** (Xu hướng thật, không hype)  
    - *Tại sao:* VGU Alumni post & Dev.to article khẳng định bài toán đã dịch từ Prompt → Context → **Harness**.  
    - *Công nghệ:* **LangGraph (stateful agents), LangSmith/LangFuse (observability), Evaluation (RAGAS, custom evals), Tool calling patterns, Memory management**.
2.  **System Design & Architecture Thinking** (Kỹ năng "bất tử")  
    - *Tại sao:* HN top comment (insight 7.0) & Dev.to "Being, Doing, Having" (expert voice 3.0) nhấn mạnh Senior craft sống ở *Context/Being* chứ không phải *Code/Have*.  
    - *Học:* Distributed systems patterns, Database internals, Observability (OpenTelemetry), **Trade-off analysis tài liệu hóa bằng ADR (Architecture Decision Records)**.
3.  **Application Security & Hardening (Network Security focus)** (Kỹ năng "đắt giá ngay lập tức" – xem Mục 6)  
    - *Tại sao:* PHP Zero-day (CVSS 9.2) bị khai thác 4 ngày trước khi công bố. Legacy stack (PHP, Java cũ, Spring Boot cũ) tại VN rất nhiều.  
    - *Công nghệ:* **SAST/DAST/IAST integration CI/CD, Sigma/YARA rule writing, eBPF runtime security, Patch management automation, OWASP Top 10 cho LLM App (LLM01-LLM10).**
4.  **Python cho AI/Automation/Security Tooling** (Ngôn ngữ "dụng cụ" bắt buộc)  
    - *Tại sao:* Hệ sinh thái AI Agent, Security tooling, Scripting automation đều dùng Python.  
    - *Học:* **FastAPI (serve model/agent), Pydantic (validation), AsyncIO (concurrency), Poetry/UV (dependency mgmt), Ruff (linting).**

### Công nghệ/Khung làm việc – Phân biệt Xu hướng thật vs Hype
| Xu hướng THẬT (Có bài viết/chuyên gia xác nhận) | Chỉ là HYPE / Đã hết hạn |
| :--- | :--- |
| **LangGraph / LangChain Expression Language (LCEL)** | "Prompt Engineering" đơn thuần (đã thành commodity) |
| **RAG Evaluation & Observability (RAGAS, LangSmith, Arize/Phoenix)** | "Vector DB nào tốt nhất" (DB chỉ là commodity, quan trọng là retrieval strategy) |
| **eBPF / Cilium / Tetragon cho Runtime Security** | "Học Kubernetes YAML bằng lòng" (cần hiểu control plane, networking, security) |
| **Architecture Decision Records (ADR) & System Thinking** | "Học thêm framework JS mới (Next.js 15, React 19...)" – nếu không kèm System Design |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy cốt lõi (từ cộng đồng & chuyên gia)
1.  **Từ "Task Executor" → "Problem Owner / Product Engineer"**  
    - *Nguồn:* HN `greenowl` ("Become a product engineer. Figure out what your company should build next") & HN `talmr` (Insight 7.0: "Systems = Tech + People + Business").  
    - *Áp dụng:* Khi nhận ticket, **đừng hỏi "code như thế nào", hãy hỏi "vấn đề business là gì, metric thành công là gì, rủi ro rollback ra sao"**. Viết ADR trước khi code.

2.  **Từ "Viết code từ con trỏ" → "Orchestrate & Verify AI Output" (Harness Mindset)**  
    - *Nguồn:* VGU Alumni (Harness Engineering), Dev.to ("Repo won't let you file it").  
    - *Áp dụng:* Mọi task lặp lại → **viết script/tool/harness để AI tự làm + tự test + tự report**. Bạn làm "meta-work": thiết kế feedback loop, eval set, guardrails.

3.  **Bảo mật là "Default", không phải "Feature sau"**  
    - *Nguồn:* PHP Zero-day incident (Mục 6).  
    - *Áp dụng:* Mọi PR phải có **Threat Model nhẹ (STRIDE 5 phút)**, dependency scan (Trivy/Snyk), unit test cover edge case bảo mật.

---

### KẾ HOẠCH TUẦN NÀY CHO DEV JAVA/SPRING BOOT ĐANG HỌC PYTHON & NETWORK SECURITY

| Ngày | Hành động cụ thể (Actionable) | Tránh gì |
| :--- | :--- | :--- |
| **Thứ 2-3** | **Build một "Harness" nhỏ bằng Python + LangGraph:** Tự động quét dependency `pom.xml`/`build.gradle` của project Java cũ → dùng LLM gợi ý CVE tiềm ẩn + sinh PR fix version + chạy `mvn test` verify. *Đây là bài tập kết hợp: Java knowledge + Python/Agent + Security.* | Chỉ đọc tutorial LangChain "hello world". |
| **Thứ 4** | **Phân tích bản vá PHP Zero-day (CVE-2024-XXXX - xem Mục 6):** Tìm hiểu root cause (memory corruption in `zend_mm_alloc`). Viết rule **Sigma/YARA** detect exploit pattern (log pattern, memory anomaly). Đẩy lên GitHub repo cá nhân. | Chỉ đọc tin tức "PHP bị hack". |
| **Thứ 5** | **Viết 1 ADR (Architecture Decision Record) giả định:** "Chuyển module thanh toán Spring Boot monolith sang microservice bảo mật cao". Xác định: Threat model, Data encryption, Inter-service mTLS, Observability stack. Review với mentor/peer. | Vẽ diagram đẹp mà không có threat model/trade-off. |
| **Thứ 6** | **Học eBPF cơ bản cho Security:** Chạy `bpftrace` trace `execve`, `connect` trên container Java. Hiểu kernel-level visibility. | Học Kubernetes certification (CKA) nếu chưa nắm vững Linux Kernel/Networking. |
| **Cuối tuần** | **Contribute 1 PR nhỏ cho open source security tool** (Trivy, Syft, Grype, hoặc LangGraph example). Ghi nhận quy trình: Fork → Branch → Test → PR → Review. | Chỉ commit code cá nhân private. |

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT (Top Insight Score)

### 1. **Hacker News – `talmr` (Insight Score: 7.0 – CAO NHẤT TOÀN DATASET)**
> **Nguồn:** [Ask HN: How to Keep the Edge as an Engineer?](https://news.ycombinator.com/item?id=50362698) | Votes: 0 (HN ẩn vote thường)  
> **Nội dung đầy đủ:**  
> > "I believe this is a good time for going from Engineer -> Architect mindset. You don't need to wait for a formal career progression. When I got into tech, as an engineer, I enjoyed learning as much as I could about building systems. Systems are comprised of technology, people, and business needs. How can we help our customers in the best way? ... The 'edge' is not knowing a specific framework, it's understanding how to compose systems that solve problems reliably."
> > **English reference:** "I believe this is a good time for going from Engineer -> Architect mindset... Systems are comprised of technology, people, and business needs."
> **Tại sao đáng đọc:** Đây là **góc nhìn Senior/Staff Engineer** xác nhận xu hướng "Architect Mindset" là kỹ năng cốt lõi sống sót trước AI. Không phải lý thuyết – là kinh nghiệm thực chiến "hệ thống = tech + people + business".

### 2. **YouTube (Suman Mpm) – `@shivaraghav8184` (Insight Score: 2.0 – Founding AI Engineer, SF)**
> **Nguồn:** [Why Is Getting an IT Job So Difficult in 2027?](https://www.youtube.com/watch?v=8Xkx7lcInuQ) | Votes: 9  
> **Nội dung đầy đủ:**  
> > "Hey guys, I am a founding AI engineer at a startup in San Francisco... the market here in the US is quite tough right now... My advice to anyone looking for a job right now is to target startups and reach out to founders directly. Also, AI is definitely here to stay, and while almost no one writes code from scratch nowadays, software development is about so much more than just coding. Try to excel at the other critical aspects."
> > **English reference:** "...almost no one writes code from scratch nowadays, software development is about so much more than just coding. Try to excel at the other critical aspects."
> **Tại sao đáng đọc:** **Thực tế tuyển dụng Silicon Valley 2024/2025** từ người đang làm Founding AI Engineer. Xác nhận: "Viết code từ 0 đã chết", "Critical aspects" (design, debug, product sense, communication) mới là giá trị. Khuyên	target startup & contact founder trực tiếp – áp dụng được cho dev VN muốn làm remote/outsource chất lượng cao.

### 3. **Facebook (J2TEAM Community) – User bình luận bài Anthropic (Insight Score: 2.0)**
> **Nguồn:** [J2TEAM Share: 4 người rời Anthropic](https://facebook.com/groups/j2team.community/permalink/3237292893269475/)  
> **Nội dung đầy đủ:**  
> > "Quan trọng nhất đối với mấy thằng OpenAI/Anthropic vẫn là mấy ông giáo sư, tiến sĩ chịu trách nhiệm nghiên cứu, training AI/LLM ấy. Chứ mấy cái như Claude Code, Claude Desktop, Harness thì nó cũng chỉ là những tools ở tầng app nên ko khó như vậy đâu, nó tìm người mới mấy mấy hồi."
> **Tại sao đáng đọc:** **Phân biệt rõ ràng "Core Research" vs "Application Layer Tooling"**. Dev VN không cần đua theo train LLM (cần PhD, tài nguyên khủng), mà nên **chuyên sâu tầng Application/Harness/Tooling** – nơi có nhu cầu lớn, barrier thấp hơn, và phù hợp với kỹ năng engineering hiện có.

### 4. **Hacker News – `vincent-uden` (Insight Score: 2.0)**
> **Nguồn:** [Ask HN: How to Keep the Edge as an Engineer?](https://news.ycombinator.com/item?id=50362698)  
> **Nội dung đầy đủ:**  
> > "As you mention in your post its more about keeping up with the moving bleeding edge rather than keeping what you have. The most important point/habit is to be invested in lifelong learning. The moment you stop learning, only doing rote work, is when you stagnate."
> > **English reference:** "...keeping up with the moving bleeding edge rather than keeping what you have... The moment you stop learning, only doing rote work, is when you stagnate."
> **Tại sao đáng đọc:** Nhấn mạnh **"Bleeding edge" (ranh giới tiên phong) chứ không phải "Best practice" (đã cũ)**. Dev VN thường học "best practice" 2-3 năm trước -> đã lỗi thời. Cần setup quy trình tự cập nhật: follow RSS security advisories, AI papers weekly, HN/Daily.dev.

### 5. **Hacker News – `kypro` (Insight Score: 2.0)**
> **Nguồn:** [Ask HN: How to Keep the Edge as an Engineer?](https://news.ycombinator.com/item?id=50362698)  
> **Nội dung đầy đủ:**  
> > "Realistically you can't. People trying to compete with AIs at processing or manipulating data are going to fall short both in capability and in speed. We've seen a lot of these posts in recent years: - 'Sure, AI can create a basic prototype, but you need real engineers to build something production ready' - 'Maybe we..."
> > **English reference:** "People trying to compete with AIs at processing or manipulating data are going to fall short both in capability and in speed."
> **Tại sao đáng đọc:** **Bác bỏ giả tưởng "AI chỉ làm prototype, dev làm production"**. AI đang xâm lấn dần production-ready code. Dev phải chuyển sang lĩnh vực AI *chưa* làm tốt: **Ambiguity resolution, Stakeholder negotiation, Novel architecture, Security/Compliance validation.**

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY (Ưu tiên Expert Voice & Relevance)

| # | Nguồn | Loại / Khu vực | Luận điểm chính & Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[HN] Ask HN: How to Keep the Edge as an Engineer?** | [Quốc tế] Forum Chuyên gia | **Top comment (Insight 7.0): Engineer → Architect Mindset.** Systems = Tech + People + Business. Lifelong learning at bleeding edge. AI commoditizes data processing. | **Cao nhất Insight Score (7.0)**. Góc nhìn Staff/Principal Engineer thực tế. Áp dụng ngay cho dev 3-5 năm kinh nghiệm. |
| **2** | **[VN] VGU Tech Alumni: Giải mã Harness Engineering** | [VN] Cộng đồng Kỹ thuật sâu | **Kiến trúc Agent = Model + Harness.** 3 giai đoạn: Prompt → Context → **Harness Engineering**. 9 thành phần Harness + Feedback Loop. | **Xu hướng kiến trúc xác định 2025-2026**. Tiếng Việt, ngữ cảnh VN, tác giả Việt Nguyễn (AI Expert). expert_voice_score cao ngầm. |
| **3** | **[Quốc tế] Dev.to: Being, Doing, Having: Why 50 Years of Senior Craft Lives in Context, Not Code** | [Quốc tế] Bài chuyên sâu (Expert Voice 3.0) | Senior craft = **Context/Being (Tư duy, kinh nghiệm, quyết định)**, không phải Code/Have. AI nhảy thẳng "Have" mà thiếu "Be/Do". | **Tác giả `gde` (Senior/Architect)**. Giải thích *tại sao* Junior bị gãy đường học: thiếu "Being/Doing" – giai đoạn AI cướp đi. |
| **4** | **[Quốc tế] CyberTales: Hackers Exploited PHP Zero-Day 4 Days Before Disclosure** | [Quốc tế] Video Sự cố lớn (Major Incident, Severity 6.0) | **CVE CVSS 9.2 (RCE PHP Core).** Khai thác thực tế 4 ngày *trước* embargo. Legacy PHP server vĩnh viễn exposed. IR baseline phải rollback. | **Trigger Mục 6**. Bài học nghề nghiệp cụ thể cho Security/DevOps/Java Legacy maintainer. |
| **5** | **[Quốc tế] YouTube (Suman Mpm): Why Is Getting an IT Job So Difficult in 2027?** | [Quốc tế] Video Thị trường (Relevance 89) | Thị trường US/Global khủng hoảng. **Comment `@shivaraghav8184` (Founding AI Eng):** Target startup, contact founder, excel at non-coding aspects. | **Relevance_score cao nhất (89)**. Comment Insight 2.0 từ người *trong nghề, tại Silicon Valley*. Thực tế tuyển dụng mới nhất. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP

### Sự cố: **PHP Zero-Day Double RCE (PHP2Shell) – Khai thác thực tế 4 ngày trước khi công bố (Pre-disclosure Exploitation)**
- **Chi tiết kỹ thuật (từ CyberTales Video):**  
  - **2 lỗ hổng RCEcritical** trong PHP Core Memory Management (`zend_mm_alloc` / fatal error handling).  
  - **CVSS 9.2 (Critical)**.  
  - **Trạng thái:** **Đã bị khai thác trong thực tế (In-the-wild)** bởi threat actors từ **ngày 17/10**, trong khi Embargo chính thức lift ngày **21/10**.  
  - **Vector:** Remote, unauthenticated. Ảnh hưởng hàng triệu server PHP legacy (shared hosting, old VPS, Docker image cũ).  
  - **Mã CVE:** (Video đề cập PHP2Shell, mapping đến **CVE-2024-XXXX** – *cần tra cứu CVE chính thức khi MITRE public, nhưng video xác nhận CVSS 9.2 & exploited*).

### BÀI HỌC NGHỀ NGHIỆP (Career Lessons) – Quan trọng cho Dev Java/Spring Boot + Python/NetSec:

| Lĩnh vực | Bài học & Hành động cụ thể tuần này |
| :--- | :--- |
| **Kỹ năng bỗng trở nên đắt giá** | **1. Legacy Hardening & Virtual Patching:** Không phải server nào patch PHP ngay được. Cần biết viết **WAF ModSecurity rules / eBPF filters / Network IDS signatures (Suricata/Zeek)** để chặn exploit *trước khi patch*. <br> **2. Software Bill of Materials (SBOM) & Dependency Tracing:** Biết ngay project dùng PHP version gì, ở đâu (container, VM, managed service). Tool: **Syft, Trivy, CycloneDX**. <br> **3. Incident Response (IR) Baseline Rollback:** Video nhấn mạnh: *"Your IR baseline must roll back to Oct 17th"*. → **Thực hành: Kiểm tra log SIEM/Splunk/ELK từ 4-7 ngày trước khi CVE public**. Tự động hóa bằng Python script query API SIEM. |
| **Nhu cầu nhân lực Security thay đổi** | - **SecOps/Platform Security Engineer** > Pure Pentester. Cần người **tự động hóa detection/response at scale** (Python + eBPF + Cloud API). <br> - **Java/Spring Boot Dev có skill Security** (Secure Code Review, SAST tuning, Runtime Protection - Java Agent) được ưu tiên cho các dự án migration legacy. |
| **Hành động TUẦN NÀY cho Persona (Java/Spring + Python/NetSec)** | 1. **Viết script Python:** Quét toàn bộ repo GitLab/GitHub nội bộ (hoặc local) → Tìm `Dockerfile`/`pom.xml`/`composer.json` chứa `php:` version < patched version → Output CSV risk report. <br> 2. **Lab thực chiến:** Pull Docker image `php:8.2-apache` (vuln) → Chạy exploit PoC (tìm trên GitHub `PHP2Shell`/`CVE-2024-XXXX`) trong VM isolate → Quan sát crash/log → Viết **Sigma rule** detect crash pattern / anomalous child process. <br> 3. **Học eBPF 1 tiếng:** Dùng `bpftrace -e 'tracepoint:syscalls:sys_enter_execve { printf("%s %s\n", comm, str(args->filename)); }'` monitor container PHP bị exploit spawn shell. Hiểu *runtime visibility* – kỹ năng core cho Security Engineer hiện đại. |

> **Lưu ý:** Không chỉ "biết tin tức". Sự cố này chứng minh: **Kỹ năng "Vá lỗi" (Patching) đã không đủ**. Kỹ năng **"Phát hiện & Chặn khi chưa có patch" (Detection & Virtual Patching / Hardening)** mới là differentiator định mức lương cao.

---