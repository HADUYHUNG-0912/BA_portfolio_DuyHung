# Nghiên Cứu Tình Huống: Phân Tích Tính Năng "Thu Hồi Tin Nhắn" & Nguyên Lý Soft Delete — Zalo

> Ứng viên: **Hà Duy Hưng** — Business Analyst, Mobile Product & Security / Privacy  
> Phương pháp: Reverse Engineering Logic (Black-box Testing), Business Rules Extraction, Defense-in-Depth Analysis  
> Phạm vi: Bóc tách 4 Business Rules cốt lõi ẩn sau nút "Thu hồi", phân tích Pain Points người dùng và đề xuất cải tiến trải nghiệm  

---

## 1. Project Context

| Hạng mục | Chi tiết |
| :--- | :--- |
| **Đơn vị nghiệp vụ** | Zalo (VNG Corporation) — Nền tảng nhắn tin và liên lạc OTT hàng đầu Việt Nam (>75 triệu MAU) |
| **Loại dự án** | Product Feature Analysis — UX Improvement & Business Rules Documentation |
| **Phân hệ mục tiêu** | Tính năng Thu hồi tin nhắn (Message Recall) trong hội thoại cá nhân 1-1 và nhóm |
| **Thời gian thực hiện** | Nghiên cứu thực nghiệm (black-box testing), phân tích hành vi và thiết kế giải pháp trong 1 tuần |
| **Stakeholders liên quan** | Người dùng cuối (End-users), Product Owner / BA Zalo, Kỹ sư Backend & Mobile, Trust & Safety Team |
| **Phương pháp tiếp cận** | Black-box Reverse Engineering (kiểm thử thực nghiệm trên thiết bị thật), Competitor Benchmark (Telegram, WhatsApp, Signal, LINE), đối soát tài liệu help.zalo.me |
| **Kết quả bàn giao** | 4 Business Rules hiện hành, 2 Pain Points có nguồn gốc, 4 Business Requirements đề xuất, 3 sơ đồ kỹ thuật (Flowchart, Sequence, State Diagram), Bộ nguồn tài liệu tham chiếu 3 tầng |

---

## 2. Business Problem Statement

Tính năng "Thu hồi tin nhắn" của Zalo có giao diện tác động đơn giản — nhấn giữ tin nhắn, chọn "Thu hồi" — nhưng cỗ máy xử lý bên trong phức tạp hơn nhiều so với thiết kế UI thể hiện. **Sự phức tạp bị ẩn này tạo ra 2 loại vấn đề:**

### Vấn đề 1 — Rào cản nhận thức người dùng (PP1)

> Nút "Thu hồi" vẫn hiển thị với mọi tin nhắn của mình dù đã gửi từ rất lâu. Người dùng thường nhầm tưởng rằng họ có thể thu hồi bất cứ lúc nào, dẫn đến thất vọng khi bị từ chối sau 1 giờ gửi.

* **Root Cause:** Việc kiểm tra thời gian được xử lý hoàn toàn ở Server-side (không phải Client), khiến UI không phân biệt được tin nhắn nào còn có thể thu hồi.
* **Business Impact:** Người dùng bị lộ thông tin nhạy cảm và giảm sút niềm tin vào tính năng bảo mật của ứng dụng.

### Vấn đề 2 — Tombstone thiếu ngữ cảnh trong nhóm chat (PP2)

> Cả người gửi lẫn người nhận đều thấy dòng chữ "Tin nhắn đã được thu hồi" — nhưng trong nhóm chat đông người, ai là người thu hồi, thu hồi tin nhắn nào trong cuộc trò chuyện dài là điều hoàn toàn mập mờ.

* **Root Cause:** Thiết kế Tombstone hiện tại chỉ đánh dấu trạng thái mà không cung cấp nguồn gốc (thu hồi bởi ai, lúc mấy giờ) để người nhận hiểu bối cảnh.
* **Business Impact:** Trong các nhóm chat công việc, tin nhắn thu hồi có thể gây hiểu nhầm về mục đích và tạo ma sát giao tiếp không cần thiết.

---

## 3. Business Rules Hiện Hành (As-Is)

Bốn Business Rule được rút ra qua kiểm thử thực nghiệm (black-box testing) trên Zalo iOS và Android, kết hợp đối chiếu với help.zalo.me:

### BR1 — Giới Hạn Thời Gian (Validation — Server-side)

| Tiêu chí | Chi tiết |
| :--- | :--- |
| **Quy tắc** | Chỉ có thể thu hồi tin nhắn gửi trong **vòng 1 giờ (60 phút)** tính từ thời điểm gửi |
| **Vị trí xử lý** | **Server-side** — Client không có logic kiểm tra thời gian |
| **Hậu quả nếu vi phạm** | Server trả về lỗi, Client hiện Toast: *"Bạn chỉ có thể thu hồi tin nhắn trong vòng 1 giờ"* |
| **Điểm đặc biệt** | Nút "Thu hồi" **vẫn hiển thị** dù đã qua 1 giờ — chỉ bị từ chối khi người dùng thực sự bấm vào |
| **Lý do thiết kế** | Tránh việc Client phải chạy ngầm timer đếm ngược cho hàng ngàn tin nhắn (hao pin, tốn tài nguyên thiết bị) |
| **Nguồn xác nhận** | help.zalo.me — mục "Thu hồi tin nhắn"; kiểm thử thực nghiệm trên thiết bị thật |

### BR2 — Phân Quyền Sở Hữu (Authorization — Client-side + Server-side)

| Tiêu chí | Chi tiết |
| :--- | :--- |
| **Quy tắc** | Chỉ người gửi mới có quyền thu hồi tin nhắn của chính mình |
| **Vị trí xử lý (Lớp 1)** | **Client-side**: Nếu là tin nhắn người khác, menu ngữ cảnh hoàn toàn **không hiển thị** nút "Thu hồi" |
| **Vị trí xử lý (Lớp 2)** | **Server-side**: Re-validate để chống API giả mạo (nguyên lý Defense-in-Depth) |
| **Hiệu quả** | Giao diện gọn gàng; ngăn chặn cả bypass qua UI lẫn bypass qua API call trực tiếp |
| **Nguồn xác nhận** | Kiểm thử thực nghiệm (thử thu hồi tin nhắn người khác); thiết kế defense-in-depth theo tiêu chuẩn bảo mật OWASP |

### BR3 — Đồng Bộ Trạng Thái (Synchronization — Soft Delete + Realtime Push)

| Tiêu chí | Chi tiết |
| :--- | :--- |
| **Quy tắc** | Khi thu hồi thành công, trạng thái tin nhắn được cập nhật trên DB và push realtime đến tất cả thiết bị |
| **Cơ chế DB** | `UPDATE Message SET status = 'Recalled'` — **Soft Delete**, không xóa vật lý (hard delete) |
| **Lý do Soft Delete** | Bảo toàn tính toàn vẹn dữ liệu (audit log, xử lý tranh chấp pháp lý); đảm bảo đồng bộ trạng thái phân tán |
| **Cơ chế Push** | Zalo push sự kiện `MESSAGE_RECALLED` qua WebSocket (realtime) đến tất cả client đang kết nối |
| **Kết quả trên Client** | Nội dung tin nhắn gốc bị thay thế bằng **Tombstone**: *"Tin nhắn đã được thu hồi"* ở cả hai phía |
| **Nguồn xác nhận** | Kiểm thử thực nghiệm; nguyên lý Soft Delete trong distributed messaging systems |

### BR4 — Minh Bạch & Trải Nghiệm (Transparency & UX — Observation)

| Tiêu chí | Chi tiết |
| :--- | :--- |
| **Phân loại** | *Observation thực nghiệm (kiểm chứng thực tế trên app Zalo)* |
| **Hiện tượng quan sát** | Phía **người gửi** sau khi thu hồi: Tombstone kèm thêm **Icon bút chì ✏️** |
| **Chức năng icon** | Bấm vào icon bút chì: nội dung tin nhắn cũ **hiển thị lại trên khung soạn thảo** để người gửi chỉnh sửa và gửi lại |
| **Insight người dùng** | Thu hồi thường do gõ sai chính tả hoặc thiếu nội dung — icon bút chì tiết kiệm công sức gõ lại toàn bộ |
| **Phía người nhận** | Chỉ hiện Tombstone thuần túy, hoàn toàn không có icon bút chì |

---

## 4. Pain Points & Root Cause Analysis

### PP1 — Rào Cản Nhận Thức: Người Dùng Không Biết Thời Hạn 1 Giờ

**Biểu hiện:** Người dùng thường phát hiện không thể thu hồi sau khi đã qua 1 giờ, trong khi nút "Thu hồi" vẫn hiển thị bình thường trong menu ngữ cảnh.

**5 Whys Analysis:**
1. *Tại sao người dùng thất vọng?* → Bấm "Thu hồi" nhưng bị hệ thống từ chối.
2. *Tại sao bị từ chối?* → Tin nhắn đã gửi quá 1 giờ — vi phạm quy tắc BR1.
3. *Tại sao người dùng không biết thời hạn?* → UI không có bất kỳ dấu hiệu trực quan nào phân biệt tin nhắn "còn hạn thu hồi" và "đã hết hạn".
4. *Tại sao UI không phân biệt?* → Logic kiểm tra thời hạn nằm hoàn toàn ở Server-side, Client không nắm thông tin này trước khi gửi request.
5. *Tại sao không đẩy logic xuống Client?* → Để tối ưu hiệu năng thiết bị (tránh chạy timer nền đếm lùi cho hàng loạt tin nhắn) — quyết định kỹ thuật hợp lý nhưng để lại lỗ hổng trải nghiệm (UX gap).

**Business Impact:** Giảm niềm tin vào tính năng bảo mật; người dùng có tâm lý e ngại nhắn tin vì sợ gửi nhầm không sửa được.

---

### PP2 — Tombstone Thiếu Ngữ Cảnh Trong Nhóm Chat

**Biểu hiện:** Trong nhóm chat nhiều người, khi dòng "Tin nhắn đã được thu hồi" xuất hiện, các thành viên khác không biết ai thu hồi, thu hồi tin nhắn nào, vào lúc mấy giờ.

**5 Whys Analysis:**
1. *Tại sao gây hiểu nhầm?* → Tombstone chỉ hiển thị văn bản tĩnh, hoàn toàn không có thông tin ngữ cảnh.
2. *Tại sao không có ngữ cảnh?* → Thiết kế Tombstone hiện tại chỉ phản ánh cờ trạng thái `is_recalled = true`, không render trường metadata người thực hiện.
3. *Tại sao không hiển thị metadata?* → Thiết kế ban đầu ưu tiên tính tối giản và bảo vệ tối đa tính ẩn danh của hành động thu hồi.
4. *Tại sao điều này thành vấn đề?* → Nhóm chat công việc đòi hỏi tính minh bạch và theo dõi trách nhiệm trao đổi thông tin cao hơn chat 1-1.
5. *Kết quả?* → Gây đứt gãy mạch giao tiếp, tạo sự hoài nghi và hiểu nhầm giữa các thành viên.

**Business Impact:** Người quản lý nhóm mất khả năng kiểm soát luồng trao đổi; giảm hiệu suất làm việc đội nhóm trên nền tảng Zalo.

---

## 5. Business Requirements Đề Xuất (To-Be)

### BR-NEW-01 — Hiển Thị Trạng Thái Thu Hồi Rõ Ràng Trên UI
* **Mức độ ưu tiên:** High
* **User Story:** Với tư cách người gửi, tôi muốn biết tin nhắn nào của tôi còn trong hạn thu hồi (dưới 1 giờ) để chủ động đưa ra quyết định kịp thời.
* **Acceptance Criteria:**
  * Tin nhắn gửi trong vòng 1 giờ: Nút "Thu hồi" hiển thị với trạng thái khả dụng bình thường.
  * Tin nhắn đã quá 1 giờ: Nút "Thu hồi" hiển thị trạng thái vô hiệu hóa kèm nhãn rõ ràng *"Đã quá hạn 1 giờ"* hoặc tự động ẩn khỏi menu.
  * *Ràng buộc kỹ thuật:* Không bắt Client chạy timer nền liên tục; chỉ tính toán độ chênh lệch thời gian `currentTime - sentTime` tại thời điểm người dùng kích hoạt nhấn giữ tin nhắn.

### BR-NEW-02 — Tombstone Trong Nhóm Hiển Thị Định Danh Người Thu Hồi
* **Mức độ ưu tiên:** Medium
* **User Story:** Với tư cách thành viên nhóm chat, tôi muốn biết thành viên nào đã thu hồi tin nhắn để nắm bắt ngữ cảnh hội thoại chính xác.
* **Acceptance Criteria:**
  * Trong nhóm chat: Tombstone hiển thị định danh: *"Tin nhắn đã được thu hồi bởi [Tên thành viên]"*.
  * Trong hội thoại 1-1: Giữ nguyên thông điệp tinh gọn hiện tại (*"Tin nhắn đã được thu hồi"*).
  * *Ràng buộc bảo mật:* Tuyệt đối không hiển thị lại nội dung gốc đã thu hồi dưới bất kỳ hình thức nào.

### BR-NEW-03 — Cảnh Báo Proactive Khi Gần Hết Hạn Thu Hồi
* **Mức độ ưu tiên:** Low
* **User Story:** Với tư cách người gửi tin nhắn quan trọng, tôi muốn nhận tín hiệu cảnh báo khi sắp hết hạn thu hồi để kịp thời sửa sai sót.
* **Acceptance Criteria:**
  * Tại mốc 50 phút sau khi gửi: Hiển thị tooltip nhẹ hoặc chấm chỉ báo nhỏ cạnh tin nhắn nhắc nhở còn 10 phút hiệu lực thu hồi.
  * Cho phép người dùng bật/tắt tính năng chỉ báo này trong mục Cài đặt riêng tư.

### BR-NEW-04 — Mở Rộng Thời Hạn Thu Hồi Cho Tài Khoản Nâng Cao (Zalo Business / Premium)
* **Mức độ ưu tiên:** Low
* **User Story:** Với tư cách tài khoản doanh nghiệp hoặc người dùng chuyên nghiệp, tôi muốn có khung thời gian thu hồi dài hơn để xử lý các sự cố truyền thông ngoài giờ làm việc.
* **Acceptance Criteria:**
  * Tài khoản Zalo Business / Premium: Mở rộng thời hạn thu hồi lên 24 giờ.
  * Không áp dụng hồi tố cho tin nhắn đã gửi trước thời điểm nâng cấp gói tài khoản.

---

## 6. Phạm Vi Triển Khai & Phân Tích Cạnh Tranh

### In-Scope (Khả thi triển khai ngay)
* Bổ sung tính toán thời gian động trên Client khi mở menu ngữ cảnh để vô hiệu hóa nút "Thu hồi" quá hạn.
* Cập nhật schema Tombstone để truyền `recalled_by_name` cho các cuộc trò chuyện nhóm.
* Bổ sung nhãn đếm lùi tĩnh dạng tooltip khi nhấn giữ tin nhắn gửi gần nhất.

### Out-of-Scope (Yêu cầu đánh giá an ninh bổ sung)
* Mở rộng vô điều kiện thời hạn thu hồi quá 1 giờ cho toàn bộ người dùng miễn phí (nguy cơ hủy hoại bằng chứng giao dịch và tranh chấp pháp lý).
* Cung cấp tính năng "Xem lịch sử chỉnh sửa" đối với tin nhắn đã thu hồi (vi phạm chính sách cam kết quyền riêng tư cốt lõi).

### Bảng So Sánh Tính Năng Thu Hồi Với Đối Thủ Cạnh Tranh

| Ứng dụng | Giới hạn thời gian thu hồi | Cơ chế hiển thị Tombstone | Đặc điểm trải nghiệm nổi bật |
| :--- | :--- | :--- | :--- |
| **Zalo** | 1 giờ (60 phút) | *"Tin nhắn đã được thu hồi"* | Icon bút chì cho phép soạn thảo lại nội dung cũ |
| **Telegram** | Không giới hạn thời gian | Xóa sạch không để lại dấu vết (hoặc *"Message deleted"*) | Cho phép xóa cả hai chiều ở mọi thời điểm |
| **WhatsApp** | Khoảng 60 giờ (2.5 ngày) | *"This message was deleted"* | Quản trị viên nhóm có quyền thu hồi tin nhắn thành viên |
| **LINE** | 24 giờ | *"Message unsent"* | Hiển thị tên người đã thu hồi trong nhóm chat |
| **Signal** | Không giới hạn thời gian | *"You deleted this message"* | Phân biệt rõ ràng giữa xóa cục bộ và xóa hai chiều |

---

## 7. Sơ Đồ Kỹ Thuật

Toàn bộ sơ đồ nghiệp vụ và kiến trúc kỹ thuật được mô hình hóa theo chuẩn phân tích hệ thống:

### Flowchart — Cây Quyết Định Thu Hồi Tin Nhắn
Mô hình hóa toàn bộ chuỗi quyết định từ thao tác nhấn giữ của người dùng, phân nhánh kiểm tra quyền sở hữu tại Client, chuyển giao xác thực thời hạn tại Server cho đến kết quả hoàn tất Soft Delete và cập nhật giao diện hai phía.

[→ Xem sơ đồ: Flowchart — Cây Quyết Định Thu Hồi Tin Nhắn](./images/flowchart-thu-hoi.png)

---

### Sequence Diagram — Luồng Kỹ Thuật Thu Hồi End-to-End
Đặc tả chi tiết chuỗi tương tác tuần tự đa bên giữa Actor người gửi, Client Zalo, API Gateway, Authentication Service, Message Store Database và WebSocket Broadcast Server tới Client người nhận. Thể hiện cơ chế Defense-in-Depth 2 lớp và cập nhật Soft Delete.

[→ Xem sơ đồ: Sequence Diagram — Luồng Kỹ Thuật Thu Hồi End-to-End](./images/sequence-thu-hoi.png)

---

### State Diagram — Vòng Đời Trạng Thái Tin Nhắn
Biểu diễn các pha chuyển đổi trạng thái của thực thể tin nhắn từ khi khởi tạo, truyền tải, hiển thị cho đến hai kịch bản xóa độc lập: Soft Delete (Thu hồi hai phía — áp dụng cờ Tombstone) và Local Delete (Xóa phía tôi — chỉ xóa bản ghi trong SQLite nội bộ thiết bị).

[→ Xem sơ đồ: State Diagram — Vòng Đời Trạng Thái Tin Nhắn](./images/state-diagram-thu-hoi.png)

---

## 8. Tài Liệu Tham Khảo & Nguồn Đối Soát

Hệ thống tài liệu tham chiếu 3 tầng đảm bảo tính xác thực và chiều sâu kỹ thuật:

### Tầng 1 — Nguồn Chính Thống Từ Zalo (VNG Corporation)

| Tài liệu tham chiếu | Nội dung nghiệp vụ xác thực |
| :--- | :--- |
| [help.zalo.me — Hướng dẫn thu hồi tin nhắn](https://help.zalo.me/huong-dan/chuyen-muc/nhan-tin-va-goi/nhan-tin/thu-hoi-tin-nhan/) | Xác thực giới hạn hiệu lực 1 giờ; hiển thị Tombstone hai phía; phân biệt giữa Thu hồi và Xóa phía tôi |
| [help.zalo.me — Quy tắc nhắn tin và gọi thoại](https://help.zalo.me/huong-dan/chuyen-muc/nhan-tin-va-goi/) | Bộ nguyên tắc vận hành tổng thể hệ thống hội thoại OTT trên nền tảng Zalo |
| [help.zalo.me — Chính sách an toàn & quyền riêng tư](https://help.zalo.me/huong-dan/chuyen-muc/bao-mat-va-rieng-tu/) | Cam kết bảo mật dữ liệu cá nhân và cơ chế quản lý dữ liệu hội thoại người dùng |

### Tầng 2 — Báo Chí & Nguồn Kiểm Thử Độc Lập

| Kênh đối chiếu | Giá trị bổ trợ phân tích |
| :--- | :--- |
| [Điện Máy Xanh — Hướng dẫn thu hồi tin nhắn Zalo](https://dienmayxanh.com/kinh-nghiem-hay/cach-thu-hoi-tin-nhan-tren-zalo-1364) | Khảo sát thực tế hành vi người dùng phổ thông; kiểm chứng giới hạn 1 giờ |
| [Viettel Store — Đánh giá tính năng thu hồi Zalo](https://viettelstore.vn/tin-tuc/cach-thu-hoi-tin-nhan-tren-zalo-don-gian-nhanh-chong.html) | Xác thực cơ chế hiển thị Tombstone và phản hồi realtime trên các phiên bản app |
| [Thế Giới Di Động — Khảo sát tính năng bảo mật Zalo](https://thegioididong.com) | Nguồn đối chiếu chéo về tính năng tin nhắn tự xóa và bảo vệ hội thoại |

### Tầng 3 — Tiêu Chuẩn Kỹ Thuật Quốc Tế & Kiến Trúc Phần Mềm

| Tiêu chuẩn / Nguyên lý | Ứng dụng thực tiễn trong Case Study |
| :--- | :--- |
| [OWASP — Access Control Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html) | Áp dụng nguyên lý Defense-in-Depth (BR2): Kiểm tra ủy quyền ở cả Client và Server |
| Martin Fowler — Patterns of Enterprise Application Architecture | Áp dụng nguyên lý Soft Delete (BR3) đảm bảo tính toàn vẹn dữ liệu trong hệ thống phân tán |
| Zalo Engineering Blog — Messaging Infrastructure | Tham khảo mô hình kiến trúc WebSocket Broadcast và đồng bộ hóa đa thiết bị |

---

## 9. Deliverables Index

Hồ sơ phân tích nghiệp vụ, tài liệu giải pháp và sơ đồ kỹ thuật được lưu trữ hoàn chỉnh trong thư mục dự án:

| Hạng mục tài liệu | Đường dẫn tham chiếu | Tóm tắt nội dung bàn giao |
| :--- | :--- | :--- |
| **Bản Ghi Chép Gốc LaTeX** | [content.tex](./content.tex) | Tài liệu nghiên cứu ban đầu và bài phân tích gốc trên LinkedIn |
| **File Thiết Kế Gốc Draw.io** | [thuhoi.drawio.xml](./diagram/thuhoi.drawio.xml) | Tệp sơ đồ Sequence Diagram nguyên bản trên nền tảng Draw.io |
| **Đặc Tả Kỹ Thuật 3 Sơ Đồ** | [thuhoi-diagrams.md](./doc/thuhoi-diagrams.md) | Bản đặc tả chi tiết logic vận hành kèm mã nguồn Mermaid gốc cho 3 sơ đồ |
| **Sơ đồ Flowchart Cây Quyết Định** | [flowchart-thu-hoi.png](./images/flowchart-thu-hoi.png) | Sơ đồ luồng quyết định kiểm tra quyền, validation 1 giờ và Soft Delete |
| **Sơ đồ Sequence Luồng Kỹ Thuật** | [sequence-thu-hoi.png](./images/sequence-thu-hoi.png) | Sơ đồ tuần tự End-to-End từ Client qua Server đến Database và Push |
| **Sơ đồ State Diagram Vòng Đời** | [state-diagram-thu-hoi.png](./images/state-diagram-thu-hoi.png) | Sơ đồ vòng đời trạng thái tin nhắn và so sánh Soft Delete vs Local Delete |

---

> ⬅️ **Quay lại trang hồ sơ cá nhân:** [Trang chủ Portfolio](../../README.md)
