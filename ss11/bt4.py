# (1) phân tích và thiết kế giải pháp

# 1. Phân tích Input

# Dữ liệu đầu vào gồm:
# - Lựa chọn menu (1-5)
# - Mã sản phẩm cần bán (str)
# - Số lượng khách mua (int)
# - Mã sản phẩm cần nhập kho (str)
# - Số lượng nhập thêm (int)

# 2. Phân tích Output

# Chương trình cần:
# - Hiển thị danh sách sản phẩm hiện có
# - Hiển thị trạng thái tồn kho của từng sản phẩm
# - Thông báo bán hàng thành công
# - Hiển thị số tiền khách cần thanh toán
# - Thông báo nhập kho thành công
# - Hiển thị báo cáo doanh thu
# - Hiển thị sản phẩm bán chạy nhất
# - Thông báo lỗi khi dữ liệu không hợp lệ
# - Thoát chương trình khi chọn chức năng 5

# 3. Cấu trúc dữ liệu sử dụng

# Sử dụng list để lưu danh sách sản phẩm.

# Mỗi sản phẩm được lưu bằng dictionary:

# {
#     "product_id": "SP001",
#     "product_name": "Áo polo nam",
#     "price": 299000,
#     "quantity": 20,
#     "sold": 5
# }

# 4. Giải pháp xử lý

# Chức năng 1:
# - Kiểm tra danh sách sản phẩm có rỗng hay không.
# - Duyệt danh sách bằng vòng lặp for.
# - Hiển thị thông tin từng sản phẩm.
# - Xác định trạng thái tồn kho:
#     + quantity == 0 => Hết hàng
#     + quantity <= 5 => Sắp hết hàng
#     + quantity > 5 => Còn hàng

# Chức năng 2:
# - Nhập mã sản phẩm cần bán.
# - Chuẩn hóa mã sản phẩm bằng strip() và upper().
# - Tìm sản phẩm trong danh sách.
# - Kiểm tra sản phẩm có tồn tại hay không.
# - Nhập số lượng mua.
# - Kiểm tra số lượng mua hợp lệ.
# - Kiểm tra tồn kho có đủ hay không.
# - Nếu hợp lệ:
#     + Giảm tồn kho.
#     + Tăng số lượng đã bán.
#     + Tính tiền thanh toán.

# Chức năng 3:
# - Nhập mã sản phẩm cần nhập kho.
# - Chuẩn hóa mã sản phẩm.
# - Tìm sản phẩm trong danh sách.
# - Kiểm tra sản phẩm có tồn tại hay không.
# - Nhập số lượng nhập thêm.
# - Kiểm tra số lượng nhập hợp lệ.
# - Nếu hợp lệ:
#     + Cộng thêm số lượng vào tồn kho.

# Chức năng 4:
# - Duyệt danh sách sản phẩm.
# - Tính doanh thu từng sản phẩm:
#     doanh_thu = price * sold
# - Tính tổng doanh thu cửa hàng.
# - Tìm sản phẩm có số lượng bán cao nhất.
# - Hiển thị báo cáo doanh thu.
# - Nếu chưa có sản phẩm nào bán:
#     + Hiển thị thông báo chưa có doanh thu.

# Chức năng 5:
# - Hiển thị thông báo thoát chương trình.
# - Kết thúc vòng lặp.

# 5. Kiểm tra dữ liệu hợp lệ

# Bẫy 1:
# - Người dùng nhập mã sản phẩm có khoảng trắng hoặc viết thường.
# - Xử lý bằng:
#   product_id = product_id.strip().upper()

# Bẫy 2:
# - Mã sản phẩm không tồn tại khi bán hàng hoặc nhập kho.
# - Thông báo:
#   "Không tìm thấy sản phẩm cần bán/Nhập kho"

# Bẫy 3:
# - Số lượng mua hoặc nhập kho là chữ.
# - Số lượng <= 0.
# - Thông báo:
#   "Số lượng mua/Nhập kho không hợp lệ"

# Bẫy 4:
# - Số lượng mua vượt quá tồn kho.
# - Thông báo:
#   "Số lượng trong kho không đủ để bán"

# Bẫy 5:
# - Người dùng nhập menu ngoài phạm vi 1-5.
# - Thông báo:
#   "Lựa chọn không hợp lệ, vui lòng nhập lại!"

# 6. Thuật toán tổng quát

# Bước 1: Khởi tạo danh sách product_list

# Bước 2: Hiển thị menu

# Bước 3: Nhận lựa chọn từ người dùng

# Bước 4:
# Thực hiện chức năng tương ứng:
# 1: Hiển thị sản phẩm
# 2: Bán sản phẩm
# 3: Nhập thêm hàng
# 4: Xem báo cáo doanh thu
# 5: Thoát

# Bước 5: Sau khi xử lý xong quay lại menu

# Bước 6: Kết thúc chương trình khi chọn 5

# (2) triển khai code
# (2) TRIỂN KHAI CODE

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("====HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY=====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            for i in range(len(product_list)):
                product = product_list[i]
                
                if product["quantity"] == 0:
                    status = "Hết hàng"
                elif product["quantity"] <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"

                print(
                    str(i + 1) +
                    ". Mã SP: " + product["product_id"] +
                    " | Tên: " + product["product_name"] +
                    " | Giá: " + str(product["price"]) +
                    " | Tồn kho: " + str(product["quantity"]) +
                    " | Đã bán: " + str(product["sold"]) +
                    " | Trạng thái: " + status
                )

    elif choice == "2":
        product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True
                quantity_buy = input("Nhập số lượng khách mua: ")

                if not quantity_buy.isdigit():
                    print("Số lượng mua không hợp lệ")
                else:
                    quantity_buy = int(quantity_buy)

                    if quantity_buy <= 0:
                        print("Số lượng mua không hợp lệ")
                    elif quantity_buy > product["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                    else:
                        product["quantity"] -= quantity_buy
                        product["sold"] += quantity_buy

                        total_money = (quantity_buy * product["price"])

                        print("Bán sản phẩm thành công")
                        print("Khách cần thanh toán:",total_money)
                break
            
        if found == False:
            print("Không tìm thấy sản phẩm cần bán")

    elif choice == "3":
        product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                quantity_import = input("Nhập số lượng nhập thêm: ")

                if not quantity_import.isdigit():
                    print("Số lượng nhập kho không hợp lệ")
                else:
                    quantity_import = int(quantity_import)

                    if (quantity_import <= 0):
                        print("Số lượng nhập kho không hợp lệ")
                    else:
                        product["quantity"] += (quantity_import)

                        print("Nhập kho thành công")
                        print("Tồn kho hiện tại:", product["quantity"])
                break

        if (found == False):
            print("Không tìm thấy sản phẩm cần nhập kho" )

    elif choice == "4":
        total_revenue = 0
        max_sold = 0
        best_seller = ""

        has_revenue = False
        print("=== BÁO CÁO DOANH THU CỬA HÀNG YODY ===")

        for i in range(len(product_list)):
            product = product_list[i]
            revenue = (product["price"] * product["sold"])

            total_revenue += revenue

            if product["sold"] > 0:
                has_revenue = True

            print(
                f"{i + 1}. {product['product_name']} | "
                f"Đã bán: {product['sold']} | "
                f"Doanh thu: {revenue}"
            )

            if product["sold"] > max_sold:
                max_sold = product["sold"]
                best_seller = product["product_name"]

        if has_revenue:
            print("Tổng doanh thu:", total_revenue)
            print("Sản phẩm bán chạy nhất:", best_seller)
        else:
            print("Chưa có doanh thu phát sinh.")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")