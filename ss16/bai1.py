"""
(1) Phân tích lỗi
Câu 1: Tại sao raw_diagnosis.strip() và raw_diagnosis.title() không làm thay đổi biến raw_diagnosis?

Vì String trong Python là Immutable (bất biến).

Điều này có nghĩa là sau khi một chuỗi được tạo ra, ta không thể thay đổi trực tiếp nội dung của chuỗi đó.

Các phương thức như:

strip()
title()
upper()
lower()
replace()

không sửa chuỗi gốc mà sẽ tạo ra một chuỗi mới rồi trả về kết quả.

Ví dụ:

name = "  viEm phE QUan  "

name.strip()

print(name)

Kết quả:

"  viEm phE QUan  "

Chuỗi vẫn giữ nguyên vì kết quả của strip() không được lưu lại.

Câu 2: Cần sửa cú pháp như thế nào?

Phải gán lại giá trị trả về cho biến.

Có thể viết:

raw_diagnosis = raw_diagnosis.strip()
raw_diagnosis = raw_diagnosis.title()

Hoặc gộp thành:

raw_diagnosis = raw_diagnosis.strip().title()

Kết quả:

"  viEm phE QUan  "

↓

"Viem Phe Quan"
Câu 3: extend() hoạt động như thế nào với String?

extend() sẽ duyệt qua từng phần tử của đối tượng truyền vào.

Với String:

text = "ABC"

Python coi nó là:

["A", "B", "C"]

Ví dụ:

data = ["Hello"]

data.extend("ABC")

print(data)

Kết quả:

['Hello', 'A', 'B', 'C']
Tại sao xuất hiện các ký tự rời rạc?

Do dòng:

current_list.extend(raw_diagnosis)

tương đương:

for char in raw_diagnosis:
    current_list.append(char)

Nên:

"  viEm phE QUan  "

bị tách thành:

' '
' '
'v'
'i'
'E'
'm'
' '
'p'
'h'
'E'
...

và đưa từng ký tự vào list.

Câu 4: Thay extend() bằng gì?

Cần dùng:

append()

Vì append() thêm nguyên vẹn một phần tử vào list.

Ví dụ:

diagnoses = ["Sốt Xuất Huyết"]

diagnoses.append("Viem Phe Quan")

Kết quả:

['Sốt Xuất Huyết', 'Viem Phe Quan']
(2) Source Code Đã Sửa
"""

# Danh sách chẩn đoán hiện tại của bệnh nhân
patient_diagnoses = ["Sốt Xuất Huyết"]


def add_diagnosis(raw_diagnosis, current_list):
    # Chuẩn hóa chuỗi
    raw_diagnosis = raw_diagnosis.strip().title()

    # Thêm nguyên vẹn chuỗi vào list
    current_list.append(raw_diagnosis)

    return current_list


# Bác sĩ nhập chẩn đoán mới
new_diagnosis = "  viEm phE QUan  "

# Cập nhật hồ sơ
updated_diagnoses = add_diagnosis(
    new_diagnosis,
    patient_diagnoses
)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)