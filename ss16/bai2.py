"""
(1) Phân tích lỗi
Câu 1: Tại sao new_prescription.append("Oresol") lại làm thay đổi cả yesterday_prescription?

Do dòng:

new_prescription = old_prescription

Không tạo ra list mới.

Python chỉ tạo thêm một biến mới cùng trỏ tới một vùng nhớ duy nhất.

Ví dụ:

a = ["Panadol", "Vitamin C"]

b = a

Bộ nhớ:

a ----------\
             > ["Panadol", "Vitamin C"]
b ----------/

Lúc này:

b.append("Oresol")

thực chất đang sửa chính list mà a đang tham chiếu tới.

Kết quả:

print(a)
['Panadol', 'Vitamin C', 'Oresol']

Đây được gọi là Aliasing (tham chiếu chung một đối tượng).

Câu 2: Làm sao tạo bản sao độc lập của List?
Cách 1: Dùng copy()
new_prescription = old_prescription.copy()
Cách 2: Dùng slicing
new_prescription = old_prescription[:]
Cách 3: Dùng constructor list()
new_prescription = list(old_prescription)

Ví dụ:

a = [1, 2, 3]

b = a.copy()

b.append(4)

print(a)

Kết quả:

[1, 2, 3]

List gốc không bị ảnh hưởng.

Câu 3: Tại sao lệnh replace() không có tác dụng?

Dòng code:

new_prescription[0].replace(
    "Panadol",
    "Paracetamol"
)

không làm thay đổi dữ liệu vì:

String là Immutable

replace() tạo ra chuỗi mới rồi trả về.

Ví dụ:

drug = "Panadol"

drug.replace(
    "Panadol",
    "Paracetamol"
)

print(drug)

Kết quả:

Panadol

Chuỗi cũ vẫn giữ nguyên.

Câu 4: Sửa như thế nào?

Phải gán kết quả trở lại vị trí trong list.

new_prescription[0] = (
    new_prescription[0].replace(
        "Panadol",
        "Paracetamol"
    )
)

Hoặc ngắn gọn:

new_prescription[0] = "Paracetamol"

Sau khi gán:

[
    "Paracetamol",
    "Vitamin C",
    "Amoxicillin"
]
(2) Source Code Đã Sửa
"""
# Danh sách thuốc ngày hôm qua
yesterday_prescription = [
    "Panadol",
    "Vitamin C",
    "Amoxicillin"
]


def update_prescription(old_prescription):
    # Tạo bản sao độc lập
    new_prescription = old_prescription.copy()

    # Đổi tên thuốc
    new_prescription[0] = (
        new_prescription[0].replace(
            "Panadol",
            "Paracetamol"
        )
    )

    # Thêm thuốc mới
    new_prescription.append("Oresol")

    return new_prescription


# Tạo đơn thuốc hôm nay
today_prescription = update_prescription(
    yesterday_prescription
)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)