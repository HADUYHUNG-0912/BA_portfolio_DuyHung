# DAC TA SO DO QUY TRINH & KIEN TRUC: THU HOI TIN NHAN ZALO

Tai lieu nay tong hop toan bo ma nguon Mermaid va dac ta ky thuat cho 3 so do cot loi trong Case Study phan tich tinh nang Thu hoi tin nhan tren Zalo.

---

## 1. Flowchart - Cay Quyet Dinh Thu Hoi

So do mo hinh hoa toan bo luong quyet dinh tu khi nguoi dung nhan giu vao tin nhan ket thuc ket thuc ket thuc ket thuc ket thuc ket thuc check quyen so huu tai Client ket thuc ket thuc check thoi gian tai Server ket thuc ket thuc Soft Delete ket thuc ket thuc Push realtime.

```mermaid
flowchart TD
    Start((x)) --> A1["Nguoi dung nhan giu vao tin nhan trong chat"]
    A1 --> D1{"Tin nhan do chinh minh gui?"}

    D1 -->|Khong| A2["Menu hien: Xoa phia toi, Phan hoi...<br/>KHONG co Thu hoi"]
    A2 --> End1((o))

    D1 -->|Co| A3["Menu hien day du bao gom nut Thu hoi<br/>(bat ke thoi gian da qua)"]
    A3 --> A4["Nguoi dung bam Thu hoi"]
    A4 --> A5["Client gui POST /recall message_id len Server"]

    A5 --> D2{"Server kiem tra: Tin nhan gui trong vong 1 gio?"}

    D2 -->|Qua 1 gio| A6["Server tra ve: 403 TIME_EXPIRED"]
    A6 --> A7["Toast: Ban chi co the thu hoi tin nhan trong vong 1 gio"]
    A7 --> End2((o))

    D2 -->|Con trong 1 gio| D3{"Server re-validate: Dung la chu tin nhan?"}

    D3 -->|Khong| A8["Server tra ve: 403 FORBIDDEN"]
    A8 --> End3((o))

    D3 -->|Co| A9["DB: UPDATE Message SET status=Recalled - Soft Delete"]
    A9 --> A10["Server Push realtime MESSAGE_RECALLED den tat ca Client"]
    A10 --> Fork1{ }

    Fork1 --> A11["Phia nguoi gui: Tombstone + Icon but chi ✏️"]
    Fork1 --> A12["Phia nguoi nhan: Tombstone (khong co icon but chi)"]

    A11 --> End4((o))
    A12 --> End4
```

---

## 2. Sequence Diagram - Luong Ky Thuat Thu Hoi

So do mo ta chi tiet tung buoc giao tiep giua Actor, Client, Server va Database.

```mermaid
sequenceDiagram
    actor A as User A (Chu tin nhan)
    participant CA as Client A
    participant Srv as Server
    participant DB as Database
    participant M as Client B (Nguoi nhan)

    A->>CA: Nhan giu vao tin nhan

    Note over CA: BR2 - Kiem tra ownership tai Client truoc khi render menu

    alt Khong phai chu tin nhan
        CA-->>A: Menu KHONG co Thu hoi
    else La chu tin nhan
        CA-->>A: Menu CO Thu hoi (bat ke da qua bao lau)
        A->>CA: Bam Thu hoi
        activate CA

        CA->>Srv: POST /recall message_id
        activate Srv

        Note over Srv: BR1 - Kiem tra gui duoi 1 gio?

        alt Qua 1 gio
            Srv-->>CA: 403 TIME_EXPIRED
            CA-->>A: Toast: Ban chi co the thu hoi trong vong 1 gio
        else Con trong 1 gio
            Note over Srv: Defense-in-depth - Re-validate ownership
            Srv->>DB: UPDATE status=Recalled WHERE message_id
            activate DB
            DB-->>Srv: OK - Soft Delete thanh cong
            deactivate DB

            Srv-->>CA: 200 OK
            CA-->>A: Tombstone + Icon but chi ✏️ (phia nguoi gui)

            loop Push den tat ca thiet bi trong hoi thoai
                Srv->>M: WebSocket Push MESSAGE_RECALLED
                M-->>M: Cap nhat UI: Tombstone
            end
        end
        deactivate Srv
        deactivate CA
    end
```

---

## 3. State Diagram - Vong Doi Trang Thai Tin Nhan

So do mo ta toan bo cac trang thai ma mot tin nhan tren Zalo co the di qua.

```mermaid
stateDiagram-v2
    [*] --> Drafting : Nguoi dung soan thao
    Drafting --> Sending : Bam Gui
    Sending --> Sent : Server nhan thanh cong
    Sending --> Failed : Mat ket noi
    Failed --> Sending : Thu lai (Retry)
    Sent --> Delivered : Client nguoi nhan download
    Delivered --> Read : Nguoi nhan mo tin nhan

    Sent --> Recalled : Thu hoi trong 1 gio
    Delivered --> Recalled : Thu hoi trong 1 gio
    Read --> Recalled : Thu hoi trong 1 gio

    Sent --> DeletedLocal : Xoa phia toi
    Delivered --> DeletedLocal : Xoa phia toi
    Read --> DeletedLocal : Xoa phia toi
    Recalled --> DeletedLocal : Xoa ca tombstone phia toi

    DeletedLocal --> [*]
    Recalled --> [*]
```
