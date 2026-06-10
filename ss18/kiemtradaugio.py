products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products(products_list):
    if len(products_list) == 0:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
        return

    print(f"{'ID':<10} | {'Tên sản phẩm':<20} | {'Giá bán':<10}")
    print('-' * 50)
    for product in products_list:
        print(f"{product['id']:<10} | {product['name']:<20} | {product['price']:<10}")

def add_product(products_list):
    while True:
        product_id = input("Nhập ID: ")
        if product_id != "":
            break
        print("Max sản phâm không được để trống!")

    while True:
        product_name = input("Nhập tên sản phẩm: ")
        if product_name != "":
            break
        print("Tên sản phẩm không được để trống!")

    while True:
        try:
            product_price = int(input("Nhập giá bán: "))
            if product_price > 0:
                break
            print("Giá bán phải lớn hơn 0!")
        except ValueError:
            print("Giá bán phải là số nguyên!")

    product = {
        'id': product_id,
        'name': product_name,
        'price': product_price
    }

    products_list.append(product)
    print("Thêm sản phẩm thành công!")

def update_price(products_list):
    product_id = input("Nhập mã sản phẩm cần sửa giá: ")

    for product in products_list:
        if product['id'] == product_id:

            while True:
                try:
                    print(f"Tìm thấy sản phẩm: {product['name']} (Giá hiện tại: {product['price']})")
                    new_price = int(input("Nhập giá mới: "))
                    if new_price > 0:
                        product['price'] = new_price
                        print("Cập nhật giá thành công!")
                        return
                    print("Giá phải lớn hơn 0!")
                except ValueError:
                    print("Giá phải là số nguyên!")

    print(f"Không tìm thấy sản phẩm có mã {product_id}!")

def main():
    while True:
        print("QUẢN LÝ CỬA HÀNG - MINI STORE")
        print("1. Xem danh sách sản phẩm hiện có")
        print("2. Thêm mới một sản phẩm")
        print("3. Cập nhật giá sản phẩm theo ID")
        print("4. Thoát chương trình")
        choice = input("Nhập lựa chọn (1-4): ")

        match choice:
            case "1":
                show_products(products)
            case "2":
                add_product(products)
            case "3":
                update_price(products)
            case "4":
                print("Thoát chương trình")
                break
            case _:
                print("Không hợp lệ! Nhập lại")

main()