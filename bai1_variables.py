# --- PHẦN 1: KHAI BÁO BIẾN (CONFIGURATION) ---
server_name = "WebServer-01"    # Kiểu String (Chuỗi)
ip_address = "10.0.0.5"         # Kiểu String (IP cũng là chuỗi)
port = 22                     # Kiểu Integer (Số)
maintenance_mode = False        # Kiểu Boolean (Đúng/Sai)

# --- PHẦN 2: XỬ LÝ (LOGIC) ---
print("--- HỆ THỐNG QUẢN TRỊ SERVER ---")

# Dùng f-string để in thông báo cấu hình
print(f"Đang kiểm tra máy chủ: {server_name}")
print(f"Kết nối tới IP: {ip_address} qua cổng {port}")

# Kiểm tra trạng thái bảo trì
print(f"Chế độ bảo trì đang bật? {True}")

print("--------------------------------")
print("Cấu hình thành công! Server đã sẵn sàng.")
