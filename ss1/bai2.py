# Phân tích lỗi

print("=== HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ===")
name_patient = input("Nhập tên bệnh nhân : ")
weight = input("Nhập cân nặng bệnh nhân : ")

print("=== KIỂM TRA DỮ LIỆU LƯU TRỮ ===")
print("Bệnh nhân :", name_patient)
print("Cân nặng đã nhập :", weight)

# Lỗi:
# input() mặc định luôn trả về dữ liệu kiểu chuỗi (str)
# Ví dụ nhập 65.5 thì hệ thống lưu thành "65.5"
# Chương trình không lỗi cú pháp nhưng sai kiểu dữ liệu
# Điều này có thể làm BMI và các phép tính khác không hoạt động đúng

print("CẢNH BÁO - Kiểu dữ liệu đang lưu là :", type(weight))


# Sửa lỗi
# Ép kiểu dữ liệu sang số thực (float)

weight = float(input("Nhập cân nặng bệnh nhân : "))