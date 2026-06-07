
# Triển khai code
student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")


def calculate_average(student):
    return (
        student["math"]
        + student["physics"]
        + student["chemistry"]
    ) / 3


def get_rank(avg):
    if avg >= 8:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        average = calculate_average(student)

        print(
            f"{index}. [{student['student_id']}] "
            f"{student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {average:.2f} - {get_rank(average)}"
        )

    print("---------------------------")


def update_student_score(records):

    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    found_student = None

    for student in records:
        if student["student_id"] == student_id:
            found_student = student
            break

    if found_student is None:
        print(
            f"Không tìm thấy sinh viên mang mã "
            f"{student_id} trong hệ thống!"
        )
        return

    print("1. Toán")
    print("2. Lý")
    print("3. Hóa")

    subject = input(
        "Chọn môn học (1-Toán, 2-Lý, 3-Hóa): "
    )

    while True:
        try:
            new_score = float(
                input("Nhập điểm mới: ")
            )

            if 0 <= new_score <= 10:
                break

            print(
                "Điểm số không hợp lệ. "
                "Vui lòng nhập từ 0 đến 10!"
            )

        except ValueError:
            print("Vui lòng nhập số!")

    if subject == "1":
        found_student["math"] = new_score
        subject_name = "Toán"

    elif subject == "2":
        found_student["physics"] = new_score
        subject_name = "Lý"

    elif subject == "3":
        found_student["chemistry"] = new_score
        subject_name = "Hóa"

    else:
        print("Môn học không hợp lệ!")
        return

    print(
        f"Đã cập nhật điểm {subject_name} của sinh viên "
        f"'{found_student['name']}' thành {new_score}."
    )


def generate_report(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    passed = 0
    failed = 0

    for student in records:

        average = calculate_average(student)

        if average >= 5:
            passed += 1
        else:
            failed += 1

    total = len(records)

    passed_percent = (passed / total) * 100
    failed_percent = (failed / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): "
        f"{passed} sinh viên "
        f"({passed_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): "
        f"{failed} sinh viên "
        f"({failed_percent:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    highest_average = calculate_average(top_student)

    for student in records:

        average = calculate_average(student)

        if average > highest_average:
            highest_average = average
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(
        f"Sinh viên: {top_student['name']} "
        f"(Mã: {top_student['student_id']})"
    )
    print(
        f"Điểm Trung Bình: "
        f"{highest_average:.2f}"
    )
    print(
        "Chúc mừng sinh viên đã đạt thành tích "
        "xuất sắc nhất khóa!"
    )
    print("--------------------------")


while True:

    display_menu()

    choice = input(
        "Chọn chức năng (1-5): "
    )

    if choice == "1":
        display_grades(student_records)

    elif choice == "2":
        update_student_score(student_records)

    elif choice == "3":
        generate_report(student_records)

    elif choice == "4":
        find_valedictorian(student_records)

    elif choice == "5":
        print(
            "Cảm ơn bạn đã sử dụng hệ thống!"
        )
        break

    else:
        print(
            "Lựa chọn không hợp lệ!"
        )