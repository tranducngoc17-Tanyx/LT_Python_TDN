number_of_forms = int(input("Nhập số lượng phiếu đăng ký: "))

# Edge Case 1
if number_of_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:

    for i in range(number_of_forms):

        print(f"\nNhập phiếu đăng ký thứ {i + 1}:")

        registration = input(
            "Họ tên | Khóa học | Mã học viên | Email: "
        )

        # Tách dữ liệu
        parts = registration.split("|")

        # Edge Case 2
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        # Chuẩn hóa dữ liệu
        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        # Edge Casee 3
        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        # Edge Case 4
        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        # Tạo mã xác nhận
        confirmation_code = (
            student_code
            + "_"
            + course_name.upper().replace(" ", "-")
        )

        # In kết quả
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirmation_code)