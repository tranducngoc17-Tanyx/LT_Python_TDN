print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

for employee_number in range(1, 4):

    total_budget = 0

    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input("  Nhập mức lương (VNĐ): "))

    total_budget = total_budget + salary

print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")

# Phân tích lỗi:
# Lỗi logic:
# Biến total_budget được đặt bên trong vòng lặp.
# Mỗi lần lặp chạy lại:
# total_budget = 0
# nên giá trị tổng cũ bị xóa.

# sửa lỗi

total_budget = 0

for employee_number in range(1, 4):

    print("Đang xử lý nhân viên số", employee_number)

    salary = int(input("  Nhập mức lương (VNĐ): "))

    total_budget = total_budget + salary

print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")