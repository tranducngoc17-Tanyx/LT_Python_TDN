while True:
    print("HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPPE")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
    print("5. Thoát chương trình")
    choice = input("> Mời bạn chọn chức năng (1-5): ")
    
    # CN1: Nhập dữ liệu sản phẩm và xem báo cáo thống kê
    if choice == "1":
        shop_name = input('Nhập tên shop: ')
        product_name = input('Nhập tên sản phẩm: ')
        describe = input('Mô tả sản phẩm: ')
        product_catalog = input('Nhập danh mục sản phẩm: ')
        list_keyword = input('Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ') 
        
        print("=== BÁO CÁO THỐNG KÊ ===")
        print(f"Tên shop: {shop_name.strip()}")
        print(f"Tên sản phẩm: {product_name.strip() .title()}")
        print(f"Mô tả sản phẩm: {describe.strip()}")
        print(f"Độ dài mô tả sản phẩm: {len(describe)}")
        print(f"Danh mục sản phẩm sau khi chuẩn hóa: {product_catalog.lower() .split(',')}")
        print(f"Danh sách từ khóa sau khi chuẩn hóa: {list_keyword.split()}")
        
        num_keyword = list_keyword.split(",")
        print(f"Số lượng từ khóa tìm kiếm: {len(num_keyword)}")
        
        print(f"Mô tả sản phẩm sang chữ thường: {describe.lower()}")
        print(f"Mô tả sản phẩm sang chữ thường: {describe.upper()}")
        
    # CN2: Chuẩn hóa tên Shop
    elif choice == "2":
        print(f"Tên shop ban đầu: {shop_name}")

        shop_name = shop_name.strip() .lower()
        shop_name = shop_name.replace(" ", "-")

        if not shop_name.startswith("shop-"):
            shop_name = "shop-" + shop_name

        print(f"Tên shop sau khi chuẩn hóa: {shop_name}")
    
    # CN3: Kiểm tra mã giảm giá hợp lệ
    elif choice == "3":
        discount_code = input("Nhập mã giảm giá: ")

        if discount_code == "":
            print("Mã giảm giá không được rỗng")
        elif " " in discount_code:
            print("Mã giảm giá không được chứa khoảng trắng")
        elif len(discount_code) < 6 or len(discount_code) > 12:
            print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
        elif discount_code != discount_code.upper():
            print("Mã giảm giá phải được viết hoa toàn bộ")
        elif not discount_code.isalnum():
            print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
        elif not discount_code.startswith("SALE"):
            print("Mã giảm giá phải bắt đầu bằng SALE")
        else:
            print("Mã giảm giá hợp lệ")

            discount_list = []
            discount_list.append(discount_code)

            print(f"Danh sách mã giảm giá hiện tại: {discount_list}")
    
    # CN4: Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm
    elif choice == "4":
        keyword_find = input("Nhập từ khóa cần tìm: ")
        keyword_replace = input("Nhập từ khóa thay thế: ")

        if keyword_find in describe:
            print(f"Số lần xuất hiện của từ khóa: {describe.count(keyword_find)}")

            new_describe = describe.replace(keyword_find, keyword_replace)

            print(f"Mô tả sau khi thay thế: {new_describe}")
        else:
            print("Không tìm thấy từ khóa trong mô tả sản phẩm")
            
    # CN5: Thoát
    elif choice == "5":
        print("Thoát chương trình")
        break
    else:
        print("Vui lòng nhập lại!")
        
    