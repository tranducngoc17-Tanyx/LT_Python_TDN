# (1) Phân tích và thiết kể giải pháp

# 1. Phân tích Input

# Dữ liệu đầu vào gồm:
# - Lựa chọn menu (1-5)
# - Mã sản phẩm (str)
# - Tên sản phẩm (str)
# - Giá sản phẩm (int)
# - Số lượng sản phẩm (int)

# 2. Phân tích Output

# Chương trình cần:
# - Hiển thị danh sách sản phẩm
# - Thông báo thêm sản phẩm thành công
# - Thông báo cập nhật thành công
# - Thông báo xóa thành công
# - Thông báo lỗi khi dữ liệu không hợp lệ
# - Thoát chương trình khi chọn chức năng 5

# 3. Cấu trúc dữ liệu sử dụng

# Sử dụng list để lưu danh sách sản phẩm.

# Mỗi sản phẩm được lưu bằng dictionary:

# {
#     "product_id": "SP001",
#     "product_name": "Áo polo nam",
#     "price": 299000,
#     "quantity": 20
# }

# 4. Giải pháp xử lý

# Chức năng 1:
# - Duyệt danh sách bằng vòng lặp for.
# - Hiển thị toàn bộ sản phẩm.
# - Nếu danh sách rỗng thì thông báo.

# Chức năng 2:
# - Nhập thông tin sản phẩm mới.
# - Chuẩn hóa mã sản phẩm bằng strip() và upper().
# - Kiểm tra mã sản phẩm có bị trùng hay không.
# - Kiểm tra giá và số lượng phải lớn hơn 0.
# - Tạo dictionary mới.
# - Dùng append() để thêm vào product_list.

# Chức năng 3:
# - Nhập mã sản phẩm cần cập nhật.
# - Chuẩn hóa mã sản phẩm.
# - Tìm sản phẩm trong danh sách.
# - Nếu tìm thấy:
#     + Cập nhật tên sản phẩm.
#     + Cập nhật giá sản phẩm.
#     + Cập nhật số lượng tồn kho.
# - Nếu không tìm thấy:
#     + Thông báo lỗi.

# Chức năng 4:
# - Nhập mã sản phẩm cần xóa.
# - Chuẩn hóa mã sản phẩm.
# - Tìm sản phẩm trong danh sách.
# - Nếu tìm thấy:
#     + Xóa sản phẩm bằng remove().
# - Nếu không tìm thấy:
#     + Thông báo lỗi.

# Chức năng 5:
# - Hiển thị thông báo thoát chương trình.
# - Kết thúc vòng lặp.

# 5. Kiểm tra dữ liệu hợp lệ

# Bẫy 1:
# - Người dùng nhập mã sản phẩm có khoảng trắng hoặc viết thường.
# - Xử lý bằng:
#   product_id = product_id.strip().upper()

# Bẫy 2:
# - Mã sản phẩm bị trùng.
# - Kiểm tra product_id trước khi thêm.

# Bẫy 3:
# - Mã sản phẩm không tồn tại khi cập nhật hoặc xóa.
# - Thông báo lỗi cho người dùng.

# Bẫy 4:
# - Giá hoặc số lượng là chữ.
# - Giá hoặc số lượng <= 0.
# - Thông báo:
#   "Giá/Số lượng không hợp lệ"

# Bẫy 5:
# - Người dùng nhập menu ngoài phạm vi 1-5.
# - Thông báo:
#   "Lựa chọn không hợp lệ, vui lòng nhập lại!"

# 6. Thuật toán tổng quát

# Bước 1:khởi tạo danh sách product_list

# Bước 2: Hiển thị menu

# Bước 3: Nhận lựa chọn từ người dùng

# Bước 4:
# Thực hiện chức năng tương ứng:
# 1: Hiển thị danh sách
# 2: Thêm sản phẩm
# 3: Cập nhật sản phẩm
# 4: Xóa sản phẩm
# 5: Thoát

# Bước 5: Sau khi xử lý xong quay lại menu
# Bước 6: Kết thúc chương trình khi chọn 5

# (2) Triển khai code
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")
            for i in range(len(product_list)):
                product = product_list[i]

                print(
                    str(i + 1) +
                    ". Mã SP: " + product["product_id"] +
                    " | Tên: " + product["product_name"] +
                    " | Giá: " + str(product["price"]) +
                    " | Số lượng: " + str(product["quantity"])
                )

    elif choice == "2":
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        is_duplicate = False

        for product in product_list:
            if product["product_id"] == product_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("Mã sản phẩm bị trùng")
        else:
            product_name = input("Nhập tên sản phẩm: ")

            price = input("Nhập giá sản phẩm: ")
            quantity = input("Nhập số lượng sản phẩm: ")

            if not price.isdigit() or not quantity.isdigit():
                print("Giá/Số lượng không hợp lệ")
            else:
                price = int(price)
                quantity = int(quantity)

                if price <= 0 or quantity <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    new_product = {
                        "product_id": product_id,
                        "product_name": product_name,
                        "price": price,
                        "quantity": quantity
                    }

                    product_list.append(new_product)
                    print("Thêm sản phẩm thành công")

    elif choice == "3":
        update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        found = False

        for product in product_list:
            if product["product_id"] == update_id:
                found = True
                product_name = input("Nhập tên mới: ")
                price = input("Nhập giá mới: ")
                quantity = input("Nhập số lượng mới: ")

                if not price.isdigit() or not quantity.isdigit():
                    print("Giá/Số lượng không hợp lệ")
                else:
                    price = int(price)
                    quantity = int(quantity)

                    if price <= 0 or quantity <= 0:
                        print("Giá/Số lượng không hợp lệ")
                    else:
                        product["product_name"] = product_name
                        product["price"] = price
                        product["quantity"] = quantity

                        print("Cập nhật sản phẩm thành công")
                break
            
        if found == False:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    elif choice == "4":
        del_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        found = False

        for product in product_list:
            if product["product_id"] == del_id:
                product_list.remove(product)
                found = True
                print("Xóa sản phẩm thành công")
                break

        if found == False:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
