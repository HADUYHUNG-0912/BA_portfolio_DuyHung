# Nghiên Cứu Tình Huống: Tối Ưu Tính Năng Tin Nhắn Tự Xóa & Bảo Mật Hội Thoại — Zalo

> Ứng viên: **Hà Duy Hưng** — Business Analyst, Mobile Product & Security / Privacy  
> Phương pháp: Reverse Engineering Logic, Competitor Benchmark, 5 Whys Root Cause Analysis, Multi-layer Defense Design  
> Phạm vi: Phân tích cơ chế Tin nhắn tự xóa hiện hành + Đề xuất mở rộng Nhóm chat, Mốc thời gian tức thời và Rào chắn chống rò rỉ  

---

## 1. Project Context

| Hạng mục | Chi tiết |
| :--- | :--- |
| **Đơn vị nghiệp vụ** | Zalo (VNG Corporation) — Nền tảng nhắn tin và liên lạc OTT hàng đầu Việt Nam (>75 triệu người dùng hoạt động hàng tháng - MAU) |
| **Loại dự án** | Product Feature Optimization — Cybersecurity & Privacy-Enhancing Technologies (PETs) |
| **Phân hệ mục tiêu** | Tính năng Tin nhắn tự xóa (Ephemeral Messaging) trong hội thoại cá nhân 1-1 (ra mắt 11/2021) và lộ trình mở rộng nhóm |
| **Thời gian thực hiện** | Nghiên cứu tài liệu kỹ thuật, phân tích hành vi người dùng, đối chuẩn đối thủ và thiết kế giải pháp trong 2 tuần |
| **Stakeholders liên quan** | Người dùng cá nhân/doanh nghiệp (End-users), Đội ngũ Product Owner/BA Zalo, Kỹ sư bảo mật (Security Engineers), Đội ngũ Phát triển Mobile (Android & iOS) |
| **Phương pháp tiếp cận** | Desk Research (thông cáo báo chí, diễn đàn công nghệ Tinhte, VOZ, Znews), Reverse Engineering luồng gửi/nhận local-first, Competitor Benchmark (Telegram Secret Chat, Signal, WhatsApp, Snapchat) |
| **Kết quả bàn giao** | 8 Business Rules hiện hành, 3 Pain Points phân tích 5 Whys, 8 Business Requirements đề xuất, 3 Sơ đồ kỹ thuật (Flowchart, Sequence, Architecture), Ma trận giải pháp In/Out-of-scope |

---

## 2. Business Problem Statement

Tính năng Tin nhắn tự xóa của Zalo được thiết kế ban đầu nhằm phục vụ bài toán **"Quản lý vòng đời dữ liệu / Dọn dẹp lưu trữ định kỳ" (Data Lifecycle Hygiene)** trên bộ nhớ thiết bị, chứ chưa phải là một **"Cơ chế bảo mật hội thoại tức thời chống rò rỉ" (Real-time Ephemeral Privacy)**. Sự lệch pha giữa mục tiêu thiết kế ban đầu và kỳ vọng an toàn thông tin thực tế của người dùng dẫn đến **3 điểm nghẽn nghiêm trọng**:

### Vấn đề 1 — Khoảng trống bảo mật trong trò chuyện nhóm (PP1)
> Zalo hiện chỉ hỗ trợ tự xóa trong hội thoại 1-1. Các nhóm trò chuyện công việc, dự án hoặc gia đình hoàn toàn không có cơ chế bảo vệ tương đương dù tính năng này đã được cam kết từ năm 2021.
- **Root Cause (5 Whys):** Xử lý nhóm phức tạp hơn 1-1 (phải phân phối và đồng bộ trạng thái xóa cho $N$ thành viên, xử lý người rời/vào nhóm giữa chừng và chính sách xem lịch sử cũ) $\rightarrow$ Đội ngũ Product ưu tiên các tính năng thúc đẩy tương tác bề mặt $\rightarrow$ *Đây là vấn đề ưu tiên hóa lộ trình phát triển (Roadmap Prioritization), không phải rào cản kỹ thuật bất khả thi*.
- **Business Impact:** Nhóm người dùng có nhu cầu trao đổi dữ liệu công việc nhạy cảm (kinh doanh, tài chính, nhân sự) buộc phải di cư sang Telegram, Signal hoặc WhatsApp để làm việc.

### Vấn đề 2 — Thang thời gian tự xóa quá dài và thiếu linh hoạt (PP2)
> Hệ thống chỉ cung cấp 3 mốc thời gian cố định: **1 ngày, 7 ngày và 30 ngày**. Không có bất kỳ mốc ngắn nào theo giờ hoặc phút.
- **Root Cause (5 Whys):** Thiết kế ban đầu nhắm vào use case dọn dẹp bộ nhớ máy định kỳ theo chu kỳ ngày $\rightarrow$ Không nhắm vào kịch bản bảo mật tức thời (Ephemeral Chat) $\rightarrow$ *Đây là giới hạn phạm vi thiết kế ban đầu (Design Scope Boundary), hoàn toàn có thể mở rộng mà không làm thay đổi kiến trúc lưu trữ*.
- **Business Impact:** Người dùng khi gửi dữ liệu siêu nhạy cảm dùng một lần (mã OTP, mật khẩu tạm, ảnh căn cước công dân, số thẻ ngân hàng) không thể chờ 24 giờ. Họ buộc phải tự thu hồi (Revoke) thủ công hoặc sử dụng nền tảng khác.

### Vấn đề 3 — Ảo tưởng an toàn trước rủi ro chụp màn hình & lưu trữ trước hạn (PP3)
> Tính năng tự xóa chỉ xóa dữ liệu quá hạn, **hoàn toàn bất lực trước rủi ro rò rỉ tức thời**. Người nhận có đủ thời gian và công cụ để chụp ảnh màn hình (Screenshot), sao chép nội dung (Copy) hoặc chuyển tiếp (Forward) sang cuộc trò chuyện khác trước khi tin biến mất.
- **Root Cause:** Phần mềm thiếu lớp kiểm soát hành vi giao diện người dùng (UI Behavioral Restrictions) và thiếu cơ chế tận dụng API an ninh phần cứng của hệ điều hành di động.
- **Business Impact:** Tạo ra "ảo tưởng an toàn" (False Sense of Security) cho người gửi; khi dữ liệu bị rò rỉ ra ngoài gây tổn thất uy tín thương hiệu và làm giảm mức độ tin cậy của người dùng vào tuyên bố bảo mật của Zalo.

---

## 3. Analysis Approach

Quy trình phân tích nghiệp vụ bám sát thực tiễn công nghệ di động và kỹ thuật an toàn thông tin:

```
GIAI ĐOẠN 1: KHƠI GỢI YÊU CẦU & ĐỐI CHUẨN TÍNH NĂNG (BENCHMARKING)
├── Desk Research & Khảo sát diễn đàn công nghệ: VietnamNet, Znews, PLO Kỷ Nguyên Số, Tinhte.vn
├── Reverse Engineering hành vi: Kiểm chứng cơ chế đếm giờ gửi vs đọc, đồng bộ offline, ngoại lệ file server
└── Đối chuẩn giải pháp đối thủ:
    ├── Signal: Hỗ trợ đếm giờ từ lúc đọc, chặn screenshot Android, thông báo iOS, tùy chỉnh linh hoạt
    ├── Telegram Secret Chat: Chặn chụp màn hình, cấm chuyển tiếp, xóa đa điểm tức thì
    └── Snapchat: Cảnh báo screenshot thời gian thực, giao diện tự hủy nguyên bản

GIAI ĐOẠN 2: BÓC TÁCH BUSINESS RULES & NGUYÊN NHÂN CỐT LÕI (ROOT CAUSE ANALYSIS)
├── Trích xuất và xác thực 8 Business Rules hiện hành (BR1 đến BR8) kèm độ tin cậy nguồn tin
└── Áp dụng kỹ thuật 5 Whys cho từng Pain Point để phân định rõ giữa giới hạn kỹ thuật và giới hạn phạm vi

GIAI ĐOẠN 3: MÔ HÌNH HÓA DÒNG CHẢY HỆ THỐNG (SYSTEM MODELING)
├── Flowchart Vòng đời tin nhắn tự xóa: Mô hình hóa luồng từ thiết lập cấu hình, gán TTL đến purge Local DB
├── Sequence Diagram Kiểm soát rò rỉ: Luồng tương tác giữa Client, Server và OS API khi người dùng chụp màn hình
└── Solution Architecture Luồng Nhóm: Kiến trúc phân phối TTL broadcast và chính sách lọc lịch sử thành viên

GIAI ĐOẠN 4: THIẾT KẾ GIẢI PHÁP ĐA TẦNG & QUẢN TRỊ PHẠM VI (SOLUTION SPECIFICATION)
├── Thiết kế giải pháp cho PP1 (Group Chat TTL cho nhóm <20 thành viên)
├── Thiết kế giải pháp cho PP2 (Bổ sung mốc 5 phút và 1 giờ trên kiến trúc TTL sẵn có)
└── Thiết kế giải pháp cho PP3 (Phòng thủ chiều sâu: UI Disclaimer + Disable Copy/Forward + FLAG_SECURE)
```

---

## 4. Business Requirements Catalog

### 4.1 Business Rules Hiện Hành (Confirmed & Baseline)

| ID | Quy tắc nghiệp vụ | Đánh giá hành vi thực tế | Độ tin cậy | Nguồn kiểm chứng & Đối soát |
| :---: | :--- | :--- | :---: | :--- |
| **BR1** | Mốc tính thời gian tự xóa | Đếm ngược **ngay từ thời điểm GỬI tin thành công**, không phụ thuộc vào thời điểm người nhận đọc | ✅ Cao | ZaX.app, tài liệu kỹ thuật Zalo SDK; kiểm chứng thực nghiệm bằng cách gửi và canh giờ |
| **BR2** | Đồng bộ trạng thái đa thiết bị | Cấu hình bật/tắt tự xóa được đồng bộ giữa Di động và Máy tính (Zalo PC/Web), nhưng có độ trễ cục bộ | ⚠️ Trung bình | VietnamNet (thông cáo 11/2021); phản ánh người dùng trên Tinhte về lỗi đồng bộ cache SQLite |
| **BR3** | Xử lý tin nhắn khi thiết bị offline | Tin nhắn lưu trên Local DB người nhận; nếu máy tắt mạng qua mốc TTL, khi online lại tin sẽ lập tức bị xóa | ⚠️ Giả định | Kiến trúc Zalo không lưu trữ tin nhắn vĩnh viễn trên server, ưu tiên local-first trên client |
| **BR4** | Phạm vi áp dụng & Hiệu lực hồi tố | Áp dụng theo **từng cuộc hội thoại độc lập; KHÔNG có hiệu lực hồi tố** với các tin nhắn đã gửi trước đó | ✅ Cao | ZaX.app, Điện Máy Chợ Lớn; tin nhắn cũ được bảo lưu trạng thái mặc định |
| **BR5** | Cơ chế xử lý tệp đính kèm và ảnh | Hai cơ chế độc lập: (1) Tự xóa theo cấu hình hội thoại; (2) Server Zalo tự động dọn dẹp file media cũ sau ~2 tháng | ✅ Cao | Cuumaytinh.com (phân tích mã lỗi 508 Zalo do file media server bị xóa định kỳ) |
| **BR6** | Thông báo hệ thống minh bạch | Khi bất kỳ ai thay đổi cài đặt tự xóa, hệ thống **tự động gửi tin nhắn hệ thống thông báo cho cả 2 bên** | ✅ Cao | Znews.vn, VietnamNet; kiểm chứng giao diện thực tế trên cả 2 tài khoản thử nghiệm |
| **BR7** | Tính bất biến sau khi xóa | Tin nhắn đã bị xóa tự động là **xóa vĩnh viễn, không thể khôi phục** bằng tính năng Sao lưu & Đồng bộ | ✅ Cao | ZaX.app, Fastcare.vn; phân biệt rõ với tính năng hoàn tác thu hồi trong 5 giây |
| **BR8** | Thẩm quyền điều chỉnh cấu hình | **Cả 2 bên tham gia hội thoại đều có quyền bật, tắt hoặc thay đổi mốc thời gian** bất kỳ lúc nào | ✅ Cao | Điện Thoại Giá Kho, MediaMart; xác nhận phân quyền ngang hàng (P2P) trong chat 1-1 |

### 4.2 Business Requirements Đề Xuất (New Requirements)

| Mã BR | Yêu cầu nghiệp vụ đề xuất | Phân loại | Mức độ ưu tiên | Pain Point liên kết |
| :---: | :--- | :---: | :---: | :---: |
| **BR-N01** | Hệ thống phải hỗ trợ kích hoạt tính năng Tin nhắn tự xóa trong các Nhóm chat có quy mô $\le 20$ thành viên | Functional | Must-have | PP1 |
| **BR-N02** | Thành viên rời nhóm chat không làm mất tính năng; các tin nhắn họ đã nhận trên máy vẫn tự xóa đúng hạn TTL | Functional | Must-have | PP1 |
| **BR-N03** | Thành viên mới gia nhập nhóm chat tuyệt đối không được truy cập các tin nhắn tự xóa đã gửi trước thời điểm vào nhóm | Functional | Must-have | PP1 |
| **BR-N04** | Bổ sung 2 mốc thời gian tự xóa ngắn: **5 phút** (cho thông tin siêu nhạy cảm/OTP) và **1 giờ** (cho cuộc trao đổi ngắn hạn) | Functional | Must-have | PP2 |
| **BR-N05** | Trên Android: Hệ thống phải kích hoạt thuộc tính `FLAG_SECURE` trên Window chat để chặn chụp/quay màn hình khi có tin tự xóa | Security | Must-have | PP3 |
| **BR-N06** | Trên iOS: Hệ thống phải phát hiện sự kiện chụp màn hình và tự động gửi tin nhắn cảnh báo công khai vào khung chat | Security | Must-have | PP3 |
| **BR-N07** | Hệ thống phải vô hiệu hóa tính năng Chuyển tiếp (Forward) và Sao chép (Copy) đối với mọi tin nhắn được gắn cờ tự xóa | Functional | Must-have | PP3 |
| **BR-N08** | Hiển thị thông báo giải thích rõ ràng (UI Disclaimer Banner) về giới hạn tính năng (không chặn được chụp bằng camera ngoài) | UX / Policy | Should-have | PP3 |

---

## 5. Solution Design & Visual Artifacts

### 5.1 Giải pháp PP1 — Mở rộng Tính năng Tự xóa cho Nhóm Chat (Group Ephemeral Messaging)

* **Phạm vi triển khai giai đoạn 1:** Ưu tiên áp dụng cho nhóm quy mô nhỏ ($\le 20$ thành viên) — đối tượng nhóm gia đình, ban quản trị dự án hoặc nhóm giao dịch tài chính nội bộ.
* **Cơ chế kỹ thuật cốt lõi:**
  * Mỗi tin nhắn gửi trong nhóm được server gắn kèm một trường giá trị **TTL (Time-To-Live)** và nhãn thời gian `created_at`.
  * Server broadcast tin nhắn tới toàn bộ thành viên đang hoạt động. SQLite cục bộ trên từng máy lưu bản ghi kèm bộ đếm lùi độc lập.
* **Quản trị quy tắc thành viên (Membership Edge Cases):**
  * *Người rời nhóm:* Bản ghi đã tải về máy họ vẫn giữ nguyên nhãn TTL và tự động bị worker ngầm xóa sạch khi hết hạn.
  * *Người mới vào nhóm:* Câu lệnh truy vấn lịch sử hội thoại thực hiện bộ lọc nghiêm ngặt: `SELECT * FROM messages WHERE created_at >= member_join_time`. Toàn bộ tin nhắn tự xóa trong quá khứ bị ẩn hoàn toàn.

[→ Xem sơ đồ: Solution Architecture — Cơ chế TTL Đồng bộ cho Nhóm chat](./images/03-architecture-dong-bo-ttl-group-chat.png)

---

### 5.2 Giải pháp PP2 — Thang Đo Thời Gian Linh Hoạt (Short-term Retention Tiers)

* **Bổ sung tùy chọn UI:** Mở rộng danh mục chọn mốc thời gian từ 3 mốc lên 5 mốc: **5 phút, 1 giờ, 1 ngày, 7 ngày, 30 ngày**.
* **Bảo toàn kiến trúc Backend:**
  * Vẫn sử dụng cùng cơ chế giá trị số nguyên TTL (ví dụ: 5 phút = 300 giây; 1 giờ = 3600 giây). Hệ thống backend và API gửi nhận không cần thay đổi cấu trúc bảng hay schema dữ liệu.
* **Tối ưu hóa hiệu năng dọn dẹp Local DB:**
  * Đối với các mốc siêu ngắn (5 phút), tránh kích hoạt quét toàn bộ database liên tục gây hao pin. Áp dụng kỹ thuật **Lazy Deletion** (kiểm tra và xóa ngay khi mở màn hình chat) kết hợp **Periodic Purge Worker** chạy nền mỗi khi ứng dụng chuyển trạng thái Idle.

---

### 5.3 Giải pháp PP3 — Cơ Chế Phòng Thủ Rò Rỉ Đa Tầng (Anti-Leak Defense in Depth)

Giải pháp kết hợp hài hòa giữa rào chắn kỹ thuật hệ thống, kiểm soát giao diện và truyền thông minh bạch:

| Lớp bảo vệ | Cơ chế can thiệp | Chi tiết kỹ thuật | Phạm vi xử lý |
| :--- | :--- | :--- | :---: |
| **Lớp 1: Kiểm soát UI** | Khóa thao tác trích xuất dữ liệu trực tiếp | Vô hiệu hóa menu ngữ cảnh (Context Menu) đối với tin tự xóa: cấm nút **Sao chép (Copy)** và cấm nút **Chuyển tiếp (Forward)** | In-scope (Cả Android & iOS) |
| **Lớp 2: Chặn Chụp Android** | Bảo vệ lớp hiển thị bằng API hệ điều hành | Gọi `getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE)` khi người dùng đang ở trong màn hình chat có tin tự xóa. Hệ điều hành tự động chặn chụp/quay màn hình | In-scope (Android) |
| **Lớp 3: Cảnh báo iOS** | Phát hiện và gửi thông điệp răn đe | Lắng nghe thông báo `UIApplication.userDidTakeScreenshotNotification`. Khi phát hiện chụp màn hình, client gửi tín hiệu về server để chèn tin nhắn cảnh báo đỏ trong chat: *"⚠️ [Tên] vừa chụp ảnh màn hình cuộc trò chuyện"* | In-scope (iOS) |
| **Lớp 4: Truyền thông Minh bạch** | Xóa bỏ ảo tưởng an toàn của người dùng | Hiển thị Banner cảnh báo khi bật tính năng và cập nhật Trung tâm Trợ giúp: Nêu rõ tính năng không thể ngăn chặn người dùng chụp bằng thiết bị thứ hai (Analog Hole) | In-scope (Chính sách & UX) |

[→ Xem sơ đồ: Sequence Diagram — Luồng Kiểm soát Chụp màn hình & Cảnh báo](./images/02-sequence-kiem-soat-screenshot-anti-leak.png)

---

### 5.4 Tổng quan Vòng Đời Tin Nhắn Tự Xóa End-to-End

[→ Xem sơ đồ: Flowchart — Vòng đời Tin nhắn Tự xóa Zalo](./images/01-flowchart-vong-doi-tin-nhan-tu-xoa.png)

---

## 6. Business Value & Expected Impact

Bảng tổng hợp tác động kinh doanh và các chỉ số đo lường hiệu quả (KPIs) trước và sau khi triển khai giải pháp:

| Chỉ số đo lường (KPI) | Hiện trạng trước giải pháp | Sau khi triển khai giải pháp | Mức độ cải thiện kỳ vọng |
| :--- | :--- | :--- | :--- |
| **Điểm hài lòng về Bảo mật & Riêng tư (Privacy CSAT)** | 62 / 100 (người dùng e ngại rò rỉ dữ liệu) | Dự kiến đạt $\ge 85$ / 100 | 🟢 **Tăng 23 điểm** mức độ tin cậy thương hiệu |
| **Tỷ lệ di cư sang Telegram/Signal vì lý do bảo mật** | Ước tính 15–20% nhóm người dùng công việc nhạy cảm | Giảm tỷ lệ di cư xuống dưới 8% | 🟢 **Giữ chân 55%** người dùng có giá trị cao |
| **Tỷ lệ cuộc trò chuyện kích hoạt Tin nhắn tự xóa** | Dưới 8% tổng số hội thoại (do mốc quá dài) | Đạt $\ge 22\%$ tổng số hội thoại kích hoạt | 🟢 **Tăng gần gấp 3 lần** mức độ phổ cập tính năng |
| **Số lượng khiếu nại về lộ lọt thông tin nhạy cảm** | Thường xuyên phát sinh do bị chụp màn hình chia sẻ | Giảm $\ge 70\%$ nhờ cơ chế khóa thao tác và răn đe | 🟢 **Giảm thiểu tối đa** rủi ro khủng hoảng truyền thông |

---

## 7. Constraints, Assumptions & Risks

### Ràng buộc kỹ thuật & Nghiệp vụ (Constraints)
* **Kiến trúc Local-First:** Zalo không vận hành theo mô hình lưu trữ vĩnh viễn trên Cloud tập trung như Telegram. Việc dọn dẹp phụ thuộc hoàn toàn vào tình trạng hoạt động của Local Database trên thiết bị người dùng.
* **Giới hạn vật lý (The Analog Hole):** Không có bất kỳ công nghệ phần mềm nào trên thế giới (kể cả Signal hay Secret Chat) có thể ngăn chặn người dùng dùng một chiếc điện thoại/camera thứ hai chụp lại màn hình vật lý. Điều này được xác định rõ ràng là **Out-of-scope** về mặt kỹ thuật.

### Giả định phân tích (Assumptions)
* Người dùng đồng thuận với quy tắc: Tính riêng tư cao hơn sự tiện lợi (sẵn sàng chấp nhận việc bị khóa chức năng Sao chép/Chuyển tiếp khi dùng chế độ tự xóa).
* Hạ tầng push notification của Zalo đảm bảo độ trễ gửi tin nhắn cảnh báo chụp màn hình trên iOS dưới 1.5 giây.

### Quản trị Rủi ro & Kế hoạch Giảm thiểu (Risks & Mitigations)

| Mã | Rủi ro nhận diện | Mức độ | Kế hoạch giảm thiểu của BA |
| :---: | :--- | :---: | :--- |
| **R-01** | Tải dọn dẹp bộ nhớ tăng đột ngột khi bổ sung mốc 5 phút trên hàng triệu máy cấu hình thấp | 🟡 Trung bình | Áp dụng kỹ thuật Lazy Purge: Chỉ kích hoạt xóa khi người dùng mở app hoặc khi thiết bị cắm sạc/nghỉ ngơi (idle) |
| **R-02** | Người dùng Android phản ứng tiêu cực khi bị chặn chụp màn hình hoàn toàn | 🟡 Trung bình | Thiết kế Tooltip giải thích trực quan: *"Chức năng chụp màn hình bị tạm khóa để bảo vệ tin nhắn tự xóa trong hội thoại này"* |
| **R-03** | Xung đột quyền điều chỉnh cấu hình trong nhóm chat đông người | 🔴 Cao | Giới hạn thẩm quyền: Trong giai đoạn 1, chỉ Trưởng nhóm (Group Admin) và Phó nhóm mới có quyền bật/tắt hoặc đổi mốc TTL |

---

## 8. Deliverables Index

Hồ sơ phân tích nghiệp vụ, tài liệu giải pháp và sơ đồ kỹ thuật được lưu trữ hoàn chỉnh trong thư mục dự án:

| Hạng mục tài liệu | Đường dẫn tham chiếu | Tóm tắt nội dung bàn giao |
| :--- | :--- | :--- |
| **Bản Ghi Chép Thô & Nguồn Đối Soát** | [tin_nhan_tu_xoa_ZALO.md](./doc/tin_nhan_tu_xoa_ZALO.md) | Tài liệu phân tích gốc, nguồn trích dẫn báo chí và đánh giá độ tin cậy BR1–BR8 |
| **Đặc Tả Kỹ Thuật 3 Sơ Đồ** | [zalo-diagrams.md](./doc/zalo-diagrams.md) | Bản đặc tả chi tiết logic vận hành kèm mã nguồn Mermaid gốc cho 3 sơ đồ |
| **File Thiết Kế Gốc Draw.io** | [tu_xoa.drawio.xml](./doc/tu_xoa.drawio.xml) | Tệp sơ đồ thiết kế đồ họa nguyên bản trên nền tảng Draw.io |
| **Sơ đồ Flowchart Vòng Đời Tin Nhắn** | [01-flowchart-vong-doi-tin-nhan-tu-xoa.png](./images/01-flowchart-vong-doi-tin-nhan-tu-xoa.png) | Sơ đồ luồng End-to-End từ kích hoạt, đếm ngược TTL đến dọn dẹp Local DB |
| **Sơ đồ Sequence Chặn Chụp Màn Hình** | [02-sequence-kiem-soat-screenshot-anti-leak.png](./images/02-sequence-kiem-soat-screenshot-anti-leak.png) | Sơ đồ tuần tự phòng thủ rò rỉ: FLAG_SECURE Android & cảnh báo iOS |
| **Sơ đồ Kiến Trúc Nhóm Chat TTL** | [03-architecture-dong-bo-ttl-group-chat.png](./images/03-architecture-dong-bo-ttl-group-chat.png) | Kiến trúc phân phối TTL đồng bộ và xử lý ngoại lệ thành viên vào/ra nhóm |

---

> ⬅️ **Quay lại trang hồ sơ cá nhân:** [Trang chủ Portfolio](../../README.md)
