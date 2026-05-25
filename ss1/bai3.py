# Phân tích Input/Output
# Input:
# Họ và tên bệnh nhân (str)
# Mã bệnh án (str)
# KKhoa/Phòng khám chỉ định (str)

# Output:
# Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]

# Thuật toán:
# b1: Nhập họ tên bệnh nhân
# b2: Nhập mã bệnh án
# b3: Nhập khoa/phòng khám
# b4: Hiển thị phiếu khám bệnh điện tử

name_patient = input("Nhập họ tên bệnh nhân: ")
medical_id = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám chỉ định: ")

print(" --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ")
print(f"Bệnh nhân: {name_patient} - Mã BA: {medical_id} - Chuyển tới: {department}")