# ĐẶC TẢ SƠ ĐỒ QUY TRÌNH & KIẾN TRÚC: TIN NHẮN TỰ XÓA ZALO

Tài liệu này tổng hợp toàn bộ mã nguồn Mermaid và đặc tả kỹ thuật cho 3 sơ đồ cốt lõi trong Case Study Tối ưu Tính năng Tin nhắn Tự xóa trên Zalo.

---

## 1. Flowchart Vòng Đời Tin Nhắn Tự Xóa (End-to-End Lifecycle)

Sơ đồ mô hình hóa toàn diện luồng vận hành từ khi người dùng kích hoạt tính năng, đồng bộ cấu hình, gắn nhãn TTL, lưu trữ Local DB hai phía đến khi dọn dẹp xóa sạch dữ liệu vĩnh viễn.

```mermaid
flowchart TD
    Start((●)) --> A1["Người dùng kích hoạt<br/>Tin nhắn tự xóa<br/>(1/7/30 ngày hoặc 5p/1h)"]
    A1 --> A2["Zalo Server ghi nhận<br/>cấu hình hội thoại"]
    A2 --> A3["Server đồng bộ cấu hình<br/>sang thiết bị người nhận (BR8)"]
    A3 --> A4["Hiển thị thông báo hệ thống<br/>cho cả 2 bên trong khung chat (BR6)"]
    A4 --> A5["Người gửi soạn thảo<br/>và bấm gửi tin nhắn"]
    A5 --> D1{Tin nhắn gửi SAU<br/>khi bật tính năng?}

    D1 -->|Sai: Tin nhắn cũ| A6["Giữ nguyên tin nhắn cũ<br/>KHÔNG áp dụng TTL<br/>(BR4 - Không hồi tố)"]
    A6 --> End1((◉))

    D1 -->|Đúng| A7["Server gán nhãn TTL<br/>tính từ thời điểm GỬI (BR1)"]
    A7 --> Fork1{ }

    Fork1 --> A8["Lưu tin nhắn + TTL<br/>vào Local DB người gửi"]
    Fork1 --> A9["Đẩy tin nhắn + TTL<br/>lưu vào Local DB người nhận"]

    A8 --> Join1{ }
    A9 --> Join1

    Join1 --> A10["Hiển thị tin nhắn kèm<br/>biểu tượng đồng hồ đếm ngược"]
    A10 --> D2{Đã hết hạn TTL?}

    D2 -->|Chưa hết hạn| A10
    D2 -->|Đã hết hạn| Fork2{ }

    Fork2 --> A11["Tự động xóa tin khỏi<br/>Local DB người gửi"]
    Fork2 --> A12["Tự động xóa tin khỏi<br/>Local DB người nhận"]

    A11 --> Join2{ }
    A12 --> Join2

    Join2 --> A13["Xác nhận xóa vĩnh viễn<br/>Không hỗ trợ khôi phục (BR7)"]
    A13 --> End1
```

---

## 2. Sequence Diagram Kiểm Soát Chụp Màn Hình & Chống Rò Rỉ (Anti-Leak Flow)

Sơ đồ đặc tả cơ chế phòng vệ rò rỉ đa tầng (PP3): xử lý chặn chụp màn hình trên Android (`FLAG_SECURE`) và cơ chế phát hiện / gửi thông báo cảnh báo leo thang trên iOS (`UIScreen.capturedDidChangeNotification`).

```mermaid
sequenceDiagram
    autonumber
    actor Sender as Người gửi (Sender)
    participant S_App as Zalo App (Sender)
    participant Server as Zalo Backend Server
    participant R_App as Zalo App (Receiver)
    actor Receiver as Người nhận (Receiver)

    Note over Sender,Receiver: Kích hoạt chế độ Tin nhắn Tự xóa trong hội thoại
    Sender->>S_App: Soạn và gửi tin nhắn nhạy cảm
    S_App->>Server: SendMessage(payload, is_ephemeral=true, ttl=300s)
    Server->>R_App: PushMessage(payload, is_ephemeral=true, ttl=300s)
    
    rect rgb(240, 248, 255)
    Note over R_App: Thiết lập rào chắn UI bảo mật
    R_App->>R_App: Khóa menu Chuyển tiếp (Forward) & Sao chép (Copy)
    end

    alt Nền tảng Android (Kích hoạt FLAG_SECURE)
        R_App->>R_App: Window.setFlags(FLAG_SECURE)
        Receiver->>R_App: Thao tác Chụp màn hình (Power + Vol Down)
        R_App-->>Receiver: Hệ điều hành chặn chụp (Màn hình đen / Báo lỗi bảo mật)
    else Nền tảng iOS (Lắng nghe sự kiện chụp màn hình)
        Receiver->>R_App: Thao tác Chụp màn hình (Side + Vol Up)
        R_App->>R_App: Bắt sự kiện userDidTakeScreenshotNotification
        R_App->>Server: EmitSecurityEvent(type=SCREENSHOT_DETECTED, chat_id)
        Server->>S_App: PushSystemAlert("⚠️ Người nhận vừa chụp màn hình cuộc trò chuyện")
        Server->>R_App: RenderSystemAlert("⚠️ Bạn vừa chụp ảnh màn hình cuộc trò chuyện này")
        S_App-->>Sender: Hiển thị cảnh báo trực quan trong khung chat
    end

    Note over S_App,R_App: Hết hạn TTL (300 giây)
    par Xóa dữ liệu cục bộ hai phía
        S_App->>S_App: Xóa bản ghi khỏi Local SQLite người gửi
    and
        R_App->>R_App: Xóa bản ghi khỏi Local SQLite người nhận
    end
```

---

## 3. Solution Architecture Luồng Đồng Bộ TTL Cho Nhóm Chat (Group Ephemeral Flow)

Sơ đồ mô hình hóa kiến trúc phân tán đồng bộ thời gian sống (TTL) cho nhóm chat quy mô nhỏ (<20 thành viên), bao gồm cơ chế kiểm soát thành viên vào/rời nhóm để tránh rò rỉ dữ liệu lịch sử.

```mermaid
flowchart TD
    subgraph Group_Admin_Action ["1. Thiết lập Cấu hình Nhóm"]
        G1["Trưởng nhóm bật Tin nhắn tự xóa<br/>cho Nhóm chat (<20 thành viên)"]
        G2["Group Policy Service<br/>ghi nhận TTL áp dụng"]
        G1 --> G2
    end

    subgraph Server_Broadcast ["2. Broadcast & Phân phối Tin nhắn"]
        G2 --> G3["Thành viên gửi tin nhắn mới"]
        G3 --> G4["Server đính kèm nhãn TTL + timestamp<br/>vào Message Packet"]
        G4 --> G5["Broadcast tin nhắn tới tất cả<br/>Active Members trong nhóm"]
    end

    subgraph Member_Handling ["3. Đồng bộ & Hiển thị trên Thiết bị"]
        G5 --> M1["Member A (Local SQLite)"]
        G5 --> M2["Member B (Local SQLite)"]
        G5 --> M3["Member N (Local SQLite)"]
    end

    subgraph Lifecycle_Edge_Cases ["4. Xử lý Trường hợp Ngoại lệ (Edge Cases)"]
        EC1["Thành viên rời nhóm"] -->|"Tin cũ đã nhận"| EC1_Action["Giữ nguyên TTL gốc<br/>Tự xóa khi hết hạn trên máy"]
        EC2["Thành viên mới gia nhập"] -->|"Lịch sử chat cũ"| EC2_Action["Query Filter: created_at >= join_time<br/>Ẩn 100% tin tự xóa cũ"]
    end

    subgraph DB_Clean_Daemon ["5. Cơ chế Tự Dọn dẹp (Auto-Purge)"]
        M1 --> D_Check{"Đồng hồ TTL chạm mốc 0?"}
        M2 --> D_Check
        M3 --> D_Check
        D_Check -->|Đúng| Purge["Background Cleanup Worker:<br/>DELETE FROM messages WHERE id = msg_id"]
        Purge --> Done((◉ Xóa vĩnh viễn))
    end
```
