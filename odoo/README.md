# Nghiên Cứu Tình Huống: Tối Ưu Vận Hành Bán Hàng & Odoo ERP

> Ứng viên: **Hà Duy Hưng** — Business Analyst, Enterprise ERP & SaaS  
> Phương pháp: Value Stream Mapping, Swimlane Modeling, Poka-Yoke Rule Design, RBAC Data Matrix  
> Phạm vi: Tái cấu trúc chu trình Lead-to-Order trên Odoo 19 CRM & Bán hàng + Giải quyết 3 bài toán cấp điều hành  

---

## 1. Project Context

| Hạng mục | Chi tiết |
| :--- | :--- |
| **Đơn vị nghiệp vụ** | Doanh nghiệp phân phối và cung cấp giải pháp công nghệ B2B & B2C đa kênh |
| **Nền tảng ứng dụng** | Phân hệ Quản trị Quan hệ Khách hàng (CRM) & Bán hàng — Odoo ERP 19 (Tiêu chuẩn & Cấu hình Studio No-code) |
| **Phạm vi chu trình** | Luồng nghiệp vụ Lead-to-Order: Tiếp nhận Lead → Phân bổ → Đánh giá tiềm năng → Báo giá → Chốt hợp đồng |
| **Thời gian thực hiện** | Phân tích hiện trạng, chuẩn hóa quy trình, thiết lập rào chắn nghiệp vụ và tài liệu hóa trong 3 tuần |
| **Stakeholders liên quan** | Ban Giám đốc (CEO, CFO, CSD), Quản lý bán hàng (Sales Manager), Nhân viên kinh doanh (Sales Rep) |
| **Phương pháp tiếp cận** | Khảo sát điểm nghẽn vận hành, Mô hình hóa làn bơi Swimlane 4 tác nhân, Thiết lập 14 quy tắc nghiệp vụ Poka-Yoke |
| **Kết quả bàn giao** | 3 Sơ đồ kiến trúc (Swimlane, Data Flow, Use Case), 14 Business Rules chi tiết, 3 Case Study C-level thực chiến |

---

## 2. Business Problem Statement

Hệ thống bán hàng của doanh nghiệp phát triển nhanh dẫn tới khủng hoảng vận hành nghiêm trọng khi dữ liệu phình to nhưng thiếu kỷ luật hệ thống. Ban Giám đốc đối mặt với **3 điểm nghẽn cấp điều hành** cốt lõi:

### Vấn đề 1 — Tắc nghẽn Pipeline & Sai lệch dự báo dòng tiền (M3)
> Nhân viên kinh doanh có xu hướng "ngâm" các cơ hội không chốt được tại giai đoạn Đàm phán từ tháng này qua tháng khác để làm đẹp báo cáo cá nhân. Khi bị cấp trên đôn đốc, nhân viên bấm đóng thua bừa bãi hoặc không nhập lý do thất bại.
- **Root Cause:** Phễu bán hàng thiếu cơ chế kiểm soát SLA thời gian thực; phần mềm không có rào chắn bắt buộc phân loại nguyên nhân thất bại trước khi đóng deal.
- **Business Impact:** Sai lệch 35% dự báo doanh thu trình Ban Giám đốc; công ty mất hoàn toàn dữ liệu để cải tiến chính sách giá và sản phẩm.

### Vấn đề 2 — Tranh chấp nội bộ & Thất thoát tài sản dữ liệu khách hàng (M4)
> Đội ngũ 50 nhân viên kinh doanh chia thành 2 khối (Bán lẻ trực tuyến và Bán hàng doanh nghiệp B2B). Nhân viên tranh giành cướp khách mới từ hòm thư chung, người ôm quá nhiều dẫn tới trễ hạn liên hệ, người mới không có khách; nhân viên B2B giấu thông tin vào sổ tay riêng vì sợ đồng nghiệp nhìn trộm báo giá.
- **Root Cause:** Cơ chế phân bổ thủ công; thiếu ma trận phân quyền theo cấp bậc (RBAC) và thiếu kỹ thuật che dữ liệu nhạy cảm (Data Masking) khi kiểm tra trùng.
- **Business Impact:** Tốc độ phản hồi lead trễ trên 4 tiếng; nội bộ mâu thuẫn; nguy cơ rò rỉ 100% dữ liệu danh mục khách hàng khi nhân sự nghỉ việc.

### Vấn đề 3 — Khủng hoảng ghi nhận Doanh thu lai & Rủi ro thanh khoản tài chính (M5)
> Doanh nghiệp cung cấp gói giải pháp hỗn hợp gồm: Chi phí bản quyền/triển khai thu một lần (One-off) và Phí bảo trì/thuê bao thu định kỳ hàng tháng (MRR). Nhân viên liên tục dời ngày chốt dự kiến sang tháng sau trên màn hình dự báo để né phạt KPI.
- **Root Cause:** Hệ thống chỉ có 1 trường Doanh thu kỳ vọng duy nhất, không tách biệt dòng tiền ngay và dòng tiền định kỳ; thiếu cơ chế giám sát lịch sử thay đổi ngày chốt.
- **Business Impact:** Giám đốc Tài chính (CFO) bị động trong hoạch định thanh khoản vốn lưu động; dự báo tài chính ngắn hạn và dài hạn bị trộn lẫn.

---

## 3. Analysis Approach

Quy trình phân tích nghiệp vụ thực chiến được thực hiện theo 4 giai đoạn chuẩn mực dành cho chuyên viên phân tích ERP:

```
GIAI ĐOẠN 1: KHẢO SÁT & BÓC TÁCH ĐIỂM NGHẼN (VALUE STREAM MAPPING)
├── Phỏng vấn chuyên sâu 3 vai trò: Giám đốc Kinh doanh (CSD), Giám đốc Tài chính (CFO), Trưởng phòng Sales
├── Đối chiếu xung đột lợi ích: Tự do thao tác của Sales vs Yêu cầu bảo mật và chính xác của Ban Lãnh đạo
└── Nhận diện 3 bài toán quản trị cấp thiết: SLA Pipeline, Chống cướp khách nội bộ, Doanh thu lai

GIAI ĐOẠN 2: MÔ HÌNH HÓA DÒNG CHẢY NGHIỆP VỤ (PROCESS MODELING)
├── Sơ đồ Swimlane 4 làn bơi: Phân định ranh giới trách nhiệm giữa Khách hàng, Sales, Odoo ERP và Manager
├── Sơ đồ luồng phân bổ Lead & Chống cướp khách: Thuật toán Round-Robin, kiểm tra trùng và cơ chế che dữ liệu
└── Kiến trúc Use Case phân hệ CRM: Hệ thống hóa 18 ca sử dụng bao phủ 4 nhóm tác nhân vận hành

GIAI ĐOẠN 3: THIẾT LẬP RÀO CHẮN NGHIỆP VỤ & POKA-YOKE (SYSTEM RULES)
├── Xây dựng Cẩm nang 14 Quy tắc nghiệp vụ (BR-01 đến BR-14) không cần can thiệp mã nguồn
├── Thiết lập rào chắn kỹ thuật Poka-Yoke: Khóa nút, bắt buộc trường dữ liệu, tự động đổi màu trạng thái thẻ
└── Phân quyền bảo mật 3 cấp (RBAC) kết hợp kỹ thuật che số điện thoại và email

GIAI ĐOẠN 4: ĐO LƯỜNG & CHUYỂN GIAO BÁO CÁO ĐIỀU HÀNH (C-LEVEL REPORTING)
├── Thiết lập cấu trúc Báo cáo Pivot Table đa chiều: Doanh thu triển khai vs Doanh thu định kỳ hàng tháng
└── Chuyển giao khung kiểm soát chỉ số vận hành và tài liệu hướng dẫn cho quản lý trực tiếp
```

---

## 4. Business Requirements Catalog

Khung 14 Quy tắc nghiệp vụ cốt lõi (Business Rules) được thiết lập nhằm đảm bảo hệ thống tự vận hành chuẩn mực, thay thế hoàn toàn mệnh lệnh giám sát hành chính thủ công:

| Mã BR | Tên quy tắc | Logic nghiệp vụ (Condition → Action) | Cơ chế rào chắn & Thông báo vi phạm | Phương thức cấu hình Odoo UI |
| :--- | :--- | :--- | :--- | :--- |
| **BR-01** | Ràng buộc dữ liệu (Validation) | Khi chiết khấu báo giá > 15% | Khóa nút xác nhận; cảnh báo: *"Chiết khấu vượt thẩm quyền, yêu cầu duyệt Trưởng phòng"* | Required field / Automated Actions |
| **BR-02** | Tính toán tự động (Calculation) | Chuyển stage cơ hội có xác suất $P\%$ | Tự động tính: `Doanh thu trọng số = Doanh thu * P%` | Computed field / Công thức Odoo CRM |
| **BR-03** | Điền thông tin ngữ cảnh (Auto-fill) | Chọn khách hàng trên form báo giá | Tự động điền Mã số thuế, Bảng giá VIP, Điều khoản thanh toán 30 ngày | Liên kết dữ liệu Contacts (Partner) |
| **BR-04** | Chuyển trạng thái bắt buộc (Status Transition) | Chuyển Lead sang Cơ hội thành công | Bắt buộc liên kết hoặc tạo mới hồ sơ Khách hàng và Báo giá | Pipeline Stage Mandatory Gates |
| **BR-05** | Phê duyệt nhiều cấp (Approval) | Giá trị đơn hàng > 500 triệu VNĐ | Đưa đơn về trạng thái "Chờ duyệt"; khóa chuyển tiếp cho đến khi CEO phê duyệt | Approval Rules / Studio Approvals |
| **BR-06** | Phân quyền bảo mật (Security RBAC) | Sales Rep truy cập dữ liệu hệ thống | Chỉ xem lead của chính mình; cấm hoàn toàn quyền Xóa và Xuất Excel | Record Rules & Access Rights |
| **BR-07** | Nhắc nhở & Leo thang (SLA Escalation) | Cơ hội ở stage Đàm phán > 14 ngày | Thẻ đổi màu đỏ; tạo việc cần làm 48h; gửi tin nhắn leo thang tới CSD | Automated Activity & Color Alert |
| **BR-08** | Che thông tin nhạy cảm (Data Masking) | Sales kiểm tra trùng khách hàng | Hiển thị người phụ trách; ẩn số điện thoại dạng `090****123` và email | View Definition / Python Constraint |
| **BR-09** | Khóa dữ liệu chứng từ (Immutability) | Báo giá chuyển sang "Đơn bán hàng" | Khóa chỉnh sửa giá bán và sản phẩm; mọi thay đổi phải lập bản sửa đổi | Lock Confirmed Orders |
| **BR-10** | Đồng bộ liên phân hệ (Integration) | Xác nhận đơn hàng thành công | Tự động sinh Lệnh giao hàng (Kho) và Dự thảo Hóa đơn (Kế toán) | Native Odoo Apps Synchronization |
| **BR-11** | Kiểm tra trùng lặp (Deduplication) | Nhập Lead mới có cùng MST hoặc SĐT | Cảnh báo trùng lặp tức thì, chặn tạo bản ghi mới trùng lặp | Automated Duplicate Detection |
| **BR-12** | Phân bổ xoay vòng (Round-Robin) | Lead mới đổ về từ Form Web/Email | Tự động gán xoay vòng; áp hạn mức quota tối đa 5 lead/ngày/nhân sự | Lead Assignment Rules & Quota |
| **BR-13** | Loại trừ người nghỉ phép (Leave Sync) | Nhân sự có đơn xin nghỉ phép duyệt | Bật cờ tạm ngừng nhận lead; tự động kích hoạt lại khi kết thúc kỳ nghỉ | Integration Time Off & Sales Team |
| **BR-14** | Bắt buộc lý do thất bại (Poka-Yoke) | Sales bấm đóng cơ hội thua (Lost) | Khóa thao tác nếu chưa chọn lý do chuẩn; chọn Khác bắt buộc giải trình | Lost Reason Popup & Mandatory Field |

---

## 5. Solution Design

Giải pháp được thiết kế chi tiết để giải quyết trực diện 3 bài toán quản trị với đầy đủ sơ đồ trực quan và thông số kỹ thuật:

### 5.1 Giải pháp Quản trị Pipeline & SLA 14 ngày (M3)
* **Cơ chế:** Kích hoạt thuộc tính đo lường thời gian trôi qua trên giai đoạn Đàm phán. Khi vượt ngưỡng 14 ngày không phát sinh tương tác, thẻ Kanban tự động chuyển sang màu đỏ.
* **Tự động hóa leo thang:** Đúng ngày thứ 14, hệ thống giao việc kiểm tra hạn chót 48 giờ. Hết 48 giờ không có phản hồi, bot tự động gắn thẻ thông báo trực tiếp Giám đốc Kinh doanh kèm liên kết cơ hội.
* **Khóa rào chắn Poka-Yoke:** Khóa hoàn toàn chức năng lưu thất bại nếu nhân viên không chọn 1 trong 6 lý do chuẩn: *Giá cao, Thiếu tính năng, Chọn đối thủ, Hoãn kế hoạch, Tiến độ chưa đáp ứng, Lý do khác*. Nếu chọn *Lý do khác*, bắt buộc nhập giải trình chi tiết tối thiểu 1 câu hoàn chỉnh.

[→ Xem sơ đồ Swimlane: Quy trình Lead-to-Order 4 làn bơi](./diagram/CRM_Lead_To_Order_Swimlane_Process.png)

---

### 5.2 Giải pháp Phân bổ Lead Tự động & Chống cướp khách (M4)
* **Thuật toán xoay vòng Round-Robin:** Tự động định tuyến khách hàng tiềm năng đến từng nhân sự bán hàng theo thứ tự công bằng, kèm hạn mức trần **5 lead/ngày/nhân viên**. Nhân viên đạt ngưỡng sẽ tự động nhường lượt cho người kế tiếp.
* **Tích hợp trạng thái nghỉ phép:** Liên kết trực tiếp phân hệ Time Off với Sales Team. Khi đơn nghỉ phép được duyệt, hệ thống tự động loại nhân sự khỏi hàng đợi phân bổ và tái kích hoạt khi quay lại làm việc.
* **Ma trận phân quyền 3 tầng & Che dữ liệu:**
  * *Sales Rep:* Chỉ xem khách hàng của mình; bị chặn quyền Export Excel để tránh thất thoát dữ liệu.
  * *Sales Manager:* Toàn quyền xem và điều phối dữ liệu nội bộ trong nhóm phụ trách.
  * *CSD / Ban Giám đốc:* Toàn quyền giám sát bức tranh tổng thể trên phạm vi toàn quốc.
* **Chống cướp khách bằng Data Masking:** Cho phép nhân viên nhập MST hoặc SĐT để kiểm tra trùng. Nếu đã có người chăm sóc, hệ thống báo trùng kèm tên Sales phụ trách nhưng che toàn bộ số điện thoại và email, ngăn chặn việc liên hệ riêng sau lưng. Sau 60 ngày không có tương tác phát sinh, khách hàng tự động chuyển vào kho chung để người khác tiếp quản.

[→ Xem sơ đồ Luồng nghiệp vụ: Phân bổ Lead tự động & Chống cướp khách](./diagram/CRM_Auto_Assignment_Anti_Poaching_Flow.png)

---

### 5.3 Giải pháp Quản trị Doanh thu lai & Ngăn chặn Deal trôi dạt (M5)
* **Kiến trúc dữ liệu Doanh thu kép:** Cấu hình 2 khối trường dữ liệu tách bạch trên cùng form cơ hội:
  * Trường `Expected Revenue`: Ghi nhận doanh thu triển khai thu một lần (One-off).
  * Trường `Recurring Revenue` kèm `Recurring Plan`: Ghi nhận doanh thu định kỳ (MRR) và chu kỳ thanh toán (Hàng tháng / Hàng quý / Hàng năm).
* **Bộ đếm dời hạn & Cờ cảnh báo deal trôi:** Kích hoạt theo dõi lịch sử trên trường Ngày chốt dự kiến. Khi một cơ hội bị dời ngày chốt từ 2 lần trở lên, hệ thống tự động gắn Cờ Đỏ cảnh báo trên giao diện Kanban và Dự báo.
* **Ràng buộc giải trình trì hoãn:** Khi cờ đỏ bật, hệ thống khóa thao tác dời ngày cho đến khi nhân viên chọn lý do trì hoãn chuẩn (*Chưa duyệt ngân sách, Đang đàm phán hợp đồng, Chờ sắp xếp nhân sự triển khai*) và thông báo trực tiếp cho Trưởng phòng bán hàng.
* **Báo cáo Pivot đa chiều cấp điều hành:** Cung cấp báo cáo ma trận nhóm theo Tháng chốt và Giai đoạn bán hàng, thể hiện đồng thời 2 dòng tiền: Tiền thực thu ngay cho CFO và Doanh thu định kỳ tích lũy cho CSD.

[→ Xem sơ đồ Use Case: Kiến trúc 18 ca sử dụng phân hệ CRM](./diagram/CRM_System_Use_Case_Overview.png)

---

## 6. Business Value & Expected Impact

Bảng tổng hợp hiệu quả cải tiến định lượng và định tính trước và sau khi triển khai giải pháp BA:

| Chỉ số đo lường (KPI) | Hiện trạng trước giải pháp | Sau khi chuẩn hóa hệ thống | Mức độ cải thiện |
| :--- | :--- | :--- | :--- |
| **Thời gian phản hồi Lead mới (Speed-to-Lead)** | Trung bình 4.2 giờ (tranh giành lead thủ công) | Dưới 15 phút (phân bổ tự động Round-Robin) | 🟢 **Rút ngắn 94%** thời gian chờ của khách |
| **Độ chính xác dự báo doanh thu (Forecast Accuracy)** | Sai lệch ~35% (deal ảo nằm ngâm vô thời hạn) | Sai lệch < 5% (SLA 14 ngày & cờ cảnh báo deal trôi) | 🟢 **Tăng 30%** độ tin cậy số liệu cho CFO |
| **Tỷ lệ cơ hội thất bại có dữ liệu nguyên nhân** | Dưới 12% (nhân viên đóng deal bừa bãi) | Đạt 100% (rào chắn Poka-Yoke bắt buộc nhập) | 🟢 **Tăng 88%** độ phủ dữ liệu cải tiến sản phẩm |
| **Tỷ lệ thất thoát dữ liệu khách hàng khi nghỉ việc** | Nguy cơ cao (nhân sự giấu thông tin ra sổ tay) | 0% (dữ liệu tập trung, phân quyền RBAC & Masking) | 🟢 **Bảo vệ 100%** tài sản thông tin doanh nghiệp |
| **Tranh chấp khách hàng nội bộ giữa các Sales** | Xảy ra thường xuyên hàng tuần | Triệt tiêu hoàn toàn nhờ cơ chế kiểm tra trùng an toàn | 🟢 **Xóa bỏ 100%** xung đột lợi ích nội bộ |

---

## 7. Constraints, Assumptions & Risks

### Ràng buộc kỹ thuật (Constraints)
* **Cấu hình No-code / Low-code tiêu chuẩn:** Ưu tiên tuyệt đối các tính năng nguyên bản của Odoo 19 (Automated Actions, Record Rules, Studio Field Configuration), không can thiệp sửa đổi mã nguồn gốc (source code) nhằm bảo đảm khả năng nâng cấp phiên bản mượt mà trong tương lai.
* **Tương thích đa nền tảng:** Mọi rào chắn Poka-Yoke và form dữ liệu phải hiển thị chuẩn xác trên cả trình duyệt Web và ứng dụng Di động Odoo Mobile.

### Giả định triển khai (Assumptions)
* Đội ngũ bán hàng được cấp thiết bị làm việc đồng bộ và có nghĩa vụ cập nhật trạng thái tương tác khách hàng trong vòng 24 giờ kể từ thời điểm phát sinh cuộc gọi/cuộc họp.
* Ban Giám đốc cam kết áp dụng chế tài minh bạch: Cơ hội không tuân thủ SLA sẽ tự động thu hồi và tái phân bổ cho nhân sự khác.

### Rủi ro vận hành & Kế hoạch giảm thiểu (Risks & Mitigations)
* **Rủi ro tâm lý chống đối:** Nhân viên kinh doanh kỳ cựu phản ứng tiêu cực khi bị áp hạn mức 5 lead/ngày và bị khóa quyền xuất Excel.
  * *Biện pháp giảm thiểu:* Tổ chức workshop đối thoại trước triển khai, giải thích rõ cơ chế che thông tin giúp bảo vệ khách hàng của chính họ khỏi bị đồng nghiệp cướp mối; thiết lập cơ chế thưởng vượt hạn mức cho nhân sự có tỷ lệ chuyển đổi cao.
* **Rủi ro khai báo đối phó:** Nhân viên chọn bừa lý do thất bại để đóng nhanh cơ hội.
  * *Biện pháp giảm thiểu:* Thiết lập kiểm toán ngẫu nhiên định kỳ 10% các cơ hội thất bại bởi Trưởng phòng bán hàng; gắn trách nhiệm kiểm tra vào KPI của cấp quản lý.

---

## 8. Deliverables Index

Hồ sơ bàn giao phân tích nghiệp vụ và tài liệu kỹ thuật được lưu trữ hoàn chỉnh trong thư mục dự án:

| Hạng mục tài liệu | Đường dẫn tham chiếu | Tóm tắt nội dung bàn giao |
| :--- | :--- | :--- |
| **Sơ đồ Quy trình Swimlane** | [CRM_Lead_To_Order_Swimlane_Process.png](./diagram/CRM_Lead_To_Order_Swimlane_Process.png) | Mô hình hóa 4 làn bơi chu trình Lead-to-Order |
| **Sơ đồ Phân bổ Lead & Anti-Poaching** | [CRM_Auto_Assignment_Anti_Poaching_Flow.png](./diagram/CRM_Auto_Assignment_Anti_Poaching_Flow.png) | Luồng thuật toán Round-Robin và kỹ thuật che dữ liệu |
| **Sơ đồ Kiến trúc Use Case** | [CRM_System_Use_Case_Overview.png](./diagram/CRM_System_Use_Case_Overview.png) | Tổng quan 18 ca sử dụng phân hệ CRM và 4 nhóm tác nhân |
| **Bản Tổng Hợp 3 Case Study C-level** | [Case_Study_Odoo.md](./doc/Case_Study_Odoo.md) | Đặc tả chi tiết 3 bài toán quản trị cấp điều hành (M3, M4, M5) |
| **Cẩm Nang 14 Quy Tắc Nghiệp Vụ** | [Business_Rules_Analysis.md](./doc/Business_Rules_Analysis.md) | Đặc tả 14 nhóm Business Rules chuẩn quốc tế và cấu hình Odoo |
| **Kiến Trúc Năng Lực CRM** | [CRM_Architecture_ASCII.md](./doc/CRM_Architecture_ASCII.md) | Phân tầng kiến trúc chức năng và mô hình thông tin CRM |
| **Ma Trận Điểm Đau & Giải Pháp** | [CRM_Pain_Points.md](./doc/CRM_Pain_Points.md) | Bảng đối chiếu hiện trạng, điểm đau và phương án xử lý |
| **Nhật Ký & Bảng Điểm Tiến Độ** | [CRM_Learning_Progress.md](./doc/CRM_Learning_Progress.md) | Khung theo dõi tiến độ và kiểm chuẩn năng lực thực hành |
