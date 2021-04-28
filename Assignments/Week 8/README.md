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
