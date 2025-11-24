# Danh sách user (Vẫn y hệt bài cũ)
server_to_ip = [
    {"ip": "192.168.1.2", "ping_status": "active", },
    {"ip": "192.168.1.3", "ping_status": "inactive",},
    {"ip": "192.168.1.4", "ping_status": "active"},
    {"ip": "192.168.1.5", "ping_status": "pending"} # Thêm thử 1 người nữa
]

print("--- BẮT ĐẦU TỰ ĐỘNG HÓA ---")

for server in server_to_ip:
    # Câu lệnh IF: Nếu trạng thái là 'active' thì mới làm
    if server['ping_status'] == "active":
        print(f"[OK] Server {server['ip']} Server [IP] Online -> Backup dữ liệu")
    elif server['ping_status'] == "pending":
        print(f"[PENDING] Server {server['ip']} Server [IP] Đang chờ xử lý")
    else:
        # Câu lệnh ELSE: Các trường hợp còn lại
        print(f"[SKIP] Server {server['ip']} CẢNH BÁO: Server {server['ip']} Mất kết nối!")

print("--- HOÀN TẤT ---")