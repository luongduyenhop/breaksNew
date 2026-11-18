📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.nnukvca75cun)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
1.  **AI Agent đang thay đổi bản chất công việc dev: từ "viết code" sang "thiết kế hệ thống & vận hành AI"**.  
    Video *No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?* (Tips Javascript) và bình luận top của **@phutran-z6h (insight 12.0)** khẳng định: AI đã làm được 95-98% việc code, test, security, UI/UX. Lập trình viên không còn là người "chia task, chia role" mà phải hiểu **business + hệ thống toàn cục + kỹ năng làm việc với người**.  
    *Nguồn: [YouTube VN](https://www.youtube.com/watch?v=gxIKlsOzq70), comment @phutran-z6h.*

2.  **Thị trường tuyển dụng "bình ổn nhưng khó hơn": Junior/Fresher bị ép KPI, Senior được săn đón.**  
    Video *Ngành lập trình và IT năm 2026 ảm đạm ra sao??* (Tôi Đi Code Dạo) chỉ ra: AI Agent bùng nổ, StackOverflow "chết", Junior bi kịch vì AI làm thay việc code cơ bản. Video *AI có thật sự thay thế lập trình viên?* (Tip - Cntt) dẫn số liệu: Google 75% code mới do AI tạo, nhưng vị trí tuyển kỹ sư **tăng 30% năm 2026** → cầu vọt về chất lượng, không phải số lượng.  
    *Nguồn: [YouTube VN](https://www.youtube.com/watch?v=mOaakWt7txY), [YouTube VN](https://www.youtube.com/watch?v=LUp-gxnxmcU).*

3.  **Công ty Việt bắt đầu triển khai AI Agent quy mô lớn, nhưng nhiều nơi "thêm agent vào quy trình lỗi" → không tăng velocity.**  
    Bài chia sẻ tại **Vietnam Java User Group** (JetBrains case study 9 công ty): Fin thành lập team chuyên trách (Team 2x) build infra cho agent (shared skills, MCP servers, backtest review code) mới thấy hiệu quả. Chỉ "đưa AI vào" không đủ, phải **tái thiết quy trình engineering**.  
    *Nguồn: [Facebook VN](https://facebook.com/groups/vnjug/permalink/2593623114396326/).*

### Trên thế giới (và ý nghĩa với Việt Nam)
1.  **AI không sa thải người, AI "thầm lặng không tuyển người mới"** → Cánh cửa vào nghề hẹp lại mạnh mẽ cho Gen Z (22-25 tuổi).  
    Video *AI Isn't Firing People. It's Quietly Not Hiring Them.* (Kilobrief) trích Goldman Sachs/Stanford: tỷ lệ việc làm nhóm 22-25 tuổi ở job bị AI tác động cao **giảm 19%** so với dự báo.  
    → *Với dev VN: Fresher/Junior phải có **portfolio thực tế + khả năng dùng AI production-grade** ngay từ đầu, không chỉ biết DSA/LeetCode.*  
    *Nguồn: [YouTube Global](https://www.youtube.com/watch?v=o5souAFfjbo).*

2.  **Vai trò mới nổi: Forward Deployed Engineer (FDE) – cầu nối giữa AI, Product, Business, Consulting.**  
    Video *₹50 LPA AI Job | The Next Big AI Career in 2026?* (Elamparithi) mô tả FDE: hiểu business problem, làm việc với AI tech, build customized solution. Lương cao (50 LPA ~ 60k USD/năm ở Ấn Độ, tương đương Senior/Lead tại VN).  
    → *Với dev VN: Đây là hướng chuyển dịch tự nhiên cho Senior/Tech Lead muốn sang AI mà không thành "AI Researcher". Cần bổ sung: Product sense, Client-facing, RAG/Agent orchestration.*  
    *Nguồn: [YouTube Global](https://www.youtube.com/watch?v=DC6YqZErQcU).*

3.  **Hạ tầng DevTool phải tiến hóa cho tốc độ AI: Anthropic tự build VCS "Scion" thay Git vì merge 30k changes/ngày.**  
    Bài *Anthropic vừa bỏ Git, tự build VCS mới tên Scion* (J2TEAM Community): Git distributed không scale cho volume code AI sinh ra (tăng 12x trong 4 tháng). Scion dùng client-server, commit/merge/rebase chạy trên server.  
    → *Với dev VN: Kỹ năng **Platform Engineering, Developer Experience (DevEx), Build/Release automation** đang trở nên cực kỳ đắt giá. Các công ty VN làm product/outsource quy mô lớn sẽ cần người build internal tooling cho AI workflow.*  
    *Nguồn: [Facebook VN](https://facebook.com/groups/j2team.community/permalink/3250611268604304/).*

4.  **Con đường thăng tiến tách rõ: Engineering Manager vs Staff Engineer – cả hai track đều ngang ngửa lương, khác nhau ở "impact through people" vs "impact through technology".**  
    Video *Engineering Manager vs Staff Engineer* (Nidhi Sharma – ex-Head of AI Innovation UK) chia sẻ framework 4 câu hỏi để chọn.  
    → *Với dev VN: Đừng mặc định "trưởng nhóm = quản lý". Nhiều công ty VN (FPT, VNG, các startup scale-up) đang xây dual-track. Hãy chọn theo năng lực soft-skill vs deep-tech.*  
    *Nguồn: [YouTube Global](https://www.youtube.com/watch?v=zbTpIHsTaeg).*

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cứng (Hard Skills) – Ưu tiên theo thứ tự
| Kỹ năng | Tại sao quan trọng (từ dữ liệu) | Nguồn/minh chứng |
|---------|--------------------------------|------------------|
| **AI Agent Orchestration / RAG / Vector DB** | Backend 5 năm hỏi có nên chuyển AI Engineer; comment @duythanh1602 (insight 3.5) & video Vector Databases (Tips Javascript) chỉ ra đây là bướcupgrade từ BE → AI Eng. | [YouTube VN](https://www.youtube.com/watch?v=kRXoK02KJow), comment @duythanh1602 |
| **System Design & Architecture (không chỉ vẽ diagram, mà trade-off thực tế)** | @phutran-z6h (insight 12.0): "AE tìm hiểu nghiệp vụ của cả hệ thống... kĩ năng đó hình thành từ nhiều năm". AI làm code, dev lo architecture. | [YouTube VN](https://www.youtube.com/watch?v=gxIKlsOzq70), comment @phutran-z6h |
| **Platform Engineering / DevEx / CI-CD Automation at scale** | Anthropic build Scion VCS, CI checkout 25M lần/ngày → cần engineer build tooling cho AI workflow. | [Facebook VN](https://facebook.com/groups/j2team.community/permalink/3250611268604304/) |
| **Security: Idempotency, Retry-safe execution, Reconciliation** | Dev.to article "Your AI Agent Retried... First One Had Succeeded": AI agent gây duplicate charge → dev phải thiết kế idempotency key, stable operation ID. | [Dev.to Global](https://dev.to/rudratosh/your-ai-agent-retried-the-tool-call-the-first-one-had-already-succeeded-3pke) |
| **Forward Deployed Engineering skills: Product sense, Client communication, Business analysis** | Video FDE (Elamparithi): FDE = SE + AI + PM + Consulting. Cần hiểu business problem trước khi code. | [YouTube Global](https://www.youtube.com/watch?v=DC6YqZErQcU) |

### Công nghệ cụ thể (Stack) – Phân biệt Xu hướng thật vs Hype
| Công nghệ | Đánh giá | Lý do |
|-----------|----------|-------|
| **Python (FastAPI/Django) + LangChain/LlamaIndex/Semantic Kernel** | **Xu hướng thật** | RAG, Agent orchestration đều dùng Python ecosystem. Video Vector DB, bài Dev.to agent-memory-mesh đều demo Python. |
| **Vector Databases: Qdrant, Milvus, Pinecone, MongoDB Vector Search** | **Xu hướng thật** | Comment @vantran_devopsinfra (insight 2.0) mô tả quy trình RAG production dùng BGE-m3 + Mongo Vector Search. |
| **Git / Scion-like VCS concepts / Monorepo tooling (Bazel, Nx, Turborepo)** | **Xu hướng thật** | Anthropic bỏ Git vì scale. Kiến thức monorepo, CI optimization bắt buộc cho team dùng AI coding nặng. |
| **Kubernetes / Infrastructure as Code (Terraform, Pulumi)** | **Xu hướng thật** | Platform Engineering cần triển khai agent runtime, GPU inference, observability. |
| **No-code/Low-code AI builders (n8n, Dify, Coze)** | **Cẩn trọng – Hype cho non-tech** | Dành cho PM/Business. Dev nên biết để *tích hợp/extends* chứ không phải *dùng thay code*. |
| **Rust/Go cho high-performance AI infra** | **Niche – Chỉ cho Platform/Infra team** | Chưa phải mainstream cho app dev VN. Ưu tiên sau khi nắm vững Python/Architecture. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy cốt lõi (từ cộng đồng VN)
1.  **Từ "Làm taskassigned" → "Hiểu Business + Hệ thống end-to-end"**.  
    @phutran-z6h: *"Chuyện lập trình viên ko cần code là chuyện trước mặt rồi... ae nên tập trung vào việc hiểu business + hệ thống + kĩ năng làm việc với mọi người xung quanh."*  
    → **Hành động:** Mỗi ticket Jira, hãy hỏi: "Feature này giải quyết problem gì của user? Tác động lên module nào khác? Metric thành công là gì?"

2.  **Từ "Sợ AI thay thế" → "Dùng AI như Senior Engineer dùng Junior"**.  
    Video *Tôi Đi Code Dạo*: *"Đừng ghét AI, hãy tận dụng AI để làm việc nhàn hơn, lương cao hơn"*.  
    → **Hành động:** Mỗi ngày setup workflow: **Spec → Prompt → Review → Test → Commit**. Đừng "vibe coding" tùy hứng (video Hỏi Dân IT nhấn mạnh Git workflow an toàn).

3.  **Từ "Chuyên sâu 1 stack" → "T-shaped: Deep Backend + Broad AI/Infra/Product"**.  
    Nidhi Sharma (Engineering Manager/Head of AI): Staff Engineer cần *broad technical influence*, EM cần *people + business*.  
    → **Hành động:** Chọn 1 deep (Java/Spring Boot), mở rộng 2 broad: **AI Agent/RAG** + **System Design/Platform**.

### Áp dụng cụ thể cho Dev nền Java/Spring Boot đang học Python + Network Security
| Tuần này nên làm gì | Tránh gì |
|----------------------|----------|
| **1. Build một mini RAG system dùng Spring Boot (backend) + Python/FastAPI (AI service) + Qdrant/Milvus.** Xử lý PDF tài liệu nội bộ, trả lời câu hỏi. Triển khai Docker Compose. | Chỉ đọc tutorial không chạy được production. Không có CI/CD, không có logging/monitoring. |
| **2. Học Python `asyncio`, `httpx`, `pydantic`, `langchain-core` (không dùng high-level chain ngay).** Viết custom retry logic với **idempotency key** (bài học từ Dev.to duplicate charge). | Dùng `langchain` high-level abstract mà không hiểu luồng data chảy như thế nào. |
| **3. Ôn System Design: Thiết kế hệ thống "AI Code Review Bot" cho team Java.** Yêu cầu: nhận PR webhook, phân tích diff, gọi LLM, comment lại GitLab/GitHub. Xử lý rate-limit, cost control, security (secret leak). | Học lý thuyết design pattern không gắn liền vấn đề thực tế team đang gặp. |
| **4. Network Security: Lab MITM attack trên local network, hiểu TLS handshake, Certificate Pinning.** Áp dụng: Viết interceptor kiểm tra cert cho outbound call từ Java service đến LLM API. | Chỉ học lý thuyết Port/Protocol không thực hành với tool (Wireshark, mitmproxy, nmap). |
| **5. Viết 1 bài blog/post LinkedIn tiếng Việt: "Tôi tích hợp RAG vào Spring Boot project như thế nào"**. Bodybuilding personal brand cho hướng FDE/AI Engineer. | Giữ im lặng, chỉ code private repo. Thị trường VN tuyển qua network & portfolio công khai. |

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

### 1. @phutran-z6h — **Insight Score: 12.0** (Cao nhất toàn bộ dataset)
> **Video:** [No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?](https://www.youtube.com/watch?v=gxIKlsOzq70) (Tips Javascript)  
> **Votes:** 14  
> **Nội dung đầy đủ:**
> "Vấn đề là ae làm việc theo kiểu chia task + chia role quen rồi, giờ bảo ae tìm hiểu nghiệp vụ của cả hệ thống thì hơi bị khó, kĩ năng đó hình thành từ nhiều năm đi làm chứ ko phải một sớm 1 chiều, mà ngay cả khi ae muốn tìm hiểu thì cũng chưa chắc có cơ hội. Chuyện AI tự thiết kế, tự chạy test từ performance,security,e2e, uiux,... giờ là chuyên quá dễ dàng rồi, tùy ko đc 100% nhưng nó cũng làm dc 95-98% tùy vào cách ae setup + research. Chuyện lập trình viên ko cần code là chuyện trước mặt rồi, ko phải tương lại nữa, thế nên ae nên tập trung vào việc hiểu bussiness + hệ thống + kĩ năng làm việc với mọi người xung quanh. Với tình trạng mất não ko thể đọc tài liệu quá 100 dòng hiện nay thì thị"
> **Tại sao đọc:** Đây là **manifesto thực chiến** cho dev VN hiện nay. Tóm gọn được 3 shift: (1) AI đã làm 95-98% code/test, (2) Kỹ năng "hiểu business + hệ thống" cần năm tháng rèn, không học 1 sớm, (3) Soft skill/làm việc nhóm thành core skill. Người comment có vẻ là Senior/Lead đã trải qua chuyển dịch.

### 2. @NguyênNguyễnVăn-m6e3o — **Insight Score: 4.5**
> **Video:** [No Code | Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?](https://www.youtube.com/watch?v=gxIKlsOzq70)  
> **Votes:** 4  
> **Nội dung đầy đủ:**
> "E nói thật chứ có kinh nghiệm kĩ thuật, năng lực,... Ở đâu cũng sống đc, chứ tại sao cứ phải suy nghĩ phải lm cho tư bản mới đc, như e làm tự do tháng đều đều trung bình cũng hơn 25 củ vưà lm vừa chơi, chưa kể sống ở nhà nông thôn nên chi phí sống vẫn dư giả chán, thấy nhiều người thất bại chỉ biết lắc đầu cười, ko phải cười họ thất bại, mà cười họ ko biết mình thất bại ở đâu rồi lấy cái lý do nào đó để tự nhủ cho cái thất bại của mình😅"
> **Tại sao đọc:** Góc nhìn **Freelance/Remote/Geographic Arbitrage** – một lối thoát hiện thực cho dev VN senior muốn tự chủ thu nhập, không phụ thuộc tuyển dụng corporate. Nhấn mạnh "năng lực kỹ thuật mang theo đi đâu cũng ăn được".

### 3. @vantran_devopsinfra — **Insight Score: 2.0**
> **Video:** [Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI (AI Engineer).](https://www.youtube.com/watch?v=kRXoK02KJow) (Tips Javascript)  
> **Votes:** 8  
> **Nội dung đầy đủ:**
> "Xưa em từng làm dự án sinh viên, nôm na là tự build 1 con AI để có thể trả lời 1 số chủ đề cụ thể trong 1 file tài liệu lớn, lúc đó em có suy nghĩ không thể đưa cho AI 1 file lớn như vậy và rồi chỉ để hỏi 1 số chủ đề trong đó, vì vậy cần 1 giải pháp tối ưu đó là RAG. Trước tiên cắt tài liệu thành các Chunks, dùng 1 model BGE (BGE-m3) để embedding các Chunks tài liệu, rồi đẩy vào Mongo Vector Search, sau đó embedding câu hỏi và truy vấn trong MongoDB Vector Search để lấy top K số Chunks liên quan, và rồi đẩy câu hỏi text kèm top K Chunks text vào LLM (Qwen2.5-3B) để trả lời. Cảm ơn video của anh làm em nhớ lại kỉ niệm sinh viên. Điểm thú vị đó là tìm ra điểm chưa tối ưu và tìm cách để tối ưu"
> **Tại sao đọc:** **Case study hands-on RAG production-like** từ dev VN (có vẻ DevOps/Infra background). Nêu rõ stack: BGE-m3 embedding + Mongo Vector Search + Qwen2.5-3B local. Đây là template kỹ thuật có thể copy ngay cho project tuần này.

### 4. @duythanh1602 — **Insight Score: 3.5**
> **Video:** [Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI (AI Engineer).](https://www.youtube.com/watch?v=kRXoK02KJow)  
> **Votes:** 1  
> **Nội dung đầy đủ:**
> "Đại ca ơi, giờ backend 5 năm kinh nghiệm có nên chuyển hướng sang AI engineering ko hay tập trung ôn tiếp BE vậy, vì em nộp thử CV thì thấy toàn AI nhiều"
> **Tại sao đọc:** Đại diện cho **nhóm Backend Senior (5 YOE) đang hoang mang trước JD market**. Câu hỏi này chính là "nỗi đau" của phân khúc lớn dev VN – cần được trả lời rõ ràng trong roadmap (xem Mục 2, 3).

### 5. @hirunguyen4522 — **Insight Score: 2.0**
> **Video:** [Ngành lập trình và IT năm 2026 ảm đạm ra sao??](https://www.youtube.com/watch?v=mOaakWt7txY) (Tôi Đi Code Dạo)  
> **Votes:** 180  
> **Nội dung đầy đủ:**
> "Dev tầm 2022 trở về trước thì đúng là sướng thật. bây giờ thì chỉ còn anh em dev cũ có vốn lớn vài tỷ thì sẽ có khả năng nhìn nhận AI lợi hơn hại. Còn không vốn phải đi làm thuê thì đói kém lắm. tầm này nhà nước đẩy mạnh bơm tiền cho xây dựng, nhiều khi làm về tay chân lương cao hơn dev mới đó."
> **Tại sao đọc:** **Góc nhìn thực tế khắc nghiệt** về thu nhập thực net sau chi phí sinh hoạt, so sánh với ngành khác. Cảnh báo cho Fresher/Junior: "đói kém" nếu không có vốn kỹ năng/số dư tài chính. So sánh với xây dựng (blue-collar) là signal mạnh về supply/demand imbalance ở entry-level.

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| # | Nguồn | Loại/Region | Luận điểm chính & Góc nhìn nổi bật | Lý do chọn |
|---|-------|-------------|-----------------------------------|------------|
| 1 | **[No Code \| Không thể nào các lập trình viên kiểu này thực sự mất việc vào năm SAU?](https://www.youtube.com/watch?v=gxIKlsOzq70)** (Tips Javascript) | YouTube **[VN]** | AI đã làm 95-98% code/test. Dev phải chuyển sang hiểu business + hệ thống + soft skill. Comment @phutran-z6h (insight 12) là "kinh thánh" mindset shift. | **Top relevance (63.5) + Expert voice (1.5) + Comment insight cao nhất cả dataset.** Bắt buộc xem để hiểu bối cảnh VN. |
| 2 | **[Ngành lập trình và IT năm 2026 ảm đạm ra sao??](https://www.youtube.com/watch?v=mOaakWt7txY)** (Tôi Đi Code Dạo) | YouTube **[VN]** | AI Agent bùng nổ, Junior bi kịch, StackOverflow chết. Khuyên: Đừng ghét AI, dùng AI để làm nhàn hơn. Comment @hirunguyen4522 (180 votes) cho real-check thu nhập. | **Relevance 56 + Community trust cao (Tôi Đi Code Dạo).** Tổng quan thị trường VN 2026 thực tế. |
| 3 | **[Anthropic vừa bỏ Git, tự build một VCS mới tên Scion vì AI viết code quá nhanh](https://facebook.com/groups/j2team.community/permalink/3250611268604304/)** (J2TEAM Community) | Facebook **[VN]** | Anthropic merge 30k changes/ngày → Git không scale → tự build Scion (client-server VCS). Signal mạnh cho Platform Engineering/DevEx. | **Incident severity 2.0 (tech shift lớn) + Region VN.** Chỉ ra hướng đầu tư kỹ năng infra/tooling. |
| 4 | **[AI Isn't Firing People. It's Quietly Not Hiring Them.](https://www.youtube.com/watch?v=o5souAFfjbo)** (Kilobrief) | YouTube **[Quốc tế]** | Goldman Sachs/Stanford: Việc làm 22-25 tuổi giảm 19% do AI không tuyển mới. Không phải layoff, là hiring freeze cho entry-level. | **Relevance 38.5 + Data-driven (Stanford/Goldman).** Áp dụng VN: Fresher phải có portfolio AI-ready ngay. |
| 5 | **[₹50 LPA AI Job \| The Next Big AI Career in 2026?](https://www.youtube.com/watch?v=DC6YqZErQcU)** (Elamparithi) | YouTube **[Quốc tế]** | Forward Deployed Engineer (FDE) = SE + AI + PM + Consulting. Role mới lương cao, cầu vọt. Skill: Business problem solving, RAG, Agent orchestration. | **Relevance 55.8 + Định nghĩa role mới rõ ràng.** Roadmap chuyển dịch cho Senior/Lead VN. |
| 6 | **[Vector Databases - Video này để hiểu sự nâng cấp từ Kỹ sư lập trình đến Kỹ sư AI (AI Engineer).](https://www.youtube.com/watch?v=kRXoK02KJow)** (Tips Javascript) | YouTube **[VN]** | Hướng dẫn kỹ thuật Vector DB, Embedding, RAG – bước đệm BE → AI Engineer. Comment @vantran_devopsinfra chia sẻ stack production. | **Relevance 56 + Expert voice 1.5 + Technical depth.** Học tập hands-on ngay. |
| 7 | **[Cùng là đưa AI Agents vào quy trình...](https://facebook.com/groups/vnjug/permalink/2593623114396326/)** (Vietnam Java User Group) | Facebook **[VN]** | JetBrains case study: Thêm agent vào quy trình lỗi = 0 hiệu quả. Phải build team infra (Team 2x) cho agent: shared skills, backtest, MCP servers. | **Relevance 53.2 + Community chuyên sâu (VJUG).** Bài học quản trị engineering team dùng AI. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào với `is_major_incident = true` (CVE/CVSS cao, KEV, khai thác thực tế). Do đó **bỏ qua mục 6** theo quy tắc.*