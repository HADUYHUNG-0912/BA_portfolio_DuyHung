# Sơ đồ Quy trình — Shopee Rewards

## 1. Quy trình Tích lũy & Xét hạng (BR-01 → BR-10)

![Quy trình Tích lũy & Xét hạng](./images/01-quy-trinh-tich-luy-xet-hang.png)

<details>
<summary><b>Xem mã nguồn Mermaid</b></summary>

```mermaid
flowchart TD
    A([👤 Người dùng Shopee]) --> B[Tự động tham gia Shopee Rewards\nBR-02: Mọi user kể từ 01/2021]

    B --> C{Đặt đơn hàng}

    C -->|Shopee thường| D[Kiểm tra loại đơn\nBR-10]
    C -->|ShopeeFood từ Quán Đối tác\nBR-03 — tính từ 01/2022| D

    D -->|❌ Đơn KHÔNG hợp lệ| E[Không tính vào tích lũy]
    E --> E1["• Voucher & Dịch vụ\n• Nạp Đấu thầu từ khóa\n• Vi phạm chính sách Shopee\n• Giao không thành công / trả hàng"]

    D -->|✅ Đơn hợp lệ| F[Giao hàng thành công]
    F --> G[Cộng vào tích lũy chu kỳ\n— số đơn + chi tiêu —]

    G --> H{Hệ thống kiểm tra\nngưỡng hạng — BR-08\ntự động, real-time}

    H -->|Chưa đủ ngưỡng nào| I[Giữ hạng Thành viên]
    H -->|≥ 3 đơn AND ≥ 1.000.000đ\nBR-05 | J[⬆️ Thăng hạng BẠC]
    H -->|≥ 20 đơn AND ≥ 5.000.000đ\nBR-06| K[⬆️ Thăng hạng VÀNG]
    H -->|≥ 75 đơn AND ≥ 15.000.000đ\nBR-07| L[⬆️ Thăng hạng KIM CƯƠNG]

    I & J & K & L --> M[Hạng được bảo lưu\nsuốt chu kỳ — BR-09]

    M --> N{Kết thúc chu kỳ 6 tháng?\nBR-04: 30/06 hoặc 31/12}

    N -->|Chưa| C
    N -->|Có — bắt đầu chu kỳ mới| O[Reset số đơn & chi tiêu về 0\nBR-04]
    O --> P[Hạng kỳ trước được 'mang sang'\nlàm hạng khởi điểm — BR-09]
    P --> C

    style A fill:#FF6033,color:#fff
    style J fill:#C0C0C0,color:#000
    style K fill:#FFD700,color:#000
    style L fill:#B9F2FF,color:#000
    style E fill:#FF4444,color:#fff
    style F fill:#44BB44,color:#fff
```
</details>

---

## 2. Quy trình Nhắc Ngưỡng Hạng — Giải pháp PP-09

![Quy trình Nhắc Ngưỡng Hạng](./images/02-sequence-nhac-nguong-hang-pp09.png)

<details>
<summary><b>Xem mã nguồn Mermaid</b></summary>

```mermaid
sequenceDiagram
    actor User as 👤 Khách hàng
    participant App as 📱 App Shopee
    participant BE as ⚙️ Backend / Logic hạng
    participant Cart as 🛒 Giỏ hàng & Checkout

    Note over BE: Dữ liệu sẵn có: tích lũy hiện tại,<br/>ngưỡng hạng tiếp theo (BR-05/06/07)

    User->>App: Mở màn hình "Khách hàng thân thiết"

    App->>BE: GET tiến độ tích lũy
    BE-->>App: { đơn_hiện_tại, chi_tiêu_hiện_tại,<br/>đơn_còn_thiếu, chi_tiêu_còn_thiếu }

    alt Gần ngưỡng tiếp theo (≤1 đơn HOẶC ≤10% giá trị)
        App-->>User: 🔔 Điểm chạm 1 — Hiển thị tiến độ ngôn ngữ hành động<br/>"Chỉ cần thêm 1 đơn nữa để lên hạng Vàng!" + gợi ý sản phẩm
    else Chưa gần ngưỡng
        App-->>User: Hiển thị số liệu thô (đơn / chi tiêu)
    end

    User->>Cart: Thêm sản phẩm vào giỏ & tiến hành thanh toán

    Cart->>BE: Kiểm tra: đơn này có đủ đưa user vượt ngưỡng?
    BE-->>Cart: Kết quả so sánh

    alt Đơn này giúp user vượt ngưỡng hạng
        Cart-->>User: 🔔 Điểm chạm 2 — Nhắc tại Checkout<br/>"Đơn này sẽ đưa bạn lên hạng Bạc!"
    end

    User->>App: Vào trang chủ (trong giai đoạn gần ngưỡng)

    alt Gần ngưỡng VÀ chưa hiển thị hôm nay
        App-->>User: 🔔 Điểm chạm 3 — Thẻ nhỏ không chặn trên trang chủ<br/>(tối đa 1 lần/ngày, có nút Đóng)
    end

    User->>Cart: Đặt đơn thành công
    Cart->>BE: Cập nhật tích lũy
    BE-->>App: Hạng mới (nếu có)
    App-->>User: 🎉 Thông báo thăng hạng (nếu đủ điều kiện)
    Note over App: Tắt thẻ nhỏ trang chủ — BR-08 tự động thăng hạng
```
</details>

---

## 3. Quy trình Chuỗi Mua Sắm Thưởng Thêm — Giải pháp PP-10

![Quy trình Chuỗi Mua Sắm Thưởng Thêm](./images/03-chuoi-mua-sam-thuong-them-pp10.png)

<details>
<summary><b>Xem mã nguồn Mermaid</b></summary>

```mermaid
flowchart LR
    subgraph MAIN ["🏅 Hệ thống Hạng Chính (không đổi — BR-09)"]
        direction TB
        M1[Hạng hiện tại\nBạc / Vàng / Kim Cương] --> M2[Bảo lưu đến hết chu kỳ]
        M2 --> M3[Reset đầu chu kỳ mới]
    end

    subgraph STREAK ["🔥 Lớp Mục tiêu Phụ Độc lập — Chuỗi Mua Sắm"]
        direction TB
        S1([Bắt đầu chu kỳ 6 tháng]) --> S2{Tháng 1\nCó đơn hợp lệ?}
        S2 -->|Có ✅| S3[Tháng 1: ✅ Hoàn thành]
        S2 -->|Không ❌| S4[Tháng 1: ❌ Bỏ lỡ]
        S3 & S4 --> S5{Tháng 2\nCó đơn hợp lệ?}
        S5 -->|Có ✅| S6[Tháng 2: ✅ Hoàn thành]
        S5 -->|Không ❌| S7[Tháng 2: ❌ Bỏ lỡ]
        S6 & S7 --> S8[... Tháng 3 → 6 ...\ncùng logic]
        S8 --> S9[Tổng kết cuối chu kỳ\nX/6 tháng hoàn thành]
    end

    subgraph UI ["📱 Màn hình Khách hàng thân thiết"]
        direction TB
        U1[Khu vực Hạng chính thức\n— không đổi —]
        U2[Khu vực Chuỗi mua sắm thưởng thêm\n— tách biệt, mới thêm —\n🗓️ T1✅ T2✅ T3❌ T4... T5... T6...]
    end

    MAIN -.->|Hiển thị riêng| U1
    STREAK -.->|Hiển thị riêng| U2

    note1[/"Đơn hợp lệ theo đúng BR-10\n(không giao thành công / trả hàng\nkhông được tính)"/]
    S2 -. kiểm tra theo BR-10 .- note1

    style MAIN fill:#FFF3CD,stroke:#FFC107
    style STREAK fill:#D4EDDA,stroke:#28A745
    style UI fill:#D1ECF1,stroke:#17A2B8
```
</details>



---

> **Ghi chú nguồn:**
> - BR-05, BR-06: điều kiện AND/OR còn **xung đột nguồn** (chưa giải quyết). Sơ đồ dùng AND theo xác nhận nhân viên hỗ trợ Shopee.
> - BR-07: AND — nhất quán mọi nguồn, độ tin cậy Cao.
> - BR-08: thăng hạng tự động, không cần thao tác người dùng.
> - PP-09 & PP-10: giải pháp đề xuất, chưa triển khai — không thay đổi BR-01 đến BR-09.
