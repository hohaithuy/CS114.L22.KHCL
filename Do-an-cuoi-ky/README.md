# **Tóm tắt đồ án máy học: Nhận biết đeo khẩu trang đúng cách**
# Danh sách thành viên
---
- Hồ Hải Thủy - 19522323 <Nhóm trưởng>
- Nguyễn Khả Tiến - 19522337
- Nguyễn Mạnh Toàn - 19522363
# Mô tả
---
Bài toán được áp dụng trên camera an ninh. Vậy nên, ta trích xuất dữ liệu từ camera bao gồm các đoạn video. Mà video lại là một tập hợp từ các ảnh, vậy nên nhiệm vụ chính của chúng ta đó chính là xử lý ảnh và đưa ra các kết quả về các đối tượng.
- Input: 1 bức ảnh được trích xuất từ camera.
- Output: 1 bức ảnh đánh dấu những đối tượng trong bức ảnh đó có đeo khẩu trang đúng cách hay không.
Khi đó việc xử lý liên tục các bức ảnh theo thứ tự, khi ghép lại thành một đoạn video hoàn chỉnh ta có thể hiển thị cảnh báo một cách rõ ràng và dễ sử dụng với người dùng.
# Thống Kê Dữ liệu
---
Bộ dữ liệu sau khi được gán nhãn để sử dụng cho mô hình bao gồm 3725 hình ảnh định dạng .png, 3725 file chú thích .txt làm label cho ảnh
+ Bộ dữ liệu được chia với tỉ lệ 70/20/10 tương ứng với các tập train/validation/test.
+ Thống kê bộ dữ liệu
  + Bộ dữ liệu ở kho giao hàng tiết kiệm gồm 878 hình, 2665 object mask và 633 object no_mask.
  + Bộ dữ liệu ở quán cafe gồm 1282 hình, 672 object mask và 3888 object no_mask.
  + Bộ dữ liệu ở nơi công cộng gồm 2106 hình, 1230 object mask và 876 object no_mask.
  + Bộ dữ liệu ở nơi công cộng được chỉnh sáng tối gồm 1252 hình, 2460 object mask và1752 object no_mask.
+ Quyền sử dụng data: Đã được cấp phép <Vì vấn đề bảo mật nên bọn em xin được nói riêng với thầy ạ>
+ Link tổng hợp data: https://drive.google.com/drive/folders/15scSAR-3FqXaA2Cx6xHINRObkBjHpJ0t
+ Linh bộ test mới để đánh giá model: https://drive.google.com/drive/folders/1rlPZ3gncHxcZ1ue7CPu3uQurBBdMNwvF?usp=sharing 
## CÁC THAY ĐỔI So với lần báo cáo
---
- Thống kê và minh hoạ lại chi tiết các bộ dữ liệu từ tổng quát cho đến chi tiết các ảnh khó xử lý
- Thêm minh họa cho các trường hợp dự đoán của model trong từng giai đoạn
- Chỉnh sửa tiêu chí thu nhập dữ liệu
- Thêm các nguồn tham khảo
