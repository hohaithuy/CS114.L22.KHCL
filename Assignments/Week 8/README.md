# Ví dụ về bài toán Regression trong thực tế

---

1. Bài toán: Dự đoán chỉ số ô nhiễm không khí ở Việt Nam
   - Input:
     - Số liệu phương tiện giao thông đang lưu hành trong cả nước của oto và xe máy: dạng số nguyên, đơn vị (triệu)
     - Dân số Việt Nam: Dạng số nguyên, đơn vị(triệu)
   - Cách thu nhập: 
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
     - Giá mua mới tại hãng: dạng số nguyên , đơn vị ( triệu VNĐ)
     - Mẫu xe: dạng chuỗi kí tự.
     - Năm sản xuất: dạng số nguyên, đơn vị (năm)
     - Màu: dạng chuỗi kí tự.
     - Thời gian đã sử dụng: dạng số nguyên, đơn vị (ngày)
     - Khu vực ra biển số: số nguyên (số hiệu tỉnh thành của các tỉnh ở Việt Nam)
     - Có hay Không có giấy tờ: 1 or 0
     - Chỉ số odometer: dạng số nguyên
     - Xe đã qua đại tu hay còn nguyên "zin": 1 or 0
     - Chỉ số dung tích phân khối của xe: dạng số nguyên, đơn vị( cc )
   - Cách thu nhập: 
     - Dữ liệu sơ cấp: khảo sát các cửa hàng bán xe máy uy tín tại nhiều khu vực.
     - Số liệu chỉ số xe như là phân khối, mẫu xe, năm sản xuất... có thể lấy trực tiếp từ các hãng bán xe máy phổ biến như:
     
         +Honda
         
         +Yamaha
         
         +...
     - Số liệu từ các trang bán xe máy qua mạng như: 
        
        +https://xe.chotot.com
        
        +https://www.webike.vn
        
        +https://choxeotofun.net/xe-may
   - Xử lý data:
     - Gộp toàn bộ dữ liệu trên thành một ma trận dưới dạng file csv,mỗi hàng của ma trận là gồm có các cột tương ứng với chỉ số input (Gía mua mới, mẫu xe, odo,...). Cột cuối cùng sẽ là giá bán của chiếc xe máy đó.
   - Output:
     - Một số nguyên dương là giá bán của 1 chiếc xe máy nào đó được đưa vào, đơn vị (Triệu VNĐ).  
       
      
    
