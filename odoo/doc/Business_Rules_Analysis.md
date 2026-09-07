# CẨM NANG PHÂN TÍCH & ĐẶC TẢ QUY TẮC NGHIỆP VỤ (BUSINESS RULES CHO BA ERP)

> **Dành cho:** Business Analyst (BA), ERP Functional Consultant, Product Owner  
> **Mục tiêu:** Cung cấp phương pháp luận chuẩn quốc tế để nhận diện, phân tích, cấu hình và đặc tả 14 nhóm Quy tắc nghiệp vụ (Business Rules - BR) cốt lõi trong hệ thống ERP mà **không cần đọc hoặc can thiệp vào mã nguồn kỹ thuật**.  
> 
> 📌 **Tài liệu liên quan:** [CRM_Architecture_ASCII.md](file:///e:/BA/Ba-case/odoo/odoo/doc/CRM_Architecture_ASCII.md) | [Learning_Checklist.md](file:///e:/BA/Ba-case/odoo/odoo/doc/Learning_Checklist.md) | [README.md](file:///e:/BA/Ba-case/odoo/odoo/README.md)

---

## 🧭 I. TỔNG QUAN VỀ QUY TẮC NGHIỆP VỤ (BUSINESS RULES LÀ GÌ?)

Trong dự án triển khai ERP, **Quy tắc nghiệp vụ (Business Rule - BR)** là những tuyên ngôn xác định hoặc ràng buộc một khía cạnh nào đó của hoạt động kinh doanh. Chúng phản ánh các chính sách quản trị, kiểm soát nội bộ, giới hạn an toàn tài chính và cam kết chất lượng dịch vụ của doanh nghiệp.

### Cấu trúc chuẩn của một Business Rule mà BA cần bàn giao:
```
NẾU (Điều kiện kích hoạt - Condition)
THÌ (Hành vi bắt buộc của hệ thống - Expected Action)
NẾU VI PHẠM (Thông báo cảnh báo nghiệp vụ rõ ràng - User-friendly Error/Warning)
```

---

## 📋 II. CHI TIẾT 14 NHÓM QUY TẮC NGHIỆP VỤ KINH ĐIỂN (BR-01 ĐẾN BR-14)

---

### BR-01: Quy tắc Ràng buộc & Thẩm định dữ liệu (Validation Rules)
* **Ý nghĩa nghiệp vụ:** Đảm bảo tính toàn vẹn và hợp lý của dữ liệu trước khi lưu vào hệ thống, ngăn chặn nhân viên nhập sai thông tin gây hậu quả tài chính.
* **Tình huống thực tế:** "Hạn mức nợ của khách hàng không được âm", "Ngày giao hàng dự kiến không được xảy ra trước ngày lập đơn", "Tỷ lệ chiết khấu vượt quá 15% bắt buộc phải có phê duyệt của Giám đốc".
* **Cách BA cấu hình trên Odoo UI:**
  * Thiết lập trường bắt buộc (`Required`) ngay trên giao diện form.
  * Cấu hình hạn mức tối đa/tối thiểu trong phần Cài đặt nghiệp vụ (*Settings*).
* **Tiêu chí nghiệm thu (Acceptance Criteria - AC):**
  * *Given:* Nhân viên bán hàng đang tạo đơn báo giá cho khách hàng mới.
  * *When:* Nhân viên nhập mức chiết khấu là 25% mà không có mã phê duyệt.
  * *Then:* Hệ thống chặn không cho bấm Lưu/Xác nhận và hiển thị cảnh báo: *"Mức chiết khấu vượt quá thẩm quyền tối đa (15%). Vui lòng gửi yêu cầu duyệt tới Trưởng phòng"*.

---

### BR-02: Quy tắc Tính toán tự động (Calculation Rules)
* **Ý nghĩa nghiệp vụ:** Tự động tính toán các chỉ số kinh tế dựa trên các biến số đầu vào, loại bỏ sai sót tính nhẩm của con người và đồng nhất công thức trên toàn doanh nghiệp.
* **Tình huống thực tế:** 
  * `Thành tiền = (Số lượng * Đơn giá) - Tiền chiết khấu + Thuế VAT`.
  * `Doanh thu dự kiến theo trọng số (Prorated Revenue) = Doanh thu kỳ vọng * Tỷ lệ xác suất thành công (%)`.
* **Cách BA cấu hình trên Odoo UI:**
  * Lựa chọn phương pháp tính giá (Bình quân gia quyền, FIFO) trong menu Cấu hình Kho.
  * Thiết lập công thức bảng giá (*Pricelist*) theo quy tắc bậc thang số lượng.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Cơ hội bán hàng có Doanh thu kỳ vọng là 100.000.000 VNĐ.
  * *When:* Cơ hội được chuyển sang giai đoạn "Đàm phán" có xác suất thành công 70%.
  * *Then:* Hệ thống tự động cập nhật Doanh thu trọng số là 70.000.000 VNĐ vào báo cáo dự báo doanh số mà không cần người dùng nhập tay.

---

### BR-03: Quy tắc Điền thông tin tự động theo ngữ cảnh (Contextual Auto-fill Rules)
* **Ý nghĩa nghiệp vụ:** Giảm thiểu thao tác gõ phím lặp lại cho nhân viên, tăng tốc độ xử lý đơn hàng và đảm bảo tính nhất quán giữa hồ sơ đối tác và chứng từ.
* **Tình huống thực tế:** Khi nhân viên chọn khách hàng "Tập đoàn Vinfast", hệ thống phải tự động kéo thông tin: Mã số thuế, Địa chỉ xuất hóa đơn, Bảng giá VIP, Điều khoản thanh toán "Trả chậm 30 ngày" vào form bán hàng.
* **Cách BA cấu hình trên Odoo UI:**
  * Thiết lập đầy đủ thông tin gốc trên Hồ sơ Khách hàng (*Contacts* $\rightarrow$ Tab Bán hàng & Mua hàng).
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Khách hàng A có điều khoản thanh toán mặc định là "30 Days Net".
  * *When:* Nhân viên tạo báo giá mới và chọn đối tác là Khách hàng A.
  * *Then:* Trường Điều khoản thanh toán trên Báo giá tự động hiển thị "30 Days Net". Nhân viên có quyền thay đổi nếu có lý do đặc biệt.

---

### BR-04: Quy tắc Vòng đời trạng thái & Luồng phê duyệt (Workflow State & Action Rules)
* **Ý nghĩa nghiệp vụ:** Kiểm soát quy trình làm việc theo đúng thứ tự bước (SOP), ngăn chặn tình trạng "đốt cháy giai đoạn" và kích hoạt các chứng từ liên đới.
* **Tình huống thực tế:** "Đơn hàng chỉ được phép giao khi đã chuyển sang trạng thái Đã duyệt", "Chỉ các chứng từ ở trạng thái Nháp (Draft) mới được phép chỉnh sửa hoặc hủy".
* **Cách BA cấu hình trên Odoo UI:**
  * Thiết lập các cột Pipeline Kanban (*CRM Stages*).
  * Bật tính năng phê duyệt đơn hàng 2 bước (*Two-step Approval*) trong Settings Bán hàng.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Một Cơ hội bán hàng đang ở trạng thái Thắng (Won).
  * *When:* Nhân viên bấm nút "Tạo Báo giá".
  * *Then:* Hệ thống tự động sinh một bản Báo giá mới ở trạng thái Nháp (Draft) với toàn bộ thông tin khách hàng và sản phẩm được sao chép sang.

---

### BR-05: Quy tắc Ẩn/Hiện & Bắt buộc có điều kiện (Conditional Visibility Rules)
* **Ý nghĩa nghiệp vụ:** Giúp giao diện làm việc luôn gọn gàng, người dùng chỉ nhìn thấy các ô dữ liệu liên quan đến đúng ngữ cảnh công việc hiện tại.
* **Tình huống thực tế:** Ô "Lý do hủy đơn" chỉ xuất hiện khi trạng thái đơn đổi thành "Đã hủy"; Ô "Biển số xe" chỉ xuất hiện khi chọn phương thức vận chuyển là "Xe tải công ty".
* **Cách BA cấu hình trên Odoo UI:**
  * Sử dụng công cụ kéo thả giao diện Odoo Studio hoặc tùy biến thuộc tính hiển thị form.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Nhân viên đang mở form chi tiết của Cơ hội bán hàng đang hoạt động.
  * *When:* Bấm nút "Đánh dấu Thua (Mark Lost)".
  * *Then:* Một cửa sổ pop-up hiện lên và trường "Lý do thua" bắt buộc phải được chọn thì mới cho phép bấm xác nhận.

---

### BR-06: Ma trận Phân quyền chức năng theo vai trò (Role-Based Functional Access)
* **Ý nghĩa nghiệp vụ:** Kiểm soát nội bộ (Internal Control), phân tách quyền hạn (SoD - Separation of Duties) nhằm triệt tiêu rủi ro gian lận.
* **Tình huống thực tế:** Nhân viên bán hàng chỉ được Tạo và Sửa báo giá nháp; chỉ Trưởng phòng mới được quyền Bấm phê duyệt đơn; Kế toán mới được quyền Xác nhận hóa đơn.
* **Cách BA cấu hình trên Odoo UI:**
  * Menu *Settings $\rightarrow$ Users & Companies $\rightarrow$ Groups*: Phân bổ người dùng vào các nhóm quyền chuẩn (*Sales: User* vs *Sales: Administrator*).
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Tài khoản đăng nhập là Nhân viên kinh doanh thông thường.
  * *When:* Xem danh sách đơn bán hàng.
  * *Then:* Nút "Xóa (Delete)" bị biến mất hoặc vô hiệu hóa. Nhân viên không thể xóa dữ liệu chứng từ.

---

### BR-07: Ma trận Phân quyền phạm vi dữ liệu (Data Scope & Ownership Rules)
* **Ý nghĩa nghiệp vụ:** Bảo vệ tài sản thông tin của công ty, chống việc sales nhìn trộm data khách hàng của nhau để cướp doanh số, và cách ly dữ liệu giữa các chi nhánh.
* **Tình huống thực tế:** "Salesman chỉ thấy cơ hội do mình chăm sóc", "Trưởng phòng chỉ thấy cơ hội trong đội ngũ của mình", "Giám đốc thấy toàn bộ công ty".
* **Cách BA cấu hình trên Odoo UI:**
  * Tại hồ sơ người dùng (*User Form*), chọn cấp độ quyền truy cập phân hệ Bán hàng:
    - *User: Own Documents Only* (Chỉ tài liệu của mình).
    - *User: All Documents* (Xem toàn bộ tài liệu).
    - *Administrator* (Quản trị viên toàn quyền).
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Sales A thuộc Đội Miền Bắc được cấp quyền "Own Documents Only".
  * *When:* Mở màn hình Pipeline CRM.
  * *Then:* Màn hình chỉ hiển thị các thẻ deal có người phụ trách là Sales A. Toàn bộ thông tin deal của đồng nghiệp khác hoàn toàn không xuất hiện.

---

### BR-08: Quy tắc Tự động hóa tác vụ & Cam kết thời gian SLA (Scheduled Automation & SLA Rules)
* **Ý nghĩa nghiệp vụ:** Tự động hóa các tác vụ lặp lại, giám sát tiến độ thực thi và cảnh báo vượt cấp khi có sự cố chậm trễ giúp duy trì chất lượng dịch vụ.
* **Tình huống thực tế:** "Nếu một cơ hội nằm yên ở giai đoạn Báo giá quá 14 ngày mà không có hoạt động mới, hệ thống tự động gắn cờ Đỏ (Rotting) và gửi email cảnh báo tới Trưởng phòng".
* **Cách BA cấu hình trên Odoo UI:**
  * Cấu hình số ngày ngâm deal (*Rotting Days*) trực tiếp trên từng Cột Kanban (*CRM Stage Form*).
  * Thiết lập tác vụ tự động tại menu *Settings $\rightarrow$ Technical / Automation $\rightarrow$ Automated Actions*.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Cột "Đàm phán" có cấu hình Rotting SLA là 14 ngày.
  * *When:* Deal X không phát sinh bất kỳ tương tác ghi nhận nào sau 15 ngày.
  * *Then:* Tiêu đề thẻ deal trên Kanban tự động chuyển sang màu đỏ cảnh báo.

---

### BR-09: Quy tắc Thiết lập giá trị mặc định thông minh (Smart Default Values)
* **Ý nghĩa nghiệp vụ:** Chuẩn hóa quy trình nhập liệu ngay từ bước đầu tiên, tránh việc nhân viên bỏ trống dữ liệu hoặc chọn nhầm thông tin cơ bản.
* **Tình huống thực tế:** Khi nhân viên bấm "Tạo mới cơ hội", hệ thống tự động điền sẵn: Người phụ trách = Chính người đang đăng nhập; Đội ngũ = Đội ngũ mà nhân viên đó trực thuộc; Đơn vị tiền tệ = VNĐ; Mức độ ưu tiên = 1 sao.
* **Cách BA cấu hình trên Odoo UI:**
  * Sử dụng tính năng "Set Defaults" trên giao diện form (bật Developer mode) hoặc thiết lập tại hồ sơ Đội bán hàng.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Nhân viên B thuộc đội "B2B Miền Nam" đăng nhập vào hệ thống.
  * *When:* Bấm nút "New" trên màn hình CRM.
  * *Then:* Ô Salesperson tự động hiển thị tên Nhân viên B, ô Sales Team tự động hiển thị "B2B Miền Nam".

---

### BR-10: Quy tắc Đánh giá & Chuẩn hóa chất lượng thông tin (Data Quality & Verification)
* **Ý nghĩa nghiệp vụ:** Làm sạch dữ liệu khách hàng ngay tại điểm chạm đầu vào, phục vụ cho các chiến dịch Telesales và Email Marketing đạt tỷ lệ gửi thành công cao nhất.
* **Tình huống thực tế:** Kiểm tra số điện thoại có đủ 10 chữ số theo chuẩn Việt Nam không; Kiểm tra cú pháp email có chứa ký tự `@` và tên miền hợp lệ không.
* **Cách BA cấu hình trên Odoo UI:**
  * Bật tính năng *Phone Validation* trong Cài đặt chung và chọn Quốc gia mặc định là Việt Nam (+84).
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Nhân viên nhập số điện thoại là `091234567`.
  * *When:* Bấm lưu hồ sơ khách hàng.
  * *Then:* Hệ thống nhận diện số điện thoại thiếu số và tự động đánh dấu trạng thái cảnh báo trên icon cuộc gọi.

---

### BR-11: Quy tắc Kiểm soát & Hợp nhất trùng lặp (Deduplication & Merge Policies)
* **Ý nghĩa nghiệp vụ:** Tránh tình trạng 2 nhân viên kinh doanh cùng gọi điện chào mời một khách hàng gây khó chịu và mất uy tín doanh nghiệp; gom toàn bộ lịch sử tương tác về một đầu mối duy nhất.
* **Tình huống thực tế:** Khi một khách hàng đã có hợp đồng năm ngoái tiếp tục đăng ký form trên landing page mới, hệ thống phải phát hiện trùng lặp theo Email hoặc Số điện thoại.
* **Cách BA cấu hình trên Odoo UI:**
  * Sử dụng tính năng "Merge Opportunities" trên danh sách List View của CRM.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Có 2 thẻ cơ hội cùng chung email `giamdoc@congtyabc.vn`.
  * *When:* Trưởng phòng chọn cả 2 deal và bấm Hành động $\rightarrow$ Gộp (Merge).
  * *Then:* Hệ thống tạo thành 1 deal duy nhất lưu giữ người phụ trách chính, cộng gộp doanh thu kỳ vọng và hợp nhất toàn bộ lịch sử trao đổi (Chatter) của cả 2 deal cũ.

---

### BR-12: Quy tắc Định tuyến tiếp nhận đa kênh & Thông báo (Omnichannel Routing & Alerts)
* **Ý nghĩa nghiệp vụ:** Đảm bảo khách hàng tiềm năng đổ về từ bất kỳ kênh nào (Website, Email, Hotline, Fanpage) đều được chuyển giao đến đúng bộ phận phụ trách trong thời gian ngắn nhất.
* **Tình huống thực tế:** Email gửi vào `duan@noithat.vn` tự động sinh deal cho Đội B2B Dự án; Khách điền form trên website bán lẻ tự động chuyển deal vào phễu Đội B2C Showroom.
* **Cách BA cấu hình trên Odoo UI:**
  * Menu *CRM $\rightarrow$ Configuration $\rightarrow$ Sales Teams*: Thiết lập địa chỉ Email Alias cho từng đội ngũ.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Khách hàng gửi email yêu cầu báo giá vào địa chỉ `duan@noithat.vn`.
  * *When:* Hệ thống nhận email thành công.
  * *Then:* Một cơ hội mới tự động xuất hiện tại cột đầu tiên của Đội B2B Dự án kèm toàn bộ nội dung email được hiển thị trong Chatter.

---

### BR-13: Quy tắc Nhật ký kiểm toán & Lịch sử biến động (Audit Trail & Activity Tracking)
* **Ý nghĩa nghiệp vụ:** Phục vụ công tác kiểm tra, đối soát và minh bạch thông tin khi có tranh chấp; đo lường chính xác hiệu suất làm việc của từng cá nhân.
* **Tình huống thực tế:** Biết được ai đã sửa giá trị hợp đồng từ 500 triệu xuống 400 triệu vào lúc mấy giờ; Đo lường xem từ lúc nhận lead đến lúc gọi cuộc gọi đầu tiên mất bao nhiêu tiếng (Time to First Contact).
* **Cách BA cấu hình trên Odoo UI:**
  * Xem trực tiếp luồng trao đổi bên dưới mỗi chứng từ (*Chatter Activity Log*).
  * Xem các chỉ số "Số ngày chốt đơn" (Days to Close), "Số ngày gán" (Days to Assign) trên báo cáo CRM Analysis.
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Cơ hội A đang có Doanh thu dự kiến là 200.000.000 VNĐ.
  * *When:* Nhân viên kinh doanh đổi thành 180.000.000 VNĐ và bấm lưu.
  * *Then:* Dòng nhật ký bên dưới ghi rõ: *"Nguyễn Văn A đã thay đổi Doanh thu dự kiến từ 200,000,000 thành 180,000,000 VNĐ lúc 14:30 ngày 05/09/2026"*.

---

### BR-14: Quy tắc Nhận diện doanh thu & Tiền tệ (Revenue Recognition & Currency Rules)
* **Ý nghĩa nghiệp vụ:** Quản lý chính xác doanh số cho các mô hình kinh doanh thuê bao định kỳ (MRR/ARR) và bảo toàn giá trị hợp đồng khi giao dịch bằng ngoại tệ (USD, EUR).
* **Tình huống thực tế:** Hợp đồng phần mềm có phí thuê bao 10 triệu/tháng ký hạn 1 năm $\rightarrow$ Tổng giá trị hợp đồng là 120 triệu nhưng Doanh thu định kỳ hàng tháng (MRR) ghi nhận vào chỉ số tăng trưởng là 10 triệu/tháng.
* **Cách BA cấu hình trên Odoo UI:**
  * Menu *CRM $\rightarrow$ Cấu hình $\rightarrow$ Recurring Plans*: Thiết lập các gói chu kỳ thanh toán (Tháng, Quý, Năm).
* **Tiêu chí nghiệm thu (AC):**
  * *Given:* Cơ hội được chọn gói doanh thu định kỳ "Hàng tháng (Monthly)".
  * *When:* Nhân viên nhập Doanh thu kỳ vọng là 15.000.000 VNĐ.
  * *Then:* Hệ thống tự động ghi nhận MRR = 15.000.000 VNĐ để phục vụ biểu đồ dự báo tăng trưởng thuê bao.

---

## 🗄️ LỊCH SỬ THAY ĐỔI TÀI LIỆU (CHANGELOG)

| Phiên bản | Ngày | Người cập nhật | Nội dung cập nhật |
| :---: | :---: | :---: | :--- |
| **v1.0** | 2026-09-02 | Lead BA & AI | Khởi tạo bảng bóc tách 7 Business Rules cơ bản. |
| **v1.5** | 2026-09-03 | Lead BA & AI | Bổ sung thêm 7 Business Rules nâng cao (BR-08 → BR-14). |
| **v2.0** | 2026-09-05 | Lead BA & AI | **Tái cấu trúc 100% Cẩm nang Business Rules cho BA**: Chuyển đổi toàn bộ từ góc nhìn đọc mã nguồn sang Cẩm nang đặc tả nghiệp vụ chuẩn quốc tế (Ý nghĩa kinh doanh, Kịch bản thực tế, Cấu hình giao diện Odoo No-Code và Tiêu chí nghiệm thu Acceptance Criteria). |
