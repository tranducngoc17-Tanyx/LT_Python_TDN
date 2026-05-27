"""
(1) Phân tích và thiết kế giải pháp
Phân tích Input / Output
Input

Người dùng nhập:

1. Số lượng phòng học
Kiểu dữ liệu: int
Ý nghĩa: số phòng cần kiểm tra

Ví dụ:

3
2. Số hàng ghế của từng phòng
Kiểu dữ liệu: int

Ví dụ:

4
3. Số ghế trên mỗi hàng
Kiểu dữ liệu: int

Ví dụ:

5
Output mong đợi

Hệ thống in sơ đồ chỗ ngồi bằng dấu *.

Ví dụ:

*****
*****
*****
Phân tích nghiệp vụ
Edge Case 1 — Số lượng phòng không hợp lệ

Nếu:

total_rooms <= 0

Hiển thị:

Số lượng phòng học không hợp lệ

Và kết thúc chương trình.

Edge Case 2 — Dữ liệu phòng không hợp lệ

Nếu:

rows <= 0

hoặc

seats <= 0

Hiển thị:

Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này

Sau đó dùng:

continue

để chuyển sang phòng tiếp theo.

Edge Case 3 — Phòng quá lớn

Nếu:

rows > 10 or seats > 10

Hiển thị:

Phòng quá lớn. Dừng nhập dữ liệu

Sau đó:

break

để dừng toàn bộ chương trình.

Đề xuất giải pháp
Sử dụng vòng lặp
Vòng lặp ngoài

Duyệt qua từng phòng học:

for room in range(total_rooms):
Vòng lặp trong

In từng hàng ghế:

for row in range(rows):
Cách in dấu *

Có thể dùng:

print("*" * seats)

Ví dụ:

print("*" * 5)

Kết quả:

*****
Thiết kế thuật toán (Pseudocode)
Bắt đầu chương trình

Nhập total_rooms

Nếu total_rooms <= 0:
    In "Số lượng phòng học không hợp lệ"
    Kết thúc chương trình

Lặp qua từng phòng học:

    Nhập rows
    Nhập seats

    Nếu rows <= 0 hoặc seats <= 0:
        In "Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này"
        continue

    Nếu rows > 10 hoặc seats > 10:
        In "Phòng quá lớn. Dừng nhập dữ liệu"
        break

    In tiêu đề phòng học

    Lặp rows lần:
        In "*" * seats

Kết thúc chương trình
(2) Source code Python hoàn chỉnh
"""

# Nhập số lượng phòng học
total_rooms = int(input("Nhập số lượng phòng học: "))

# Kiểm tra số lượng phòng hợp lệ
if total_rooms <= 0:
    print("Số lượng phòng học không hợp lệ")

else:
    # Duyệt từng phòng học
    for room in range(total_rooms):

        print(f"\n--- Phòng học {room + 1} ---")

        # Nhập số hàng ghế
        rows = int(input("Nhập số hàng ghế: "))

        # Nhập số ghế mỗi hàng
        seats = int(input("Nhập số ghế mỗi hàng: "))

        # Edge Case 2:
        # Dữ liệu không hợp lệ
        if rows <= 0 or seats <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        # Edge Case 3:
        # Phòng quá lớn
        if rows > 10 or seats > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        # In sơ đồ chỗ ngồi
        print("Sơ đồ chỗ ngồi:")

        for row in range(rows):
            print("*" * seats)