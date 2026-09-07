# KẾ HOẠCH BỘ SƠ ĐỒ PORTFOLIO ODOO CRM (IT-BA)

> **Dự án:** Tư vấn & Triển khai Odoo CRM (TechCorp)  
> **Mục tiêu:** Xây dựng bộ tài liệu trực quan (Visual Artifacts) phục vụ Portfolio GitHub cho vị trí IT Business Analyst.  
> **Tiêu chuẩn áp dụng:** Nguyên tắc thiết kế sơ đồ từ `diagram-skills-package` (Mermaid native cho GitHub Markdown & PlantUML cho quy trình đa vai trò).

---

## 1. BẢNG MA TRẬN BỘ SƠ ĐỒ PORTFOLIO

| STT | Loại sơ đồ | Tên sơ đồ | Công cụ | Trọng tâm nghiệp vụ | File đích / Output | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **Use Case** | Bức tranh tổng quan chức năng CRM | **PlantUML** | Phân quyền Actor (Sales, Manager, Marketing, System) & System Boundary | [CRM_UseCase_Overview.md](file:///e:/BA/Ba-case/odoo/odoo/diagram/CRM_UseCase_Overview.md) | ✅ Hoàn thành |
| **02** | **Activity Swimlane** | Quy trình phối hợp Lead-to-Opportunity đa vai | **PlantUML Swimlane** | Luồng tương tác chéo giữa Marketing $\rightarrow$ Hệ thống $\rightarrow$ Sales $\rightarrow$ Quản lý | [CRM_Lifecycle_Swimlane.md](file:///e:/BA/Ba-case/odoo/odoo/diagram/CRM_Lifecycle_Swimlane.md) | ✅ Đã có nền tảng |
| **03** | **Decision Flowchart** | Thuật toán Phân bổ & Khử trùng lặp Lead | **Mermaid & PlantUML** | Kiểm tra trùng lặp email/contact, tự động gộp, lọc Domain đội, ưu tiên chuyên gia & xoay vòng Round-Robin | [Lead_Assignment_Decision_Flow.md](file:///e:/BA/Ba-case/odoo/odoo/diagram/Lead_Assignment_Decision_Flow.md) | ✅ Hoàn thành (100% Odoo Standard) |
| **04** | **State Machine** | Vòng đời Cơ hội Bán hàng (Opportunity Pipeline) | **Mermaid** | Trạng thái Deal: `New` $\rightarrow$ `Qualified` $\rightarrow$ `Proposition` $\rightarrow$ `Won`/`Lost` kèm điều kiện chuyển | `diagram/crm-opportunity-state.md` | 🎯 **Ưu tiên số 1** |
| **05** | **ERD Diagram** | Mô hình Dữ liệu Quan hệ Thực thể Odoo CRM | **Mermaid** | Bảng chính: `crm.lead`, `res.partner`, `res.users`, `crm.team`, `mail.activity` | `diagram/crm-erd.md` | ⏳ Ưu tiên số 2 |
| **06** | **Sequence** *(Bonus)* | Luồng Tích hợp Thu thập Lead từ Website Form | **Mermaid** | Tương tác Webhook: Khách điền Form $\rightarrow$ Landing Page $\rightarrow$ Odoo API CRM | `diagram/crm-lead-integration-seq.md` | 💡 Điểm cộng |

---

## 2. CHI TIẾT ĐẶC TẢ TỪNG SƠ ĐỒ

### 01. Sơ đồ Use Case — Tổng quan Phạm vi (System Scope)
*   **Mục đích:** Cung cấp cái nhìn 30.000 feet cho nhà tuyển dụng/stakeholder thấy hệ thống CRM gồm những ai sử dụng và có những cụm tính năng nào.
*   **Các thành phần chính:**
    *   **Actors:** Sales Representative, Sales Manager, Marketing Executive, Odoo Cron System.
    *   **Packages/Chức năng:**
        *   *Lead Acquisition:* Nhập lead thủ công, nhận lead qua Web/Form.
        *   *Lead Routing:* Phân bổ tự động, chống cướp khách.
        *   *Pipeline Execution:* Thẩm định, tạo cơ hội, báo giá, chốt Won/Lost.
        *   *Supervision & Reporting:* Báo cáo KPI, duyệt ngoại lệ phân bổ.

---

### 02. Sơ đồ Quy trình Đa vai trò (Activity Swimlane)
*   **Mục đích:** Thể hiện năng lực mô hình hóa quy trình nghiệp vụ phối hợp liên phòng ban (Cross-functional Process).
*   **Các làn (Lanes):**
    *   `Marketing`: Chạy chiến dịch, thu thập Contact.
    *   `Odoo System`: Đánh giá Lead Score, kiểm tra trùng lặp, tự động gán Sales.
    *   `Sales Rep`: Tiếp cận trong 15 phút, gọi điện, demo, báo giá.
    *   `Sales Manager`: Can thiệp khi quá hạn SLA hoặc phê duyệt chính sách giá đặc biệt.

---

### 03. Sơ đồ Quyết định Phân bổ Lead (Decision Flowchart) - 100% Odoo Standard
*   **Mục đích:** Mô hình hóa thuật toán lõi chuẩn Odoo 19 Standard (`crm_team.py`, `crm_team_member.py`, `crm_lead.py`), xử lý các trường hợp biên khi phân bổ khách.
*   **Nội dung chuẩn Odoo 19:**
    *   *Khử trùng lặp (`_get_lead_duplicates`):* Phát hiện trùng lặp email/contact $\rightarrow$ Tự động gộp vào bản ghi chính (`_merge_opportunity`) trước khi phân bổ.
    *   *Phân bổ Đội bán hàng (`_allocate_leads`):* Lọc `team.assignment_domain` $\rightarrow$ Phân bổ theo trọng số dung tích `team.assignment_max` $\rightarrow$ Treo bể chưa gán nếu không khớp đội nào.
    *   *Phân bổ Nhân sự (`_assign_and_convert_leads`):* Lọc thành viên không tạm dừng (`not assignment_optout`) và còn quota $\rightarrow$ Vòng 1 ưu tiên chuyên gia (`domain_preferred`) theo xác suất cao nhất $\rightarrow$ Vòng 2 xoay vòng Round-Robin công bằng $\rightarrow$ Tự động chuyển đổi thành Cơ hội (`convert_opportunity`).

---

### 04. Sơ đồ Trạng thái Vòng đời Cơ hội (State Machine Diagram) ⭐
*   **Mục đích:** Mô tả trạng thái và quy tắc di chuyển của một Deal trong Sales Pipeline.
*   **Các State chuẩn Odoo CRM:**
    1.  `[New]` (Mới nhận từ Lead chuyển sang).
    2.  `[Qualified]` (Đã xác thực ngân sách, thẩm quyền, nhu cầu - BANT criteria).
    3.  `[Proposition]` (Đã gửi báo giá/đề xuất giải pháp chính thức).
    4.  `[Won]` (Chốt thành công $\rightarrow$ Đẩy sang đơn hàng Sales Order).
    5.  `[Lost]` (Thất bại $\rightarrow$ Bắt buộc chọn Lý do rớt deal: Giá cao, Đối thủ, v.v.).

---

### 05. Sơ đồ Quan hệ Thực thể Dữ liệu (ERD Diagram)
*   **Mục đích:** Thể hiện tư duy cấu trúc dữ liệu, hiểu tầng Database & Object của Odoo để làm việc với Developer.
*   **Các Entity chính:**
    *   `crm.lead` (Lưu thông tin Lead/Cơ hội).
    *   `res.partner` (Khách hàng doanh nghiệp hoặc cá nhân liên kết).
    *   `res.users` (Nhân viên phụ trách).
    *   `crm.team` (Đội ngũ bán hàng).
    *   `mail.activity` (Lịch gọi, hẹn gặp, gửi email định kỳ).

---

### 06. Sơ đồ Tuần tự Tích hợp (Sequence Diagram - Bonus)
*   **Mục đích:** Thể hiện kiến thức kỹ thuật về tích hợp API giữa hệ thống bên thứ 3 (Website, Facebook Lead Ads) vào Odoo CRM qua Webhook.

---

## 3. CHECKLIST TIẾN ĐỘ THỰC HIỆN

- [x] Sơ đồ Quyết định Phân bổ Lead & Chống cướp khách (`lead-assignment-mermaid.md`)
- [ ] Sơ đồ Trạng thái Vòng đời Cơ hội (`crm-opportunity-state.md`)
- [ ] Sơ đồ ERD Dữ liệu Odoo CRM (`crm-erd.md`)
- [x] Sơ đồ Use Case tổng thể (`crm-usecase.puml` & `CRM_UseCase_Overview.md`)
- [ ] Rà soát & nhúng toàn bộ sơ đồ vào `README.md` chính của Portfolio
