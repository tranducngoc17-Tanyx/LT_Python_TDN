"""
1. Phân tích và thiết kế giải pháp
Hàm display_patients(patient_list)
Input
patient_list

Kiểu dữ liệu:

list

Ví dụ:

[
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]
Output
None

Nhiệm vụ:

Hiển thị danh sách bệnh nhân.
Hàm validate_gender(gender_input)
Input
gender_input

Kiểu:

str

Ví dụ:

"nam"
" nu "
"Không rõ"
Output
bool

Trả về:

True

nếu:

nam
nu

Ngược lại:

False
Hàm find_patient_index(patient_list, patient_id)
Input
patient_list
patient_id
Output
int

Ví dụ:

0
1
2

Nếu không tìm thấy:

-1
Hàm add_patient(patient_list)
Input
patient_list
Output
None

Nhiệm vụ:

Nhập bệnh nhân mới
Kiểm tra dữ liệu
Append vào danh sách
Hàm update_diagnosis(patient_list)
Input
patient_list
Output
None

Nhiệm vụ:

Tìm bệnh nhân
Cập nhật chẩn đoán
Hàm search_by_disease(patient_list)
Input
patient_list
Output
None

Nhiệm vụ:

Tìm kiếm theo tên bệnh
Thống kê số lượng
String và List tương tác như thế nào?

Ví dụ:

patient = [
    "BN001",
    "Nguyen Van A",
    "Nam",
    "Viem Phoi"
]

Trong đó:

Mỗi phần tử là String
Toàn bộ bệnh nhân là List

Danh sách bệnh nhân:

patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

=> Đây là List chứa nhiều List con.

Truyền patient_list vào hàm là truyền gì?

Python truyền tham chiếu đối tượng (Object Reference).

Ví dụ:

def add_patient(patient_list):
    patient_list.append(...)

Danh sách bên ngoài cũng thay đổi.

Không cần return lại list.

2. Source Code Hoàn Chỉnh
"""

# ==========================
# DỮ LIỆU BAN ĐẦU
# ==========================

patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


def display_patients(patient_list):
    """
    Hiển thị danh sách bệnh nhân.
    """

    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    for index, patient in enumerate(patient_list, start=1):
        print(
            f"{index}. Mã: {patient[0]} | "
            f"Tên: {patient[1]} | "
            f"Giới tính: {patient[2]} | "
            f"Bệnh: {patient[3]}"
        )


def validate_gender(gender_input):
    """
    Kiểm tra giới tính hợp lệ.
    """

    gender = gender_input.strip().lower()

    return gender in ["nam", "nu"]


def find_patient_index(patient_list, patient_id):
    """
    Tìm vị trí bệnh nhân theo mã.
    """

    patient_id = patient_id.strip().upper()

    for index in range(len(patient_list)):
        if patient_list[index][0] == patient_id:
            return index

    return -1


def add_patient(patient_list):
    """
    Tiếp nhận bệnh nhân mới.
    """

    print("\n----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print(
            "Mã bệnh nhân đã tồn tại trong hệ thống, "
            "vui lòng kiểm tra lại!"
        )
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip().title()

    if len(patient_name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        gender = input("Nhập giới tính Nam/Nu: ")

        if validate_gender(gender):
            gender = gender.strip().capitalize()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    patient = [
        patient_id,
        patient_name,
        gender,
        diagnosis
    ]

    patient_list.append(patient)

    print("\nTiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    """
    Cập nhật chẩn đoán bệnh.
    """

    print("\n----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(
        patient_list,
        patient_id
    )

    if index == -1:
        print(
            f"Không tìm thấy hồ sơ mang mã {patient_id}!"
        )
        return

    print(
        f"Tìm thấy bệnh nhân: "
        f"{patient_list[index][1]}"
    )

    print(
        f"Chẩn đoán hiện tại: "
        f"{patient_list[index][3]}"
    )

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    ).strip().capitalize()

    if len(new_diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[index][3] = new_diagnosis

    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    """
    Tìm kiếm bệnh nhân theo bệnh.
    """

    print(
        "\n----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----"
    )

    keyword = input(
        "Nhập từ khóa tên bệnh: "
    ).strip()

    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    count = 0

    print("\nKết quả tìm kiếm:")

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1

            print(
                f"{count}. Mã: {patient[0]} | "
                f"Tên: {patient[1]} | "
                f"Giới tính: {patient[2]} | "
                f"Bệnh: {patient[3]}"
            )

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(
        f"\nCó tổng cộng {count} bệnh nhân "
        f"mắc bệnh liên quan đến '{keyword}'."
    )


def main():
    """
    Hàm điều khiển chương trình.
    """

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")

        choice = input(
            "Nhập lựa chọn của bạn: "
        )

        if choice == "1":
            display_patients(patients)

        elif choice == "2":
            add_patient(patients)

        elif choice == "3":
            update_diagnosis(patients)

        elif choice == "4":
            search_by_disease(patients)

        elif choice == "5":
            print(
                "Cảm ơn bác sĩ đã sử dụng hệ thống!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ, "
                "vui lòng nhập số từ 1-5!"
            )


main()