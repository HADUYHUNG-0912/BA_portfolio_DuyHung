# BẢNG CÁC ĐIỂM ĐAU CÒN TỒN ĐỌNG TRONG ODOO CRM (CẦN BA CẤU HÌNH XỬ LÝ)

> **Mục tiêu tài liệu:** Chỉ lưu giữ những **điểm đau THỰC SỰ CHƯA ĐƯỢC ODOO GIẢI QUYẾT MẶC ĐỊNH**, đòi hỏi BA Leader phải can thiệp cấu hình hoặc thiết lập quy chế cho doanh nghiệp.  
> *(Các điểm đau mà Odoo 19 đã giải quyết sẵn như tính năng chống ngâm deal Rotting và chống trùng lead đã được lược bỏ khỏi danh sách này).*  
> **Tài liệu liên quan:** [Case_Study_Odoo.md](./Case_Study_Odoo.md) | [Sơ đồ Swimlane (PNG)](../diagram/CRM_Lead_To_Order_Swimlane_Process.png)

---

## 📊 MA TRẬN CÁC ĐIỂM ĐAU CHƯA ĐƯỢC GIẢI QUYẾT MẶC ĐỊNH

| Mã | Điểm đau thực tế còn tồn đọng | Đối tượng chịu trận | Triệu chứng & Hậu quả | Hiện trạng Odoo mặc định | Giải pháp BA cần triển khai |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **PP-01** | **Thiếu cơ chế Cảnh báo Vượt cấp (Lack of Escalation Alert)** | • Trưởng phòng Bán hàng<br>• Giám đốc Kinh doanh (CCO) | • Thẻ Kanban tuy có đổi màu nhưng nếu nhân viên lười/nghỉ việc thì deal vẫn nằm chết.<br>• Quản lý không có thời gian rà soát hàng trăm deal mỗi ngày $\rightarrow$ Mất khách vào tay đối thủ. | ❌ **Odoo chưa có sẵn:** Odoo chỉ hiển thị nhãn màu cảnh báo chứ **không tự động gửi tin nhắn/email báo động cho Sếp**. | 🟡 **Cấu hình Automated Action:** Thiết lập quy tắc: Nếu `rotting_days > 16 ngày` mà chưa có cập nhật $\rightarrow$ Hệ thống tự động bắn tin nhắn tag tên Trưởng nhóm (`@team_id.user_id`) trên Chatter hoặc tự động chuyển deal. |
| **PP-02** | **Lỗ hổng cho phép Đóng deal bừa bãi không ghi lý do** | • Giám đốc Sản phẩm (CPO)<br>• Giám đốc Chiến lược | • Nhân viên đóng deal chỉ cần bấm nút mà không chọn nguyên nhân.<br>• Mất khách nhưng "mù thông tin", không biết do giá đắt hay sản phẩm thiếu tính năng. | ❌ **Odoo chưa khóa:** Trên Popup Wizard `crm.lead.lost`, trường `lost_reason_id` **chưa bắt buộc (`required=True`)**, nhân viên không chọn gì vẫn bấm nút "Mark as Lost" được! | 🟡 **Khóa chốt chặn Poka-Yoke:** Cấu hình thuộc tính `required="1"` cho trường lý do thua trên màn hình popup để nút xác nhận bị vô hiệu hóa nếu chưa chọn lý do chuẩn hóa. |

---

## 🔍 CHI TIẾT TỪNG ĐIỂM ĐAU & GIẢI PHÁP CẤU HÌNH

### 1. Điểm đau PP-01: Thiếu cơ chế Cảnh báo Vượt cấp (Escalation Alert)
* **Hiện trạng phần mềm mặc định:**
  * Odoo 19 đã đếm được ngày ngâm deal (`rotting_days = 6d`) và có bộ lọc `Rotting`.
  * **NHƯNG:** Hệ thống hoàn toàn bị động, chỉ ngồi chờ Quản lý tự vào mở bộ lọc để xem. Nếu Quản lý bận họp không vào xem thì deal vẫn bị bỏ quên.
* **Tác động:** Không có tính chủ động (Proactive Alert), SLA bị đứt gãy giữa nhân viên và cấp quản lý.
* **Hành động của BA:**
  * Thiết lập 1 **Automated Action** (không cần viết code Python):
    * *Model:* `crm.lead`
    * *Trigger:* `Based on Timed Condition` (Sau 16 ngày kể từ ngày cập nhật stage cuối).
    * *Action:* Gửi thông báo trực tiếp vào hộp thư nội bộ của Sales Manager.

---

### 2. Điểm đau PP-02: Lỗ hổng đóng deal không bắt buộc chọn lý do
* **Hiện trạng phần mềm mặc định (Đã kiểm chứng thực tế trên Runbot):**
  * Odoo đã làm popup với các nút bấm đẹp mắt (`widget="selection_badge"`).
  * **NHƯNG:** Nút tím `Mark as Lost` lại **sáng sẵn ngay từ đầu**. Nhân viên không cần bấm vào bất kỳ lý do nào (`Too expensive`, `Not enough stock`...) mà vẫn bấm thẳng nút tím để đóng deal thành công.
* **Tác động:** 
  * Dữ liệu báo cáo Lost Opportunity Analysis bị rỗng (Blank reasons).
  * Ban Giám đốc và đội ngũ Sản phẩm không thể phân tích nguyên nhân thất bại của các chiến dịch bán hàng.
* **Hành động của BA:**
  * Thêm ràng buộc kiểm tra (Validation Rule / UI Constraint):
    * Bắt buộc trường Lý do thua (`lost_reason_id`) phải có giá trị mới cho phép bấm nút "Mark as Lost" đóng deal.
    * Khóa chặt quy trình, ép 100% nhân viên phải tuân thủ chuẩn hóa dữ liệu.

---

## 📌 GHI CHÚ: CÁC ĐIỂM ĐAU ODOO 19 ĐÃ GIẢI QUYẾT XONG (ĐÃ XÓA KHỎI DANH SÁCH TỒN ĐỌNG)
* ✅ **Đã giải quyết:** Điểm đau *Ngâm deal không ai biết* $\rightarrow$ Đã được Odoo 19 giải quyết triệt để bằng tính năng native **Rotting Engine** (`rotting_threshold_days` + `widget="rotting"` đổi màu thẻ).
* ✅ **Đã giải quyết:** Điểm đau *Trùng lặp khách hàng & Tranh chấp lead* $\rightarrow$ Đã được Odoo giải quyết bằng tính năng **Duplicate Detection** (`_compute_potential_lead_duplicates`) và **Rule-based Lead Assignment** theo dung tích tháng.

---

## 🗄️ LỊCH SỬ THAY ĐỔI TÀI LIỆU (CHANGELOG)

| Phiên bản | Ngày | Người cập nhật | Nội dung cập nhật |
| :---: | :---: | :---: | :--- |
| **v1.0** | 2026-09-04 | Lead BA & AI | Khởi tạo ma trận 4 điểm đau trong Odoo CRM. |
| **v2.0** | 2026-09-04 | Lead BA & AI | Tinh gọn tài liệu theo yêu cầu: Lược bỏ các điểm đau Odoo 19 đã giải quyết mặc định (Rotting indicator & Duplicate lead); chỉ tập trung phân tích 2 điểm đau thực sự cần BA cấu hình (PP-01 & PP-02). |
