# Cho ChatGPT tự đọc bản tin & cập nhật lộ trình — cài 1 lần, tự động mãi

## Cơ chế

1. Pipeline bản tin ngày chạy như cũ. Mỗi sáng thứ Hai, một bản **digest tuần**
   được sinh tự động tại `reports/digests/LATEST.md` (đường link cố định, nội
   dung luôn mới nhất) + bản lưu theo tuần `ROADMAP_DIGEST_<năm>-W<tuần>.md`.
2. Trong ChatGPT (gói Go có **Scheduled Tasks**: tối đa 3 task, chạy theo
   khung giờ), bạn tạo **1 task duy nhất** chạy sáng thứ Hai: nó tự mở link
   LATEST.md, đọc digest và cập nhật lộ trình trong cuộc hội thoại đó, rồi
   thông báo cho bạn. Sau lần cài này, bạn không phải làm gì thêm.

Link digest cố định (repo public, không cần đăng nhập để đọc):

```
https://raw.githubusercontent.com/luongduyenhop/breaksNew/main/reports/digests/LATEST.md
```

## Cài đặt trong ChatGPT (khoảng 2 phút, làm 1 lần)

1. Mở chatgpt.com → mục **Scheduled** ở thanh bên (hoặc mở 1 chat mới và gõ
   yêu cầu tạo task như bước 2).
2. Tạo task mới với nội dung ở mục "Prompt cho task" bên dưới, lịch chạy:
   **hằng tuần, sáng thứ Hai** (gói Go chọn theo khung giờ buổi sáng).
3. Bật thông báo (Settings → Notifications → Push/Email) để nhận kết quả.
4. Kiểm tra ngay lần đầu bằng nút chạy thử (Run now) nếu có — ChatGPT phải
   mở được link và tóm tắt đúng nội dung digest. Nếu nó báo không mở được
   link, báo lại cho Muse để đổi phương án (API).

## Prompt cho task (dán nguyên văn)

```
Mỗi sáng thứ Hai, hãy mở và đọc toàn bộ nội dung tại link này:
https://raw.githubusercontent.com/luongduyenhop/breaksNew/main/reports/digests/LATEST.md

Đó là digest tuần tổng hợp tín hiệu thị trường IT Việt Nam & quốc tế (ưu tiên
lời khuyên từ senior, tech lead, project manager), trong đó tín hiệu lặp lại
nhiều ngày được đánh dấu là xu hướng.

Hồ sơ của tôi: dev nền Java/Spring Boot, đang học Python hướng network
programming & network security (phân tích gói tin, phát hiện tấn công tầng
TCP như SYN flood/port scan). Thị trường mục tiêu: Việt Nam.

Nhiệm vụ của bạn trong mỗi lần chạy:
1. Nếu đây là lần chạy đầu: hãy xây dựng LỘ TRÌNH PHÁT TRIỂN NGHỀ NGHIỆP cho
   tôi theo giai đoạn (tháng/quý) dựa trên digest: mỗi giai đoạn gồm mục
   tiêu, kỹ năng + công nghệ cụ thể, dự án minh chứng cần làm, tiêu chí tự
   đánh giá. Cuối cùng cho tôi checklist việc cần làm trong 2 tuần tới.
2. Các lần sau: HIỆU CHỈNH lộ trình đã có theo digest mới — giữ nguyên phần
   còn đúng, chỉ sửa phần lỗi thời, và nói rõ "thay đổi gì, vì tín hiệu nào
   trong digest (nguồn/ai nói)". Ưu tiên tín hiệu lặp lại nhiều ngày; không
   chạy theo tin nóng 1 ngày. Kết thúc bằng checklist 2 tuần tới đã cập nhật.
3. Phân biệt kỹ năng sống còn dài hạn (tư duy hệ thống, hiểu nghiệp vụ, bảo
   mật nền tảng) với xu hướng ngắn hạn (tool/framework đang nóng) và ưu tiên
   nguồn lực cho nhóm đầu.
4. Nếu không mở được link hoặc link rỗng, hãy báo rõ cho tôi thay vì bịa
   nội dung.
Trình bày bằng tiếng Việt, gọn, dễ hành động.
```

## Lưu ý

- Gói Go giới hạn 3 scheduled tasks — task này dùng 1 slot.
- Digest chỉ chứa dữ liệu tối đa 7 ngày gần nhất; qua các tuần, ChatGPT dựa
  vào chính cuộc hội thoại lộ trình để nhớ tiến trình dài hạn, nên đừng xóa
  cuộc hội thoại/task này.
