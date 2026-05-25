import random

patientName = input("Tên bệnh nhân: ")
gender = input("Giới tính: ")
year = int(input("Năm sinh: "))
phoneNumber = input("Số điện thoại: ")
email = input("Email: ")
initialSymptoms = input("Triệu chứng ban đầu: ")
expense = float(input("Chi phí khám: "))

print("--- THẺ BỆNH NHÂN ---")
code_random = random.randint(100, 999)

print(f"Mã bệnh nhân: BN{year}{code_random}")
print("Tên:", patientName, type(patientName))
print("Giới tính:", gender, type(gender))
print("Năm sinh:", year, type(year))
print("Điện thoại:", phoneNumber, type(phoneNumber))
print("Email", email, type(email))
print("Triệu chứng:", initialSymptoms, type(initialSymptoms))
print("Chi phí: ", expense, "VNĐ", type(expense))