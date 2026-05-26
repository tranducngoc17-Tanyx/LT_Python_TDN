print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")

    working_days = int(input("Nhập số ngày công trong tháng: "))

    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")

    bonus_amount = working_days * 200000
    print("→ Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiền thưởng!")
    print("------------------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")

# Phân tích lỗi
# logic: Chương trình thiếu lệnh dừng hoặc bỏ qua (như 'continue' hoặc 'else').
# Khi kết thúc khối if này, chương trình không thoát vòng lặp

# sửa lỗi
print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")
    working_days = int(input("Nhập số ngày công trong tháng: "))
    
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
    else:
        bonus_amount = working_days * 200000
        print("→ Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiền thưởng!")
    ư
print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")