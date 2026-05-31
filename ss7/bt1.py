student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

# Chuẩn hóa dữ liệu
student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

# Hiển thị kết quả
print("===== THÔNG TIN HỌC VIÊN SAU CHUẨN HÓA =====")
print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)