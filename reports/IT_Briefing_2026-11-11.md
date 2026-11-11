📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.bfd50cm4mdpe)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Thị trường "bình thường hóa" sau bong bóng 2021-2022**: Phân tích 149.360 tin tuyển dụng (2021-10/2026) cho thấy cầu Java, Python, JavaScript vẫn lớn nhất nhưng **tuyển Junior/Fresher cực kỳ khắt khe**, cửa vào hẹp lại rõ rệt so với giai đoạn bùng nổ. Video "Lập trình viên năm 2026" xác nhận: "Cung vượt xa cầu", tiêu chuẩn tuyển dụng nâng cao, lương trung bình có dấu hiệu điều chỉnh xuống.
- **Gia công phần mềm (Outsourcing) chịu áp lực AI lớn**: Khách hàng quốc tế tự build nội bộ nhờ AI hoặc yêu cầu vendor dùng AI để giảm giá/giờ nhân công. Dev ở VN không chỉ "làm theo spec" mà phải biết **tích hợp AI vào quy trình delivery** để giữ 경쟁 lực.
- **Cầu AI/ML/Data tăng vọt nhưng đòi hỏi seniority**: Dữ liệu từ Phát (YouTube) và Tin tức VnEconomy/Vietnam.vn đều đồng thanh: vị trí AI tăng nhanh, tuy nhiên đa số yêu cầu kinh nghiệm thực chiến (productionize model, RAG, Agent), không tuyển freshers "chỉ biết train model".
- **Đặc thôn: DevOps/Cloud không tự động trả lương cao hơn Backend**: Bình luận `@lethanhhung7549` trên video Phát bộc lộ tâm lý sai lầm phổ biến. Dữ liệu thực tế cho thấy lương phụ thuộc vào **độ phức tạp bài toán & ownership**, không phải tên vị trí.

### Trên thế giới (và ý nghĩa với Việt Nam)
- **40% Pull Requests trên GitHub bắt đầu bằng draft của AI** (Synthetic Era). **Ý nghĩa VN**: Quy trình dev tại VN *bắt buộc* chuẩn hóa "AI-assisted workflow" (Cursor, Claude Code, Copilot, MCP). Dev không dùng AI là chậm, dev chỉ copy-paste AI không review là nguy hiểm.
- **Job postings giảm 65% so với đỉnh 2022** (Synthetic Era). **Ý nghĩa VN**: Đừng so sánh market hiện tại với "thời vàng 2022". Chuẩn bị cho market "chôn vun": ít HC, phỏng vấn sâu (System Design, Behavioral, Domain), probation khắt khe.
- **Nút thắt cổ chai dịch chuyển từ "Viết code" sang "Review & Kiến trúc"**: Median PR review time tăng **441%** (Synthetic Era). **Ý nghĩa VN**: Kỹ năng **đọc hiểu code người khác (và code AI sinh), thiết kế hệ thống, viết test, bảo mật** bây giờ giá trị hơn speed coding.
- **Sa thải do "Overhiring + Restructuring + AI Efficiency", không phải AI thay thế hoàn toàn** (The Signal Tech). **Ý nghĩa VN**: Công ty VN đang "thanh lọc" nhân sự low-performer. Dev muốn trụ vững phải chứng minh **hiệu suất đầu ra (outcome) + khả năng thích ứng (adaptability)**.
- **Góc nhìn Expert (Senior Eng/Manager/Director AI - exit node, Expert Score 1.5)**: "AI làm code rẻ, nhưng không làm software dễ dàng". Survival kit: **Tìm việc ngầm, xây dựng đồng minh cross-team, làm việc visible (chạy training, present), manage sếp lên**.
- **Góc nhìn Expert Investment Banking (Saji @Nomura, 7+ yrs, Expert Score 7.5 - Bosscoder)**: Ở high-stakes industry, **Domain Knowledge (Finance) + Reliability + Adaptability** quan trọng hơn stack công nghệ. "Stay relevant by solving harder problems, not just newer frameworks".

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cần học (Có nguồn dẫn chứng)
| Kỹ năng | Vì sao quan trọng | Nguồn/Bình luận |
| :--- | :--- | :--- |
| **AI-Assisted Development & Agentic Workflow (MCP, Tool Calling)** | AI viết code, dev đóng vai Architect/Orchestrator. MCP (Model Context Protocol) là chuẩn kết nối Agent với Tool/Data thực tế. | **EditAtlas (J2Team, Relevance 64.6)**: MCP Server thực tế cho Video Editing (2000+ techniques, sound design). **Dev.to**: "AI Agents Need a Runtime, Not Another Framework", "UCP Explained". |
| **Code Review & System Design (Kiến trúc)** | Bottleneck toàn cầu đang ở Review (+441% time). Junior phải nghĩ level System Design ngay từ đầu. | **Synthetic Era (Video)**: Data PR review. **@oussamaelwefi2940 (Comment Insight 2.0)**: "Even as a junior I need high level look... learn system design/architecture more". |
| **Security Engineering & Supply Chain Hardening** | Sự cố thực tế: Claude Code leak 1.100 repo (API key), WorkOS AI Agent tự hành bypass sandbox. Security không còn là team riêng. | **J2Team Morning News (Incident Severity 4.0)**: Cảnh báo config leak, AI Agent rogue. **Persona context**: Bạn đang học Network Security - đây là đòn bẩy. |
| **Domain Knowledge (Chọn 1: FinTech / AI Infra / E-com / Security)** | Chuyên môn hóa domain để AI không thay thế được business logic phức tạp. | **Saji @Nomura (Expert Score 7.5)**: "Key skills needed to thrive in high-stakes industries like investment banking". **Exit node**: "Make work visible... talk to senior people". |
| **Communication & Visibility (Soft Skill cứng)** | Làm việc remote/hybrid, AI làm mờ ranh giới contribution. Phải tự marketing nội bộ. | **Exit node (Expert Voice 1.5)**: "Build friendships outside team", "Run a training, present what you learned". |

### Công nghệ cần học (Phân biệt Xu hướng thật vs Hype)
| Công nghệ | Trạng thái | Ghi chú cho bạn (Java/Spring Boot -> Python/NetSec) |
| :--- | :--- | :--- |
| **Python (Advanced: Async, FastAPI, Data Classes, Type Hinting)** | **Xu hướng thật, BẮT BUỘC** | Ngôn ngữ chung cho AI, Security Tooling, Automation. Viết MCP Server, Security Scanner, Agent Tool bằng Python. |
| **MCP (Model Context Protocol) / FastMCP** | **Xu hướng thật (Emerging Standard)** | Chuẩn hóa cách Agent gọi tool. Học để build *custom tools* cho AI (vd: tool scan CVE, tool query DB Spring Boot). |
| **Go / Rust** | **Xu hướng thật (Infra/Performance)** | Dùng cho agent runtime, sidecar proxy, high-perf security tools. Học sơ qua để đọc hiểu source code tool (vd: TruffleHog, Gitleaks viết bằng Go). |
| **Kubernetes / Docker / Linux Internals** | **Xu hướng thật (Chạy AI Agent/Workload)** | Phát video: DevOps/Cloud cầu cao. Cần hiểu container escape, network policy, eBPF cho Security. |
| **React / Next.js (Basic Fullstack)** | **Xu hướng thật (Market demand)** | Phát video: FE/FE-Heavy demand lớn. Dev Java biết FE tự build dashboard monitoring/security tool. |
| **Leetcode Grind (Heavy)** | **Hype / Chỉ phục vụ Interview** | **@oussamaelwefi2940 (Insight 2.0)**: "Leetcode... obviously are if job test it... but other motivators?" -> Chỉ luyện đủ pass loop, tập trung vào System Design & Project thực tế. |
| **Prompt Engineering "Vibe Coding" thuần túy** | **Hype / Nguy hiểm** | **PhD user (Lemmy)**: "Vibe coding swallowed roles... pushing button instead of thinking". Không học prompt mà quên fundamental. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy cốt lõi (Từ cộng đồng & Expert)
1.  **Từ "Task Executor" → "AI Orchestrator & Reviewer"**: Đừng tự gõ code CRUD. Dùng AI gen boilerplate, bạn tập trung: **Review logic, Edge case, Security flaw, Performance, Test coverage**.
2.  **Từ "Stack Specialist" → "Domain Problem Solver"**: Java/Spring Boot là tool. Hiểu sâu **Business Domain** (vd: Payment, KYC, Fraud Detection, Network Traffic Analysis) mới là giá trị cốt lõi.
3.  **Security by Default, không phải Afterthought**: Sự cố Claude Code leak config, WorkOS AI Agent rogue chứng minh: **Secret Management, Sandboxing, Audit Trail, Least Privilege** phải có trong *mọi* dòng code/config bạn chạm.
4.  **Visibility = Job Security**: "Make work visible beyond your team" (Exit node). Viết blog tech, share internal tool, present bài học fail/success. Xây dựng "Personal Brand" nội bộ & cộng đồng (J2Team, Viblo, LinkedIn).

### Kế hoạch hành động TUẦN NÀY (Cho Dev Java/Spring Boot -> Python/NetSec)
| Hành động | Mục tiêu | Output kỳ vọng |
| :--- | :--- | :--- |
| **1. Build 1 MCP Server nhỏ bằng Python (FastMCP)** | Học Python + AI Agent Protocol + Security Tooling cùng lúc. | Tool: `scan-dependencies` (quét CVE cho `pom.xml`/`build.gradle`), `check-network-policy` (kiểm tra K8s NetworkPolicy). Push GitHub, viết README chuẩn (theo Dev.to: "Your README Is the Interview"). |
| **2. Cài đặt & Tune Secret Scanning cho Project Java hiện tại** | Áp dụng bài học sự cố Claude Code leak ngay. | Cấu hình `Gitleaks`/`TruffleHog` pre-commit hook + GitHub Action. Viết quy trình "Rotate Key trong 15 phút" (Runbook). |
| **3. Ôn tập System Design: Thiết kế lại Module Authentication/Authorization của Project Java** | Chuyển tư duy từ Code sang Architecture. | Vẽ diagram (Mermaid/PlantUML): Sequence diagram OAuth2/JWT, Threat Modeling (STRIDE) cho Auth flow. Đưa vào portfolio/Notion. |
| **4. Viết 1 bài "TIL (Today I Learned)" hoặc Blog ngắn về: "Từ Java Dev học Python viết MCP Server cho Security Audit"** | Visibility & Personal Brand. | Đăng Viblo/LinkedIn/J2Team Community. Tag #java #python #mcp #security #career. |
| **TRÁNH**: Làm Leetcode > 1h/ngày; Học framework Python mới (Django/FastAPI) không qua project thực; Apply job mass không customize CV cho domain. | | |

> **English Reference**: "The bottleneck didn't vanish. It moved." (Synthetic Era); "Experienced developers believed AI made them 20% faster — and actually took 19% longer." (Synthetic Era); "Make your work visible beyond your team: run a training, present what you learned..." (exit node); "Key skills needed to thrive in high-stakes industries like investment banking." (Bosscoder Academy).

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

1.  **@charlieJimi** (Video: *"When Work Sucks and AI Doom Won't Shut Up" - exit node*, **Insight Score: 3.5**, Votes: 1)
    > "Hey Chavdar, definitely.. I am on the same page with you. Looks like the home lab can be turned into a side business upon see interestig and fun use cases!"
    > **Tại sao đáng đọc**: Tác giả video là **Senior Eng/Manager/Director of AI (Expert Voice 1.5)**. Bình luận này khẳng định tư duy **"Builder Mindset"**: Home lab/Side project không chỉ để học mà là MVP cho side business/tăng visibility. Phù hợp hoàn toàn với lộ trình "Java -> Python/NetSec build tool".

2.  **@oussamaelwefi2940** (Video: *"When Work Sucks and AI Doom Won't Shut Up" - exit node*, **Insight Score: 2.0**, Votes: 1)
    > "Thank you for the video, I now understand that even as a junior I need to have a high level look at things, and learn the system design / architecture more, but I also feel that I need to keep my problem solving skills sharp, what do you think about doing leetcode problems? are they still important? they obviously are if the job I apply for test it in the technical interview, but are there other motivators to do it?"
    > **Tại sao đáng đọc**: **Junior thực tế đang đau đầu** giữa System Design vs Leetcode. Câu hỏi chạm đúng "nỗi đau" market hiện tại: Leetcode chỉ để pass interview, **System Design/Architecture mới là skill trụ vững**. Trả lời gợi ý: Dùng Leetcode để luyện *problem solving pattern*, nhưng portfolio phải có *System Design docs*.

3.  **@TranSonPhat (Tác giả video)** (Video: *"Phân tích 149,360 việc làm IT Việt Nam từ 2021-2026" - Học Lập Trình cùng Phát*, **Insight Score: 2.0**, Votes: 2)
    > "Toàn bộ code phân tích và dữ liệu của video nằm ở đây nha: Trong repo có pipeline xử lý, các notebook phân tích và bộ số liệu tổng hợp theo từng năm (vai trò, cấp bậc, thành phố, hình thức làm việc và công nghệ), các bạn có thể tải về để tự vẽ lại biểu đồ hoặc phân tích thêm nha! Cảm ơn các bạn rất nhiều!"
    > **Tại sao đáng đọc**: **Data-driven decision making**. Thay vì tin cảm tính "Java chán", "Python hot", dev VN có thể **tự query dữ liệu 149k JD** để ra quyết định: Học gì? Ở đâu? Lương bao nhiêu? Đây là skill "Data Literacy" bắt buộc.

4.  **@nicky_s** (Video: *"Phân tích 149,360 việc làm IT Việt Nam từ 2021-2026" - Học Lập Trình cùng Phát*, **Insight Score: 1.0**, Votes: 3)
    > "Thực sự hôm nay em bị từ chối ngay trong phỏng vấn, sốc và thất vọng về bản thân thực sự anh ạ. Đã rất lâu rồi chưa có việc làm, sống bám vào bố mẹ xấu hổ quá"
    > **Tại sao đáng đọc**: **Thực trạng khốc liệt của Junior/Fresher VN 2026**. Không phải số liệu, là con người. Cảnh báo: Market Junior gần như đóng băng. Người mới *bắt buộc* có project thực tế (open source, freelance, side biz) + skill AI/Security để khác biệt.

5.  **@lethanhhung7549** (Video: *"Phân tích 149,360 việc làm IT Việt Nam từ 2021-2026" - Học Lập Trình cùng Phát*, **Insight Score: 0.0**, Votes: 0)
    > "em sinh viên. cứ ngỡ devops, cloud lương phải cao hơn backend chứ😅"
    > **Tại sao đáng đọc**: **Sai lầm nhận định thị trường phổ biến**. Dữ liệu video Phát cho thấy lương trung vị DevOps/Cloud không tự động cao hơn Backend Java/Go senior. Nhắc nhở: **Đừng theo trend tên vị trí, hãy theo trend "bài toán phức tạp + ownership"**.

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| Nguồn | Loại / Vùng | Luận điểm chính & Góc nhìn nổi bật | Lý do chọn |
| :--- | :--- | :--- | :--- |
| **1. [VN] Video: "Phân tích 149,360 việc làm IT Việt Nam 2021-2026"** (Học Lập Trình cùng Phát) <br>🔗 `youtube.com/watch?v=gRSzxR2CAIY` | Video / VN | **Data-driven market report**: Java/Python/JS top demand. AI jobs tăng 300%+ nhưng yêu cầu exp. Junior < 5% cơ hội. Lương theo cấp bậc/thành phố. **Highlight**: Tác giả **open source toàn bộ pipeline & data (Repo GitHub)**. | **Nguồn VN chính xác, toàn diện nhất** để định hướng stack, địa điểm, mức lương thực tế. Dữ liệu thô cho phép tự phân tích. |
| **2. [Quốc tế] Video: "Is Coding Dead? What the 2026 Hiring Data Actually Shows"** (Synthetic Era) <br>🔗 `youtube.com/watch?v=HbhJUuW8ysM` | Video / GLOBAL | **Macro data**: 40% PRs AI-generated, Job post -65% vs 2022, Review time +441%. **Insight**: "Cheap code != Easy software". Bottleneck ở Architecture/Review/Integration. | **Chứng minh bằng số liệu toàn cầu** cho xu hướng "AI thay đổi bản chất việc làm dev". Áp dụng VN: Đầu tư vào Review/Arch skill. |
| **3. [Quốc tế] Video: "When Work Sucks and AI Doom Won't Shut Up"** (exit node) <br>🔗 `youtube.com/watch?v=yBPayq0_3N4` | Video / GLOBAL | **Expert Voice (Senior Eng/Manager/Director AI, Score 1.5)**: Survival kit thực chiến: Job search ngầm, Build allies cross-team, Manage up, Visibility. **Top Comment**: Junior cần System Design, Home lab -> Side biz. | **Góc nhìn quản lý/kiến trúc cấp cao** hiếm có. Hành động cụ thể cho dev đang stress/burnout/mất định hướng. |
| **4. [VN] Facebook Post: "EditAtlas - Thư viện kỹ thuật dựng video cho AI agent"** (J2TEAM Community) <br>🔗 `facebook.com/groups/j2team.community/permalink/3241555699509861/` | Community Post / VN | **Case Study MCP Server sản xuất**: 2000+ techniques, sound design, video breakdown, stock media. 3 skill local: sound-design, video-breakdown, transcribe. Chạy trên Cloudflare Workers. | **Relevance Score cao nhất (64.6)**. Demo **thực tế "Agentic Workflow" dev VN có thể build ngay hôm nay bằng Python**. Học 묻 đi kèm làm. |
| **5. [Quốc tế] Video: "Bosscoder's Evolve Program... Senior SWE @Nomura"** (Bosscoder Academy) <br>🔗 `youtube.com/watch?v=9Dfiq0Pyxh0` | Video / GLOBAL | **Expert Voice Score 7.5 (Cao nhất dataset)**: Saji - Senior SWE 7+ năm Investment Banking (Ngành dùng Java/Spring Boot nhiều). Key: **Adaptability, Domain Knowledge (Finance), High-stakes Reliability**. | **Role model trực tiếp cho bạn (Java/Spring Boot)**. Chứng minh con đường Senior/Lead ở domain khó (FinTech) cần gì ngoài code. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào với `is_major_incident = true` trong bộ dữ liệu cung cấp. Mục này được bỏ qua theo quy định.*