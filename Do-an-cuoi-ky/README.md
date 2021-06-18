# **Đồ án máy học: Nhận biết đeo khẩu trang đúng cách**

## Mô tả

Input: 1 bức ảnh được chuyển về dạng ma trận số
Output: Xuất ra 1 hoặc 0 tương ứng với việc người đó đeo khẩu trang đúng cách hay k

Dữ liệu:
Cách thức xây dựng: Thu nhập các ảnh về người trên mạng và thực tế

+ Ảnh: người đeo khẩu trang, người đeo khẩu trang sai cách, người không đeo khẩu trang, các hình ảnh không phải là con người.
+ Nguồn: Ảnh được lấy từ camera an ninh tại hai vị trí:
  + Chi nhánh giao hàng tiết kiệm
  + Quán cafe
+ Quyền sử dụng data: Đã được cấp phép <Vì vấn đề bảo mật nên bọn em xin được nói riêng với thầy ạ>
+ Số lượng: - Tính đến nay hiện tại đã có 900 bức ảnh
+ Train/dev/test: 60/20/20

Mô tả đặc trưng:

+ feature engineering: object detection, tức là tìm cái khung chứa vật thể chúng ta cần dự đoán đây là bài toán nhận dạng khuôn mặt, chúng ta cần tìm được vị trí các khuôn mặt trong ảnh và crop các khuôn mặt đó trước khi làm các bước tiếp theo. Ngay cả khi đã xác định được các khung chứa các khuôn mặt (và có thể resize các khung đó về cùng một kích thước), ta vẫn phải làm rất nhiều việc nữa vì hình ảnh của khuôn mặt còn phụ thưộc vào góc chụp, ánh sáng, … và rất nhiều yếu tố khác nữa.

Phát triển tương lai: Nhận biết thêm khoảng cách an toàn giữa mọi người

---

## Cách thực hiện

B1: Thu nhập data - ảnh từ camera an ninh

- Đối với giao hàng tiết kiệm, bọn em record các video từ camera an ninh ở đây
  - Số lượng: 10 videos
  - Độ dài: Ít nhất là 30p  và nhiều nhất là 1h30p
- Đối với quán cafe, vì camera không có chức năng lưu video sẵn, nên bọn em sử dụng chắc năng record trên camere
  - Số lượng: 39 videos
  - Độ dài: Vì chức năng của nó có hạn nên mỗi record chỉ dài 5p

B2: Tiền xử lý ảnh với phần mềm lblImage dùng để để gán nhãn ảnh

- Tải và cài đặt phần mềm tại đây: https://github.com/tzutalin/labelImg

- Cách thức dán nhãn: Với mỗi ảnh bọn em phân ra 3 lớp sau:

  - 0 - person: người, xác định khung người ở trong bức hình
  - 1 - have_facemasked: có đeo khẩu trang, với mỗi khung người xác định khung khuôn mặt để đánh dấu người đó có đeo khẩu trang 
  - 2 - no_facemasked: không đeo khẩu trang,  với mỗi khung người xác định khung khuôn mặt để đánh dấu người đó không đeo khẩu trang 

- Format: Bọn em sử dụng tính năng yolo của phần mềm để dự đoán ảnh, sau khi dán nhãn mỗi bức hình sẽ có format như sau:

  - .png: Là ảnh của hình đã dán nhãn
  - .txt: có cấu trúc: object - x y w h, với object là classes của chúng ta tương ứng số 0, 1, 2. x và y tương ứng với điểm đầu tiên hình chữ nhật. w và h lần lượt là chiều rộng và chiều dài của hình chữ nhật đó.

  Cuối cùng là file.classes chứa 3 lớp mà bọn em đã phân ra

