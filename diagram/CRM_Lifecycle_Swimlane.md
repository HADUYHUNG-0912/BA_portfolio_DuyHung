# QUY TRÌNH VÒNG ĐỜI ODOO CRM (SWIMLANE PROCESS FLOW)

> **Mục tiêu:** Bản vẽ quy trình Swimlane tổng quát, súc tích, **chữ lớn và tiếng Việt có dấu 100%**.  
> **Các bên tham gia (4 làn bơi):** Khách hàng | Nhân viên Kinh doanh | Hệ thống Odoo 19 | Quản lý Kinh doanh.  
> **File nguồn:** [crm-lifecycle-swimlane.puml](crm-lifecycle-swimlane.puml) | [crm-lifecycle-swimlane.drawio](crm-lifecycle-swimlane.drawio)  
> **File ảnh xuất ra:** [crm-lifecycle-swimlane.svg](crm-lifecycle-swimlane.svg) (Vector sắc nét) | [crm-lifecycle-swimlane.png](png/crm-lifecycle-swimlane.png) (Ảnh lớn)  
> 📌 **Tài liệu liên quan:** [README.md](../README.md)

---

## 1. BẢN VẼ SƠ ĐỒ HÌNH ẢNH (BẢN CHỮ LỚN - TIẾNG VIỆT CÓ DẤU)

![Sơ đồ Swimlane Odoo CRM](crm-lifecycle-swimlane.svg)

---

## 2. SƠ ĐỒ MERMAID ĐỌC TRỰC TIẾP TRÊN MARKDOWN

```mermaid
flowchart TD
    %% 4 Làn bơi với nhãn tiếng Việt rõ ràng
    subgraph LANE_CUSTOMER["👤 1. KHÁCH HÀNG"]
        C1([Bắt đầu: Gửi nhu cầu Web / Email / Hotline])
        C2[Xem xét Báo giá & Thỏa thuận hợp đồng]
        C_Decision{Khách ký hợp đồng / Xác nhận đơn?}
    end

    subgraph LANE_SALES["💼 2. NHÂN VIÊN KINH DOANH"]
        SP1[Nhận Lead & Gọi khảo sát BANT]
        SP_Qualify{Khách có nhu cầu thật?}
        SP_LostJunk[Đánh dấu Thua: Lead rác]
        SP2[Bấm Convert to Opportunity: Cột Qualified]
        SP3[Khảo sát & Bấm New Quotation: Tạo Báo giá]
        SP4[Gửi Báo giá & Kéo sang Proposition]
        SP_Won[Bấm WON: Xác nhận Thắng deal]
        SP_Lost[Bấm LOST: Chốt thua]
        SP_Reason[Chọn Lý do thua & Ghi chú]
    end

    subgraph LANE_ODOO["⚙️ 3. HỆ THỐNG ODOO 19 (AI & ENGINE)"]
        S1[Tự tạo Lead & Chấm điểm tiềm năng AI]
        S2[Tự động phân bổ Lead theo đội bán hàng]
        S_LostArchive1[Lưu trữ Lead: active = False]
        S3[AI tự tính Xác suất & Doanh thu trọng số]
        S_RottingCheck{Deal bị ngâm quá ngưỡng quy định?}
        S_RottingAlert[Đổi màu thẻ Kanban: Rotting indicator]
        S_WonAction[Set Xác suất = 100%, Pháo hoa 🎉, Kích hoạt đơn bán]
        S_LostArchive2[Đưa xác suất = 0%, Ẩn thẻ: Archive active = False]
    end

    subgraph LANE_MANAGER["👔 4. QUẢN LÝ KINH DOANH (CCO)"]
        M_Escalate[Lọc theo dõi deal ngâm: Filter Rotting]
        M_BI[Xem báo cáo phân tích Lost Analysis định kỳ]
    end

    %% Luồng nghiệp vụ liên kết
    C1 --> S1 --> S2 --> SP1 --> SP_Qualify
    SP_Qualify -- Không đạt --> SP_LostJunk --> S_LostArchive1 --> End1([Kết thúc])
    SP_Qualify -- Đạt chuẩn --> SP2 --> SP3 --> SP4 --> S3 --> S_RottingCheck
    S_RottingCheck -- Có ngâm --> S_RottingAlert --> M_Escalate --> C2
    S_RottingCheck -- Đúng tiến độ --> C2
    C2 --> C_Decision
    C_Decision -- Đã ký hợp đồng --> SP_Won --> S_WonAction --> EndWon([🎉 THÀNH CÔNG: CHUYỂN GIAO HÀNG & KẾ TOÁN THU TIỀN])
    C_Decision -- Từ chối ký --> SP_Lost --> SP_Reason --> S_LostArchive2 --> M_BI --> EndLost([❌ THẤT BẠI: ĐÓNG DEAL & PHÂN TÍCH])

    %% Định kiểu màu sắc nổi bật
    style EndWon fill:#d4edda,stroke:#28a745,stroke-width:3px;
    style EndLost fill:#f8d7da,stroke:#dc3545,stroke-width:3px;
    style S_RottingAlert fill:#fff3cd,stroke:#ffc107,stroke-width:3px;
```

---

## 3. TÓM TẮT 4 BƯỚC NGHIỆP VỤ CỐT LÕI

| Giai đoạn | Thao tác của Người dùng (User Action) | Hệ thống Odoo 19 tự động xử lý (System Logic) |
| :--- | :--- | :--- |
| **1. Tiếp nhận Lead** | Khách gửi thông tin liên hệ $\rightarrow$ Sale nhận thông báo. | Tự tạo Lead, kiểm tra trùng lặp và tự động phân bổ theo dung tích (Capacity). |
| **2. Thẩm định (Qualification)** | Sale gọi điện khảo sát nhu cầu theo chuẩn BANT. | Nếu tiềm năng $\rightarrow$ Bấm **Convert to Opportunity** (chuyển sang cột Qualified). |
| **3. Báo giá & Đàm phán** | Bấm **New Quotation** tạo Báo giá $\rightarrow$ Kéo sang cột **Proposition**. | AI tự tính xác suất chốt deal; Theo dõi mốc ngâm deal (**Rotting Threshold: 5, 14, 30 ngày tùy cấu hình**) để đổi màu cảnh báo. |
| **4. Chốt giao dịch** | **Thắng:** Bấm **Won** $\rightarrow$ Kích hoạt đơn hàng bán.<br>**Thua:** Bấm **Lost** $\rightarrow$ Bắt buộc chọn Lý do thua. | Won: Xác suất nhảy 100%, ghi nhận doanh số.<br>Lost: Xác suất về 0%, lưu trữ bản ghi và cập nhật báo cáo BI. |

> 💡 **Lưu ý nghiệp vụ BA về Rotting:**
> * Trong mã nguồn Odoo gốc: Giá trị mặc định là **`0`** (Tắt cảnh báo).
> * Trong dữ liệu mẫu Demo (Runbot): Cột *Proposition* được cài mẫu là **`5 ngày`** (đó là lý do thẻ 6 ngày bị đổi màu `6d`).
> * Trong thực tế triển khai: BA sẽ cùng Giám đốc Kinh doanh thỏa thuận SLA riêng cho từng giai đoạn (ví dụ: 7 ngày cho B2C, 14–21 ngày cho B2B phần mềm).

---

## 🗄️ LỊCH SỬ THAY ĐỔI TÀI LIỆU (CHANGELOG)

| Phiên bản | Ngày | Người cập nhật | Nội dung cập nhật |
| :---: | :---: | :---: | :--- |
| **v1.0** | 2026-09-04 | Lead BA & AI | Thiết kế sơ đồ Swimlane 4 luồng cho Vòng đời Odoo CRM. |
| **v2.0** | 2026-09-04 | Lead BA & AI | Tinh chỉnh chuẩn hóa luồng Won: Làm rõ điều kiện rẽ nhánh "Khách ký hợp đồng / Xác nhận đơn" và kích hoạt Đơn bán hàng chuyển Giao hàng & Kế toán thu tiền. |
