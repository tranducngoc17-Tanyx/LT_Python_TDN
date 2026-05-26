print("===== HỆ THỐNG NHẬP LIỆU NHÂN SỰ =====")

while True:

    while True:
        employee_id = input("\nNhập mã nhân viên (VD: NV001): ")

        if employee_id.strip() == "":
            print("[ERROR] Mã nhân viên không được để trống!")
        else:
            break

    while True:
        employee_fullname = input("Nhập họ tên nhân viên: ")

        if employee_fullname.strip() == "":
            print("[ERROR] Họ tên không được để trống!")
        else:
            break

    while True:
        employee_age = int(input("Nhập tuổi nhân viên: "))

        if employee_age <= 0:
            print("[ERROR] Tuổi phải lớn hơn 0!")
        else:
            break

    while True:
        employee_salary = float(
            input("Nhập lương cơ bản (VD: 15000000): ")
        )

        if employee_salary <= 0:
            print("[ERROR] Lương phải lớn hơn 0!")
        else:
            break

    while True:
        employee_kpi = float(
            input("Nhập điểm KPI (1.0 - 5.0): ")
        )

        if employee_kpi < 1.0 or employee_kpi > 5.0:
            print("[ERROR] KPI phải từ 1.0 đến 5.0!")
        else:
            break

    print("\nHỒ SƠ NHÂN SỰ ĐIỆN TỬ")
    print(f"Mã nhân viên : {employee_id}")
    print(f"Họ và tên    : {employee_fullname}")
    print(f"Tuổi         : {employee_age}")
    print(f"Lương cơ bản : {employee_salary}")
    print(f"Điểm KPI     : {employee_kpi}")

    print("\nSYSTEM LOG")

    print(
        f"employee_id = {employee_id} | kiểu dữ liệu: {type(employee_id)}"
    )

    print(
        f"employee_fullname = {employee_fullname} | kiểu dữ liệu: {type(employee_fullname)}"
    )

    print(
        f"employee_age = {employee_age} | kiểu dữ liệu: {type(employee_age)}"
    )

    print(
        f"employee_salary = {employee_salary} | kiểu dữ liệu: {type(employee_salary)}"
    )

    print(
        f"employee_kpi = {employee_kpi} | kiểu dữ liệu: {type(employee_kpi)}"
    )


    continue_input = input(
        "\nTiếp tục nhập nhân viên khác? (y/n): "
    )

    if continue_input.lower() == "n":
        break

print("\nĐã kết thúc chương trình nhập liệu.")