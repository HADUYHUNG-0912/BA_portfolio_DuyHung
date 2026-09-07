# ĐẶC TẢ GIẢI PHÁP NGHIỆP VỤ: DỰ BÁO DOANH SỐ LAI (HYBRID REVENUE) & KIỂM SOÁT DÒNG TIỀN (MODULE 5)

> **Dự án:** Tư vấn & Triển khai Odoo CRM (TechCorp)  
> **Phân hệ:** Odoo CRM (v19.0)  
> **Chủ đề:** Recurring Revenues (MRR/ARR), Sales Forecasting & Slipping Deals Control  
> **Tác giả:** Lead Business Analyst (BA Leader)  
> **Người tiếp nhận:** Ban Giám đốc (CEO, CFO, CCO)  
> 
> 📌 **Tài liệu liên quan:** [ba_teaching_rules.md](file:///e:/BA/Ba-case/odoo/odoo/.agents/rules/ba_teaching_rules.md) | [Business_Rules_Analysis.md](file:///e:/BA/Ba-case/odoo/odoo/doc/Business_Rules_Analysis.md) | [CRM_Learning_Progress.md](file:///e:/BA/Ba-case/odoo/odoo/doc/CRM_Learning_Progress.md)

---

## 1. TỔNG QUAN HIỆN TRẠNG & BÀI TOÁN TÀI CHÍNH - KINH DOANH

Doanh nghiệp TechCorp kinh doanh theo mô hình phức hợp (Hybrid Model) bao gồm bản quyền giải pháp chuyển đổi số và dịch vụ bảo trì định kỳ cho chuỗi bán lẻ. Doanh nghiệp đối mặt với 3 điểm đau lớn:
1. **Khủng hoảng định giá cơ hội hỗn hợp:** Một hợp đồng vừa có phí triển khai một lần (One-off: 150 triệu), vừa có phí thuê bao hàng tháng (Recurring MRR: 15 triệu/tháng). Sales bối rối không biết ghi nhận sao cho vừa phản ánh đúng doanh thu định kỳ, vừa không bỏ sót cục tiền triển khai.
2. **"Deal trôi dạt" (Slipping Deals) làm vỡ kế hoạch dòng tiền:** Sales thường xuyên kéo deal từ cuối tháng này sang tháng sau trên Forecast View để né phạt không đạt KPI, khiến CFO lên kế hoạch ngân sách bị thiếu hụt thanh khoản nghiêm trọng.
3. **Thiếu góc nhìn Dashboard phân tầng cho C-Level:** CEO và CFO không phân biệt được đâu là dòng tiền thu ngay và đâu là dòng tiền tích lũy định kỳ để chuẩn bị tài chính và nhân sự kỹ thuật.

---

## 2. GIẢI PHÁP CHI TIẾT CỦA LEAD BA

### 2.1. Giải pháp Bài toán 1: Quản lý Cơ hội hỗn hợp (Hybrid Deal Architecture)
* `[CHUẨN ODOO STANDARD]`
  * **Cơ chế 2 trường song song trên Form Cơ hội (`crm.lead`):**
    * Khi kích hoạt tính năng **Recurring Revenues** tại *Settings*, Odoo cung cấp sẵn đồng thời **2 khối dữ liệu độc lập** trên cùng một màn hình cơ hội:
      1. **Khối Doanh thu bán đứt (One-off Revenue):** Ghi nhận tại trường `expected_revenue` $= 150.000.000 \text{ VNĐ}$ (Chi phí triển khai & đào tạo nghiệm thu 1 lần).
      2. **Khối Doanh thu định kỳ (Recurring Revenue):** Ghi nhận tại trường `recurring_revenue` $= 15.000.000 \text{ VNĐ}$ đi kèm gói `recurring_plan` $=$ **Hàng tháng (Monthly)**.
  * **Giá trị quản trị:**
    * CCO theo dõi được chỉ số **New MRR** tăng trưởng hàng tháng: $+15.000.000 \text{ VNĐ/tháng}$.
    * CFO theo dõi được tổng giá trị hợp đồng (Total Contract Value - TCV) năm đầu tiên:
      $$\text{TCV} = 150.000.000 + (15.000.000 \times 12) = 330.000.000 \text{ VNĐ}$$

---

### 2.2. Giải pháp Bài toán 2: Hệ thống Tracking & Bật cờ (Flagger) kiểm soát "Deal trôi dạt"
* `[CHUẨN ODOO STANDARD]`
  * Kích hoạt thuộc tính theo dõi lịch sử (**Field Tracking**) trên trường Ngày chốt dự kiến (`expected_closing`). Mọi thao tác kéo deal từ tháng này sang tháng khác đều bị ghi lại trên Chatter kiểm toán: *"Hạn chốt thay đổi từ 31/08/2026 sang 30/09/2026 bởi Nguyễn Văn A"*.
* `[GIẢ ĐỊNH NGHIỆP VỤ / TÙY BIẾN FIT-GAP]`
  * **Cơ chế đếm số lần dời deal (Reschedule Counter):**
    * Thiết lập trường tự động đếm: `reschedule_count`. Mỗi lần nhân viên sửa ngày chốt hoặc kéo thả trên Forecast View sang một tháng mới, hệ thống tự động cộng $+1$.
  * **Quy chế Bật cờ cảnh báo (Slipping Deal Flag):**
    * Khi `reschedule_count >= 2`: Thẻ deal trên màn hình Kanban và Forecast View tự động chuyển sang **Cờ cảnh báo màu Đỏ (Slipping Flag)**.
    * **Ràng buộc Poka-Yoke:** Xuất hiện popup bắt buộc nhân viên phải chọn **Lý do trì hoãn (Delay Reason)** trong danh mục chuẩn:
      1. *Khách hàng chưa duyệt ngân sách*
      2. *Đang thương thảo điều khoản hợp đồng/pháp chế*
      3. *Đợi khách hàng bố trí nhân sự tiếp nhận*
      4. *Lý do khác (yêu cầu giải trình)*
    * Hệ thống tự động gửi thông báo gắn thẻ Quản lý trực tiếp trên Chatter để cùng sales tìm phương án tháo gỡ.

---

### 2.3. Giải pháp Bài toán 3: Dashboard Báo cáo Đa tầng cho Ban Giám đốc
* `[CHUẨN ODOO STANDARD]`
  * **Phân tích phễu Pipeline (*CRM $\rightarrow$ Reporting $\rightarrow$ Pipeline Analysis*):**
    * Sử dụng giao diện **Pivot Table (Bảng tổng hợp đa chiều)**:
      * Hàng (Rows): Nhóm theo **Ngày chốt dự kiến: Tháng (Expected Closing by Month)**.
      * Cột (Columns): Nhóm theo **Giai đoạn (Stage)** hoặc **Đội bán hàng (Sales Team)**.
      * Chỉ số đo lường (Measures): Bật đồng thời 2 thước đo:
        * Thước đo 1: **Expected Revenue** (Phản ánh 150 triệu tiền triển khai).
        * Thước đo 2: **Recurring Revenue (MRR)** (Phản ánh 15 triệu/tháng tiền thuê bao tích lũy).
  * **Tích hợp Odoo Spreadsheet Dashboard:**
    * Xây dựng Dashboard trực quan bằng Odoo Spreadsheet hiển thị biểu đồ cột ghép: Cột xanh là tiền One-off về ngay, đường line đỏ là lũy kế MRR phát sinh, giúp CEO chuẩn bị nhân sự kỹ thuật triển khai và CFO cân đối dòng tiền chi trả máy chủ chính xác đến từng tuần.

---

## 3. ĐÓNG GÓI USER STORIES & TIÊU CHÍ NGHIỆM THU (ACCEPTANCE CRITERIA)

### 📌 User Story: Nhận diện & Bật cờ cảnh báo Deal trôi dạt (Slipping Deal Control)
* **Là một:** Giám đốc Tài chính (CFO) / Giám đốc Kinh doanh (CCO)
* **Tôi muốn:** Hệ thống tự động theo dõi số lần nhân viên kinh doanh dời ngày chốt dự kiến sang tháng sau và bật cờ cảnh báo trực quan khi vượt quá 2 lần.
* **Để tôi:** Kịp thời nhận diện các cơ hội bán hàng ảo, chủ động cân đối kế hoạch dòng tiền thực tế và đôn đốc đội ngũ kinh doanh chốt hợp đồng.

#### Tiêu chí nghiệm thu (Acceptance Criteria - AC):
* **Given (Bối cảnh):** Cơ hội "Triển khai phần mềm Nhà thuốc PharmaCity" có ngày chốt dự kiến ban đầu là `31/08/2026` với `reschedule_count = 1`.
* **When (Hành động):** Nhân viên kéo cơ hội trên màn hình Forecast View từ cột "Tháng 8/2026" sang "Tháng 9/2026".
* **Then (Kết quả mong đợi):**
  1. Trường `expected_closing` cập nhật sang ngày thuộc tháng 9/2026.
  2. Trường `reschedule_count` tự động tăng lên $2$.
  3. Thẻ cơ hội trên Forecast View và Kanban tự động bật cờ cảnh báo màu Đỏ (Slipping Flag).
  4. Hệ thống hiển thị ô bắt buộc nhập "Lý do trì hoãn" trước khi cho phép lưu thay đổi.
  5. Một thông báo tự động được ghi nhận vào Chatter của cơ hội kèm tag tên Trưởng phòng kinh doanh.

---

## 4. BẢNG FIT-GAP ANALYSIS MODULE 5

| STT | Yêu cầu nghiệp vụ | Đánh giá Fit-Gap | Hướng xử lý của BA |
| :---: | :--- | :---: | :--- |
| **1** | Quản lý đồng thời Doanh thu One-off và MRR trên 1 deal | `[CHUẨN ODOO STANDARD]` | Kích hoạt tính năng *Recurring Revenues* trong *CRM Settings*. Nhập đồng thời cả 2 trường. |
| **2** | Dự báo bán hàng trực quan theo tháng | `[CHUẨN ODOO STANDARD]` | Sử dụng giao diện *CRM Forecast View* kéo thả theo `expected_closing`. |
| **3** | Ghi nhận lịch sử mỗi khi dời ngày chốt | `[CHUẨN ODOO STANDARD]` | Kích hoạt thuộc tính *Tracking* trên trường `expected_closing` để ghi nhận vào Chatter. |
| **4** | Tự động đếm số lần dời deal & Bật cờ cảnh báo quá 2 lần | `[GIẢ ĐỊNH / TÙY BIẾN FIT-GAP]` | Cấu hình trường tính toán/No-code Automated Action tăng biến đếm và đổi màu hiển thị Kanban. |
| **5** | Bắt buộc nhập lý do trì hoãn khi dời deal quá ngưỡng | `[GIẢ ĐỊNH / TÙY BIẾN FIT-GAP]` | Ràng buộc điều kiện (Validation Rule) trên giao diện khi `reschedule_count >= 2`. |
| **6** | Báo cáo phân tích đa chiều tách bạch One-off và MRR | `[CHUẨN ODOO STANDARD]` | Sử dụng *CRM Pipeline Analysis Pivot Table* với 2 thước đo: Expected Revenue & Recurring Revenue. |
