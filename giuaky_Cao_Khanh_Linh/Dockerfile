FROM alpine:latest

# Tạo thư mục 105463
RUN mkdir -p /105463

# Tạo file 105463-txt với nội dung yêu cầu bên trong thư mục vừa tạo
RUN echo "cao Khánh Linh" > /105463/105463-txt

# Đặt thư mục làm việc mặc định (tùy chọn)
WORKDIR /105463

# Lệnh hiển thị nội dung file khi chạy container (tùy chọn để kiểm tra)
CMD ["cat", "105463-txt"]
