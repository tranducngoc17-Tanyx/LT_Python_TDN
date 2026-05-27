"""
(1) Phân tích lỗi
Vì sao báo cáo không gom dữ liệu theo từng chi nhánh?

Trong chương trình cũ, lập trình viên đang duyệt:

for month in range(3):
    for branch in range(3):

Nghĩa là:

Vòng lặp ngoài → duyệt theo tháng
Vòng lặp trong → duyệt theo chi nhánh

Do đó kết quả hiển thị sẽ là:

Tất cả chi nhánh của tháng 1
Tất cả chi nhánh của tháng 2
Tất cả chi nhánh của tháng 3

Ví dụ:

Chi nhánh 1, tháng 1
Chi nhánh 2, tháng 1
Chi nhánh 3, tháng 1

Trong khi yêu cầu nghiệp vụ cần:

Chi nhánh 1:
    tháng 1
    tháng 2
    tháng 3

Tức là phải gom toàn bộ dữ liệu của từng chi nhánh lại với nhau.

Theo yêu cầu nghiệp vụ:
Vòng lặp ngoài nên duyệt gì?

✅ Duyệt theo chi nhánh

Vì báo cáo cần nhóm dữ liệu theo từng chi nhánh.

Vòng lặp trong nên duyệt gì?

✅ Duyệt theo tháng

Vì trong mỗi chi nhánh cần hiển thị doanh thu của từng tháng.

Cấu trúc đúng
for branch in range(3):
    for month in range(3):

Ý nghĩa:

Chi nhánh 1
tháng 1
tháng 2
tháng 3
Chi nhánh 2
tháng 1
tháng 2
tháng 3

Đúng với yêu cầu nghiệp vụ.

(2) Source code đúng chuẩn
"""

# Khởi tạo danh sách lưu doanh thu
revenues = []

# Nhập dữ liệu
for branch in range(3):
    monthly_revenue = []

    for month in range(3):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch + 1}, tháng {month + 1}: "))
        monthly_revenue.append(revenue)

    revenues.append(monthly_revenue)

# Hiển thị báo cáo
print("-------------- Kết quả --------------")

for branch in range(3):
    for month in range(3):
        print(
            f"Chi nhánh {branch + 1}, tháng {month + 1}: "
            f"{revenues[branch][month]} triệu đồng"
        )