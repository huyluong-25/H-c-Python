import subprocess # 1. Gọi thư viện subprocess

# Địa chỉ cần kiểm tra (Thử google.com hoặc 8.8.8.8)
host = "10.251.0.30"

print(f"--- Bắt đầu kiểm tra kết nối tới {host} ---")

# 2. Xây dựng câu lệnh (Giống hệt gõ trong CMD)
# Lưu ý: Trên Windows dùng "-n", trên Linux/Mac dùng "-c"
command = f"ping -n 4 {host}"

# 3. Chạy lệnh
# shell=True nghĩa là: "Hãy mở CMD lên và chạy lệnh này cho tôi"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print("--------------------------------")
# 4. Kiểm tra kết quả (returncode)
# returncode == 0 nghĩa là lệnh chạy ngon (Thành công)
if result.returncode == 0:
    print(f"✅ KẾT QUẢ: Server {host} đang ONLINE!")
else:
    print(f"❌ KẾT QUẢ: Server {host} không phản hồi (OFFLINE)!")
    print("   -> Chi tiết lỗi:", result.stderr)
    