# BẢNG CHECKLIST QUẢN LÝ TIẾN ĐỘ HỌC TẬP BA ERP (ODOO + AI)

> **Hướng dẫn sử dụng:**
> * `[x]` : Đã hoàn thành và đạt yêu cầu.
> * `[/]` : Đang học / Đang thực hiện.
> * `[ ]` : Chưa học.
> * Cập nhật ngày hoàn thành, điểm số và liên kết sản phẩm (Deliverable) sau mỗi bài học.

---

## 📊 TỔNG QUAN TIẾN ĐỘ HỌC TẬP

```
[██████░░░░░░░░░░░░░░] 30% Tổng lộ trình 3 Giai đoạn

• Giai đoạn 1 (Lead-to-Order & Sales):  [████████████░] 62.5%
• Giai đoạn 2 (Supply Chain & Kho):     [░░░░░░░░░░░░░]  0.0%
• Giai đoạn 3 (Tài chính & Tư vấn ERP): [░░░░░░░░░░░░░]  0.0%
```

---

## 🧭 GIAI ĐOẠN 1: LEAD-TO-ORDER & BÁN HÀNG DOANH THU

### 1.1. Phân hệ CRM Chuyên sâu (8 Module BA Leader)
*Tài liệu chi tiết kèm điểm thi: [CRM_Learning_Progress.md](file:///e:/BA/Ba-case/odoo/odoo/doc/CRM_Learning_Progress.md)*

- [x] **Module 1: Nền tảng CRM** *(Đã xong)*
  - [x] Phân biệt Lead vs Opportunity (khi nào dùng Lead, khi nào dùng thẳng Opportunity)
  - [x] Cấu trúc Pipeline & Phễu bán hàng (Sales Funnel)
  - [x] Các chỉ số đo lường hiệu suất CRM (Win Rate, Conversion Rate, Sales Velocity)
  - *Điểm: Trắc nghiệm 10/10 | Tự luận 8/10*
- [x] **Module 2: Vòng đời Lead** *(Đã xong)*
  - [x] Nguồn lead & Tracking chiến dịch Marketing (UTM Source, Medium, Campaign)
  - [x] Đánh giá & Chấm điểm tiềm năng (Lead Scoring)
  - [x] Cơ chế chuyển đổi Lead $\rightarrow$ Opportunity (tạo mới vs gán vào khách có sẵn)
  - [x] Quy tắc phân bổ Lead cho nhân viên (Lead Assignment & Rule-based allocation)
  - *Điểm: Trắc nghiệm 10/10 | Tự luận 8.5/10*
- [x] **Module 3: Pipeline & Stage** *(Đã xong)*
  - [x] Thiết kế các cột Kanban & Định nghĩa điều kiện chuyển giai đoạn (Exit Criteria)
  - [x] Thuật toán tính xác suất thành công tự động (Predictive Lead Scoring - Bayes)
  - [x] Cơ chế đánh dấu Thắng/Thua (Won/Lost) & Phân tích lý do thất bại (Lost Reasons)
  - [x] Dự báo doanh thu kỳ vọng theo trọng số (Expected Revenue vs Prorated Revenue)
  - *Điểm: Trắc nghiệm 7.5/10 | Tự luận 8.5/10*
  - *Sản phẩm hoàn thành:* [case.md](file:///e:/BA/Ba-case/odoo/odoo/doc/case.md) | [CRM_Lifecycle_Swimlane.md](file:///e:/BA/Ba-case/odoo/odoo/diagram/CRM_Lifecycle_Swimlane.md) | [CRM_Pain_Points.md](file:///e:/BA/Ba-case/odoo/odoo/doc/CRM_Pain_Points.md)
- [x] **Module 4: Đội bán hàng & Phân quyền nghiệp vụ (Sales Team & Security)** *(Đã xong)*
  - [x] Thiết lập Đội bán hàng (Sales Team), phân công Trưởng đội (Team Leader)
  - [x] Quản lý dung tích tiếp nhận lead của nhân viên (Capacity Quota 5 lead/ngày & Round-Robin)
  - [x] Thiết lập Ma trận phân quyền chức năng theo vai trò (Salesman vs Team Leader vs Sales Manager)
  - [x] Chính sách bảo mật dữ liệu khách hàng & chống cướp khách kết hợp Data Masking & Lead Recycling
  - *Điểm: Trắc nghiệm 7.5/10 | Tự luận 9.0/10*
  - *Sản phẩm hoàn thành:* [case_module_4.md](file:///e:/BA/Ba-case/odoo/odoo/doc/case_module_4.md)
- [x] **Module 5: Doanh thu định kỳ (MRR) & Dự báo (Forecasting)** *(Đã xong)*
  - [x] Quản lý doanh thu định kỳ cho mô hình thuê bao dịch vụ SaaS/Subscription (`crm.recurring.plan`)
  - [x] Quản lý cơ hội hỗn hợp One-off Implementation và Recurring MRR trên cùng 1 deal
  - [x] Dự báo doanh số theo tháng/quý (Sales Forecast view) và kiểm soát Slipping Deals
  - *Điểm: Trắc nghiệm 10/10 | Tự luận 9.5/10*
  - *Sản phẩm hoàn thành:* [case_module_5.md](file:///e:/BA/Ba-case/odoo/odoo/doc/case_module_5.md)
- [/] **Module 6: Tự động hóa & Tích hợp (Automation & Omnichannel)** *(TIẾP THEO)*
  - [ ] Kênh tiếp nhận khách hàng tự động từ Email Alias, Website & Webforms
  - [ ] Thiết lập Kế hoạch hoạt động tự động đa bước (Activity Plans: Call, Meeting, To-do)
  - [ ] Cấu hình Tự động hóa thông minh (Automated Actions: Escalate SLA, đổi trạng thái)
- [ ] **Module 7: Báo cáo & Phân tích chuyên sâu (Analytics & BI)**
  - [ ] Phân tích phễu Pipeline Analysis (Pivot table, Bar chart, Funnel view)
  - [ ] Phân tích năng suất hoạt động của Sales (Activity Report)
  - [ ] Phân tích tỷ lệ rớt deal theo từng giai đoạn (Stage Drop-off Analysis)
- [ ] **Module 8: Cấu hình hệ thống & Thi tốt nghiệp CRM**
  - [ ] Cấu hình tổng thể Settings CRM trên giao diện chuẩn
  - [ ] Bài kiểm tra thực chiến tổng hợp toàn bộ 8 module CRM giải quyết Case Study lớn

---

### 1.2. Phân hệ Bán hàng & Quản lý Sản phẩm (Sales & Products)
- [ ] **Cấu trúc Dữ liệu Sản phẩm (Product Master Data)**
  - [ ] Phân biệt `product.template` (Mẫu sản phẩm) vs `product.product` (Biến thể cụ thể)
  - [ ] Quản lý Thuộc tính & Giá trị (Attributes & Values: Màu sắc, Kích cỡ)
  - [ ] Đơn vị tính (Units of Measure - UoM) & Tỷ lệ quy đổi
- [ ] **Bảng giá & Chính sách thương mại (Pricelists)**
  - [ ] Bảng giá theo đối tượng khách hàng (VIP, Đại lý, Bán lẻ)
  - [ ] Bảng giá đa tiền tệ (VND, USD) & Chiết khấu theo bậc số lượng
- [ ] **Quy trình Bán hàng chuẩn (Sales Order Flow)**
  - [ ] Vòng đời Báo giá: Báo giá nháp (Quotation) $\rightarrow$ Gửi email $\rightarrow$ Xác nhận đơn hàng (Sales Order)
  - [ ] Tích hợp CRM sang Sales: Tạo Báo giá trực tiếp từ Opportunity
  - [ ] Hạn mức công nợ khách hàng (Credit Limit Warning)
- [ ] **Hóa đơn Bán hàng cơ bản (Invoicing)**
  - [ ] Chính sách xuất hóa đơn: Theo số lượng đặt (Ordered) vs Theo số lượng đã giao (Delivered)
  - [ ] Tạo hóa đơn khách hàng (Customer Invoice) từ đơn hàng & Kiểm tra trạng thái thanh toán

---

## 📦 GIAI ĐOẠN 2: CHUỖI CUNG ỨNG & VẬN HÀNH KHO

### 2.1. Quản lý Kho chuẩn quốc tế (Inventory)
- [ ] **Nguyên lý Kho Hạch toán kép (Double-entry Inventory)**
  - [ ] Bản chất các loại Địa điểm kho (Locations: Physical, Virtual, Customer, Vendor, Production)
  - [ ] Dịch chuyển kho (Stock Move & Stock Move Line)
- [ ] **Quy trình Giao/Nhận hàng đa bước (Multi-step Routes)**
  - [ ] Quy trình 1 bước: Giao ngay từ kho
  - [ ] Quy trình 2 bước: Nhặt hàng (Pick) $\rightarrow$ Giao hàng (Ship)
  - [ ] Quy trình 3 bước: Nhặt hàng (Pick) $\rightarrow$ Đóng gói (Pack) $\rightarrow$ Xuất hàng (Ship)
- [ ] **Phương pháp Định giá Tồn kho & Tính giá vốn**
  - [ ] Giá tiêu chuẩn (Standard Price)
  - [ ] Bình quân gia quyền (Average Cost - AVCO)
  - [ ] Nhập trước xuất trước (FIFO)
- [ ] **Quy tắc Tái đặt hàng tự động (Reordering Rules)**
  - [ ] Thiết lập Min/Max Stock và tự sinh yêu cầu mua hàng khi tồn kho dưới ngưỡng an toàn
- [ ] **Quản lý Lô, Serial & Ngoại lệ Kho**
  - [ ] Quản lý số Lô (Lot), Số Serial, Hạn sử dụng (Expiry Date)
  - [ ] Khách trả hàng (Customer Return) & Trả hàng cho NCC (Return to Vendor)
  - [ ] Hàng phế phẩm/tiêu hủy (Scrap) & Cân đối kiểm kê kho (Inventory Adjustment)

---

### 2.2. Mua hàng & Quản lý Nhà cung cấp (Procure-to-Pay - P2P)
- [ ] **Luồng Mua hàng chuẩn (P2P Flow)**
  - [ ] Yêu cầu báo giá NCC (RFQ) $\rightarrow$ Đơn mua hàng (Purchase Order) $\rightarrow$ Nhận hàng $\rightarrow$ Hóa đơn NCC (Vendor Bill)
- [ ] **Quy tắc Đối soát 3 bên (3-Way Matching)**
  - [ ] Kiểm tra đối soát: Số lượng trên PO == Số lượng Phiếu nhập kho == Số lượng trên Hóa đơn NCC
  - [ ] Xử lý sai lệch đơn giá hoặc hàng giao thiếu/thừa (Backorders)
- [ ] **Chiến lược Cung ứng liên kết (Fulfillment Strategies)**
  - [ ] MTO (Make-to-Order) vs MTS (Make-to-Stock)
  - [ ] Bán hàng Dropshipping (NCC giao hàng trực tiếp cho người mua)

---

## 💰 GIAI ĐOẠN 3: TÀI CHÍNH, TỰ ĐỘNG HÓA & TƯ VẤN ERP

### 3.1. Kế toán Cốt lõi cho BA (Accounting Core)
- [ ] **Hệ thống Tài khoản & Cơ chế Bút toán tự động**
  - [ ] Hệ thống tài khoản kế toán (Chart of Accounts - COA), Sổ nhật ký (Journals)
  - [ ] Bút toán tự động sinh khi Xuất kho: Nợ Giá vốn (COGS) / Có Hàng tồn kho
  - [ ] Bút toán tự động sinh khi Xuất hóa đơn: Nợ Phải thu (AR) / Có Doanh thu & Thuế
  - [ ] Bút toán tự động sinh khi Nhận hóa đơn NCC: Nợ Tạm tính / Có Phải trả (AP)
- [ ] **Thu tiền, Thanh toán & Đối soát Ngân hàng**
  - [ ] Ghi nhận thanh toán khách hàng & Chi trả nhà cung cấp
  - [ ] Cơ chế đối soát sao kê ngân hàng (Bank Reconciliation) & Đóng kỳ kế toán

---

### 3.2. Tự động hóa & Báo cáo Quản trị BI
- [ ] **Tự động hóa No-code / Low-code**
  - [ ] Cấu hình Automated Actions (Trigger theo điều kiện thời gian hoặc thay đổi dữ liệu)
  - [ ] Thiết lập Webhooks & Gửi thông báo tự động qua Email/Chatter
- [ ] **Dashboard Phân tích cho Ban Giám đốc**
  - [ ] Xây dựng Dashboard bằng Odoo Spreadsheet liên kết trực tiếp dữ liệu ERP
  - [ ] Thiết kế báo cáo tài chính P&L, Dòng tiền và KPI vận hành theo thời gian thực

---

### 3.3. Phương pháp luận Tư vấn Triển khai ERP (Fit-Gap & Leadership)
- [ ] **Khảo sát & Phân tích Hiện trạng (AS-IS vs TO-BE)**
  - [ ] Kỹ thuật phỏng vấn phòng ban & bóc tách điểm nghẽn quy trình
  - [ ] Vẽ sơ đồ quy trình tương lai (TO-BE Process Flow)
- [ ] **Ma trận Phân tích Khoảng cách (Fit-Gap Matrix)**
  - [ ] Đánh giá: Standard (80%) vs Configuration (10%) vs Customization (10%)
  - [ ] Đưa ra giải pháp thay thế (Workarounds) để bảo vệ tính nguyên bản của ERP
- [ ] **Kỹ năng Quản trị Dự án dành cho BA Leader**
  - [ ] Kỹ năng quản lý phạm vi (Scope Management) & Phòng chống Scope Creep
  - [ ] Kỹ năng ước lượng khối lượng công việc (Effort Estimation) cho Dev
  - [ ] Kế hoạch làm sạch và chuyển đổi dữ liệu (Data Migration / ETL Plan)

---

## 📋 DANH MỤC 14 QUY TẮC NGHIỆP VỤ CỐT LÕI (BUSINESS RULES CHECKLIST CHO BA)
*Chi tiết phân tích & cấu hình nghiệp vụ tại: [Business_Rules_Analysis.md](file:///e:/BA/Ba-case/odoo/odoo/doc/Business_Rules_Analysis.md)*

- [x] **BR-01:** Quy tắc Ràng buộc & Thẩm định tính hợp lệ dữ liệu (Validation Rules)
- [x] **BR-02:** Quy tắc Tính toán công thức tự động (Calculation Rules: Thành tiền, Thuế, Hoa hồng)
- [x] **BR-03:** Quy tắc Điền thông tin tự động theo ngữ cảnh (Contextual Auto-fill Rules)
- [x] **BR-04:** Quy tắc Vòng đời trạng thái & Điều kiện chuyển chặng (Workflow State & Transition Rules)
- [x] **BR-05:** Quy tắc Ẩn/Hiện & Bắt buộc nhập liệu theo điều kiện (Conditional Visibility Rules)
- [x] **BR-06:** Ma trận Phân quyền chức năng theo vai trò chức danh (Role-Based Access Matrix)
- [x] **BR-07:** Ma trận Phân quyền phạm vi dữ liệu & Bảo vệ khách hàng (Data Scope & Ownership Rules)
- [x] **BR-08:** Quy tắc Tự động hóa tác vụ & Cam kết thời gian SLA (Scheduled Automation & SLA Rules)
- [x] **BR-09:** Quy tắc Thiết lập giá trị mặc định thông minh (Smart Default Value Rules)
- [x] **BR-10:** Quy tắc Đánh giá & Chuẩn hóa chất lượng thông tin liên hệ (Data Quality & Verification Rules)
- [x] **BR-11:** Quy tắc Kiểm soát & Hợp nhất dữ liệu trùng lặp (Deduplication & Merge Policies)
- [x] **BR-12:** Quy tắc Định tuyến đa kênh & Thông báo tự động (Omnichannel Routing & Alert Rules)
- [x] **BR-13:** Quy tắc Nhật ký kiểm toán & Theo dõi lịch sử biến động (Audit Trail & Activity Tracking)
- [x] **BR-14:** Quy tắc Nhận diện doanh thu & Quản trị tiền tệ (Revenue Recognition & Currency Rules)

---

## 📂 HỒ SƠ NĂNG LỰC ĐẦU RA (PORTFOLIO DELIVERABLES)

- [ ] **Deliverable 1:** Bảng điểm tốt nghiệp 8 Module CRM đạt chuẩn BA Leader (Hiện tại TB: 9.0/10 - [CRM_Learning_Progress.md](file:///e:/BA/Ba-case/odoo/odoo/doc/CRM_Learning_Progress.md)).
- [x] **Deliverable Sơ đồ:** Sơ đồ Swimlane Vòng đời Odoo CRM chuẩn 4 luồng ([diagram/CRM_Lifecycle_Swimlane.md](file:///e:/BA/Ba-case/odoo/odoo/diagram/CRM_Lifecycle_Swimlane.md) | Ảnh: [PNG](file:///e:/BA/Ba-case/odoo/odoo/diagram/png/crm-lifecycle-swimlane.png) & [SVG](file:///e:/BA/Ba-case/odoo/odoo/diagram/crm-lifecycle-swimlane.svg)).
- [x] **Deliverable Case Study M3:** Bản đề xuất giải pháp tối ưu Pipeline, Rotting SLA 14 ngày & Chuẩn hóa lý do thua ([doc/case.md](file:///e:/BA/Ba-case/odoo/odoo/doc/case.md)).
- [x] **Deliverable Case Study M4:** Bản đặc tả giải pháp Phân bổ Lead Round-Robin, Ma trận phân quyền 3 cấp & Cơ chế chống cướp khách/chống trùng khách ([doc/case_module_4.md](file:///e:/BA/Ba-case/odoo/odoo/doc/case_module_4.md)).
- [x] **Deliverable Case Study M5:** Bản đặc tả giải pháp Cơ hội hỗn hợp One-off + MRR, Bật cờ Slipping Deals và Dashboard C-Level ([doc/case_module_5.md](file:///e:/BA/Ba-case/odoo/odoo/doc/case_module_5.md)).
- [x] **Deliverable Nghiệp vụ:** Ma trận 2 Điểm đau Thực tế chưa được Odoo giải quyết & Giải pháp BA ([doc/CRM_Pain_Points.md](file:///e:/BA/Ba-case/odoo/odoo/doc/CRM_Pain_Points.md)).
- [ ] **Deliverable 2:** Bộ tài liệu đặc tả yêu cầu nghiệp vụ chuẩn (FSD: Lead-to-Order Flow).
- [ ] **Deliverable 3:** Bộ sơ đồ quy trình BPMN 2.0 hoàn chỉnh cho Chuỗi Cung ứng (P2P & Kho).
- [ ] **Deliverable 4:** Bộ 20 Test Cases xử lý ngoại lệ (Edge Cases) theo chuẩn BDD Gherkin.
- [ ] **Deliverable 5:** Bản phân tích Fit-Gap Matrix hoàn chỉnh cho 1 dự án ERP doanh nghiệp mẫu.

---

## 🗄️ LỊCH SỬ THAY ĐỔI TÀI LIỆU (CHANGELOG)

| Phiên bản | Ngày | Người cập nhật | Nội dung cập nhật |
| :---: | :---: | :---: | :--- |
| **v1.0** | 2026-09-02 | AI Trainer | Khởi tạo Checklist 3 giai đoạn. |
| **v2.0** | 2026-09-04 | Lead BA & AI | Hoàn thành Module 3 CRM, cập nhật 3 deliverables thực chiến (Sơ đồ Swimlane 4 luồng, Case Study ngâm deal và Ma trận 2 điểm đau thực tế). |
| **v2.1** | 2026-09-05 | Lead BA & AI | **Hiệu chỉnh 100% sang Checklist Nghiệp vụ BA**: Chuẩn hóa 14 Business Rules từ lăng kính phân tích quy trình nghiệp vụ thay vì code Python. |
| **v2.2** | 2026-09-06 | Lead BA & AI | **Nghiệm thu hoàn thành Module 4 CRM**: Đạt 9.0/10 bài tập tình huống lớn, xuất bản `doc/case_module_4.md`, tiến độ Giai đoạn 1 đạt 50%, sẵn sàng bước sang Module 5. |
| **v2.3** | 2026-09-06 | Lead BA & AI | **Nghiệm thu hoàn thành Module 5 CRM**: Đạt 10/10 Trắc nghiệm và 9.5/10 Tự luận Voice Audio, xuất bản `doc/case_module_5.md`, tiến độ GĐ1 đạt 62.5% (Điểm TB 9.0/10). |
