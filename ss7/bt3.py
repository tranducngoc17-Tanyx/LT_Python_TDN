raw_data = (
    " eMP-001; nguyen van a ;0987654321;sale | "
    "Emp-002; Tran Thi B; 0912-345-678 ; mkt | "
    "EMP-003 ; le van C ; 0988abc123 ; IT "
)

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng: ").strip()

    if choice == "1":

        print("\n===== DỮ LIỆU GỐC =====")
        print(raw_data)
    elif choice == "2":

        employees = raw_data.split("|")

        print("\n===== BÁO CÁO NHÂN SỰ =====")

        print(
            f"{'ID':<12}"
            f"{'HỌ TÊN':<25}"
            f"{'ĐIỆN THOẠI':<20}"
            f"{'PHÒNG BAN':<15}"
        )

        for employee in employees:

            fields = employee.split(";")

            emp_id = fields[0].strip().upper()
            name = fields[1].strip().title()
            phone = fields[2].strip()
            department = fields[3].strip().upper()

            # Xử lý số điện thoại
            phone = phone.replace("-", "")

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            print(
                f"{emp_id:<12}"
                f"{name:<25}"
                f"{phone:<20}"
                f"{department:<15}"
            )

    elif choice == "3":

        search_id = input(
            "Nhập mã nhân viên cần tìm: "
        ).strip().upper()

        employees = raw_data.split("|")

        found = False

        for employee in employees:

            fields = employee.split(";")

            emp_id = fields[0].strip().upper()
            name = fields[1].strip().title()
            phone = fields[2].strip()
            department = fields[3].strip().upper()

            phone = phone.replace("-", "")

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            if emp_id == search_id:

                print("\n===== THÔNG TIN NHÂN VIÊN =====")
                print("ID:", emp_id)
                print("Họ tên:", name)
                print("Điện thoại:", phone)
                print("Phòng ban:", department)

                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == "4":

        print("Thoát chương trình")
        break

    else:

        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")