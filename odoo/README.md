# Nghiên Cứu Tình Huống: Tối Ưu Vận Hành Bán Hàng & Odoo ERP

> Đánh giá dự án từ góc nhìn người phỏng vấn  
> Ứng viên: Hà Duy Hưng - Trọng tâm: Business Analyst chuyên mảng ERP và SaaS  
> Mục tiêu: Tái cấu trúc chu trình Lead-to-Order, thiết lập 14 quy tắc nghiệp vụ và giải quyết bài toán cấp điều hành  

---

## 🚀 Những Gì Đã Làm Được

### 1. Chuẩn hóa và Mô hình hóa Quy trình Nghiệp vụ
* **Quy trình Lead-to-Order với 4 làn bơi:** Phân định ranh giới trách nhiệm rõ ràng giữa Khách hàng, Nhân viên kinh doanh, Hệ thống Odoo và Quản lý bán hàng. [Xem sơ đồ quy trình Swimlane](./diagram/CRM_Lead_To_Order_Swimlane_Process.png)
* **Phân bổ Lead tự động và chống cướp khách:** Thiết lập thuật toán phân bổ xoay vòng Round-Robin kèm hạn mức 5 lead mỗi ngày cho từng nhân sự và tự động đồng bộ theo trạng thái nghỉ phép. [Xem sơ đồ phân bổ Lead và chống cướp khách](./diagram/CRM_Auto_Assignment_Anti_Poaching_Flow.png)
* **Kiến trúc Use Case hệ thống:** Xây dựng 18 ca sử dụng bao phủ 4 nhóm tác nhân, phân định minh bạch giữa tính năng tiêu chuẩn và giải pháp tùy biến may đo. [Xem sơ đồ Use Case tổng quan](./diagram/CRM_System_Use_Case_Overview.png)

### 2. Khung 14 Quy Tắc Nghiệp Vụ Cốt Lõi [Xem chi tiết tại doc/Business_Rules_Analysis.md](./doc/Business_Rules_Analysis.md)
* Đặc tả chi tiết 14 nhóm quy tắc trọng yếu: Ràng buộc tính hợp lệ của dữ liệu, công thức tính toán tự động, cổng phê duyệt nhiều cấp, ma trận bảo mật 3 cấp và cơ chế cảnh báo vượt cấp tự động.

### 3. Giải Quyết 3 Bài Toán Quản Trị Từ Cấp Điều Hành

| Tình huống thực tế | Điểm nghẽn quản trị | Giải pháp nghiệp vụ của BA | Giá trị đạt được |
| :--- | :--- | :--- | :--- |
| **Tình huống M3: Quản trị Pipeline & SLA 14 ngày** [Xem chi tiết](./doc/Case_Study_Odoo.md#case-study-1-quản-trị-pipeline-thiết-lập-sla-14-ngày--chuẩn-hóa-lý-do-thua) | Nhân viên ngâm cơ hội quá hạn làm sai lệch dự báo doanh thu, bấm đóng cơ hội thua bừa bãi không rõ lý do. | Kích hoạt cảnh báo đổi màu thẻ sau 14 ngày trên Kanban, áp dụng nguyên lý Poka-Yoke bắt buộc chọn lý do thất bại theo danh mục chuẩn. | 100% cơ hội thất bại có dữ liệu nguyên nhân, cấp quản lý nhận diện ngay điểm nghẽn bán hàng. |
| **Tình huống M4: Phân bổ tự động & Chống cướp khách** [Xem chi tiết](./doc/Case_Study_Odoo.md#case-study-2-phân-bổ-lead-tự-động-round-robin--cơ-chế-chống-cướp-khách-nội-bộ) | Tranh giành khách hàng ở khối bán lẻ, nhân viên khối doanh nghiệp giấu thông tin vào sổ tay riêng vì sợ mất khách nội bộ. | Cơ chế phân bổ xoay vòng tự động kèm hạn mức 5 lead mỗi ngày, kết hợp ma trận phân quyền 3 cấp và kỹ thuật che số điện thoại hoặc email. | Xóa bỏ xung đột giữa các nhóm kinh doanh, loại trừ hoàn toàn nguy cơ rò rỉ dữ liệu khi nhân sự nghỉ việc. |
| **Tình huống M5: Doanh thu lai & Kiểm soát deal trôi dạt** [Xem chi tiết](./doc/Case_Study_Odoo.md#case-study-3-doanh-thu-lai-và-kiểm-soát-deal-trôi-dạt-bằng-cờ-cảnh-báo) | Hợp đồng hỗn hợp vừa bán đứt vừa có phí thuê bao hàng tháng, nhân viên liên tục dời ngày chốt cơ hội sang tháng sau để né phạt chỉ tiêu. | Tách biệt hai khối dữ liệu doanh thu một lần và doanh thu định kỳ hàng tháng, thiết lập bộ đếm tự động bật cờ cảnh báo khi dời ngày chốt từ 2 lần trở lên. | Giúp Giám đốc Tài chính chủ động thanh khoản tiền mặt, cung cấp số liệu tăng trưởng doanh thu định kỳ thời gian thực. |

---

## 💡 Insight Nghiệp Vụ Thực Chiến

1. **Kỷ luật hệ thống Poka-Yoke thay vì mệnh lệnh hành chính:**  
   Mệnh lệnh nhắc nhở miệng rất dễ bị lãng quên trong vận hành thực tế. Giải pháp BA hiệu quả nhất là đưa rào chắn trực tiếp vào phần mềm: khóa nút chuyển trạng thái khi chưa điền lý do, tự động đổi màu thẻ cảnh báo khi vượt ngưỡng thời gian. Hệ thống tự động vận hành chuẩn mực mà không tiêu tốn công sức giám sát thủ công.

2. **Cân bằng tinh tế giữa vận hành mở và bảo mật dữ liệu:**  
   Trong kinh doanh B2B, nếu khóa kín dữ liệu thì nhân viên sẽ tạo trùng khách hàng và giẫm chân nhau, còn nếu mở hoàn toàn thì dễ xảy ra tình trạng cướp khách nội bộ. Ứng dụng giải pháp che dữ liệu số điện thoại và email giúp nhân viên nhận biết khách hàng đã có người chăm sóc mà vẫn bảo vệ tuyệt đối thông tin liên hệ.

3. **Minh bạch hóa doanh thu lai để bảo vệ dòng tiền:**  
   Gộp chung doanh thu triển khai một lần và doanh thu thuê bao định kỳ vào một con số tổng sẽ làm sai lệch bức tranh tài chính. Tách biệt hai luồng tiền giúp Giám đốc Tài chính chủ động nguồn vốn lưu động, đồng thời giúp Giám đốc Kinh doanh đánh giá chính xác giá trị vòng đời khách hàng.

---

## 📁 Cấu Trúc Thư Mục Lưu Trữ

```
odoo/
├── README.md                                          # Bản tổng hợp đánh giá nghiệp vụ
├── diagram/                                           # Bộ sơ đồ quy trình chất lượng cao định dạng PNG
│   ├── CRM_Lead_To_Order_Swimlane_Process.png         # Sơ đồ 4 làn bơi luồng Lead-to-Order
│   ├── CRM_Auto_Assignment_Anti_Poaching_Flow.png      # Sơ đồ phân bổ Lead và chống cướp khách
│   └── CRM_System_Use_Case_Overview.png               # Sơ đồ Use Case tổng quan phân hệ CRM
└── doc/                                               # Hồ sơ phân tích nghiệp vụ và tài liệu giải pháp
    ├── Case_Study_Odoo.md                             # Bản tổng hợp 3 tình huống thực chiến kinh điển
    ├── Business_Rules_Analysis.md                     # Cẩm nang 14 quy tắc nghiệp vụ doanh nghiệp
    ├── CRM_Architecture_ASCII.md                      # Kiến trúc phân tầng năng lực chức năng CRM
    ├── CRM_Pain_Points.md                             # Ma trận điểm đau và giải pháp khắc phục
    ├── BA_Master_Learning_Plan.md                     # Khung lộ trình năng lực chuyên viên phân tích nghiệp vụ
    ├── CRM_Learning_Progress.md                       # Nhật ký đánh giá và bảng điểm tiến độ
    └── Learning_Checklist.md                          # Danh mục kiểm tra kỹ năng thực hành
```

---

> ⬅️ **Quay lại trang hồ sơ cá nhân:** [Trang chủ Portfolio](../README.md)
