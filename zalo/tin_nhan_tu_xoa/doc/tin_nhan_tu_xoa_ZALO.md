

| \# | Business rule | Đánh giá | Nguồn | Cách kiểm chứng thêm |
| ----- | ----- | ----- | ----- | ----- |
| **BR1** | Đếm từ GỬI hay ĐỌC? | **Từ lúc GỬI** — độ tin cậy CAO | ZaX.app (mô tả cơ chế: xóa đúng 1 ngày sau khi gửi); eSMS.vn nói "từ khi đọc" — độ tin cậy THẤP (bài SEO, lệch với thang đo theo ngày của Zalo) | Gửi tin, không đọc ở máy nhận, canh giờ xem tự xóa theo mốc nào |
| **BR2** | Đồng bộ đa thiết bị | Có ngụ ý đồng bộ, nhưng cần thận trọng | VietnamNet (tính năng bật với 100% người dùng, cả di động/PC); Tinhte.vn (người dùng phàn nàn lỗi đồng bộ Zalo nói chung) | Bật ở 1 thiết bị, xem thiết bị còn lại đồng bộ đúng không |
| **BR3** | Xử lý khi offline | Chưa có tài liệu chính thức — giả thuyết | Tinhte.vn (bình luận: Zalo không lưu server, chỉ lưu trên thiết bị) | Tắt mạng máy nhận qua mốc xóa, đo độ trễ khi online lại |
| **BR4** | Theo hội thoại, có hồi tố không | **Theo từng hội thoại, KHÔNG hồi tố** — độ tin cậy CAO | ZaX.app; Điện Máy Chợ Lớn (hội thoại chưa bật vẫn ở chế độ mặc định) | Bật giữa chừng, quan sát tin cũ có bị ảnh hưởng không |
| **BR5** | Ngoại lệ ảnh/file | 2 cơ chế xóa file dễ nhầm: tự xóa theo cấu hình vs. server tự dọn file cũ \~2 tháng (độc lập) | Cuumaytinh.com (lỗi 508, dọn file server sau \~2 tháng) | Test file trong 2 tình huống tách biệt |
| **BR6** | Thông báo 2 bên | **Có, độ tin cậy CAO** | Znews.vn; VietnamNet (cùng thông cáo 19/11/2021) | Quan sát 2 màn hình cùng lúc |
| **BR7** | Không khôi phục được | **Đúng, độ tin cậy TRUNG BÌNH-CAO** | ZaX.app; Fastcare.vn (để phân biệt với khôi phục thủ công trong 5 giây) | Thử Sao lưu & khôi phục sau khi tin tự xóa biến mất |
| **BR8** | Ai đổi được cài đặt | Cả 2 phía đổi/tắt được bất cứ lúc nào | Điện Thoại Giá Kho; MediaMart.vn; Điện Máy Chợ Lớn | Test đổi từ cả 2 tài khoản |

**Về chống screenshot:** theo PLO/Tuổi Trẻ (Kỷ Nguyên Số), người nhận vẫn lưu/chia sẻ được nội dung trước khi tin tự xóa — hạn chế tương tự Signal/Telegram/WhatsApp.

Pain-point

### **PP3: Không chống được screenshot/lưu trước hạn**

**Bản chất vấn đề**: Tính năng "tin nhắn tự xóa" của Zalo chỉ giải quyết bài toán **lưu trữ lâu dài** — tức là đảm bảo nội dung không còn tồn tại vĩnh viễn trong lịch sử trò chuyện sau một khoảng thời gian nhất định (1/7/30 ngày). Nhưng nó **không giải quyết được bài toán rò rỉ tức thời** — tức là khoảng thời gian từ lúc tin được gửi đến lúc nó tự xóa, người nhận hoàn toàn có đủ thời gian và công cụ để giữ lại nội dung đó theo ý muốn.

**Các cách người nhận vẫn có thể "cứu" nội dung trước khi tin biến mất:**

* Chụp màn hình (screenshot) — Zalo không có cơ chế phát hiện hay cảnh báo khi bị chụp màn hình (khác với Snapchat từng làm điều này).  
* Copy văn bản ra ứng dụng ghi chú/tin nhắn khác.  
* Chuyển tiếp (forward) tin nhắn sang một cuộc trò chuyện khác — bản chuyển tiếp không chịu ràng buộc bởi cấu hình tự xóa của cuộc trò chuyện gốc.  
* Chụp ảnh màn hình bằng một thiết bị khác (camera ngoài) — cách này không app nào chống được, kể cả Signal.

**Nguồn xác nhận**: PLO/Tuổi Trẻ (chuyên mục Kỷ Nguyên Số) lưu ý rằng dù tính năng tự xóa được kích hoạt, người nhận vẫn có thể lưu lại hoặc chia sẻ nội dung tin nhắn trước khi nó tự động biến mất

**In-scope**: Cảnh báo rõ trong UI về giới hạn tính năng; chặn screenshot nội bộ (kỹ thuật `FLAG_SECURE`); cập nhật Help Center.

**Out-of-scope**: Chặn người dùng chụp bằng máy/camera khác (analog hole) — vì đây là giới hạn vật lý, không công nghệ nào giải được, kể cả Signal.

.

### **PP1: Không có tính năng cho group chat**

**Root cause (5 Whys rút gọn):**  
 Tại sao chưa có? → Vì mở rộng sang nhóm phức tạp hơn nhiều so với 1-1 (phải đồng bộ trạng thái xóa cho N thành viên, xử lý người rời/vào nhóm giữa chừng, xử lý tin nhắn đã tồn tại trước khi có người mới) → Vì độ phức tạp kỹ thuật cao hơn hẳn so với lợi ích cảm nhận ngắn hạn → **Root cause: đây là vấn đề ưu tiên hóa roadmap (đã hứa từ 2021 nhưng liên tục bị đẩy lùi), không phải giới hạn kỹ thuật bất khả thi** — khác hẳn PP3, đây là bài toán **giải được**, chỉ là chưa được đầu tư.

**Problem Statement:**

> Vì tính năng tự xóa chưa được mở rộng sang nhóm chat dù đã cam kết từ 2021, nên nhóm người dùng có nhu cầu trò chuyện nhóm nhạy cảm (công việc, gia đình) không có lựa chọn bảo vệ riêng tư tương đương, dẫn đến bất lợi cạnh tranh so với Telegram/WhatsApp/Signal vốn đã hỗ trợ đầy đủ.

> 

> **In-scope**: Áp dụng tự xóa cho nhóm nhỏ (ví dụ dưới 20 thành viên) trước, xử lý case đơn giản (không có người vào/ra giữa chừng).

> **Out-of-scope** (ở giai đoạn đầu): Xử lý case phức tạp như nhóm cực lớn, người mới vào nhóm có thấy tin cũ trước khi rời không — để dành cho phiên bản sau (v2).

> 

### **PP2: Phạm vi thời gian bắt đầu xóa quá dài (chỉ có 1/7/30 ngày, không có mốc ngắn hơn)**

**Root cause:**  
 Tại sao chỉ có 3 mốc theo ngày, không có mốc theo giờ/phút? → Vì mục tiêu thiết kế ban đầu của tính năng là "giảm rủi ro lưu trữ lâu dài" (dọn dẹp định kỳ), không phải "trò chuyện tức thời tự hủy" (ephemeral chat kiểu Snapchat) → **Root cause: tính năng được thiết kế cho use case "dọn dẹp dữ liệu cũ", nên thang đo mặc định chọn theo ngày — đây là giới hạn phạm vi thiết kế ban đầu (design scope), có thể mở rộng thêm mốc chứ không phải giới hạn kỹ thuật.**

**Problem Statement:**

> Vì tính năng được thiết kế ban đầu chỉ nhắm tới mục tiêu "giảm lưu trữ lâu dài" với thang đo theo ngày, nên người dùng có nhu cầu trò chuyện thực sự nhạy cảm/tức thời (như chia sẻ OTP, thông tin tài chính) không có lựa chọn mốc thời gian ngắn (giây/phút), dẫn đến họ phải tự thu hồi tin thủ công hoặc chuyển sang app khác cho nhu cầu này.

> 

**In-scope**: Bổ sung thêm 1-2 mốc ngắn hơn (ví dụ 1 giờ, 5 phút) bên cạnh 3 mốc hiện có.

**Out-of-scope**: Cho phép tùy chỉnh tự do theo giây như Signal — vì độ phức tạp UI/UX và khối lượng xử lý tăng vọt so với lợi ích thêm được.

**pain point thô → root cause → scope → đề xuất có ưu tiên)**

## **Tổng quan giải pháp theo từng pain point**

### **PP1 — Không hỗ trợ nhóm chat**

* **Triển khai trước cho nhóm nhỏ (dưới \~20 thành viên).**  
* **Chưa xử lý case người vào/rời nhóm giữa chừng ở phiên bản đầu (để cho v2).**  
* **Cơ chế kỹ thuật: mỗi tin nhắn gắn 1 giá trị TTL (Time-To-Live), hệ thống tự xóa khi hết hạn cho tất cả thành viên trong nhóm.**  
* **Business rule cần chốt trước khi giao cho dev: người rời nhóm trước khi tin hết hạn có bị xóa tin ngay không; người mới vào nhóm có thấy các tin cũ đang chờ xóa không.**

### **PP2 — Thang thời gian xóa quá dài (chỉ 1/7/30 ngày)**

* **Bổ sung thêm 1-2 mốc ngắn hơn (ví dụ 1 giờ, 5 phút).**  
* **Không triển khai tùy chỉnh tự do theo giây/phút.**  
* **Cơ chế kỹ thuật: vẫn dùng cùng cơ chế TTL hiện có, chỉ thêm option mốc thời gian mới trong UI, không đổi kiến trúc.**  
* **Lý do giới hạn không tùy chỉnh tự do: phát sinh chi phí ở validation input và xử lý lỗi vận hành (support khó debug hơn), không nằm ở tầng lưu trữ.**

### **PP3 — Không chống được screenshot/lưu trước hạn**

* **Thêm cảnh báo rõ trong UI khi bật tính năng, giải thích giới hạn (không ngăn được việc lưu/chụp lại nội dung).**  
* **Cập nhật Help Center chính thức, làm rõ phạm vi bảo vệ của tính năng.**  
* **Bổ sung kỹ thuật theo từng nền tảng:**  
  * **Android: dùng `FLAG_SECURE` để chặn chụp/quay màn hình trong khung chat.**  
  * **iOS: dùng `UIScreen.capturedDidChangeNotification` để phát hiện khi người dùng chụp màn hình, gửi thông báo cho người gửi biết (không chặn được hành động chụp, chỉ phát hiện sau khi xảy ra).**  
* **Không triển khai: chặn việc chụp lại bằng thiết bị/camera khác (nằm ngoài khả năng kỹ thuật của mọi nền tảng).**

 

