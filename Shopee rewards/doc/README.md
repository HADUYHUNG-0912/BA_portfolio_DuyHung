# Nghiên Cứu Tình Huống: Tối Ưu Hệ Thống Khách Hàng Thân Thiết & Gamification — Shopee Rewards

> Ứng viên: **Hà Duy Hưng** — Business Analyst, E-Commerce & Product Analytics  
> Phương pháp: Desk Research, Stakeholder Interview (CSKH Shopee), Behavioral Analysis  
> Phạm vi: Phân tích nghiệp vụ chương trình Loyalty hiện hành + Đề xuất tối ưu vận hành

---

## 1. Project Context

| Hạng mục | Chi tiết |
| :--- | :--- |
| **Đơn vị nghiệp vụ** | Shopee Việt Nam — Chương trình Khách hàng thân thiết (Shopee Rewards) |
| **Loại dự án** | Loyalty Program Optimization — Business Analysis & Solution Design |
| **Phạm vi hệ thống** | Phân hệ xếp hạng thành viên: Thành viên → Bạc → Vàng → Kim Cương |
| **Thời gian thực hiện** | Nghiên cứu, phỏng vấn và mô hình hóa trong 1 tuần |
| **Stakeholders liên quan** | Người dùng cuối (Buyer), Bộ phận Product/Marketing Shopee (tham khảo qua tài liệu công khai và kênh CSKH) |
| **Phương pháp thu thập** | Desk Research (blog, help center, video hướng dẫn chính thức), Direct Inquiry (phỏng vấn nhân viên hỗ trợ CSKH Shopee), Behavioral Survey (khảo sát nhanh nhóm người dùng thường xuyên) |
| **Kết quả bàn giao** | 10 Business Rules, 2 Pain Points, 3 sơ đồ quy trình, 2 đề xuất giải pháp có scope rõ ràng |

---

## 2. Business Problem Statement

Chương trình Shopee Rewards vận hành ổn định về cơ chế xếp hạng cốt lõi, nhưng **để lộ 2 khoảng trống hành vi** gây tổn thất doanh thu tiềm năng trực tiếp:

### Vấn đề 1 — Near-threshold Drop (PP-09)
> Hệ thống **thụ động hoàn toàn** sau mỗi giao dịch: tính điểm, không phản hồi. Khi người dùng chỉ còn thiếu 1–2 đơn hoặc vài chục nghìn đồng để thăng hạng, hệ thống không phát ra bất kỳ tín hiệu nào. Doanh nghiệp bỏ lỡ **khoảnh khắc quyết định mua hàng có xác suất cao nhất** trong toàn bộ hành trình khách hàng.

- **Root Cause:** Kiến trúc tính hạng hiện tại thiếu lớp logic "khoảng cách đến ngưỡng" (threshold-gap tracking). Hệ thống chỉ so sánh tích lũy với ngưỡng sau giao dịch, không theo dõi và phát tín hiệu chủ động trước giao dịch.
- **Business Impact:** Tổn thất doanh thu cận ngưỡng — phân khúc khách hàng sẵn sàng chi thêm nhất nhưng không nhận được kích thích phù hợp.

### Vấn đề 2 — Mid-cycle Motivation Gap (PP-10)
> Cơ chế bảo lưu hạng suốt chu kỳ (BR-09) tạo ra **khoảng trống động lực** tức thì sau khi khách đạt hạng mong muốn. Cấu trúc chương trình chỉ có **một mục tiêu duy nhất** trong 6 tháng — khi đã đạt, không còn lý do để tiếp tục mua sắm thường xuyên.

- **Root Cause:** Thiết kế hệ thống mục tiêu đơn tầng (single-goal structure). Không có cơ chế mục tiêu phụ nối tiếp (secondary goal layer) giữ chân người dùng sau khi hoàn thành mục tiêu chính.
- **Business Impact:** Suy giảm tần suất giao dịch trong nửa sau chu kỳ ở nhóm khách hàng status-driven — đây thường là phân khúc có giá trị đơn hàng trung bình cao nhất.

---

## 3. Analysis Approach

```
ELICITATION
├── Desk Research (Primary): Đọc và đối chiếu blog.shopee.vn, help.shopee.vn, video FAQ chính thức
├── Direct Inquiry: Phỏng vấn kênh CSKH Shopee để xác nhận điều kiện AND/OR (BR-05, BR-06)
└── Behavioral Survey: Khảo sát nhanh nhóm người mua thường xuyên về trải nghiệm nhắc nhở

ANALYSIS
├── Business Rules Extraction: Bóc tách và phân loại 10 quy tắc nghiệp vụ theo nguồn và độ tin cậy
├── Conflict Detection: Phát hiện mâu thuẫn AND vs OR tại BR-05/BR-06 → Ghi nhận xung đột nguồn
└── Pain Point Mapping: 5 Whys cho từng pain point → Xác định root cause cấu trúc

MODELING
├── Process Flowchart (Mermaid): Luồng tích lũy và xét duyệt hạng đầu-cuối
├── Sequence Diagram (Mermaid): Đặc tả kỹ thuật 3 điểm chạm nhắc ngưỡng
└── Solution Architecture Flow (Mermaid): Kiến trúc lớp mục tiêu phụ song song

SOLUTION DESIGN
├── PP-09: Thiết kế 3 điểm chạm (Loyalty screen, Checkout, Homepage card)
└── PP-10: Thiết kế "Chuỗi mua sắm thưởng thêm" độc lập với BR-09
```

---

## 4. Business Requirements Catalog

### 4.1 Business Rules Hiện Hành (Confirmed)

| ID | Quy tắc nghiệp vụ | Nguồn xác nhận | Độ tin cậy | Ghi chú |
| :---: | :--- | :--- | :---: | :--- |
| **BR-01** | Xếp hạng dựa trên tích lũy đơn hàng + chi tiêu trong chu kỳ cố định 6 tháng, không phải rolling window | shopee.vn/blog | ✅ Cao | — |
| **BR-02** | Mọi người dùng Shopee tự động tham gia chương trình từ tháng 01/2021, không cần đăng ký thủ công | help.shopee.vn | ✅ Cao | — |
| **BR-03** | Đơn ShopeeFood từ "Quán Đối tác" được tính vào tích lũy từ tháng 01/2022, điều kiện: giao hàng thành công | help.shopee.vn | ✅ Cao | — |
| **BR-04** | Chu kỳ cố định: 01/01–30/06 và 01/07–31/12. Đầu chu kỳ mới: reset tích lũy về 0, giữ hạng | shopee.vn/blog | ✅ Cao | — |
| **BR-05** | Hạng Bạc: ≥3 đơn **AND** ≥1.000.000đ chi tiêu | Nhân viên CSKH Shopee | ⚠️ Trung bình | Xung đột: Blog/Video ghi OR; CSKH xác nhận AND |
| **BR-06** | Hạng Vàng: ≥20 đơn **AND** ≥5.000.000đ chi tiêu | Nhân viên CSKH Shopee | ⚠️ Trung bình | Xung đột tương tự BR-05 — chưa giải quyết |
| **BR-07** | Hạng Kim Cương: ≥75 đơn **AND** ≥15.000.000đ chi tiêu | Tất cả nguồn đồng thuận | ✅ Cao | Điều kiện AND nhất quán mọi kênh |
| **BR-08** | Thăng hạng tự động real-time khi đủ điều kiện, không cần thao tác người dùng | shopee.vn/blog, video | ✅ Cao | — |
| **BR-09** | Hạng bảo lưu suốt chu kỳ. Sang kỳ mới: tích lũy reset → 0, hạng cũ được mang sang làm hạng khởi điểm | shopee.vn/blog | ✅ Cao | Root cause của PP-10 |
| **BR-10** | 4 nhóm đơn không tính tích lũy: (1) Voucher & Dịch vụ, (2) Nạp Đấu thầu từ khóa, (3) Vi phạm chính sách, (4) Giao thất bại / Trả hàng / Hoàn tiền | help.shopee.vn, blog | ✅ Cao | — |

> ⚠️ **Lưu ý Data Conflict:** BR-05 và BR-06 có xung đột giữa kênh truyền thông (OR) và kênh CSKH (AND). Baseline sử dụng điều kiện **AND** theo xác nhận CSKH — cần Product Owner/Stakeholder xác nhận chính thức trước khi bàn giao Dev.

### 4.2 Business Requirements Đề Xuất (New)

| ID | Yêu cầu nghiệp vụ | Loại | Priority | Liên kết Pain Point |
| :---: | :--- | :---: | :---: | :---: |
| **BR-N01** | Hệ thống phải tính và cập nhật khoảng cách còn thiếu đến ngưỡng tiếp theo (đơn + chi tiêu) theo thời gian thực sau mỗi giao dịch | Functional | Must-have | PP-09 |
| **BR-N02** | Khi khoảng cách đến ngưỡng ≤1 đơn hoặc ≤10% giá trị còn thiếu, App phải hiển thị thông điệp hành động cá nhân hóa tại màn hình Loyalty | Functional | Must-have | PP-09 |
| **BR-N03** | Khi đơn hàng hiện tại đủ để đưa người dùng vượt ngưỡng, hệ thống phải hiển thị thông điệp xác nhận tại bước Checkout trước khi thanh toán | Functional | Must-have | PP-09 |
| **BR-N04** | Thẻ nhắc nhở trang chủ chỉ được hiển thị tối đa 1 lần/ngày và phải có nút đóng (Dismiss); tự tắt khi người dùng đã thăng hạng | Non-functional | Should-have | PP-09 |
| **BR-N05** | Hệ thống phải theo dõi độc lập trạng thái "Đã có đơn hợp lệ" cho từng tháng trong chu kỳ 6 tháng, tách biệt hoàn toàn với logic tính hạng chính (BR-01 đến BR-09) | Functional | Must-have | PP-10 |
| **BR-N06** | Tiến độ chuỗi mua sắm hàng tháng phải hiển thị trong khu vực UI riêng biệt, không được gộp chung với khu vực hiển thị hạng chính thức | Functional | Must-have | PP-10 |
| **BR-N07** | Đơn hàng hợp lệ cho chuỗi mua sắm hàng tháng phải tuân thủ đúng các điều kiện loại trừ theo BR-10 | Functional | Must-have | PP-10 |

---

## 5. Solution Design & Visual Artifacts

### Giải pháp PP-09 — Cơ Chế Nhắc Ngưỡng 3 Điểm Chạm

> **Nguyên tắc thiết kế:** Đưa tín hiệu đúng vào đúng khoảnh khắc người dùng sẵn sàng ra quyết định nhất — không spam, không chặn trải nghiệm.

| Điểm chạm | Kênh | Trigger Condition | Nội dung thông điệp | Tần suất |
| :---: | :--- | :--- | :--- | :--- |
| **#1** | Màn hình Loyalty | Mở màn hình + Gần ngưỡng (≤1 đơn hoặc ≤10% giá trị) | "Chỉ cần thêm 1 đơn nữa để lên hạng Vàng! Gợi ý hôm nay: [...]" | Mỗi lần mở |
| **#2** | Checkout | Đơn hiện tại đủ đưa user vượt ngưỡng | "Đơn này sẽ đưa bạn lên hạng Bạc!" | Mỗi đơn đủ điều kiện |
| **#3** | Homepage Card | Gần ngưỡng + Chưa hiển thị hôm nay | Thẻ nhỏ không chặn, có nút đóng | 1 lần/ngày |

[→ Xem sơ đồ: Sequence Diagram — 3 Điểm chạm Nhắc Ngưỡng Hạng (PP-09)](./images/02-sequence-nhac-nguong-hang-pp09.png)

---

### Giải pháp PP-10 — Chuỗi Mua Sắm Thưởng Thêm (Parallel Goal Layer)

> **Nguyên tắc thiết kế:** Không sửa đổi quy tắc gốc đã ổn định. Bổ sung lớp mục tiêu phụ hoàn toàn độc lập — người dùng luôn có mục tiêu mới để hướng tới sau khi đã đạt hạng mong muốn.

| Thuộc tính | Hệ thống Hạng Chính | Chuỗi Mua Sắm Thưởng Thêm (New) |
| :--- | :---: | :---: |
| **Đơn vị đo** | Số đơn + Tổng chi tiêu | Số tháng có đơn hợp lệ (X/6) |
| **Reset** | Đầu chu kỳ 6 tháng | Đầu chu kỳ 6 tháng |
| **Ảnh hưởng hạng** | Có | Không |
| **Điều kiện đơn hợp lệ** | BR-10 | BR-10 (kế thừa) |
| **Khu vực UI** | Section "Hạng chính thức" | Section riêng — tách biệt |
| **Độc lập với BR-09** | N/A | ✅ Hoàn toàn độc lập |

[→ Xem sơ đồ: Solution Architecture — Chuỗi Mua Sắm Thưởng Thêm (PP-10)](./images/03-chuoi-mua-sam-thuong-them-pp10.png)

---

### Tổng quan Quy Trình Tích Lũy & Xét Hạng Hiện Hành

[→ Xem sơ đồ: Flowchart — Quy trình Tích lũy & Xét Hạng Shopee Rewards](./images/01-quy-trinh-tich-luy-xet-hang.png)

---

## 6. Business Value & Expected Impact

| KPI | Baseline (Hiện tại) | Target (Sau triển khai) | Cách đo lường |
| :--- | :---: | :---: | :--- |
| **Tỷ lệ người dùng cận ngưỡng hoàn tất thăng hạng** | Không có dữ liệu baseline | Tăng ≥15% so với nhóm kiểm soát | A/B Test: Bật/tắt 3 điểm chạm trên hai nhóm tương đương |
| **Giá trị đơn hàng trung bình (AOV) tại Checkout khi kích hoạt thông điệp #2** | Không có dữ liệu baseline | Tăng ≥10% so với Checkout không kích hoạt | So sánh AOV giữa đơn có/không có thông điệp ngưỡng |
| **Tần suất đặt hàng trung bình của nhóm status-driven sau tháng đạt hạng** | Cần đo tại baseline | Giảm không quá 5% so với tháng đang leo hạng | Cohort analysis: So sánh tháng T (đạt hạng) vs T+1, T+2 |
| **Tỷ lệ người dùng hoàn thành ≥4/6 tháng trong Chuỗi Mua Sắm** | Không áp dụng (feature mới) | ≥30% người dùng Vàng/Kim Cương | Dashboard đo tỷ lệ hoàn thành chuỗi mỗi chu kỳ |

> **Lưu ý:** Tất cả giải pháp đề xuất triển khai qua **Feature Flag** — cho phép bật/tắt độc lập từng tính năng mà không ảnh hưởng hệ thống tính hạng lõi.

---

## 7. Constraints & Risks

### 7.1 Ràng Buộc

| Loại | Nội dung |
| :--- | :--- |
| **Kinh doanh** | Không được sửa đổi bất kỳ quy tắc nào trong BR-01 đến BR-09 đã ổn định |
| **Kỹ thuật** | Giải pháp PP-09 phải dùng API tính giỏ hàng hiện có, không yêu cầu hạ tầng push notification riêng |
| **Tài chính** | Ngân sách phần thưởng cho Chuỗi Mua Sắm (PP-10) nằm ngoài phạm vi phân tích — cần Marketing/Finance phê duyệt |
| **UX** | Thông điệp nhắc nhở không được gây trải nghiệm bị gián đoạn hoặc spam |

### 7.2 Rủi Ro & Giả Định

| ID | Rủi Ro | Mức độ | Biện pháp giảm thiểu |
| :---: | :--- | :---: | :--- |
| **R-01** | BR-05/BR-06 thực tế là OR, không phải AND → Giải pháp PP-09 tính sai ngưỡng | 🔴 Cao | Xác nhận điều kiện với Product Owner trước khi phát triển |
| **R-02** | Chuỗi Mua Sắm (PP-10) không đủ kích thích nếu không có phần thưởng cụ thể | 🟡 Trung bình | Triển khai giai đoạn 1 đo hành vi, bổ sung reward sau khi có dữ liệu |
| **R-03** | Thẻ nhắc nhở trang chủ bị người dùng coi là quảng cáo, ảnh hưởng NPS | 🟡 Trung bình | Giới hạn 1 lần/ngày + có nút đóng + tự tắt sau khi thăng hạng |

---

## 8. Deliverables Index

| Tài liệu | Mô tả | Trạng thái |
| :--- | :--- | :---: |
| [shopee-rewards-business-analysis.md](./doc/shopee-rewards-business-analysis.md) | Hồ sơ phân tích nghiệp vụ: 10 BR, 2 Pain Points, Scope & Solution Design chi tiết | ✅ Hoàn thành |
| [shopee-rewards-diagrams.md](./doc/shopee-rewards-diagrams.md) | Đặc tả kỹ thuật sơ đồ: Flowchart, Sequence, Solution Architecture kèm mã nguồn Mermaid | ✅ Hoàn thành |
| [images/01-quy-trinh-tich-luy-xet-hang.png](./images/01-quy-trinh-tich-luy-xet-hang.png) | Sơ đồ quy trình tích lũy và xét duyệt thăng hạng (PNG 2x + SVG) | ✅ Hoàn thành |
| [images/02-sequence-nhac-nguong-hang-pp09.png](./images/02-sequence-nhac-nguong-hang-pp09.png) | Sequence diagram đặc tả 3 điểm chạm nhắc ngưỡng hạng (PNG 2x + SVG) | ✅ Hoàn thành |
| [images/03-chuoi-mua-sam-thuong-them-pp10.png](./images/03-chuoi-mua-sam-thuong-them-pp10.png) | Sơ đồ kiến trúc giải pháp chuỗi mua sắm thưởng thêm (PNG 2x + SVG) | ✅ Hoàn thành |
| Acceptance Criteria & Test Scenarios | Kịch bản kiểm thử chi tiết cho từng điểm chạm | 🔲 Chưa thực hiện |

---

> ⬅️ **Quay lại trang hồ sơ cá nhân:** [Trang chủ Portfolio](../README.md)
