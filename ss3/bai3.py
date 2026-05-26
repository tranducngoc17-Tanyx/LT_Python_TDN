# Phân tích giải pháp
# Hệ thống cần nhập thông tin đúng 3 nhân viên bằng vòng lặp for.
# Mỗi nhân viên nhập:
#  Mã nhân viên (str)
#  Họ và tên (str)
#  Phòng ban (str)

# Xử lý lỗi / Edge Cases:
# - Lỗi 1: Người dùng bỏ trống mã nhân viên ("")
# - Lỗi 2: Người dùng bỏ trống họ tên ("")
# - Lỗi 3: Người dùng nhập dữ liệu rác chỉ chứa khoảng trắng (" ")

# Cách xử lý: dùng .strip() để xóa khoảng trắng đầu và cuối

# Thuật toán:
# B1: Lặp từ 1 -> 3
# B2: Nhập thông tin nhân viên
# B3: Kiểm tra dữ liệu hợp lệe
# B4: Nếu lỗi -> cảnh báo
# B5: Nếu đúng -> in phiếu hồ sơ
# B6: Sau khi đủ 3 nhân viên -> kết thúc chương trình

print("=== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ ===")

for i in range(1, 4):

    print(f"\n--- Nhập thông tin nhân viên {i} ---")

    employee_id = input("Nhập mã nhân viên: ").strip()
    employee_name = input("Nhập họ và tên: ").strip()
    department = input("Nhập phòng ban: ").strip()

    if employee_id == "" or employee_name == "":
        print("\n[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ!")
        print("Hủy bỏ tạo hồ sơ cho nhân viên này.")

    else:
        print("PHIẾU HỒ SƠ NHÂN SỰ ĐIỆN TỬ")
        print("==============================")
        print("Mã nhân viên:", employee_id)
        print("Họ và tên:", employee_name)
        print("Phòng ban:", department)
        
print("\n=== ĐÃ HOÀN TẤT TIẾP NHẬN 3 NHÂN SỰ ===")