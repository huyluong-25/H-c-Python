import subprocess
import datetime
import platform

servers = ["google.com", "10.251.0.30", "192.168.1.2", "192.168.1.3","10.251.0.1","10.251.0.10","10.251.0.55","10.10.10.6","192.168.1.1"] # Đã thêm IP lỗi để test
filename = "baocao.txt"

param = "-n" if platform.system().lower() == "windows" else "-c"

print(f"--- ĐANG QUÉT TRÊN HỆ ĐIỀU HÀNH: {platform.system()} ---")

with open(filename, "w", encoding="utf-8") as f:
    time_now = datetime.datetime.now()
    header = f"BÁO CÁO HỆ THỐNG - Lúc: {time_now}\n------------------------------------------\n"
    f.write(header)
    
    for host in servers:
        command = f"ping {param} 1 {host}"
        
        # Chú ý: text=True để kết quả trả về là dạng chữ (String) thì mới tìm kiếm được
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # --- ĐOẠN CODE NÂNG CẤP ---
        # Lấy toàn bộ chữ mà lệnh ping in ra, đổi thành chữ thường để dễ so sánh
        output_text = result.stdout.lower()
        
        # Logic mới: Phải vừa không lỗi (code 0) VÀ phải tìm thấy chữ "ttl="
        if result.returncode == 0 and ("ttl=" in output_text):
            status = "ONLINE"
            icon = "✅"
        else:
            status = "OFFLINE"
            icon = "❌"
        # ---------------------------
            
        line = f"{icon} Server: {host} -> Trạng thái: {status}"
        print(line)
        f.write(line + "\n")

print("------------------------------------------")