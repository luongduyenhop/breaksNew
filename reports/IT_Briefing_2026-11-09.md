📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.ckha6bgdt3oy)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Đại dân cắt giảm nhưng nhu cầu "chất lượng" vẫn tăng**: Microsoft VN sa thải nhân sự (Google News, relevance 34) song song với tin VnEconomy "Nhu cầu tuyển dụng lập trình viên vẫn tăng dù đã có AI" (relevance 34). **Dịch chuyển**: Thị trường không thiếu *số lượng* dev, mà thiếu dev *có tư duy hệ thống, an ninh mạng và biết dùng AI làm đòn bẩy* — ngân hàng (ANZ) vẫn tuyển mạnh profile 5 năm kinh nghiệm qua khóa Engineer Pro (Viblo, relevance 35.5, expert 1.5).
- **Vibe Coding & AI Agent hóa thành kỹ năng "bắt buộc" cho fresher/junior**: Kênh **Hỏi Dân IT** (VN) ra series hướng dẫn *Git an toàn cho Vibe Coding*, *Antigravity IDE*, *Gemini AI* (relevance 51–52). Tín hiệu rõ: cộng đồng VN đang chuyển từ "học code" sang "học điều khiển AI code an toàn (Git, workflow, review)". Đây là tiêu chuẩn mới cho CV fresher 2025.

### Trên thế giới (và ý nghĩa với Việt Nam)
- **AI thay Junior, không thay Senior — nhưng "lối vào Senior" đang bị chặn**  
  Video **Deric Yee** (expert 3.0, relevance 40.6): *"If AI does the junior work, how does anyone become a senior?"*. **Ý nghĩa VN**: Các công ty outsourcing/outstaffing VN thường dùng Junior làm CRUD/test — việc này AI làm được. Dev VN **bắt buộc** tự xây "portfolio hệ thống" (system design, infra, security) ngay từ năm 1–2 thay vì chờ giao task.
- **Chi phí AI là rào cản thay thế hoàn toàn — AI như "Junior đắt tiền cần review"**  
  Bình luận **@DakshChaudhary** (insight 2.0, video *yournishaant*): *"AI will be like a Junior dev if its code made production fu*ked up you would be able to make it back alive... companies got their yearly budget burnt in 2-3 months"*. **Áp dụng VN**: Khách hàng VN (SME, startup) nhạy cảm chi phí — họ sẽ không trả $20–50/user/tháng cho Copilot/Devin cho toàn team. Dev biết **tự host model cục bộ, dùng Git control luồng AI, review code AI** sẽ được ưu tiên hơn dev chỉ biết "tab-tab-enter".
- **Tuyển dụng chuyển từ "biết syntax" sang "hiểu business + hệ thống + bảo mật"**  
  Video **exit node** (Chavdar — Senior/Manager/Director AI, expert 1.5, relevance 55.7): *"Make your work visible beyond your team: run a training, present what you learned, talk to senior people... Learn system design/architecture more"*. **Ý nghĩa VN**: Lương dev VN 3–5 năm kinh nghiệm đang phân cực: nhóm làm task giữ mức 1.5–2.5k USD; nhóm *dẫn dắt kiến trúc, hardening security, nói chuyện được với business* lên 3.5–5k USD.
- **Layoff không chỉ do AI — do "skill gap in understanding, not syntax"**  
  Video **yournishaant** (Senior Engineer 5 năm, expert 3.0, relevance 59): *"Tech layoffs are a skill gap in understanding, not syntax"*. **Áp dụng VN**: Các công ty VN đang cắt giảm bên "code tay" (outsource thuần) nhưng mở thêm position "Tech Lead/Architect/Security Engineer". Dev cần **chuyển từ "viết code chạy" sang "thiết kế giải pháp an toàn, tiết kiệm chi phí, mở rộng được"**.
- **Tài năng cốt lõi AI tập trung ở tầng Research — tầng App (Claude Code, Cursor...) đang commoditize**  
  Nhóm J2Team (expert 3.0, community lane) + bình luận FB (insight 2.0): *"Quan trọng nhất... vẫn là mấy ông giáo sư, tiến sĩ chịu trách nhiệm training... mấy cái như Claude Code, Claude Desktop... chỉ là tools ở tầng app nên ko khó như vậy"*. **Lời khuyên VN**: Đừng FOMO tool mới mỗi tuần. Hãy **nắm vững nguyên lý LLM (token, context, RAG, agent loop)** và **kỹ năng tích hợp/an toàn hóa (guardrails, eval, sandbox)** — đây là lớp vững chắc không bị lỗi thời khi tool thay đổi.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

### Kỹ năng cần học (kèm nguồn/bình luận)
| Kỹ năng | Vì sao quan trọng | Nguồn dẫn chứng |
|---|---|---|
| **System Design & Architecture (tư duy high-level)** | Junior cần nhìn thấy "toàn cảnh" để review code AI, thiết kế module an toàn, không chỉ làm task. | @oussamaelwefi2940 (insight 2.0, exit node): *"even as a junior I need to have a high level look at things, and learn the system design / architecture more"* |
| **Git & Workflow an toàn cho AI (Vibe Coding)** | AI sinh code nhanh nhưng dễ hallucinate, xóa code, commit nhầm. Git là "bảo hiểm" duy nhất. | Series **Hỏi Dân IT**: *"Git Siêu Dễ... Tự Tin Code Bằng AI"*, *"Vibe Coding Cùng AI Siêu An Toàn Với Git"* (relevance 51–52) |
| **Network Security / AppSec cơ bản (OWASP, hardening, zero-trust)** | Khách hàng VN (bank, fintech, e-com) yêu cầu bảo mật mặc định. AI sinh code thường bỏ qua authz, input validation. | User profile (Java/Spring + Python + NetSec) + xu hướng *shift-left security* toàn cầu. |
| **Prompt Engineering / Agent Orchestration (Claude Code, Gemini, Antigravity, Cursor)** | Biết "nói chuyện" với AI để sinh code đúng chuẩn, test, refactor, doc. | Hỏi Dân IT series Antigravity/Gemini; Deric Yee: *"senior engineer with AI can now handle what used to be entry-level work"* |
| **CS Fundamentals (DSA, OS, Network, DB) tự học có lộ trình** | Không có mentor tại trường → tự xây curriculum. Đây là rào cản lớn nhất fresher tier 3. | @Xyz-e6x (insight 2.0, yournishaant): *"how to build the fundamentals completely through self study... I can't rely on my college... guidance... overwhelming"* |
| **Business/Product Thinking** | Dev hiểu business mới thiết kế được schema DB, API, security phù hợp, không over-engineering. | exit node (Chavdar): *"focus on the work... make your work visible... talk to senior people"* |

### Công nghệ cần học (phân biệt xu hướng thật vs hype)
| Công nghệ | Trạng thái | Ghi chú cho dev VN |
|---|---|---|
| **Java 21+ / Spring Boot 3.x** | **XU HƯỚNG THẬT (Enterprise VN)** | Ngân hàng, logistics, gov VN vẫn core Java. Học *virtual threads, GraalVM native, Spring Security 6, Observability (Micrometer/Prometheus)*. |
| **Python 3.11+ (FastAPI, Pydantic, asyncio)** | **XU HƯỚNG THẬT (AI/Automation/Tooling)** | Viết script automation, wrapper LLM, build RAG pipeline, security scanner. Kết hợp với Java qua gRPC/Message Queue. |
| **Git (CLI + GitHub/GitLab CI) + Conventional Commits** | **BẮT BUỘC (Foundation)** | Không có Git tốt → không dám Vibe Coding. Học *rebase, bisect, hook, signed commit*. |
| **Docker / Kubernetes (k8s) cơ bản + Helm** | **XU HƯỚNG THẬT (Infra/Deploy)** | Dev VN cần tự deploy staging/prod, hiểu resource limit, network policy, secret management. |
| **PostgreSQL (advance: partitioning, advisory lock, row-level security)** | **XU HƯỚNG THẬT (Data/Backend)** | Thay MySQL trong project mới. RLS giúp enforce security ở tầng DB — quan trọng cho compliance VN. |
| **LLM Local (Ollama, vLLM, llama.cpp) + RAG (LangChain/LlamaIndex)** | **XU HƯỚNG THẬT (Cost control, Data sovereignty)** | Khách VN không cho dữ liệu ra cloud. Biết self-host model, eval prompt, guardrail. |
| **Antigravity / Cursor / Claude Code / GitHub Copilot** | **TOOL HỖ TRỢ (Chọn 1–2 làm chủ)** | Đừng học hết. Chọn **Cursor (code editor)** + **Claude Code (CLI agent)** hoặc **Antigravity (Gemini workflow)**. Tập trung vào *workflow review code AI qua PR*. |
| **Rust / Go (viết CLI tool, sidecar, high-perf service)** | **NICE TO HAVE (Senior+)** | Nếu muốn viết security scanner, proxy, agent sidecar hiệu năng cao. Ưu tiên sau khi vững Java/Python. |
| **Blockchain / Web3 / "On-chain lock for AI"** | **HYPE (Niche)** | Dev.to article "The model said yes..." (relevance 40.5) — chỉ áp dụng niche fintech/crypto. Không ưu tiên cho dev mainstream VN. |

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy được cộng đồng nhắc nhiều nhất
1. **Từ "Code chạy là xong" → "Code an toàn, قابل review, có test, có observability"**  
   AI sinh code nhanh → gánh nặng chuyển sang *review, test, secure, monitor*.
2. **Từ "Học theo syllabus" → "Tự thiết kế lộ trình học (Self-curriculum)"**  
   @Xyz-e6x (tier 3 college) kêu cứu guidance → không ai cầm tay. Phải tự phân rã mục tiêu thành *weekly deliverable* (vd: tuần này xong module auth với Spring Security + testcontainers + GitHub Actions).
3. **Từ "Sợ AI thay" → "Dùng AI như Junior dev: giao task nhỏ, review chặt, không cho quyền merge thẳng production"**  
   @DakshChaudhary: AI đắt tiền, hay lỗi → treat như intern có năng lực cao nhưng thiếu context.
4. **Từ "Làm taskassigned" → "Tự tìm vấn đề business, đề xuất giải pháp, làm visible"**  
   Chavdar (exit node): *"Run a training, present what you learned, talk to senior people"* — đây là cách lên lương/position nhanh nhất ở VN.
5. **Từ "Leetcode để pass interview" → "Problem solving để debug production & design system"**  
   @oussamaelwefi2940 hỏi Leetcode còn cần không → Chavdar: *"keep problem solving skills sharp"* nhưng context là *system design/architecture*.

### Cách áp dụng CỤ THỂ cho dev nền **Java/Spring Boot đang học thêm Python & Network Security** (Tuần này làm gì, tránh gì)

| Tuần | Hành động cụ thể (3–5h/tuần) | Tránh |
|---|---|---|
| **Tuần 1** | 1. Setup **Git workflow chuẩn**: `main`/`develop`, branch `feat/`, `fix/`, `security/`; bật *signed commit*, *pre-commit hook* (checkstyle, secret scan).<br>2. Viết **1 script Python** (FastAPI + Pydantic) đọc log Spring Boot → detect anomaly (failed login, SQL error) → alert Telegram/Slack. Dùng `asyncio`, `httpx`.<br>3. Đọc **OWASP Top 10 2023** + **ASVS Level 1** — map sang code Spring Security hiện tại (CSRF, XSS, Rate Limit, Secure Headers). | ❌ Học tool AI mới (Devin, Cursor beta, v.v.)<br>❌ Đọc lý thuyết_network security dày cộm không code |
| **Tuần 2** | 1. **Container hóa** app Spring Boot + Python script bằng Docker Compose. Cấu hình *network isolation*, *read-only filesystem*, *non-root user*, *secret qua Docker secret/env file*.<br>2. Thêm **Integration Test** dùng **Testcontainers** (Postgres, Redis, Kafka) cho flow login/register + rate limit.<br>3. Thử **Vibe Coding có Git**: Mở Cursor/Claude Code → prompt: *"Add rate limiting per IP+user using Bucket4j, write unit+integration test, update OpenAPI spec"*. **Review từng file diff**, commit message chuẩn. | ❌ Copy-paste code AI không hiểu<br>❌ Deploy thẳng production/server thật |
| **Tuần 3** | 1. Học **System Design cơ bản**: Vẽ diagram (C4 model) cho hệ thống vừa build: Spring Boot API, Python Worker, Postgres, Redis, Nginx. Xác định *trust boundary*, *data flow*, *threat model* (STRIDE).<br>2. Cài **OWASP ZAP** hoặc **Trivy** vào CI/CD (GitHub Actions) → scan SAST/DAST/Container image mỗi PR.<br>3. Viết **1 bài blog/note nội bộ** (Markdown trong repo `docs/`) tóm tắt: *"Cách tôi thêm Rate Limit + Security Scan cho Spring Boot app dùng AI assistant"*. Share lên group team/LinkedIn. | ❌ Học Kubernetes phức tạp (chỉ cần Docker Compose cho dev)<br>❌ FOMO cert (CISSP, CEH) — ưu tiên *hands-on* trước |
| **Tuần 4** | 1. **Self-host LLM nhỏ** (Ollama + `codellama:7b` hoặc `qwen2.5-coder:7b`) trên máy local → dùng làm *coding assistant offline* cho code bảo mật (không gửi data ra cloud).<br>2. Tham gia **1 open-source security project** (vn: `owasp-java-html-sanitizer`, `spring-security`, hoặc tool scan секрет `trufflehog`) — đọc code, fix 1 issue `good first issue`.<br>3. Ôn **System Design interview pattern**: *Design a rate limiter*, *Design a URL shortener*, *Design a secure file upload service* — vẽ trên Excalidraw, giải thích trade-off. | ❌ Học fine-tuning model (cần GPU, research)<br>❌ Apply job lung tung — chỉ apply khi có **portfolio GitHub công khai** 3–4 project có CI/CD, test, security config, docs. |

> **Golden Rule**: *Mỗi tuần phải có 1 artifact công khai (code, diagram, blog, PR) chứng minh "tôi hiểu hệ thống + tôi biết dùng AI an toàn + tôi quan tâm bảo mật".*

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

| # | Bình luận (trích dài) | Tác giả / Votes / Insight | Nguồn (Link) | Vì sao đáng đọc |
|---|---|---|---|---|
| 1 | **Home lab → side business pipeline**<br><br>> *"Hey Chavdar, definitely.. I am on the same page with you. Looks like the home lab can be turned into a side business upon see interestig and fun use cases!"* | **@charlieJimi** · 1 vote · **Insight 3.5** | [exit node – "When Work Sucks..."](https://www.youtube.com/watch?v=yBPayq0_3N4) | Khẳng định tư duy *"build in public, build for yourself"* — home lab không chỉ học tập mà là MVP cho side hustle/saas, cực kỳ phù hợp dev VN muốn đa dòng thu nhập. |
| 2 | **Junior cần System Design + Problem Solving, không chỉ syntax**<br><br>> *"Thank you for the video, I now understand that even as a junior I need to have a high level look at things, and learn the system design / architecture more, but I also feel that I need to keep my problem solving skills sharp, what do you think about doing leetcode problems? are they still important? ... but are there other motivators to do it?"* | **@oussamaelwefi2940** · 1 vote · **Insight 2.0** | [exit node – "When Work Sucks..."](https://www.youtube.com/watch?v=yBPayq0_3N4) | Đặt đúng câu hỏi cốt lõi: *Leetcode có còn giá trị?* → Trả lời: Có, nhưng động lực là *debug production, design system*, không phải pass interview. |
| 3 | **Fresher tier 3 college: tự xây curriculum thế nào?**<br><br>> *"Simple question: how to build the fundamentals completely through self study. Context: I am from a tier 3 private college and I can't rely on my college and expect any kind of guidance. I am in 2nd yr and I just have 2.5 yrs left to make my bachelors worth something. My biggest problem is guidance... I tried seeking guidance from social media but it's too overwhelming."* | **@Xyz-e6x** · 2 votes · **Insight 2.0** | [yournishaant – "I Asked 5 Engineers Is Coding Dead"](https://www.youtube.com/watch?v=KbtYW-C3E4M) | Tâm thanh của đa số sinh viên VN (trường không dạy thực chiến). Cần một *roadmap có sequence, có checkpoint, có project thực* — không phải list link lung tung. |
| 4 | **AI như Junior đắt tiền, không thể thay dev hoàn toàn do chi phí & rủi ro**<br><br>> *"Look, I m not a person to do a comment on this Statement that AI will Replace Developers, but what i think is by the time AI will have dedicated budget for a Dev per month as its so costly companies got their yearly budget burnt in 2-3 months. So what I think is AI will be like a Junior dev if its code made production fu*ked up you would be able to make it back alive."* | **@DakshChaudhary-cv8pe** · 2 votes · **Insight 2.0** | [yournishaant – "I Asked 5 Engineers Is Coding Dead"](https://www.youtube.com/watch?v=KbtYW-C3E4M) | Góc nhìn *finance & risk* rất thực tế cho khách hàng VN: chi phí token + rủi ro production → AI chỉ là "intern siêu tốc cần review". |
| 5 | **Giá trị cốt lõi AI ở tầng Research, App layer tool thì commoditize**<br><br>> *"Quan trọng nhất đối với mấy thằng OpenAI/Anthropic vẫn là mấy ông giáo sư, tiến sĩ chịu trách nhiệm nghiên cứu, training AI/LLM ấy. Chứ mấy cái như Claude Code, Claude Desktop, Harness thì nó cũng chỉ là những tools ở tầng app nên ko khó như vậy đâu, nó tìm người mới mấy mấy hồi."* | **Facebook user (J2Team Community)** · 0 vote · **Insight 2.0** | [J2Team – "Hai tuần, bốn người rời Anthropic"](https://facebook.com/groups/j2team.community/permalink/3237292893269475/) | Nhận định đúng đắn cho dev VN: **đừng theo-tool**, hãy học *nguyên lý model, eval, guardrails, system integration* — kỹ năng này chuyển dùng được mọi tool. |

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| # | Tiêu đề + Link | Khu vực | Luận điểm chính / Góc nhìn nổi bật | Lý do chọn |
|---|---|---|---|---|
| 1 | **Future of IT Jobs in 2027: Is Your Job Safe?** (Technical Suneja) — [YouTube](https://www.youtube.com/watch?v=FTluskbqczc) | Quốc tế | Abhishek Dwivedi (15+ năm) chia sẻ: *AI không thay dev, dev biết AI sẽ thay dev không biết AI; System Design + Soft Skill + Continuous Learning là 3 trụ cột.* | **Relevance 86** — Tổng quan toàn diện từ góc nhìn senior thực chiến, phù hợp dev VN định hướng 3–5 năm. |
| 2 | **I Asked 5 Engineers Is Coding Dead** (yournishaant) — [YouTube](https://www.youtube.com/watch?v=KbtYW-C3E4M) | Quốc tế | Senior Engineer 5 năm: *"Layoffs là skill gap in understanding, not syntax. Học: Fundamentals, DSA, Projects, Internships, System Design, đọc trend không theo trend."* | **Expert 3.0, Relevance 59** — Lời khuyên cụ thể cho fresher/junior: học gì, học như thế nào, tránh bẫy FOMO. |
| 3 | **When Work Sucks and AI Doom Won't Shut Up** (exit node) — [YouTube](https://www.youtube.com/watch?v=yBPayq0_3N4) | Quốc tế | Chavdar (Engineer → Manager → Director AI): *4 hành động sinh tồn: (1) Tìm việc ngầm, (2) Kết bạn cross-team, (3) Không cho manager khó tính lý do, (4) Làm visible work (training, demo, talk to seniors).* | **Expert 1.5, Relevance 55.7** — Tư duy "survival + growth" trong môi trường toxic/layoff — áp dụng ngay cho dev VN ở môi trường áp lực. |
| 4 | **How do juniors become seniors with AI** (Deric Yee) — [YouTube](https://www.youtube.com/watch?v=dGJp9VXEpVI) | Quốc tế | *"Senior + AI làm được việc Junior. Vậy Junior học gì để thành Senior?"* → Cần *ownership, architectural thinking, AI supervision skill*. | **Expert 3.0, Relevance 40.6** — Đặt ra bài toán cốt lõi cho pipeline nhân sự VN: junior phải tự tạo cơ hội "làm việc cấp senior" ngay từ bây giờ. |
| 5 | **Hai tuần, bốn người rời Anthropic: Claude Code team sang OpenAI** (J2Team) — [Facebook](https://facebook.com/groups/j2team.community/permalink/3237292893269475/) | Việt Nam | Dòng chảy talent top-tier集中 ở *Research*, *App-layer tool (Claude Code) dễ thay thế*. Bình luận insight: *"Giá trị cốt lõi là researcher, tool app layer thì commoditize."* | **Expert 3.0, Community Lane, Relevance 38** — Tín hiệu rõ nhất từ cộng đồng VN về đâu là "bền vững" vs "hype" trong AI. |
| 6 | **Series Git Siêu Dễ + Vibe Coding An Toàn** (Hỏi Dân IT) — [YouTube Playlist](https://www.youtube.com/watch?v=r_4pDELxZz8) | Việt Nam | Hướng dẫn *từng bước*: Git flow cho AI coding, Antigravity IDE, Gemini CLI, cách review/fix lỗi AI sinh ra. | **Relevance 51–52** — **Tài liệu thực hành duy nhất tiếng Việt** dạy "code với AI nhưng không mất code/hỏng code" — bắt buộc cho fresher/junior VN. |
| 7 | **Nhu cầu tuyển dụng lập trình viên vẫn tăng dù đã có AI** (VnEconomy) — [Google News](https://news.google.com/rss/articles/CBMilgFBVV95cUxORUI4YkdyZG5mUy1MbDJzMVhReFc2amN4Y2hzZVczVFZMNUo1Ujhra1V2TktOWTU2dExPTWcxTlNKWGlfc0t5NnNFcW5yWGxTdWVuRXdwNnQwNGFEcV9IRGc1QzEtWkoyckJLY0tZT0RNOVpQQWhhUlhuaGlLRTRidlNBWnduNE1qNFlrSlF4XzZ0UUlHZ3c) | Việt Nam | Báo cáo thị trường VN: *AI tạo ra việc mới (prompt engineer, AI integrator, AI security) > việc mất đi. Doanh nghiệp cần dev "biết dùng AI + chuyên môn sâu".* | **Relevance 34** — Dữ liệu thực tế VN chống lại narrative "AI ăn việc IT". |
| 8 | **BÍ QUYẾT VƯỢT QUA PHỎNG VẤN ANZ SAU KHÓA HỌC ENGINEER PRO** (Viblo) — [Article](https://viblo.asia/p/bi-quyet-vuot-qua-phong-van-anz-sau-khoa-hoc-engineer-pro-PoL7eOKe4vk) | Việt Nam | Case study: 5 năm exp → pass ANZ (ngân hàng lớn) nhờ *system design, clean code, security awareness, behavioral interview*. | **Expert 1.5, Relevance 35.5** — Benchmark thực tế cho dev VN muốn vào enterprise/banking: họ hỏi gì, đánh giá như thế nào. |

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục dữ liệu nào có `is_major_incident = true` trong batch này. Bỏ qua mục 6.*