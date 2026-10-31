# IT Market & Career Survival Tracker

Hệ thống tự động thu thập thông tin thị trường IT hàng ngày, tổng hợp phân tích xu hướng và cẩm nang phát triển nghề nghiệp, gửi báo cáo qua Gmail kèm liên kết Google Docs và lưu trữ lịch sử báo cáo định dạng Markdown.

---

## 1. Nguồn Dữ Liệu Theo Dõi

- **Việt Nam:**
  - YouTube Channels: Hỏi Dân IT, Tips Javascript, Tôi Đi Code Dạo.
  - Tech Blogs & Portals: Viblo, TopDev Blog.
- **Quốc Tế:**
  - YouTube Channels: Fireship, ThePrimeTime, ByteByteGo.
  - Diễn đàn & Cộng đồng kỹ sư: Hacker News, Reddit (r/ExperiencedDevs, r/cscareerquestions, r/programming), Dev.to.

---

## 2. Lọc Theo Chủ Đề & Chuẩn Hóa Báo Cáo

- **Chấm điểm liên quan (mới):** Mọi mục thu về đều qua `src/filters/relevance.py` — chấm điểm theo 3 nhóm chủ đề trong `config/sources.json` (`thi_truong_tuyen_dung`, `ai_va_huong_di_moi`, `career_survival`), khớp từ khóa không phân biệt dấu tiếng Việt. Chỉ mục đạt ngưỡng (`relevance.min_score`, mặc định 25) mới vào báo cáo, kèm lý do chọn (`score_reason`). Tutorial/khóa học không khớp chủ đề sẽ bị loại.
- **Nguồn thu thập:** Hacker News chuyển sang tìm kiếm theo từ khóa (Algolia, 7 ngày gần nhất) thay cho top stories toàn cục; Reddit nới cửa sổ lên 7 ngày + lọc từ khóa; RSS lọc theo ngày xuất bản; YouTube lấy transcript trước, cắt dòng quảng cáo/khóa học trong description, bình luận sắp theo số votes thật.
- **Tổng hợp:** Gemini chỉ nhận 20 mục điểm cao nhất và viết theo 5 mục: thị trường dịch chuyển → góc nhìn/tranh luận cộng đồng → bình luận đắt giá → hướng đi mới & việc nên làm → nguồn nên xem. Nếu Gemini lỗi, báo cáo chèn **cảnh báo fallback** ở đầu thay vì im lặng. Model mặc định: `gemini-3.8-flash` (model Flash hiện hành, GA 2026-09); dự phòng lần lượt `gemini-3.6-flash`, `gemini-3.5-flash-lite`. Lưu ý: dòng Gemini 2.5 đã bị giới hạn cho người dùng cũ từ 2026-09-18 nên API key mới không gọi được. Code thử cả generateContent lẫn Interactions API cho từng model. Nếu Gemini lỗi hết, pipeline tự chuyển sang chuỗi dự phòng **OpenCode Zen** (`deepseek-v4.1-flash-free` → `glm-5.3-flash-free` → `mimo-v2.6-flash-free`, cần secret `OPENCODE_API_KEY`, đổi danh sách qua `OPENCODE_MODELS`). Lưu ý: model free của Zen bị giới hạn chỉ trong app OpenCode từ 2026-09 nên gọi từ GitHub Actions có thể bị 403/429 — log sẽ ghi rõ từng model; Zen trả phí / OpenCode Go thì gọi API bình thường qua cùng đường này. Cả hai nhà cung cấp đều lỗi mới dùng báo cáo fallback cục bộ.
- **Chuẩn hóa dữ liệu:** Tự động loại bỏ các tham số theo dõi (UTM, fbclid), lọc bỏ thẻ HTML và deduplicate trùng lặp bài viết.
- **Bình luận định hướng là trọng tâm (PR #2):** Bình luận YouTube lấy qua **YouTube Data API v3** (secret `YOUTUBE_API_KEY`, miễn phí — đường scrape cũ gọi sai tham số `sort=` nên luôn trả 0 bình luận, nay là dự phòng có giới hạn). Bình luận được chấm điểm *giá trị định hướng* (insight: nên học gì, kỹ năng, business, tư duy...) và báo cáo mở đầu bằng mục bình luận định hướng hay nhất; prompt tổng hợp xoay quanh: hướng đi của ngành → cần học gì (kỹ năng + công nghệ) → tư duy & cách áp dụng. Link Google Docs được gắn vào đầu mọi bản báo cáo đã phát hành.
- **Google Docs dễ đọc (mới):** Phía Python chuyển markdown thành định dạng Docs thật (heading, bullet, in đậm, link, trích dẫn) qua `src/publishers/markdown_to_docs.py`; Apps Script dự phòng cũng parse từng dòng tương tự — không còn nhét markdown thô.
- **Song ngữ Việt - Anh:** Toàn bộ nội dung phân tích, nhận định và hướng dẫn hành động bằng Tiếng Việt; trích dẫn và thuật ngữ gốc bằng Tiếng Anh đặt ngay bên dưới (`> English reference: ...`).
- **Lưu trữ & Phân phối:**
  - Tạo văn bản Google Docs trực tuyến trên Google Drive.
  - Gửi bản tin HTML chuyên nghiệp qua Gmail kèm banner link Google Docs.
  - Lưu file Markdown trong thư mục `reports/`.

---

## 3. Hướng Dẫn Cấu Hình GitHub Actions (Tự động chạy mỗi ngày)

Đưa dự án lên GitHub và vào mục **Settings > Secrets and variables > Actions > New repository secret**:

| Tên Secret | Ý nghĩa | Bắt buộc |
| :--- | :--- | :--- |
| `GEMINI_API_KEY` | API Key miễn phí từ Google AI Studio | Có |
| `GMAIL_USER` | Tài khoản Gmail dùng để gửi báo cáo | Có |
| `GMAIL_APP_PASSWORD` | Mật khẩu ứng dụng 16 ký tự của Gmail | Có |
| `RECIPIENT_EMAIL` | Hòm thư nhận báo cáo mỗi ngày | Có |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | JSON Credentials của Google Cloud Service Account để tạo Google Docs | Tùy chọn |

Workflow `.github/workflows/daily_briefing.yml` sẽ tự động kích hoạt vào lúc **06:30 AM (Giờ Việt Nam)** mỗi ngày. Bạn cũng có thể bấm **Run workflow** thủ công bất kỳ lúc nào trên tab Actions.

---

## 4. Chạy Thử Nghiệm Tại Máy Cục Bộ

1. Cài đặt các gói phụ thuộc:
```powershell
pip install -r requirements.txt
```

2. Tạo file `.env` từ `.env.example`:
```powershell
Copy-Item .env.example .env
```

3. Chạy chế độ Dry-run (không gọi API bên ngoài):
```powershell
py src/main.py --dry-run
```

4. Chạy toàn diện:
```powershell
py src/main.py
```

5. Chạy bộ kiểm thử tự động:
```powershell
py -m unittest discover tests
```
