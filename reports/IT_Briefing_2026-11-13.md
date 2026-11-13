📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.asou7skak0io)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
**1.1. "Bong bóng" gia công (outsourcing) đang xép lỳ, chuyển dịch sang sản phẩm (product) & in-house enterprise**
*   **Dẫn chứng:** Video phân tích 149.360 tin tuyển dụng 2021–2026 (Kênh *Học Lập Trình cùng Phát*) chỉ ra ngành gia công chịu tác động mạnh nhất do AI tự động hóa code CRUD/base. Microsoft mở văn phòng mới tại TP.HCM *sau* đợt sa thải (VnExpress) cho thấy Big Tech vẫn đầu tư VN nhưng **chỉ tuyển senior/specialized** (AI, Cloud, Security) thay cho mass hiring junior trước đây.
*   **Dữ liệu:** Tin tuyển dụng dev tại Mỹ tăng ~15% từ 2/2025 dù AI viết code (Vietnam.vn), nhưng tại VN, comment thực tế: *"Thực sự hôm nay em bị từ chối ngay trong phỏng vấn... đã rất lâu chưa có việc làm"* (@nicky_s). **Cung junior vượt xa cầu, cầu dịch sang senior/niche.**

**1.2. Vị trí AI/ML bùng nổ nhưng "khép kín" – yêu cầu nền tảng hệ thống + domain knowledge**
*   **Dẫn chứng:** Cùng video phân tích VN: nhóm việc làm AI tăng nhanh nhất nhưng chủ yếu Senior/Lead. Tin tức *"AI viết mã hàng loạt nhưng tin tuyển dụng vẫn tăng"* thực chất là tăng ở **vai trò điều phối/hệ thống** (AI Engineer, Platform Engineer), không phải coder thuần.

### Trên thế giới (Ý nghĩa với Dev Việt Nam)
**1.3. "Ghost Postings" & Khoảng cách Posting vs Headcount thực** ➜ **Dev VN đừng tin số lượng JD trên LinkedIn/TopCV**
*   **Dẫn chứng:** The Seasoned CTO (expert_voice_score 3.0) phân tích: *"Job postings rise while actual hiring numbers shrink... teams authorized for far fewer roles"*.
*   **Áp dụng VN:** Nhiều công ty đăng JD để build employer brand/giữ pipeline, không có budget(headcount) thật. **Chiến thuật:** Chỉ apply qua referral/nội bộ, hoặc target công ty vừa raise fund/mở entity mới (như Microsoft HCMC).

**1.4. Phân hóa lương cực đại: Senior $136k median vs Fresher "0 offer"** ➜ **Mục tiêu 3-5 năm đầu là "thoát Fresher" bằng mọi giá**
*   **Dẫn chứng:** HowMuchSalaryUS (expert_voice_score 7.5): Median dev $136k/năm, nhưng *"new grads struggling to get hired"*. Stanford research (video My AI Life): *"Young workers in highly AI-exposed occupations falling behind, mainly through reduced hiring"*.
*   **Áp dụng VN:** Mức lương VN đang phân hóa tương tự (Senior 40-80tr, Fresher 8-12tr hoặc unpaid intern). **Không có "thang máy" cho junior nữa – phải leo cầu thang (slope).**

**1.5. Kỹ năng "Vibe Coding" (code bằng AI) đang hạ giá trị viết code tay – Giá trị chuyển sang Kiến trúc, An ninh, Hệ thống**
*   **Dẫn chứng:** Bài Lemmy (PhD Stats/CS): *"Vibe coding has taken over... few open positions... just pushing a button instead of thinking"*. Dev.to articles về MCP Server/Agent API Access: Xây dựng agent an toàn, quản lý context window, permission boundary là skill mới.
*   **Áp dụng VN:** Công ty VN (FPT, VNG, các startup AI) đang tuyển **AI Application Engineer** – người biết *hệ thống* để gắn LLM vào production an toàn, không phải prompt engineer.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

| Kỹ năng / Công nghệ | Phân loại | Tại sao (Nguồn) | Cách học thực chiến ( cho background Java/Spring Boot) |
| :--- | :--- | :--- | :--- |
| **System Design & Software Architecture** | **Core - Bắt buộc** | The Seasoned CTO: *"Software architecture knowledge helps you stand out when hiring managers prioritizing quality over quantity"*. John Kim: *"Hard problems and trust to lead them come about 3 years into a job"*. | Học pattern: CQRS, Event Sourcing, Modular Monolith. Viết ADR (Architecture Decision Record) cho project Spring Boot cũ. Đọc *Designing Data-Intensive Applications* (DDIA) Chương 1-3, 6, 9. |
| **AI Agent / LLM App Engineering (MCP, RAG, Tool Calling, Guardrails)** | **Core - Xu hướng thật (Not hype)** | Dev.to (Necoz, Mudraid): MCP Server drain context window; Agent API Access control. Fireship comment: Bubble chưa vỡ, tooling đang trưởng thành. | Build 1 **Internal Tool** bằng Python (FastAPI/LangGraph): Agent tự review PR Spring Boot (check security, naming convention). Triển khai local (Ollama) + MCP server cho DB/Log. |
| **Network Security / Observability / Hardening** | **Niche - Đắt giá, ít cạnh tranh** | User context (đang học NetSec) + Layoff context: Công ty cần người "bảo vệ" hệ thống khi AI mở rộng bề mặt tấn công. Microsoft HCMC hiring = cần Security/Infra. | Học **eBPF (Cilium/Hubble)** để observe network K8s. Làm lab: Detect anomalous traffic từ compromised container. Cert: **eJPT/OSCP** (nếu muốn chuyên Security) hoặc **CKS** (K8s Security). |
| **Cloud Native / Platform Engineering (K8s, Terraform, GitOps)** | **Core - Infrastructure as Code** | Polance (expert 4.5): Yêu cầu 3+ năm exp Java/Python/JS + Cloud. Video "Why Layoffs": Restructuring = cần Platform team tự phục vụ dev. | Chuyển project Spring Boot deploy manual sang **ArgoCD + Helm + K8s (Kind/k3d local)**. Viết Terraform cho VPC/RDS. Hiểu *control plane* vs *data plane*. |
| **Business Acumen / Product Sense** | **Soft Skill - Yếu tố晋升 (Promotion)** | John Kim: *"Optimize for Slope (learning), not Salary"*. KaiPov (expert 3.0): Staff/CTO làm *trade-off business*, không chỉ code. | Tham gia **Product Review meeting** (xin vào nghe). Học viết **PR/FAQ (Amazon style)** cho feature mới. Hỏi PM: "Metric thành công là gì? Rolling back thế nào?". |

> **Phân biệt Hype vs Thật:**
> *   **Hype:** "Prompt Engineering" course, "AI No-code builder", Cert AWS/Azure entry-level (SAA/CP) *nếu không có project thực*.
> *   **Thật:** **MCP Server development**, **eBPF/Kernel tracing**, **Distributed Systems correctness (TLA+/formal methods basics)**, **System Design thực chiến**.

---

## 3. TƯ DUY & CÁCH ÁP DỤNG (CHO DEV JAVA/SPRING BOOT → PYTHON + NETWORK SECURITY)

### Thay đổi tư duy cốt lõi
1.  **Từ "Task Executor" ➜ "Problem Owner & Risk Mitigator"**
    *   AI làm task (viết code, fix bug syntax). Bạn chịu trách nhiệm: *Architecture có scale không? Security có leak không? Cost có explode không?*
    *   **Action:** Mỗi PR tự hỏi: "Nếu traffic x100 thì chỗ nào chết? Nếu dependency này bị supply-chain attack thì sao?".
2.  **Từ "Học công nghệ mới" ➜ "Xây dựng 'Slope' (Độ dốc tăng trưởng)"**
    *   John Kim: *"Jump jobs for $20k more often stall at Senior... hard problems come at year 3"*.
    *   **Action:** Cam kết ở project/công ty hiện tại **tối thiểu 2-3 năm** nếu có: (a) Legacy system phức tạp, (b) Mentor Senior/Architect, (c) Quyền decide tech stack. Nếu thiếu 2/3 ➜ chuyển ngay.
3.  **Từ "Code Java thuần" ➜ "Polyglot System Thinker"**
    *   Java/Spring Boot mạnh: Enterprise domain modeling, Transaction, Type safety.
    *   Python mạnh: AI/ML ecosystem, Scripting automation, Security tooling.
    *   **Bridge:** Dùng **GraalVM Polyglot** hoặc **gRPC/Message Queue** để nối Spring Boot (Core Business) ↔ Python Service (AI Analysis/Network Scan).

### Kế hoạch tuần này (Cụ thể, có thể làm ngay)
| Thứ | Focus | Deliverable | Tránh |
| :--- | :--- | :--- | :--- |
| **2** | **System Design Depth** | Viết xong **1 ADR** cho module phức tạp nhất dự án hiện tại (VD: Migration Monolith → Modular Monolith). Review với Senior/Lead. | Đọc sách passively, không viết tài liệu. |
| **3** | **Python + AI Agent (MCP)** | Setup **FastAPI + LangGraph** local. Tạo 1 Tool: `scan_java_dependencies` (dùng `cyclonedx`/`owasp-dep-check` output) ➜ LLM tóm tắt CVE critical. Expose qua **MCP Server**. | Copy code tutorial không hiểu lifecycle (State, Checkpoint, Tool Call). |
| **4** | **Network Security Lab** | Chạy **Wireshark/Zeek** trên VM. Capture traffic của Spring Boot app gọi DB. Viết script Python (Scapy/pyshark) detect: *Plaintext password, Unencrypted JDBC, Strange IP*. | Chỉ đọc lý thuyết TCP/IP, không bắt gói tin thật. |
| **5** | **Career "Slope" Audit** | Lập bảng: *Kỹ năng đã có (Java, SQL, Spring)* vs *Kỹ năng cần có 1 năm sau (K8s, eBPF, Agent Design, System Design)*. Chọn **1 gap** lớn nhất ➜ Làm side project cover gap đó. | Apply lung tung JD Senior/Lead khi mới 1-2 năm exp. |
| **6-7** | **Rest & Synthesize** | Viết **Bài blog/Note nội bộ** tóm tắt: "Tôi build AI Agent scan security cho Spring Boot app như thế nào". Đẩy GitHub (Public/Private). | Burnout. Không có output hữu hình. |

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT (Top Insight Score)

### 1. @SyberSmoke – Video *"Why your first dev job is getting harder to land"* (Insight: 4.5)
> **Trích dẫn đầy đủ:**
> *"The answer is simple, and it is an answer that IBM actually said months ago. 'The sr. technicians and programmers of the future stars as the entry level workers of today. So being short sighted and cutting out entry level only creates problems later.' But many business's can not see past their next quarter no less ten or twenty years down the line so...I am thinking about getting into wood working."*
> **Nguồn:** [YouTube Link](https://www.youtube.com/watch?v=V8vt9nZ-IX0) | Votes: 0 (Insight score hệ thống: 4.5)
> **Tại sao đọc:** **Cảnh báo cấu trúc thị trường lao động.** IBM (người khổng lồ enterprise) công khai nhận việc cắt Junior = tự sát pipeline Senior 10 năm sau. Điều này giải thích tại sao *hiện tại* khó xin việc cực độ: các công ty đang tối ưu ngắn hạn (quarterly earnings) chấp nhận rủi ro dài hạn. **Dev Junior hiểu được này sẽ không tự ti, mà tập trung build portfolio "giả lập kinh nghiệm Senior" (side project phức tạp, open source contribution) để bù đắp khoảng trống.**

### 2. @nicky_s – Video *"Phân tích 149,360 việc làm IT Việt Nam"* (Insight: 1.0 - *Giá trị thực tế cao nhất*)
> **Trích dẫn đầy đủ:**
> *"Thực sự hôm nay em bị từ chối ngay trong phỏng vấn, sốc và thất vọng về bản thân thực sự anh ạ. Đã rất lâu rồi chưa có việc làm, sống bám vào bố mẹ xấu hổ quá"*
> **Nguồn:** [YouTube Link](https://www.youtube.com/watch?v=gRSzxR2CAIY) | Votes: 5
> **Tại sao đọc:** **Ground truth (Thực trạng mặt đất) của Fresher/Junior VN 2026.** Con số 149k job posting là *macro*, comment này là *micro* – nỗi đau thực của người đang trong luồng. Nhắc nhở: **Dữ liệu macro không cứu được cá nhân.** Cần hành động micro: mock interview, review CV bởi senior, apply referral, side project có demo live.

### 3. @TranSonPhat (Author) – Video *"Phân tích 149,360 việc làm IT Việt Nam"* (Insight: 2.0)
> **Trích dẫn đầy đủ:**
> *"Toàn bộ code phân tích và dữ liệu của video nằm ở đây nha: Trong repo có pipeline xử lý, các notebook phân tích và bộ số liệu tổng hợp theo từng năm (vai trò, cấp bậc, thành phố, hình thức làm việc và công nghệ), các bạn có thể tải về để tự vẽ lại biểu đồ hoặc phân tích thêm nha!"*
> **Nguồn:** [YouTube Link](https://www.youtube.com/watch?v=gRSzxR2CAIY) | Votes: 3
> **Tại sao đọc:** **Tính minh bạch & khả năng tự phân tích.** Tác giả chia sẻ full pipeline (code + data). Đây là **skill Portfolio điển hình**: Data Engineering + Domain Knowledge (IT Job Market). Dev VN nên clone repo, chạy lại, thêm feature (VD: Predict salary cho stack Java+Python+Security tại HN/HCM) ➜ Đẩy GitHub ➜ Talking point phỏng vấn cực mạnh.

### 4. @diego4195 – Video *"Did the AI bubble just pop?"* (Fireship) (Insight: 2.5)
> **Trích dẫn đầy đủ:**
> *"Remember: If the headline/title is a question instead of a statement, the answer is 'no'."*
> **Nguồn:** [YouTube Link](https://www.youtube.com/watch?v=nEaJMdM1djM) | Votes: 6,864
> **Tại sao đọc:** **Media Literacy cho Dev.** Betteridge's Law of Headlines. 90% video/bài viết "AI replace dev?", "Bubble pop?" chỉ là clickbait. **Dev nên tập trung vào *tooling thật* (MCP, RAG, Agent Framework) thay vì lo lắng về *headline*.**

### 5. @yourytking – Video *"Optimize For Slope, Not Salary"* (Insight: 0.0 - *Nhưng resonates cao*)
> **Trích dẫn:** *"I agree with this. I am trying to do this now. I feel pigeon holed."*
> **Nguồn:** [YouTube Link](https://www.youtube.com/watch?v=IOhRr-C2y6o)
> **Tại sao đọc:** Từ khóa **"Pigeon holed" (Bị g bó vào một hốc)**. Nhiều dev Java 3-5 năm chỉ biết Spring Boot CRUD, không biết K8s, không biết System Design, không biết AI. Bình luận này là tiếng nói của đông đảo "Mid-level trapped". Xác nhận tư duy **"Optimize for Slope"** là đúng và gấp.

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY (Ưu tiên Expert Voice & VN Context)

| # | Nguồn | Loại/Khu vực | Luận điểm chính & Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[VN] Phân tích 149,360 việc làm IT Việt Nam 2021-2026** (Học Lập Trình cùng Phát) | Video / Data Analysis | **Dữ liệu thô duy nhất quy mô lớn về VN.** Xu hướng: Java/Spring vẫn top 1 backend nhưng *growth* xuống; Python/AI/Cloud lên mạnh; Junior < 5% tin tuyển; Gia công sụt giảm. **Repo open source** (comment tác giả). | **Cơ sở dữ liệu chính thức cho mọi quyết định học tập/apple ở VN.** Expert voice: Data-driven, không phán đoán chủ quan. |
| **2** | **[GLOBAL] Why You're Not Getting Hired: The Hidden Truth** (The Seasoned CTO) | Video / Hiring Strategy | **Job Posting ≠ Hiring.** "Ghost postings" nhiều. Hiring manager ưu tiên **System Architecture & Quality** hơn quantity. AI Engineer mindset (chỉ prompt) không đủ, cần hiểu hệ thống. | **Expert Voice Score 3.0 (CTO level).** Giải mã "tại sao apply nhiều mà không rep" – giúp dev VN đổi chiến thuật apply. |
| **3** | **[GLOBAL] Optimize For Slope, Not Salary - Day 26** (John Kim) | Video / Career Strategy | **Long-term compounding > Short-term cash.** Ở lại 3+ năm để chịu "hard problems" và xây "trust". Job hopping lần-lục khiến stall ở Senior. | **Tư duy cốt lõi cho Dev 1-5 năm exp.** Áp dụng ngay cho background Java: chọn project/module khó nhất để "gặm" 2-3 năm. |
| **4** | **[GLOBAL] Software Engineer Salary: New Grads vs Senior Engineers** (HowMuchSalaryUS) | Video / Market Data | **Median $136k (Senior) vs Fresher near 0 hire.** Phân hóa cực đoan. Chi phí sống cao ăn mòn lương. | **Expert Voice Score 7.5 (Data authority).** Benchmark thực tế cho Dev VN định hướng remote/relocate: mục tiêu là đạt level Senior US-standard (System Design, English, Architecture). |
| **5** | **[GLOBAL] Why Are Software Engineers Getting Laid Off?** (The Signal Tech) | Video / Macro Analysis | Layoff = **Overhiring + Restructuring + AI Investment** (không chỉ AI replace). Junior bị ảnh hưởng nặng nhất do "productivity bar" nâng cao. | **Phân tích khách quan, tách biệt narrative.** Giúp dev VN hiểu: Layoff không có nghĩa là "hết việc", mà là "yêu cầu skill cao hơn". |
| **6** | **[VN] Microsoft mở văn phòng mới TP.HCM sau sa thải** (VnExpress/Google News) | News / Market Signal | Big Tech **mở rộng** tại VN *sau* layoff global ➜ VN vẫn là **Strategic Hub** (Chi phí thấp, Talent tốt). Nhưng tuyển **Senior/Specialized** (AI, Cloud, Security). | **Tín hiệu macro quan trọng.** Khẳng định: Nên đầu tư skill "Specialized" (Security, AI Infra, K8s) để hớp wave tuyển dụng Big Tech tại VN. |

> **English reference (The Seasoned CTO):**
> > *"The tech job market is sending mixed signals as software developer job postings rise while actual hiring numbers shrink. We examine the contradiction between public data and internal headcount reality, where teams are authorized for far fewer roles than the raw numbers suggest. Even if you are an expert in artificial intelligence, you need to understand that learning remains a critical factor for entry-level success... software architecture knowledge helps you stand out when hiring managers are prioritizing quality over quantity."*

> **English reference (John Kim):**
> > *"Optimize for learning instead: the more learning opportunities you have, the more your career's long-term output grows, and it gets exponential. Engineers who jump jobs every year or two for small raises often stall at senior or staff, because the really hard problems and the trust to lead them usually come about three years into a job."*

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*(Bỏ qua: Không có mục dữ liệu nào có `is_major_incident: true`)*