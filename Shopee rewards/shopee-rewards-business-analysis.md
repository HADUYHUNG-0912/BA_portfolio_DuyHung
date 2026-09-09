# Tài liệu mô tả nghiệp vụ — Chương trình Shopee Rewards

## 1. Tổng quan chương trình

Shopee Rewards là chương trình khách hàng thân thiết áp dụng cho toàn bộ người dùng Shopee, xếp hạng theo hành vi mua sắm tích lũy trong từng chu kỳ 6 tháng. Có 4 hạng: Thành viên (mặc định), Bạc, Vàng, Kim Cương.

## 2. Business Rules (BR-01 đến BR-10)

| ID | Mô tả | Nguồn | Độ tin cậy |
|---|---|---|---|
| BR-01 | Thứ hạng được tính dựa trên số đơn hàng và/hoặc chi tiêu tích lũy trong mỗi chu kỳ cố định 6 tháng, không phải cửa sổ trượt liên tục. | shopee.vn/blog | Cao |
| BR-02 | Mọi người dùng Shopee tự động là thành viên chương trình kể từ 1/2021, không cần đăng ký. | help.shopee.vn | Cao |
| BR-03 | Đơn hàng ShopeeFood (từ "Quán Đối tác") được tính điểm vào Shopee Rewards kể từ 1/2022, nếu giao hàng thành công. | help.shopee.vn | Cao |
| BR-04 | Chu kỳ xét hạng cố định 2 lần/năm: 01/01–30/06 và 01/07–31/12. Đầu mỗi chu kỳ, số đơn và chi tiêu tích lũy reset về 0. | shopee.vn/blog | Cao |
| BR-05 | Hạng Bạc: đạt 3 đơn hàng và 1.000.000đ chi tiêu. Có ghi nhận mâu thuẫn nguồn về việc là điều kiện OR hay AND (blog/video nói OR; nhân viên hỗ trợ Shopee xác nhận là AND). | shopee.vn/blog + video (OR) vs. hỗ trợ Shopee (AND) | Trung bình — xung đột nguồn chưa giải quyết |
| BR-06 | Hạng Vàng: đạt 20 đơn hàng và 5.000.000đ chi tiêu. Cùng tình trạng mâu thuẫn nguồn như BR-05. | shopee.vn/blog + video (OR) vs. hỗ trợ Shopee (AND) | Trung bình — xung đột nguồn chưa giải quyết |
| BR-07 | Hạng Kim Cương: bắt buộc đạt CẢ 75 đơn hàng VÀ 15.000.000đ chi tiêu (AND, nhất quán ở mọi nguồn). | shopee.vn/blog + fptshop + video + hỗ trợ Shopee | Cao |
| BR-08 | Hệ thống thăng hạng tự động ngay khi tài khoản đạt đủ điều kiện, không cần người dùng thao tác. | shopee.vn/blog + video | Cao |
| BR-09 | Thứ hạng được bảo lưu trong suốt chu kỳ hiện tại. Sang chu kỳ mới, hạng khởi điểm được tính lại dựa trên kết quả tích lũy của chu kỳ vừa kết thúc (hạng được "mang sang" dù số liệu tích lũy đã về 0). | shopee.vn/blog | Cao |
| BR-10 | 4 nhóm đơn hàng không được tính vào tích lũy: (1) Đơn Voucher & Dịch vụ, (2) Đơn nạp Đấu thầu từ khóa (quảng cáo shop), (3) Đơn vi phạm chính sách Shopee, (4) Đơn giao không thành công hoặc trả hàng/hoàn tiền. | help.shopee.vn + shopee.vn/blog | Cao |

## 3. Pain Points

### PP-09: Thiếu nhắc nhở "gần đạt hạng" (near-threshold nudge)

**Mô tả**: Hệ thống không có cơ chế chủ động nhắc khách hàng khi họ gần đạt ngưỡng lên hạng (ví dụ: "chỉ còn thiếu 2 đơn nữa là lên Vàng"). Màn hình hiện tại chỉ hiển thị số liệu thô (đơn hàng, chi tiêu), không có gợi ý hành động cụ thể.

**Root cause**: Thiếu tính năng nhắc theo ngưỡng cá nhân hóa (personalized threshold notification). Hệ thống tính hạng hiện tại vận hành theo cơ chế thụ động — chỉ tính lại khi có giao dịch mới, chưa có lớp chủ động theo dõi khoảng cách còn thiếu đến ngưỡng để kích hoạt nhắc nhở.

**Bằng chứng hỗ trợ**: Khảo sát nhanh với nhóm khách hàng mua sắm thường xuyên cho thấy phần lớn không nhớ từng nhận thông báo dạng này; khi được hỏi giả định, phần lớn cho biết sẽ mua thêm ngay nếu biết mình gần đạt ngưỡng.

**Tác động kinh doanh**: Bỏ lỡ đúng khoảnh khắc khách hàng dễ ra quyết định mua thêm nhất — cơ hội tăng doanh thu bị bỏ trống.

### PP-10: Mất động lực "leo hạng" giữa chu kỳ do cơ chế bảo lưu hạng

**Mô tả**: Cơ chế bảo lưu hạng trong suốt chu kỳ (BR-09) khiến khách hàng mất động lực "leo hạng" ngay sau khi đạt được ngưỡng mong muốn, vì hạng đã chắc chắn giữ nguyên đến hết chu kỳ dù không mua thêm — không còn mục tiêu cụ thể để phấn đấu.

**Root cause**: Cấu trúc rule chỉ có 1 mục tiêu duy nhất (đạt hạng), không có mục tiêu phụ nối tiếp trong cùng chu kỳ. Khi mục tiêu duy nhất đã đạt, động lực biến mất ngay lập tức — đây là hệ quả cấu trúc, không phải lỗi vận hành.

**Bằng chứng hỗ trợ**: Khảo sát nhanh (n nhỏ) cho thấy nhóm khách hàng mua theo nhu cầu thực tế không bị ảnh hưởng bởi cơ chế này; pain point có khả năng chỉ đúng với phân khúc khách hàng mua có mục đích leo hạng (status-driven), cần thêm dữ liệu để xác nhận quy mô ảnh hưởng.

**Tác động kinh doanh**: Khoảng trống động lực (motivation gap) ở giữa chu kỳ, có khả năng làm giảm tần suất mua sắm ở nhóm khách hàng giá trị cao (những người theo đuổi mục tiêu hạng).

## 4. Scope giải quyết

### PP-09

- **In-scope**: Logic tính khoảng cách còn thiếu đến ngưỡng tiếp theo (dựa trên BR-05/06/07); thiết kế nội dung và thời điểm nhắc; thiết kế màn hình hiển thị tiến độ.
- **Out-of-scope**: Hạ tầng gửi push notification; chi phí vận hành gửi thông báo hàng loạt; tích hợp hệ thống CRM/marketing automation nội bộ của Shopee.
- **Ràng buộc**: Không thay đổi BR-01 đến BR-08 (chỉ thêm lớp thông báo, không sửa cách tính hạng); không gây spam/làm phiền.

### PP-10

- **In-scope**: Thiết kế lớp mục tiêu phụ hoạt động song song, không thay thế BR-09; xác định mốc theo dõi; thiết kế hiển thị tiến độ.
- **Out-of-scope**: Thay đổi cơ chế carry-over hạng gốc (BR-09); ngân sách khuyến mãi cho phần thưởng (thuộc quyết định Marketing/Finance).
- **Ràng buộc**: Không được lấy đi bất kỳ quyền lợi nào khách đã đạt được; giải pháp phải độc lập với BR-09, không sửa logic gốc.

## 5. Đề xuất giải pháp

### Giải pháp cho PP-09 (3 điểm chạm)

1. **Cải tiến hiển thị tiến độ hạng**: Trong màn hình "Khách hàng thân thiết" hiện có, hiển thị khoảng cách còn thiếu bằng ngôn ngữ hành động cụ thể (ví dụ "chỉ cần thêm 1 đơn nữa để lên hạng Vàng") kèm gợi ý sản phẩm để hoàn tất điều kiện. Tận dụng dữ liệu và API đã có, không cần hệ thống mới.
2. **Nhắc nhở tại checkout**: Nếu đơn hàng hiện tại đủ để đưa khách vượt ngưỡng lên hạng tiếp theo, hiển thị một dòng nhắc ngay tại bước thanh toán. Xử lý bằng so sánh đồng bộ ngay trong luồng tính giỏ hàng.
3. **Thẻ nhỏ không chặn ở trang chủ**: Chỉ hiện khi khách rất gần ngưỡng (còn ≤1 đơn hoặc ≤10% giá trị), tối đa 1 lần/ngày trong giai đoạn gần ngưỡng, có nút đóng, tự động dừng khi đã lên hạng.

**Lý do lựa chọn**: Cả ba điểm chạm nằm trong phạm vi thiết kế nghiệp vụ, không cần đầu tư hạ tầng kỹ thuật mới; tuân thủ nguyên tắc không gây phiền (chỉ hiện đúng lúc, đúng ngữ cảnh); tận dụng đúng nguyên tắc hành vi tiêu dùng (thông điệp hiệu quả nhất khi xuất hiện đúng lúc khách sẵn sàng ra quyết định).

### Giải pháp cho PP-10 (2 phần)

1. **Lớp mục tiêu phụ độc lập ("Chuỗi mua sắm thưởng thêm")**: Theo dõi hoạt động mua sắm theo từng tháng trong chu kỳ, tách biệt hoàn toàn khỏi hệ thống tính hạng chính. Mỗi khi khách hàng có đơn hàng hợp lệ (theo đúng BR-10), ghi nhận tháng đó là "đã hoàn thành" trong chuỗi.
2. **Hiển thị tiến độ trên giao diện**: Bổ sung khu vực riêng trên màn hình "Khách hàng thân thiết", hiển thị tiến độ chuỗi mua sắm thưởng thêm, tách biệt rõ với phần hiển thị hạng chính thức.

**Lý do lựa chọn**: Không ảnh hưởng đến cơ chế carry-over hạng đã ổn định (BR-09); tạo mục tiêu mới, riêng biệt để khách hàng tiếp tục phấn đấu; có thể thử nghiệm/điều chỉnh độc lập mà không ảnh hưởng trải nghiệm cốt lõi.

**Lưu ý về chi phí**: Giải pháp trên chưa bao gồm cơ chế phát thưởng cụ thể (voucher, hoàn tiền) để tránh chi phí khuyến mãi liên tục, khó dự toán trước, và vượt phạm vi quyết định của phân tích nghiệp vụ (cần Marketing/Finance phê duyệt ngân sách). Đây nên được xem là bước triển khai ban đầu (đo lường và quan sát hành vi), làm cơ sở dữ liệu để đề xuất cơ chế phần thưởng phù hợp ở giai đoạn sau. Rủi ro đi kèm: nếu chỉ dừng ở theo dõi/hiển thị mà không có bất kỳ hình thức ghi nhận nào, động lực thực tế duy trì hành vi có thể không đủ mạnh.

## 6. Ràng buộc chung xuyên suốt

- Không sửa đổi các Business Rule đã ổn định (BR-01 đến BR-09) khi triển khai giải pháp cho PP-09 và PP-10.
- Mọi giải pháp mới phải có khả năng triển khai/thử nghiệm độc lập (feature flag), không ảnh hưởng đến chương trình Shopee Rewards gốc nếu cần tắt hoặc điều chỉnh.
- Nguyên tắc xuyên suốt: không lấy đi quyền lợi khách hàng đã có được; chỉ thêm cơ chế hỗ trợ/động viên mới.
