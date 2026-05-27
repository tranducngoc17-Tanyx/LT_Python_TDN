"""
(1) Phân tích lỗi
Nguyên nhân lỗi

Lỗi xảy ra vì biến:

total_students

được đặt ngoài vòng lặp chi nhánh.

Ví dụ code sai thường có dạng:

total_students = 0

for branch in range(3):

    for classroom in range(3):
        students = int(input())
        total_students += students

    print(total_students)

Điều này khiến:

Sau khi tính xong Chi nhánh 1 → total_students = 83
Sang Chi nhánh 2 → hệ thống KHÔNG reset về 0
Nó tiếp tục cộng thêm dữ liệu mới vào 83 cũ

=> dẫn đến cộng dồn sai giữa các chi nhánh.

Trace code chi tiết
Chi nhánh 1

Dữ liệu:

30, 25, 28

Ban đầu:

total_students = 0

Lần cộng thứ 1:

0 + 30 = 30

Lần cộng thứ 2:

30 + 25 = 55

Lần cộng thứ 3:

55 + 28 = 83

Kết quả:

Chi nhánh 1: 83 học viên

✅ Đúng

Vì ban đầu biến total_students đang là 0.

Chi nhánh 2

Dữ liệu:

20, 22, 18

Sau Chi nhánh 1:

total_students = 83

Nhưng chương trình không reset.

Lần cộng thứ 1:

83 + 20 = 103

Lần cộng thứ 2:

103 + 22 = 125

Lần cộng thứ 3:

125 + 18 = 143

Kết quả hiển thị:

Chi nhánh 2: 143 học viên

❌ Sai

Đúng ra chỉ được tính:

20 + 22 + 18 = 60

Nhưng hệ thống lại cộng thêm 83 của Chi nhánh 1.

Chi nhánh 3

Dữ liệu:

35, 32, 30

Sau Chi nhánh 2:

total_students = 143

Tiếp tục cộng:

Lần cộng thứ 1:

143 + 35 = 178

Lần cộng thứ 2:

178 + 32 = 210

Lần cộng thứ 3:

210 + 30 = 240

Kết quả:

Chi nhánh 3: 240 học viên

❌ Sai

Đúng ra phải là:

35 + 32 + 30 = 97
Kết luận lỗi logic
Sai ở đâu?

Biến tổng:

total_students

được khai báo sai vị trí.

Đúng phải làm gì?

Mỗi chi nhánh cần có tổng riêng.

Vì vậy:

Khi bắt đầu xử lý chi nhánh mới
Phải reset tổng về 0
(2) Source code đúng chuẩn
"""

# Duyệt từng chi nhánh
for branch in range(3):

    # Reset tổng học viên cho từng chi nhánh
    total_students = 0

    # Duyệt các lớp trong chi nhánh
    for classroom in range(3):
        students = int(
            input(
                f"Nhập số học viên Chi nhánh {branch + 1}, lớp {classroom + 1}: "
            )
        )

        total_students += students

    # In kết quả từng chi nhánh
    print(
        f"Chi nhánh {branch + 1}: "
        f"{total_students} học viên"
    )