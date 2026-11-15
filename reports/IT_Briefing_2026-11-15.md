📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.5qgm1kiy20pl)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Chuyển dịch mạnh mẽ sang "Agentic Engineering" & AI Application Layer**: Các sự kiện cộng đồng lớn như **GDG DevFest Hanoi 2026** (chủ đề "Build, Secure, Scale: Developers and Builders in the Agentic Era") và thảo luận tại nhóm *Forum Machine Learning cơ bản* về VLM (Vision-Language Model) & VLA (Vision-Language-Action) cho thấy nhu cầu thực tế đang dồn vào **xây dựng hệ thống multi-agent, RAG, fine-tune model nhẹ (distillation) chạy on-device** (ví dụ: project OpenDubber dùng Knowledge Distillation giảm model TTS từ 82M → 8.6M params chạy WASM trên browser).  
  > *Nguồn: [GDG DevFest Hanoi 2026](https://facebook.com/groups/machinelearningcoban/permalink/2692681647855892/) (region=VN, relevance=34.3); [OpenDubber/Kokoro Distillation](https://facebook.com/groups/j2team.community/permalink/3246328055699292/) (region=VN, relevance=34.6).*
- **Tiêu chuẩn Senior/Middle rõ ràng hóa theo hướng "System Ownership"**: Bài chia sẻ từ cộng đồng **VGU Tech Alumni** (5-7 năm kinh nghiệm) khẳng định Senior không phải code nhanh hơn mà khác ở: **tư duy kiến trúc (scalability, security), chủ động tìm vấn đề gốc, phối hợp cross-func (BA, QA, DevOps), và mentoring**. Điều này khớp với xu hướng toàn cầu: tuyển dụng ít hơn nhưng yêu cầu "bán thành phẩm" cao hơn.  
  > *Nguồn: [Senior khác Middle ở đâu?](https://facebook.com/groups/vgu.tech.alumni/permalink/1503945988308577/) (region=VN, relevance=70.4, expert_voice_score=7.5).*
- **Thị trường tuyển dụng "giả象" (phantom hiring)**: Tin tức từ *Vietnam.vn* & *VietNamNet* cho thấy tin tuyển dụng lập trình viên Mỹ tăng ~15% từ 2/2025 dù AI viết code giỏi hơn, nhưng thực tế **headcount thực tế không tăng tương ứng** — nhiều công ty đăng tuyển để "giữ thương hiệu" hoặc chờ budget. Tại VN, hiện tượng tương tự: đăng nhiều, phỏng vấn khắt khe, chốt ít.  
  > *Nguồn: [AI viết mã nhưng tin tuyển dụng tăng](https://news.google.com/rss/articles/CBMiugFBVV95cUxOQzRaZ28wZEhFZklSUmoyaDVNejluMzViNy1yX25RMi1COWJ5OUhDcktoYnVlNHo2M1ZDVENadHhweEEyQ1VSc0ppTkwzSW43OXJlX1JoaHhoVERza0kyMGV6LXBNR2FpeUlodjZNSmR4Y21hWV8taUd5YkVjWnFSZUozOGlBT1JpblRuMUU2T3VicmFsdnBfRnRUdUxEa3ZWVi1nNHNxQnJaaDQ0aHc2YkRvOUpWNnNkM0E?oc=5) (region=VN, relevance=35.0).*

### Trên thế giới (và ý nghĩa với Việt Nam)
- **AI thay đổi bản chất "Entry-level" — Junior bị loại ra khỏi vòng lặp sản xuất code cơ bản**: Video *Microsoft Engineer (Kushal Vijay)* và *The Seasoned CTO* đều chỉ ra: **công ty tạm dừng tuyển fresher, ép team hiện tại "document workflow" để thay bằng AI agent**. Stanford research (trích trong video *My AI Life*) xác nhận: young workers in highly AI-exposed occupations falling behind mainly through **reduced hiring**.  
  > *Ý nghĩa VN:* Doanh nghiệp VN outsource/freshers nhiều sẽ bị tác động sớm — fresher cần **biết dùng AI để deliver end-to-end feature** (không chỉ code snippet) mới có giá trị.
  > *Nguồn: [Software Engineer in 2027](https://www.youtube.com/watch?v=Tgq6wdLZSCs) (relevance=86.0); [Why You're Not Getting Hired](https://www.youtube.com/watch?v=h_3Km3DYEic) (relevance=69.6, expert_voice_score=4.5).*
- **Khoảng cách lương New Grad vs Senior giãn cực lớn — "First job is the hardest"**: Median US dev ~$136k nhưng new gradstruggle to get hired; senior roles account for most posting increase (video *HowMuchSalaryUS*, *The Seasoned CTO*).  
  > *Ý nghĩa VN:* Ở VN gap lương Fresher vs Senior cũng đang giãn (Senior 3-5k USD, Fresher 500-800 USD). Chiến lược: **nhanh chóng đạt mức "Senior mindset" (system design, ownership) trong 2-3 năm** thay vì dài dẳng ở SDE1.
  > *Nguồn: [Software Engineer Salary 2026](https://www.youtube.com/watch?v=RnuBVVetqw0) (relevance=71.8, expert_voice_score=7.5).*
- **Embedded / Firmware & Hardware-AI là "mỏ vàng" bị bỏ quên**: Bài Dev.to *15 embedded interview questions that trip up strong candidates* nhấn mạnh firmware interview **không phải LeetCode inverted** — cần hiểu memory layout, interrupt, DMA, RTOS, linker script. Kết hợp xu hướng VLA (Vision-Language-Action) cho robot tại nhóm ML VN → **cần dev hiểu cả low-level + AI**.  
  > *Ý nghĩa VN:* VN có base mạnh embedded (Foxconn, Samsung, VinFast, FPT Automotive) — đây là niche **ít bị AI thay thế, lương cao, cầu vọt nhân lực**.
  > *Nguồn: [15 embedded interview questions](https://dev.to/firmwareprep/15-embedded-interview-questions-that-trip-up-strong-candidates-3hho) (relevance=42.0).*

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cốt lõi (Must-have)
| Kỹ năng | Tại sao quan trọng | Nguồn / Bình luận điển hình |
|---|---|---|
| **System Design & Architecture Thinking** | Senior = trade-off scalability, security, maintainability; không chỉ "code chạy". | VGU Alumni post (5 yếu tố Senior) — *expert_voice_score=7.5* |
| **AI Agent / Multi-Agent Orchestration** (LangGraph, AutoGen, CrewAI, Google ADK) | DevFest Hanoi 2026 focus "Agentic Engineering"; thực tế VN đang build internal copilot, RAG pipeline. | GDG DevFest Hanoi 2026 announcement |
| **Model Optimization & On-device Deployment** (Quantization, Distillation, ONNX Runtime, WASM, TensorRT-LLM) | OpenDubber case: giảm 82M→8.6M params, chạy realtime trên CPU browser — skill cực khan hiếm. | J2Team Community post (OpenDubber/Kokoro) |
| **End-to-End Feature Ownership** (Product sense + Infra + Observability) | "Stop viewing career as coding tasks" — BuilderVeda; Seasoned CTO: hiring managers prioritize quality over quantity. | Video *Why You're Stuck at SDE1* (relevance=43.6, expert_voice_score=4.5) |
| **Security Fundamentals** (AppSec, Supply Chain, Hardening) | "Secure" là 1/3 pillar DevFest 2026; layoff wave → companies need engineers tự bảo vệ hệ thống. | GDG DevFest Hanoi 2026 (Secure track) |

### Công nghệ cụ thể — Phân biệt Xu hướng thật vs Hype
| Công nghệ | Đánh giá | Hành động |
|---|---|---|
| **Python (AI/ML stack), TypeScript/Node.js (Agent backend), Go (Infra/CLI)** | **Xu hướng thật** — backbone của AI app layer. | Học sâu: `asyncio`, `FastAPI`, `pydantic`, `langchain/langgraph`, `go-kit`. |
| **Rust (WASM, high-perf inference)** | **Xu hướng thật** — dùng cho WASM edge (như Kokoro ONNX WASM). | Học đủ để compile model sang WASM, optimize memory. |
| **React/Next.js (Frontend)** | **Vẫn cần** nhưng chuyển sang *AI-enhanced UI* (streaming response, tool-use rendering). | Học `Vercel AI SDK`, `React Server Components`. |
| **Kubernetes / Cloud Native (CKA level)** | **Cần có** cho Senior/Staff — nhưng fresher chỉ cần hiểu deployment flow, observability (Prometheus/Grafana). | Không đào sâu K8s admin nếu không muốn đi DevOps/Platform. |
| **Blockchain / Web3 / Metaverse** | **Hype giảm mạnh** — ít mention trong data set. | Bỏ qua trừ khi có domain knowledge riêng. |
| **Embedded Linux / Zephyr / FreeRTOS + TinyML** | **Xu hướng thật, niche cao** — VLA/robotics cần low-level + AI. | Nếu thích hardware: học `Yocto`, `Buildroot`, `TFLite Micro`, `ONNX Runtime Mobile`. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy được cộng đồng nhắc nhiều nhất
1. **Từ "Task Executor" → "Problem Owner"**  
   - Senior không chờ BA đưa ticket; tự tìm root cause, đề xuất giải pháp, chịu trách nhiệm kết quả (VGU Alumni).  
   - *Áp dụng:* Mỗi ticket Jira, hãy tự hỏi: "Vấn đề business gốc là gì? Solution này có scale không? Có rủi ro bảo mật gì?" → ghi chú vào PR description.
2. **Từ "Code-centric" → "System & Business-centric"**  
   - BuilderVeda: "Primary output shifts from features to architecture".  
   - *Áp dụng:* Hàng tuần dành 2h đọc RFC/ADR của team, hiểu data flow end-to-end, không chỉ module mình own.
3. **AI as Teammate, not Tool**  
   - Kushal Vijay (Microsoft): "Staying relevant beyond just coding" — dùng AI agent để *orchestrate* workflow (spec → test → deploy).  
   - *Áp dụng:* Thiết lập pipeline: `Cursor/Copilot` sinh code → `AI agent` chạy test/lint → `AI agent` tạo PR description + migration script.
4. **Communication & Cross-func Collaboration là Technical Skill**  
   - VGU Alumni: "Phối hợp BA, QA, Product, DevOps" là yếu tố 4/5 của Senior.  
   - *Áp dụng:* Chủ động demo cho QA trước khi merge, viết docs cho BA hiểu flow, pair-program với DevOps để cải thiện CI/CD.

### Kế hoạch tuần này cho Dev nền Java/Spring Boot đang học Python + Network Security
| Thứ | Hành động cụ thể (2-3h/ngày) | Mục tiêu |
|---|---|---|
| **Thứ 2-3** | **Python:** Xây mini-project **FastAPI + LangGraph** đơn giản: nhận request → gọi LLM → trả về structured output (Pydantic). Deploy lên Render/Fly.io (free tier). | Biết dựng AI backend end-to-end, hiểu async, dependency injection (giống Spring). |
| **Thứ 4** | **Network Security:** Lab **Wireshark + Zeek** phân tích pcap mẫu (malware traffic, C2 beacon). Viết script Python (scapy/pyshark) tự động extract IOC. | Kết hợp Python + Security — skill hiếm, đắt giá cho SOC/DevSecOps. |
| **Thứ 5** | **System Design:** Vẽ diagram (Mermaid/Excalidraw) cho project Spring Boot hiện tại: boundary, data flow, threat model (STRIDE). Đề xuất 1 hardening (rate-limit, input validation, secret rotation). | Tư duy Architect + Security — chứng minh Senior mindset. |
| **Thứ 6** | **AI Agent:** Thử **Google ADK** hoặc **LangGraph** build agent tự động: đọc Jira ticket → sinh code change → tạo PR. Chạy local với Ollama (llama3.1:8b). | Hands-on Agentic Engineering — trend DevFest 2026. |
| **Thứ 7** | **Review & Share:** Viết bài 300-500 từ (LinkedIn/FB group VN) tóm tắt bài học tuần: "Từ Spring Boot sang AI Agent + Security: những bẫy và tip". Tag mentor/lead để xin feedback. | Xây personal brand, tinh thần "Chia sẻ kiến thức" (yếu tố 5 của Senior). |
| **CN** | **Nghe/Đọc:** Video *Software Engineer in 2027* (Microsoft Engineer) + bài *Why You're Stuck at SDE1* — ghi 3 action item áp dụng cho Q3. | Cập nhật macro view, định hướng 6 tháng tới. |

**Tránh tuyệt đối:**  
- Học lướt framework mới mỗi tuần (Next.js, Svelte, Astro...) mà không có project thực.  
- Chỉ làm LeetCode — không có system design, không có AI, không có security.  
- ỷ lại AI sinh code mà không review, không hiểu business logic, không test.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

| # | Bình luận (trích đầy đủ) | Tác giả / Votes / Insight | Nguồn (Link) | Tại sao đáng đọc |
|---|---|---|---|---|
| 1 | **Ngoài ra, em đã đọc một số paper về các model VLA vài năm gần đây và nhận thấy các mô hình sẽ có dạng như trong ảnh.(π₀, OpenVLA, FAST và DREAMZero, …) Phần mềm mô phỏng Maniskill cánh tay robot có thể lắp camera lên đó. Bản thân em cũng đã có nền tảng lý thuyết cơ bản về các Diffusion, Flow Matching, RL, chưa có nhiều kinh nghiệm thực tế với hệ thống robot vật lý, cần học thêm. Nếu anh chị nào làm việc về VLA hay điều khiển hoặc gì đó liên quan thì cho em xin vài review với ạ, cụ thể về những khó khăn trong việc phát triển nó, những điều cần lưu ý. Em cảm ơn mọi người rất nhiều ạ!** | Facebook user / 0 votes / **insight_score=9.5** | [Forum ML cơ bản - VLM Model](https://facebook.com/groups/machinelearningcoban/permalink/2693050277819029/) | **Chứng minh xu hướng VLA (Vision-Language-Action) đang vào thực tế tại VN** — người học theory đang chủ động tìm mentor, project robot. Cho thấy *skill gap* lớn: Diffusion + RL + Robotics sim (ManiSkill) + Real hardware. |
| 2 | **My company just paused all hiring and made us document our workflows. Made me think of what Dane Vexlan said about the 90-day phase out before they cut your whole department.** | @karthickkarthick9555 / 13 votes / **insight_score=1.0** | [Software Engineer in 2027](https://www.youtube.com/watch?v=Tgq6wdLZSCs) | **Báo động thực tế**: Company đang "document workflow" để thay thế bằng AI agent — giai đoạn 90 ngày trước khi cắt team. Khuyên dev phải *chủ động automate workflow của chính mình* trước khi bị automate. |
| 3 | **The answer is simple, and it is an answer that IBM actually said months ago. "The sr. technicians and programmers of the future stars as the entry level workers of today. So being short sighted and cutting out entry level only creates problems later." But many business's can not see past their next quarter no less ten or twenty years down the line so...I am thinking about getting into wood working.** | @SyberSmoke / 1 vote / **insight_score=4.5** | [Why your first dev job is getting harder](https://www.youtube.com/watch?v=V8vt9nZ-IX0) | **Phân tích gốc rễ**: Hiring freeze fresher = tự sát pipeline senior. Dev VN cần hiểu: *nếu công ty không tuyển fresher, bạn phải tự tạo trải nghiệm "entry-level work" qua side project, open source, AI agent building* để bù đắp. |
| 4 | **Đây là CV của em ạ. Hiện tại em đang tìm kiếm một cơ hội việc làm phù hợp trong lĩnh vực AI Research/Engineering. Định hướng dài hạn của em là về VLA, hiện tại em đang sinh sống tại TP.HCM, nhưng sẵn sàng chuyển đến bất kỳ nơi nào nếu cần để phù hợp với công việc. Em cũng sẵn sàng tham gia các công việc part-time, dự án nghiên cứu phát triển công nghệ.** | Facebook user / 0 votes / **insight_score=4.5** | [Forum ML cơ bản - VLM Model](https://facebook.com/groups/machinelearningcoban/permalink/2693050277819029/) | **Thực trạng job seeking AI tại VN**: Candidate sẵn sàng relocate, làm part-time, research project — cho thấy *cung cầu nhân lực AI Research/Engineering còn khan hiếm, mềm dẻo về hình thức hợp tác*. |
| 5 | **Which market are you seeing where you work: roles being cut, senior roles opening, or both at once? Tell me your level and what changed on your team this year. I read every one.** | @TheSeasonedCTO (Author) / 0 votes / **insight_score=1.0** | [Why You're Not Getting Hired](https://www.youtube.com/watch?v=h_3Km3DYEic) | **Góc nhìn Engineering Manager/CTO**: Đang thu thập data real-time từ dev toàn cầu về "cut roles vs open senior". Cho thấy *hiring bar nâng cao, chỉ còn Senior+ với system ownership*. |

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| # | Tiêu đề + Link | Nhãn | Luận điểm chính | Góc nhìn nổi bật từ bình luận / Expert | Lý do chọn |
|---|---|---|---|---|---|
| 1 | **Software Engineer in 2027? AI, Layoffs & Job Market Reality \| Microsoft Engineer**  <br>🔗 https://www.youtube.com/watch?v=Tgq6wdLZSCs | [Quốc tế] | Microsoft Engineer Kushal Vijay chia sẻ: AI agent thay đổi cách dev học & làm việc; DSA/project vẫn quan trọng nhưng phải *apply AI vào workflow*; startup vs Big Tech trade-off. | Comment @karthickkarthick9555: company paused hiring, bắt document workflow cho 90-day phase-out. | **Relevance cao nhất (86)**, expert voice (Microsoft Engineer), góc nhìn thực tế từ Big Tech — map trực tiếp vào bối cảnh VN outsource/enterprise. |
| 2 | **🚀 SENIOR DEVELOPER KHÁC MIDDLE Ở ĐIỂM NÀO?**  <br>🔗 https://facebook.com/groups/vgu.tech.alumni/permalink/1503945988308577/ | [VN] | 5 yếu tố phân biệt Senior: Problem solving gốc rễ, Architecture thinking, Proactiveness, Cross-func coordination, Knowledge sharing. | Expert_voice_score=7.5 (tác giả là alumni VGU, kinh nghiệm 5-7 năm, tone mentoring). | **Đánh trúng pain point dev VN**: nhiều người 3-4 năm vẫn "code task", bài viết cho roadmap rõ ràng để lên Senior. |
| 3 | **GDG DevFest Hanoi 2026 - BUILD, SECURE, SCALE: DEVELOPERS AND BUILDERS IN THE AGENTIC ERA**  <br>🔗 https://facebook.com/groups/machinelearningcoban/permalink/2692681647855892/ | [VN] | Sự kiện lớn nhất cộng đồng Google Dev tại VN năm 2026, focus **Agentic Engineering, Multi-Agent, Security, Scaling**. | Chủ đề "Agentic Era" khớp với xu hướng toàn cầu; track "Secure" nhấn mạnh AppSec/Supply chain. | **Tín hiệu chính thức từ Google VN** về hướng đi công nghệ 2026 — dev VN nên attend (free) để nắm trend, network. |
| 4 | **OpenDubber: Knowledge Distillation cho TTS tiếng Việt chạy on-device (WASM)**  <br>🔗 https://facebook.com/groups/j2team.community/permalink/3246328055699292/ | [VN] | Case study thực tế: Distill Kokoro 82M → 8.6M params, INT8 ONNX, chạy realtime trên browser WASM đơn luồng. | Tác giả chia sẻ full pipeline: Teacher-Student training, quantization, deployment — **skill cực hot: Model Optimization + Edge Deployment**. | **Đếm ngược xu hướng "AI to lớn chạy không được" → "AI nhỏ, chạy mọi nơi"**. Kỹ năng này áp dụng ngay cho VN (low-end device, offline). |
| 5 | **Why You're Stuck at SDE1 #softwareengineering #career #tech**  <br>🔗 https://www.youtube.com/watch?v=_vDcMURsTBw | [Quốc tế] | BuilderVeda phân tích: SDE1→Staff không phải code nhiều hơn mà *shift scope*: end-to-end system ownership, technical direction, architecture as output. | Expert_voice_score=4.5; nhấn mạnh "primary output shifts from features to architecture". | **Blueprint cho dev VN muốn lên cấp**: từ "làm task" → "own system" — phù hợp văn hóa enterprise VN đang chuyển型. |
| 6 | **15 embedded interview questions that trip up strong candidates**  <br>🔗 https://dev.to/firmwareprep/15-embedded-interview-questions-that-trip-up-strong-candidates-3hho | [Quốc tế] | Firmware interview ≠ LeetCode; hỏi memory layout, interrupt latency, DMA, linker script, RTOS scheduling, watchdog, bootloader. | Không có comment nhưng nội dung *highly technical, từ người trong nghề firmware* (expert_voice ngầm). | **Mỏ vàng niche**: VN có base embedded lớn (manufacturing, automotive) — dev Java/Spring Boot học thêm network security có thể pivot sang **Embedded Security / Automotive Cybersecurity** (UN R155, ISO 21434). |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào với `is_major_incident = true` trong bộ dữ liệu cung cấp. Bỏ qua mục này.*