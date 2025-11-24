# Một danh sách (List) chứa các từ điển (Dict) bên trong
# Đây là cấu trúc dữ liệu phổ biến nhất thế giới DevOps
users_to_create = [
    {"username": "dev_huy", "role": "admin", "shell": "/bin/bash"},
    {"username": "test_user", "role": "guest", "shell": "/bin/false"},
    {"username": "deploy_bot", "role": "service", "shell": "/bin/sh"}
]

print("--- BẮT ĐẦU QUY TRÌNH TẠO USER ---")

# Lấy user đầu tiên ra (vị trí số 0)
user_1 = users_to_create[0]
print(f"1. Tạo user: {user_1['username']}")
print(f"   - Quyền hạn: {user_1['role']}")
print(f"   - Shell mặc định: {user_1['shell']}")

# Lấy user thứ hai ra (vị trí số 1)
user_2 = users_to_create[1]
print(f"2. Tạo user: {user_2['username']}")
print(f"   - Quyền hạn: {user_2['role']}")
print(f"   - Shell mặc định: {user_2['shell']}")
# --- Bài tập nhỏ: Bạn hãy tự viết lệnh print để
#  in ra 'role' của user_2 ở đây ---
user_3 = users_to_create[2]
print(f"3. Tạo user: {user_3['username']}")
print(f"   - Quyền hạn: {user_3['role']}")
print(f"   - Shell mặc định: {user_3['shell']}")
print("--- KẾT THÚC QUY TRÌNH TẠO USER ---")
