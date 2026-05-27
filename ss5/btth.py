employee_count = int(input("Nhập số lượng nhân viên: "))

for employee in range(employee_count):
    employee_name = input("\n Nhập tên nhân viên: ")

    working_day = int(input("Nhập số ngày làm: "))

    if working_day < 0 or working_day > 22:
        print("Dữ liệu không hợp lệ")
        continue

    if working_day == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
        continue
    
    print(f"{employee_name}: ", end =" ")

    for star in range(working_day):
        print("*", end = " ")

    print()

    if working_day >= 18:
        print("Làm việc chăm chỉ")
    elif working_day < 10:
        print("làm việc ít")
    else:
        print("làm việc bình thường")
