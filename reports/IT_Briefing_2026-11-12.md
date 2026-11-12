📑 **Google Docs (bản đã chuẩn hóa, dễ đọc):** [Mở Google Docs hôm nay](https://docs.google.com/document/d/10syAjctsVTj-hme3sU3hkQs5aF1ILKv6LWBYt0-7PIs/edit?tab=t.msx2crzgqfl4)

---

# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY

### Tại Việt Nam
- **Thị trường tuyển dụng đang "thanh lọc" chứ không "hết thời"**: Phân tích 149.360 tin tuyển dụng 2021–2026 (kênh *Học Lập Trình cùng Phát*) cho thấy cầu việc làm IT vẫn tăng, nhưng phân cực: **AI/ML, Cloud, DevOps, Data** lên mạnh; **Web/App thuần túy, outsourcing (gia công) truyền thống** bị ép biên. Video *Siêu Kiến Thức* xác nhận: "bong bóng tuyển dụng sau Covid vỡ, lương đi xuống, tiêu chuẩn khắt khe, cung vượt cầu ở fresher/junior".
- **Junior/Fresher gặp "mùa đông" thực sự**: Bình luận của `@nicky_s` (insight_score 1.0) là minh chứng sống động — bị từ chối ngay phỏng vấn, thất nghiệp lâu, áp lực tâm lý lớn. Điều này khớp với dữ liệu globale: job postings giảm 65% so với đỉnh 2022 (*Synthetic Era*), gánh nặng dịch sang khâu review (thời gian review PR tăng 441%).
- **Công ty Việt Nam đang chuyển từ "thuê người viết code" sang "thuê người giải quyết bài toán với AI"**: Chia sẻ EditAtlas (MCP server cho agent dựng video/âm thanh) trên J2TEAM Community cho thấy xu hướng **tooling cho AI agent** đang nổi lên tại VN. Bài Viblo về *retry/timeout/idempotency cho AI agent* khẳng định: khi agent gọi công cụ thay đổi dữ liệu (hoàn tiền, đặt hàng...), kỹ thuật **hệ thống đáng tin cậy** trở thành yêu cầu bắt buộc.

### Trên thế giới (và ý nghĩa với Việt Nam)
- **AI không giết nghề lập trình, nó di chuyển nút thắt cổ chai**: 40% PR trên GitHub bắt đầu bằng draft của AI, nhưng *developer giàu kinh nghiệm tin AI giúp nhanh 20% — thực tế lại chậm 19%* do phải review nhiều hơn (*Synthetic Era*). **Ý nghĩa VN**: Không cần lo "thay thế", cần lo "review code AI sinh ra" — kỹ năng **đọc hiểu, kiểm chứng, kiến trúc, bảo mật** sẽ đắt giá hơn kỹ năng gõ code nhanh.
- **Sa thải do overhiring & tái cấu trúc, không chỉ do AI**: Meta, Uber, Amazon cắt giảm vì thuê quá nhiều 2020–2022 và ép hiệu suất (*The Signal Tech*). **Ý nghĩa VN**: Các outsourcer VN đang bị khách hàng Mỹ/EU ép giảm team size, yêu cầu density (sản lượng/người) cao hơn — dev phải chứng minh **giá trị business/feature**, không chỉ ticket closed.
- **Tuyển dụng Mỹ tăng 15% từ 2/2025 dù AI viết code hàng loạt** (Vietnam.vn, VietNamNet, VnEconomy). **Ý nghĩa VN**: Cầu việc làm *chuyển dịch* sang vai trò "AI-augmented engineer" — người biết prompt, biết gắn tool, biết eval output, biết fallback khi agent lỡ.
- **Optimize for slope (độ dốc học tập), not salary** (*John Kim*): Nhảy việc +$20k/năm thường khiến dừng lại ở Senior/Staff vì vấn đề khó & niềm tin lead chỉ đến sau ~3 năm ở một chỗ. **Áp dụng VN**: Dev 2–4 năm kinh nghiệm nên ở lại проекта đủ sâu để gặp *hard problems* thay vì job-hop theo lương.
- **United Airlines cấm AI agent đặt vé** (*Hacker News*). **Ý nghĩa VN**: Enterprise chưa tin AI agent tự quyết định rủi ro cao → vai trò **human-in-the-loop, guardrails, observability** sẽ được tuyển nhiều.

---

## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ

| Kỹ năng / Công nghệ | Vì sao quan trọng | Nguồn / Bằng chứng |
|---|---|---|
| **Kiến trúc & Review code sinh bởi AI** | Bottleneck đã dịch sang review (PR review time +441%). Phải đọc hiểu, bắt bug logic, security, performance của code AI. | *Synthetic Era* (relevance 57.4), *The Signal Tech* |
| **Prompt engineering + Tool calling / MCP / Agent orchestration** | Xu hướng "AI agent làm việc" (EditAtlas, Viblo retry/idempotency). Cần biết thiết kế prompt, gán tool, xử lý lỗi lặp, idempotency. | *EditAtlas (J2TEAM, relevance 62.6)*, *Viblo (relevance 34)* |
| **System design, Observability, Reliability (retry, timeout, circuit breaker, idempotency)** | Khi agent tự gọi API/thay đổi DB, hệ thống phải chịu đựng được lỗi mạng, duplicate request. | *Viblo article* |
| **Python cho AI/ML & Data** | Phát dùng Python phân tích 149k job; AI/ML roles tăng nhanh nhất tại VN. Python là lingua franca của AI tooling. | *Phát video (relevance 53)*, *Siêu Kiến Thức* |
| **Cloud (AWS/GCP/Azure), Kubernetes, Terraform** | Công nghệ "đi lên" nhất trong data 2021–2026 tại VN. | *Phát video* |
| **Network Security / API Security / AppSec** | Target persona đang học: Java/Spring Boot + Python + Network Security. Enterprise cần người hiểu cả code path lẫn network path để hardening. | *Bối cảnh người đọc*, *United Airlines ban* |
| **Business thinking & Communication** | Các level Senior/Staff/CTO tại *KaiPov* đều nhấn mạnh: hiểu business, trade-off, nói chuyện với stakeholder. | *KaiPov (expert_voice 3.0)* |
| **Data analysis cơ bản (SQL, Pandas, visualization)** | Tự phân tích market, log, metric thay vì chờ team data. Phát tự làm pipeline phân tích job market. | *Phát video (comment insight 2.0 chia sẻ repo)* |

**Phân biệt xu hướng thật vs hype**:
- **Thật**: AI-augmented workflow, system reliability cho agent, cloud-native, security, data-driven decision.
- **Hype**: "No-code thay dev", "Agent tự động hóa一切" (United Airlines đã cấm), "Vibe coding không cần hiểu code" (PhD stats trên Lemmy than thở: "chỉ ấn nút thay vì tư duy").

---

## 3. TƯ DUY & CÁCH ÁP DỤNG

### Thay đổi tư duy cốt lõi
1. **Từ "làm task xong" → "giải quyết bài toán end-to-end với AI làm copilot"**: Biết khi nào dùng AI, khi nào tự viết, cách eval output, cách fallback.
2. **Từ "học framework mới" → "học nguyên lý hệ thống (retry, idempotency, observability, security)"**: Framework thay, nguyên lý ở lại — Viblo article là ví dụ điển hình.
3. **Từ "job-hop cho lương" → "chọn project/team cho slope học tập"**: Theo *John Kim*, 3 năm ở một chỗ mới được giao hard problem & trust để lên Staff.
4. **Từ "code sạch" → "code có thể verify, audit, rollback"**: AI sinh code nhanh, nhưng phải review được → viết code/test/log sao cho *dễ review*.

### Áp dụng cụ thể cho dev **Java/Spring Boot đang học Python + Network Security** (tuần này)
| Thứ | Hành động cụ thể | Mục tiêu |
|---|---|---|
| 2 | Viết **một script Python** gọi LLM API (OpenAI/Anthropic) + **tool calling** (ví dụ: `nmap` scan port, `curl` check header) → in kết quả có cấu trúc. | Hiểu luồng agent-tool, prompt engineering cơ bản. |
| 3 | Thêm **retry với exponential backoff + idempotency key** cho script trên (tham khảo Viblo article). Test case: network đứt, API trả 5xx, duplicate request. | Nắm pattern reliability cho agent. |
| 4 | Dùng **Spring Boot** expose một endpoint nhận webhook từ script Python → lưu kết quả scan vào DB, có **audit log** (ai, khi nào, request/response). | Kết hợp stack cũ + mới, tư duy audit/security. |
| 5 | Đọc **một PR thật** trong project opensource (hoặc code review nội bộ) — tập *chỉ đọc, không sửa*, ghi chú: chỗ nào AI có thể sinh sai, test case nào thiếu. | Train kỹ năng review code AI sinh. |
| 6–7 | Xem **video Phát (phân tích 149k job)** + clone repo GitHub của anh ấy → chạy notebook, tự vẽ biểu đồ: top 10 skill Java + Security tại VN 2025. | Data-driven chọn skill tiếp theo, tập Python/Pandas. |

**Tránh**: Học vội framework AI mới (LangChain, LlamaIndex...) mà chưa nắm vững HTTP, JSON, retry, auth, observability.

---

## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT

> Chỉ có 2 bình luận có `insight_score > 0` trong toàn bộ dữ liệu. Cả hai đều trên video của **Phát (Học Lập Trình cùng Phát)**.

| # | Bình luận (trích đầy đủ) | Tác giả / Votes / Insight | Video / Link | Tại sao đáng đọc |
|---|---|---|---|---|
| 1 | **"Toàn bộ code phân tích và dữ liệu của video nằm ở đây nha: Trong repo có pipeline xử lý, các notebook phân tích và bộ số liệu tổng hợp theo từng năm (vai trò, cấp bậc, thành phố, hình thức làm việc và công nghệ), các bạn có thể tải về để tự vẽ lại biểu đồ hoặc phân tích thêm nha! Cảm ơn các bạn rất nhiều!"** | `@TranSonPhat` (chủ kênh) · 3 votes · **insight_score 2.0** | *Phân tích 149,360 việc làm IT Việt Nam 2021-2026*<br>https://www.youtube.com/watch?v=gRSzxR2CAIY | **Dữ liệu thô + pipeline sẵn sàng** — bạn có thể tự verify xu hướng, không chỉ tin lời video. Cực kỳ quý cho dev muốn data-driven career. |
| 2 | **"Thực sự hôm nay em bị từ chối ngay trong phỏng vấn, sốc và thất vọng về bản thân thực sự anh ạ. Đã rất lâu rồi chưa có việc làm, sống bám vào bố mẹ xấu hổ quá"** | `@nicky_s` · 5 votes · **insight_score 1.0** | Cùng video trên | **Thực tế khốc liệt của junior market** — không phải số liệu, là con người. Nhắc nhở: chuẩn bị kỹ lưỡng, tâm lý bền bỉ, có plan B (freelance, project cá nhân, upskill mục tiêu). |

*Lưu ý*: Các video toàn cầu (Synthetic Era, John Kim, The Signal Tech, KaiPov...) có bình luận nhưng `insight_score = 0` — chủ yếu là reaction, ít insight nghề nghiệp sâu.

---

## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY

| # | Nguồn | Loại / Vùng | Luận điểm chính & Góc nhìn nổi bật | Lý do chọn |
|---|---|---|---|---|
| 1 | **Phân tích 149.360 việc làm IT Việt Nam 2021-2026** | Video [VN] | Dữ liệu thực tế 6 năm: tech nào lên/xuống, lương, địa điểm, junior opportunity, AI roles. Có repo mở để tự phân tích. | **Cơ sở dữ liệu lớn nhất về VN**, relevance 53, có insight_comment 2.0. |
| 2 | **Is Coding Dead? What the 2026 Hiring Data Actually Shows** (Synthetic Era) | Video [Quốc tế] | 40% PR do AI draft, dev giàu kinh nghiệm chậm 19% do review, PR review time +441%. Coding không chết — bottleneck dịch sang *verify & integrate*. | **Số liệu GitHub/Indeed/Stanford** xác thực, relevance 57.4, incident_severity 2.0 (dữ liệu nóng). |
| 3 | **Optimize For Slope, Not Salary — Day 26** (John Kim) | Video [Quốc tế] | Đừng nhảy việc cho +$20k; 3 năm mới gặp hard problem & trust để lên Staff/Principal. Slope học tập > salary jump. | **Triết lý career dài hạn** phù hợp dev VN hay job-hop, relevance 56.6. |
| 4 | **Why Are Software Engineers Getting Laid Off?** (The Signal Tech) | Video [Quốc tế] | Layoff do overhiring + restructuring + AI productivity, không chỉ AI replace. Meta, Uber, Amazon case study. | **Phân biệt nguyên nhân** rõ ràng, relevance 56.5. |
| 5 | **Level Up Your Software Engineering Career** (Polance) | Video [Quốc tế] | Dịch vụ coaching cho mid/senior dev vào thị trường US: resume, interview, on-the-job support. **Expert voice 4.5** (chuyên gia career). | **Góc nhìn employer/coach** cấp cao, relevance 52.8. |
| 6 | **Your Life at Every Level of a Fullstack Developer** (KaiPov) | Video [Quốc tế] | 7 cấp độ từ self-taught → CTO: trách nhiệm, lương, pain point, bài học. **Expert voice 3.0** (senior content creator). | **Roadmap hình dung rõ** từng level, relevance 45. |
| 7 | **Lập trình viên năm 2026: AI cướp việc hay cơ hội mới?** (Siêu Kiến Thức) | Video [VN] | Bong bóng vỡ, outsourcing áp lực, fresher khủng hoảng, lương giảm, tiêu chuẩn cao. | **Tóm gọn bối cảnh VN** nhanh, relevance 47. |
| 8 | **Retry, timeout và idempotency cho AI agent** (Viblo) | Article [VN] | Khi agent gọi tool thay đổi state (payment, booking), bắt buộc có retry/timeout/idempotency. Code mẫu Java/Kotlin. | **Kỹ thuật hệ thống cho AI agent** — ít ai nói, relevance 34. |
| 9 | **EditAtlas - MCP server cho AI agent edit video/âm thanh** (J2TEAM) | Facebook [VN] | Tool thực tế: 2000+ kỹ thuật dựng, 2300+ SFX, skill local cho agent. Cộng đồng VN quan tâm lớn. | **Case study AI agent production** tại VN, relevance 62.6. |
| 10 | **AI viết mã hàng loạt nhưng tin tuyển dụng lập trình viên tại Mỹ vẫn tăng gần 15% từ 2/2025** (Vietnam.vn / VietNamNet / VnEconomy) | News [VN] | 3 bài báo độc lập xác nhận hiring tăng dù AI code. Cầu dịch sang vai trò augmented. | **Tín hiệu macro** tích cực, relevance 36/34. |

> **English reference**:  
> > "More than 40% of pull requests on GitHub now start with an AI agent's draft... experienced developers believed AI made them 20% faster — and actually took 19% longer. Median pull-request review time jumped 441%." — *Synthetic Era, "Is Coding Dead? What the 2026 Hiring Data Actually Shows"*  
> > "Optimize for learning instead: the more learning opportunities you have, the more your career's long-term output grows, and it gets exponential." — *John Kim, "Optimize For Slope, Not Salary"*

---

## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
*Không có mục nào trong dữ liệu có `is_major_incident = true` → bỏ qua mục này.*