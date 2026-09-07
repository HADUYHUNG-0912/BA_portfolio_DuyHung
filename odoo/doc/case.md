# CASE STUDY NGHIỆP VỤ: TỐI ƯU QUẢN TRỊ PIPELINE & NGĂN CHẶN "NGÂM DEAL"

> **Phân hệ:** Odoo CRM (v19.0)  
> **Chủ đề:** Pipeline, Stage Management & Lost Reasons Analysis  
> **Vai trò:** Lead Business Analyst (BA Leader)  
> **Khách hàng / Stakeholder:** Giám đốc Kinh doanh (CCO)  
> 
> 📌 **Tài liệu liên quan:** [Sơ đồ Lead-to-Order Swimlane (PNG)](../diagram/CRM_Lead_To_Order_Swimlane_Process.png) | [CRM_Pain_Points.md](./CRM_Pain_Points.md) | [README.md](../README.md)

---

## 1. BỐI CẢNH & ĐỀ BÀI TÌNH HUỐNG

Bạn là BA Leader đang tư vấn triển khai hệ thống Odoo CRM cho một công ty B2B chuyên cung cấp giải pháp phần mềm và chuyển đổi số cho doanh nghiệp.

Trong buổi khảo sát quy trình bán hàng, **Giám đốc Kinh doanh (CCO)** phàn nàn:
> *"Nhân viên của tôi có thói quen xấu: khi không chốt được deal, họ cứ để mặc deal nằm mốc meo ở giai đoạn 'Đàm phán' tháng này qua tháng khác khiến dự báo doanh số của tôi bị sai bét. Hoặc khi bị tôi nhắc nhở gắt gao, họ mới bấm bừa nút Lost nhưng không thèm ghi lý do, hoặc chỉ ghi qua loa 'khách không mua'."*

### Yêu cầu đặt ra cho BA Leader:
Đề xuất giải pháp toàn diện kết hợp giữa **Cấu hình chuẩn hệ thống Odoo 19** và **Quy trình vận hành nội bộ** nhằm giải quyết dứt điểm 2 bài toán:
1. Làm sao để phát hiện và ngăn chặn việc "ngâm deal" tại các giai đoạn?
2. Làm sao để bắt buộc nhân viên thu thập dữ liệu lý do thua một cách chuẩn hóa phục vụ cho việc cải tiến sản phẩm và chính sách giá sau này?

---

## 2. BẢN ĐỀ XUẤT GIẢI PHÁP CHUẨN HÓA (BA LEADER PROPOSAL)

**Kính gửi:** Giám đốc Kinh doanh (CCO)  
**Người lập:** Đội ngũ Tư vấn Giải pháp CRM (BA Leader)

Để giải quyết triệt để 2 vấn đề trên mà không làm gián đoạn hay gây ức chế cho trải nghiệm người dùng, chúng tôi đề xuất giải pháp gồm 2 phần như sau:

---

### VẤN ĐỀ 1: PHÁT HIỆN VÀ NGĂN CHẶN VIỆC "NGÂM DEAL"

#### a. Cảnh báo trực quan trên Kanban (Visual SLA - Rotting Threshold)
* **Giải pháp Odoo 19:** Trên giai đoạn `crm.stage` "Đàm phán", kích hoạt trường:
  $$\text{rotting\_threshold\_days} = 14 \text{ (ngày)}$$
* **Cơ chế vận hành:** 
  * Nếu một cơ hội nằm ở giai đoạn "Đàm phán" quá 14 ngày mà không có bất kỳ tương tác mới nào (không có cuộc gọi, lịch hẹn, email hay cập nhật tiến độ), thẻ deal trên màn hình Kanban sẽ tự động **đổi sang màu cảnh báo (Rotting Indicator)**.
  * CCO và Trưởng nhóm kinh doanh chỉ cần lướt qua màn hình Kanban là nhận diện ngay các "điểm nghẽn" mà không cần xuất báo cáo Excel thủ công.

#### b. Tự động hóa nhắc việc & Báo cáo vượt cấp (Automated Action & Escalation)
* **Mốc 14 ngày (Nhắc nhở nhân viên):** Hệ thống tự động tạo 1 công việc (`mail.activity`) loại **"Đôn đốc cập nhật trạng thái cơ hội"** trên Chatter, gán trực tiếp cho nhân viên phụ trách với thời hạn xử lý trong vòng 48 giờ.
* **Mốc 16 ngày (Quy tắc Escalation vượt cấp):** Nếu sau 48 giờ nhân viên vẫn không có hành động cập nhật, hệ thống tự động gửi thông báo trực tiếp lên kênh trao đổi nội bộ của **Sale Manager / CCO** kèm đường link dẫn thẳng vào cơ hội để quản lý can thiệp kịp thời.

---

### VẤN ĐỀ 2: BẮT BUỘC THU THẬP DỮ LIỆU LÝ DO THUA CHUẨN HÓA

#### a. Chuẩn hóa danh mục lý do thua (`crm.lost.reason`)
Khảo sát thực tế đội ngũ kinh doanh để thống nhất danh mục **5 – 7 lý do cốt lõi** (chọn 1 lý do chính để đảm bảo biểu đồ phân tích không bị phân mảnh dữ liệu):
1. *Giá cao hơn ngân sách dự kiến của khách hàng*
2. *Thiếu tính năng cốt lõi (Sản phẩm chưa đáp ứng)*
3. *Khách hàng lựa chọn đối thủ cạnh tranh*
4. *Khách hàng hoãn / hủy kế hoạch chuyển đổi số năm nay*
5. *Dịch vụ triển khai chưa đáp ứng được tiến độ yêu cầu*
6. *Lý do khác (Yêu cầu giải trình chi tiết)*

#### b. Chặn lỗi ngay từ cấp độ hệ thống (System Constraint / Poka-Yoke)
Áp dụng nguyên lý *"Không dùng kỷ luật để phạt những lỗi mà phần mềm có thể chặn đứng từ đầu"*:
* **Khóa nút xác nhận:** Trên màn hình popup đóng deal (`crm.lead.lost`), thiết lập trường `lost_reason_id` thành **Bắt buộc nhập (`required = True`)**. Nhân viên bắt buộc phải chọn 1 lý do trong danh mục thì nút "Submit / Đánh dấu thua" mới sáng lên.
* **Logic điều kiện cho lý do đặc thù:** Khi nhân viên chọn mục *"Lý do khác"*, ô Ghi chú chi tiết (`lost_feedback`) sẽ tự động chuyển sang trạng thái bắt buộc nhập (tối thiểu 1 câu mô tả rõ ràng nguyên nhân cụ thể).

#### c. Phục vụ Cải tiến Sản phẩm và Chính sách Giá (BI & Lost Analysis)
* Dữ liệu deal thua được tự động tổng hợp vào báo cáo **Lost Opportunity Analysis**:
  * Nhóm theo ma trận: **Lý do thua $\times$ Quy mô doanh thu $\times$ Đối thủ cạnh tranh**.
  * Báo cáo này là cơ sở trực tiếp cho cuộc họp định kỳ hàng tháng giữa **CCO, Giám đốc Sản phẩm (CPO) và Ban Giám đốc** nhằm nhận diện chính xác:
    * Có phải chính sách giá đang bị định giá quá cao so với mặt bằng chung?
    * Sản phẩm đang liên tục bị thua đối thủ ở tính năng hay module cụ thể nào?

---

## 3. TÁC ĐỘNG & GIÁ TRỊ MANG LẠI CHO DOANH NGHIỆP

| Tiêu chí | Trước khi áp dụng | Sau khi chuẩn hóa hệ thống |
| :--- | :--- | :--- |
| **Độ chính xác dự báo (Forecast Accuracy)** | Sai lệch lớn do hàng chục deal "ảo/chết" vẫn nằm ở giai đoạn Đàm phán. | Dữ liệu thời gian thực; CFO và CCO tự tin lập kế hoạch doanh số và dòng tiền. |
| **Tỷ lệ thất thoát cơ hội (Deal Leakage)** | Nhiều deal tiềm năng bị nhân viên bỏ quên hoặc chăm sóc chậm trễ. | Cảnh báo visual đổi màu thẻ + Escalation rule giúp cứu vãn kịp thời các deal bị nghẽn. |
| **Chất lượng dữ liệu đầu vào (Data Integrity)** | Dữ liệu phân mảnh, lý do ghi bừa bãi không thể dùng để ra quyết định. | 100% deal thua có lý do chuẩn hóa, phân loại rõ ràng theo đối thủ và ngân sách. |

---

## 🗄️ LỊCH SỬ THAY ĐỔI TÀI LIỆU (CHANGELOG)

| Phiên bản | Ngày | Người cập nhật | Nội dung cập nhật |
| :---: | :---: | :---: | :--- |
| **v1.0** | 2026-09-04 | Lead BA & AI | Soạn thảo giải pháp xử lý ngâm deal Rotting SLA 14 ngày & chuẩn hóa lý do thua theo case CCO. |
