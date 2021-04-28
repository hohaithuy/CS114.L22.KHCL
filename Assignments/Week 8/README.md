# Ví dụ về bài toán Regression trong thực tế
---

### Team member:
|No.| Full name         |Student ID       |Class      |
|:-:|:------------------|:---------:|:--------:|
| 1	|[Hồ Hải Thủy](https://www.facebook.com/suzu2k1)	| 19522323	| CS114.L22.KHCL |
| 2	|[Nguyễn Khả Tiến](https://www.facebook.com/tiennguyenbangde)	| 19522337	| CS114.L22.KHCL |
| 3	|[Nguyễn Mạnh Toàn](https://www.facebook.com/acma.thosan.1)	  | 19522363	| CS114.L22.KHCL  |
---
---

1. Bài toán: Dự đoán chỉ số ô nhiễm không khí ở Việt Nam
   - Input:
     - Số liệu phương tiện giao thông đang lưu hành trong cả nước của oto và xe máy: dạng số nguyên, đơn vị (triệu)
     - Dân số Việt Nam: Dạng số nguyên, đơn vị(triệu)
   - Cách thu thập: 
     - Số liệu phương tiện giao thông đang lưu hành trong cả nước của oto và xe máy được thống kê tại :http://www.vr.org.vn/thong-ke/Pages/tong-hop-so-lieu-phuong-tien-giao-thong-trong-ca-nuoc.aspx#. Ta thống kê lại theo năm
     - Dân số Việt Nam: Tra cứu tại google sẽ hiện lên một bảng thống kê dân số Việt Nam theo từng năm bởi Ngân hàng thế giới. Ta thống kê lại theo năm
     - Chỉ số ô nhiễm không khí ở Việt Nam: Thống kê trên trang https://www.iqair.com/vi/. Ta thống kê lại theo năm
   - Xử lý data:
     - Gộp toàn bộ dữ liệu trên thành một ma trận dưới dạng file csv, gồm có feature là số liệu phương tiện giao thông, dân số Việt Nam. Label sẽ là chỉ số ô nhiễm không khí ở Việt Nam
   - Output:
     - Một số nguyên dương  là chỉ số ô nhiễm không khí ở Việt Nam mà mô hình dự đoán

---

2. Bài toán: Dự đoán giá mua xe máy (đã qua sử dụng) ở Việt Nam, giúp người tiêu dùng mua xe không bị "hớ"
   - Input:
     - Mẫu xe: dạng chuỗi kí tự.
     - Năm sản xuất: dạng số nguyên, đơn vị (năm)
     - Màu: dạng chuỗi kí tự.
     - Thời gian đã sử dụng: dạng số nguyên, đơn vị (ngày)
     - Khu vực ra biển số: số nguyên (số hiệu tỉnh thành của các tỉnh ở Việt Nam)
     - Có hay Không có giấy tờ: 1 or 0
     - Chỉ số odometer: dạng số nguyên
     - Xe đã qua đại tu hay còn nguyên "zin": 1 or 0
   - Cách thu thập: 
     - Dữ liệu sơ cấp: khảo sát các cửa hàng bán xe máy uy tín tại nhiều khu vực.
     - Số liệu chỉ số xe như là phân khối, mẫu xe, năm sản xuất... có thể lấy trực tiếp từ các hãng bán xe máy phổ biến như:
     
         +Honda
         
         +Yamaha
         
         +...
     - Số liệu từ các trang bán xe máy qua mạng như: 
        
        +https://xe.chotot.com
        
        +https://www.webike.vn
        
        +https://choxeotofun.net/xe-may
        
        +...
        
      -  Ngoài ra các feature thêm vào được cân nhắc và tham khảo qua các trang tư vấn và blog mua xe máy cũ như: 
        
         
         +https://giaoduc.net.vn/mo-to/kinh-nghiem-mua-xe-may-cu-cho-nguoi-khong-sanh-ve-xe-post73620.gd
        
         
         +https://thibanglaixe.com.vn/xe-may-cu/
        
         
         +https://blog.muaban.net/5-luu-y-khi-mua-xe-o-cua-hang-xe-may-cu/   
         
         +...
        
   - Xử lý data:
     - Gộp toàn bộ dữ liệu trên thành một ma trận dưới dạng file csv, mỗi hàng của ma trận là gồm có các cột tương ứng với chỉ số input (Gía mua mới, mẫu xe, odo,...). Cột cuối cùng sẽ là giá bán của chiếc xe máy đó.
   - Output:
     - Một số nguyên dương là giá bán của 1 chiếc xe máy nào đó được đưa vào, đơn vị (Triệu VNĐ).  
 

 ----
3. Bài toán: Dự đoán mức độ hài lòng của nhân viên đối với công việc theo mức lương, nơi làm việc
   - Input:
     - Tên công việc: dạng chuỗi string
     - Địa điểm làm việc(tỉnh): dạng chuỗi string
     - Số tiền lương: float, đơn vị(triệu)
   - Cách thu nhập: 
     - Tạo google form, khảo sát nặc danh bao gồm tên công việc, địa điểm làm việc(tỉnh), mức lương, mức độ hài long từ 0 đến 10 trên các group việc làm
     - Phỏng vấn nhân viên ở các công ty.
     - Tham khảo mức lương của công việc trên trang https://jobsgo.vn/tra-cuu-luong.html . 
       +Nếu tiền lương input bằng với mức lương trung bình của trang thì độ hài lòng bằng 8
       +Nếu tiền lương input bằng với
   - Xử lý data:
     - Gộp toàn bộ dữ liệu trên thành một ma trận dưới dạng file csv, mỗi hàng của ma trận gồm có 4 cột tương ứng là tên công việc: string, địa điểm làm việc(tỉnh): string, số tiền lương(đơn vị triệu): float, cột cuối cùng sẽ là mức độ hài lòng của nhân viên đối với công việc( từ 0 đến 10).
   - Output:
     - Một số nguyên dương từ 0 đến 10: là mức độ hài lòng của nhân viên đối với công việc.

---
    
