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

## 2. Chuẩn Hóa & Định Dạng Báo Cáo

- **Chuẩn hóa dữ liệu:** Tự động loại bỏ các tham số theo dõi (UTM, fbclid), lọc bỏ thẻ HTML và deduplicate trùng lặp bài viết.
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
