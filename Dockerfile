# 1. Chọn nền tảng (Giống như chọn HĐH Windows hay Linux)
# Ở đây ta chọn Python phiên bản nhỏ gọn (slim) để nhẹ máy
FROM python:3.9-slim

# 2. Tạo thư mục làm việc bên trong cái hộp
WORKDIR /app

RUN apt-get update && apt-get install -y iputils-ping
# 3. Copy toàn bộ code từ máy thật vào trong hộp
COPY . .

# 4. Quy định lệnh sẽ chạy khi mở hộp ra
# (Tương đương lệnh: python final_tool.py)
CMD ["python", "final_tool.py"]