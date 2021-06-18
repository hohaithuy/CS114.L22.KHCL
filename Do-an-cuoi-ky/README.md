# **Đồ án máy học: Nhận biết đeo khẩu trang đúng cách**


Input: 1 bức ảnh được chuyển về dạng ma trận số
Output: Xuất ra 1 hoặc 0 tương ứng với việc người đó đeo khẩu trang đúng cách hay k

Dữ liệu:
Cách thức xây dựng: Thu nhập các ảnh về người trên mạng và thực tế
+ Ảnh: người đeo khẩu trang, người đeo khẩu trang sai cách, người không đeo khẩu trang, các hình ảnh không phải là con người.
+ Nguồn: - Từ trên mạng(Google ảnh), kaggle, cắt từ video
		- Từ thực tế: Tự chụp ảnh bản thân bằng camera
		- Cắt từ video: Xin từ một số camera
+ Số lượng: - Chưa có câu trả lời <Dự kiến 2 nghìn tấm ảnh>
+ Train/dev/test: 60/20/20

Mô tả đặc trưng:
+ feature engineering: object detection, tức là tìm cái khung chứa vật thể chúng ta cần dự đoán

đây là bài toán nhận dạng khuôn mặt, chúng ta cần tìm được vị trí các khuôn mặt trong ảnh và crop các khuôn mặt đó trước khi làm các bước tiếp theo. Ngay cả khi đã xác định được các khung chứa các khuôn mặt (và có thể resize các khung đó về cùng một kích thước), ta vẫn phải làm rất nhiều việc nữa vì hình ảnh của khuôn mặt còn phụ thưộc vào góc chụp, ánh sáng, … và rất nhiều yếu tố khác nữa.


Phát triển tương lai: Nhận biết thêm khoảng cách an toàn giữa mọi người




