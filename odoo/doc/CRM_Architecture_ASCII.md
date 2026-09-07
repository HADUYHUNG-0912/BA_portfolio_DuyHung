# KIẾN TRÚC CHỨC NĂNG & NĂNG LỰC NGHIỆP VỤ ODOO CRM

> **Dành cho:** Business Analyst (BA) & ERP Solution Consultant  
> **Mục tiêu:** Mô tả kiến trúc tổng thể của hệ thống Odoo CRM dưới góc độ **Dòng chảy nghiệp vụ (Business Flows)**, **Vai trò người dùng (User Personas)** và **Bản đồ năng lực chức năng (Functional Capabilities)** mà không sử dụng khái niệm mã nguồn kỹ thuật.  
> 
> 📌 **Tài liệu liên quan:** [Business_Rules_Analysis.md](./Business_Rules_Analysis.md) | [Sơ đồ Swimlane (PNG)](../diagram/CRM_Lead_To_Order_Swimlane_Process.png) | [README.md](../README.md)

---

## 🧭 1. SƠ ĐỒ PHÂN TẦNG KIẾN TRÚC CHỨC NĂNG (FUNCTIONAL LAYERS)

```
+===========================================================================+
|                     ODOO CRM - KIẾN TRÚC CHỨC NĂNG                        |
+===========================================================================+
|                                                                           |
|  [1. TẦNG VAI TRÒ NGƯỜI DÙNG - Stakeholders & Personas]                   |
|   +-------------------+  +--------------------+  +--------------------+   |
|   |  Nhân viên Sales  |  | Trưởng phòng Kinh  |  | Giám đốc Kinh doanh|   |
|   | (Telesales/Direct)|  | doanh (Team Leader)|  | (CCO / CEO)        |   |
|   +-------------------+  +--------------------+  +--------------------+   |
|             |                      |                       |              |
|             +----------------------+-----------------------+              |
|                                    v                                      |
|  [2. TẦNG GIAO DIỆN & TRẢI NGHIỆM - Workspace & UI Views]                 |
|   Kanban (Kéo thả) | Danh sách (List) | Biểu mẫu (Form) | Lịch hẹn (Cal)  |
|   Phân tích Phễu (Funnel) | Báo cáo Pivot | Dự báo Doanh số (Forecast)    |
|                                    |                                      |
|                                    v                                      |
|  [3. TẦNG NĂNG LỰC NGHIỆP VỤ CỐT LÕI - Core Business Capabilities]        |
|   +-------------------------------------------------------------------+   |
|   | QUẢN TRỊ KHÁCH HÀNG TIỀM NĂNG (Leads & Contacts Management)       |   |
|   | • Tiếp nhận đa kênh (Website Form, Email, Hotline, Quảng cáo Ads) |   |
|   | • Đánh giá & Chấm điểm tiềm năng (Scoring & Qualification)        |   |
|   | • Kiểm tra trùng lặp & Gộp hồ sơ (Deduplication & Merge)          |   |
|   +-------------------------------------------------------------------+   |
|   | QUẢN TRỊ PHỄU CƠ HỘI BÁN HÀNG (Pipeline & Opportunity Management) |   |
|   | • Tùy biến các giai đoạn bán hàng & Điều kiện chuyển chặng        |   |
|   | • Giám sát thời gian ngâm deal (Rotting SLA) & Cảnh báo trễ hạn   |   |
|   | • Dự báo doanh số theo trọng số xác suất (Weighted Forecasting)   |   |
|   | • Đóng deal Thắng/Thua & Chuẩn hóa nguyên nhân thất bại           |   |
|   +-------------------------------------------------------------------+   |
|   | QUẢN TRỊ ĐỘI NGŨ & CHÍNH SÁCH BÁN HÀNG (Sales Team & Quota)       |   |
|   | • Phân bổ Lead tự động xoay vòng (Round-Robin Assignment)         |   |
|   | • Quản lý hạn mức nhận khách theo ngày/tháng (Capacity Quota)     |   |
|   | • Phân vùng địa bàn kinh doanh (Territory: Miền Bắc vs Miền Nam)  |   |
|   +-------------------------------------------------------------------+   |
|                                    |                                      |
|                                    v                                      |
|  [4. TẦNG TỰ ĐỘNG HÓA & KIỂM SOÁT - Automation & Governance]              |
|   • Tự động nhắc việc, gửi email báo giá & lịch hẹn (Activity Plans)  |   |
|   • Cảnh báo vượt cấp (Escalation Alerts) khi deal bị đình trệ        |   |
|   • Nhật ký kiểm toán (Audit Trail) ghi nhận mọi thay đổi dữ liệu     |   |
|   • Ma trận phân quyền đa tầng bảo vệ thông tin khách hàng nhạy cảm   |   |
|                                    |                                      |
|                                    v                                      |
|  [5. TẦNG LIÊN THÔNG LIÊN PHÂN HỆ - Enterprise Integration]              |
|   Bán hàng (Sales Orders) <---> Kho vận (Stock) <---> Kế toán (Invoicing) |
+===========================================================================+
```

---

## 🔄 2. VÒNG ĐỜI DÒNG CHẢY DỮ LIỆU NGHIỆP VỤ (LEAD-TO-OPPORTUNITY FLOW)

```
+----------------+      +------------------+      +-------------------+      +------------------+
| 1. TIẾP NHẬN   | ---> | 2. THẨM ĐỊNH &   | ---> | 3. NUÔI DƯỠNG &   | ---> | 4. CHỐT DEAL &   |
| ĐẦU MỐI (LEAD) |      | CHUYỂN ĐỔI       |      | ĐÀM PHÁN          |      | CHUYỂN BÁN HÀNG  |
+--------+-------+      +--------+---------+      +---------+---------+      +--------+---------+
         |                       |                          |                         |
         v                       v                          v                         v
  • Đổ về từ Web,        • Lọc rác, chuẩn hóa       • Phân loại giai đoạn      • Thắng (Won):
    Email, Facebook        SĐT/Email                  Kanban (Mới -> Khảo        Tự động sinh
  • Cơ chế xoay vòng     • Bấm Chuyển đổi sang        sát -> Báo giá ->          Báo giá / Hợp đồng
    Round-Robin            Cơ hội (Convert)           Đàm phán)                • Thua (Lost):
  • Khống chế hạn mức    • Tự động sinh hoặc        • Cảnh báo ngâm deal         Bắt buộc chọn
    tránh quá tải          liên kết khách hàng        Rotting SLA 14 ngày        lý do phục vụ
                           sẵn có trong Danh bạ     • Lên lịch chăm sóc          phân tích thị trường
```

---

## 🔗 3. MỐI LIÊN THÔNG DOANH NGHIỆP (CROSS-MODULE INTEGRATION)

Dưới lăng kính BA, phân hệ CRM không đứng độc lập mà là **cửa ngõ mở đầu** cho toàn bộ chuỗi giá trị vận hành của doanh nghiệp:

```
+---------------------------------------------------------------------------------------+
|                                    PHỄU MARKETING                                     |
|                      (Chiến dịch quảng cáo, Landing Page, Hòm thư)                     |
+-------------------------------------------+-------------------------------------------+
                                            │
                                            ▼
+---------------------------------------------------------------------------------------+
|                             ODOO CRM (QUẢN TRỊ CƠ HỘI)                                 |
|               Quản lý Pipeline, Nuôi dưỡng khách hàng, Đàm phán giá cả                |
+-------------------------------------------+-------------------------------------------+
                                            │ (Bấm "Tạo Báo giá" khi khách đồng ý)
                                            ▼
+---------------------------------------------------------------------------------------+
|                           PHÂN HỆ BÁN HÀNG (SALES ORDER)                              |
|           Lập Báo giá (Quotation), Phê duyệt chiết khấu, Khóa Hợp đồng bán            |
+-----------------------------------+---------------+-----------------------------------+
                                    │               │
      (Kích hoạt giao hàng)         │               │ (Kích hoạt xuất hóa đơn)
                                    ▼               ▼
+---------------------------------------+   +-------------------------------------------+
|          PHÂN HỆ KHO VẬN (STOCK)      |   |       PHÂN HỆ KẾ TOÁN (INVOICING)         |
|   Kiểm tra tồn kho, Đóng gói & Giao   |   |   Phát hành Hóa đơn VAT, Đối soát công nợ |
+---------------------------------------+   +-------------------------------------------+
```

---

## 🗺️ 4. BẢN ĐỒ NĂNG LỰC NGHIỆP VỤ & TÍNH NĂNG CHUẨN ODOO (NO-CODE)

Dưới đây là bảng tra cứu giúp BA nhanh chóng xác định **bài toán nghiệp vụ tương ứng với màn hình cấu hình nào trên Odoo**:

| Bài toán nghiệp vụ của Doanh nghiệp | Tính năng Odoo giải quyết (UI Standard) | Menu thao tác trên hệ thống |
| :--- | :--- | :--- |
| **Chia đều khách hàng cho nhân viên, không ai bị quá tải** | Cấu hình Đội bán hàng & Hạn mức Capacity theo tháng | *CRM $\rightarrow$ Configuration $\rightarrow$ Sales Teams* |
| **Khách hàng gửi thư hỏi giá tự động tạo cơ hội** | Thiết lập Hòm thư tiếp nhận (Email Alias) cho từng đội | *CRM $\rightarrow$ Configuration $\rightarrow$ Sales Teams* |
| **Quy chuẩn các bước bán hàng theo ngành nghề** | Thiết lập Danh mục các cột giai đoạn bán hàng (Stages) | *CRM $\rightarrow$ Configuration $\rightarrow$ Stages* |
| **Cảnh báo nhân viên bỏ quên không chăm sóc khách** | Thiết lập Rotting Days (Đổi màu đỏ khi vượt quá số ngày) | *CRM $\rightarrow$ Configuration $\rightarrow$ Stages* |
| **Tìm hiểu nguyên nhân tại sao hụt hợp đồng** | Danh mục Lý do thất bại chuẩn hóa (Lost Reasons) | *CRM $\rightarrow$ Configuration $\rightarrow$ Lost Reasons* |
| **Ngăn chặn 2 sales cùng gọi điện cho 1 khách hàng** | Tính năng Tìm kiếm & Gộp cơ hội trùng lặp (Merge) | Chọn các deal trong *CRM List View $\rightarrow$ Action $\rightarrow$ Merge* |
| **Bảo mật dữ liệu, nhân viên không thấy khách của nhau** | Phân cấp quyền tài khoản: *Own Documents Only* | *Settings $\rightarrow$ Users & Companies $\rightarrow$ Users* |
| **Đo lường doanh thu định kỳ cho phần mềm/dịch vụ** | Kích hoạt Doanh thu định kỳ (Recurring Plans - MRR) | *CRM $\rightarrow$ Configuration $\rightarrow$ Settings & Recurring Plans* |
| **Theo dõi tỷ lệ chuyển đổi và lý do rớt deal** | Báo cáo Phân tích Phễu & Bảng tổng hợp Pivot | *CRM $\rightarrow$ Reporting $\rightarrow$ Pipeline Analysis* |

---

## 🗄️ LỊCH SỬ THAY ĐỔI TÀI LIỆU (CHANGELOG)

| Phiên bản | Ngày | Người cập nhật | Nội dung cập nhật |
| :---: | :---: | :---: | :--- |
| **v1.0** | 2026-09-02 | AI Solution Architect | Xây dựng sơ đồ kiến trúc ASCII phân tầng kỹ thuật. |
| **v2.0** | 2026-09-05 | Lead BA & AI | **Chuyển đổi toàn diện sang Kiến trúc Chức năng Nghiệp vụ cho BA**: Thay thế việc liệt kê mã nguồn kỹ thuật bằng Bản đồ Năng lực chức năng, Dòng chảy dữ liệu nghiệp vụ Lead-to-Order và Bảng tra cứu giải pháp Odoo No-Code. |
