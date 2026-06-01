sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
order_code = ""
delivery_note = ""

while True:
    print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa trong ghi chú giao hàng")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn 1-5: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    if choice == "1":
        sender_name = input("Nhập tên người gửi: ")
        sender_phone = input("Nhập số điện thoại người gửi: ")
        pickup_address = input("Nhập địa chỉ lấy hàng: ")
        receiver_name = input("Nhập tên người nhận: ")
        receiver_phone = input("Nhập số điện thoại người nhận: ")
        delivery_address = input("Nhập địa chỉ giao hàng: ")
        order_code = input("Nhập mã đơn hàng: ")
        delivery_note = input("Nhập ghi chú giao hàng: ")

        if sender_name.strip() == "":
            print("Tên người gửi không được bỏ trống")
            continue

        if sender_phone.strip() == "":
            print("Số điện thoại người gửi không được bỏ trống")
            continue

        if pickup_address.strip() == "":
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue

        if receiver_name.strip() == "":
            print("Tên người nhận không được bỏ trống")
            continue

        if receiver_phone.strip() == "":
            print("Số điện thoại người nhận không được bỏ trống")
            continue

        if delivery_address.strip() == "":
            print("Địa chỉ giao hàng không được bỏ trống")
            continue

        if order_code.strip() == "":
            print("Mã đơn hàng không được bỏ trống")
            continue

        if delivery_note.strip() == "":
            print("Ghi chú giao hàng không được bỏ trống")
            continue

        sender_name = sender_name.strip().title()
        receiver_name = receiver_name.strip().title()
        pickup_address = pickup_address.strip()
        delivery_address = delivery_address.strip()
        delivery_note = delivery_note.strip()

        print("\n===== BÁO CÁO THỐNG KÊ =====")
        print("Tên người gửi:", sender_name)
        print("Tên người nhận:", receiver_name)
        print("Địa chỉ lấy hàng:", pickup_address)
        print("Địa chỉ giao hàng:", delivery_address)
        print("Ghi chú giao hàng:", delivery_note)
        print("Độ dài ghi chú:", len(delivery_note))
        print("Số lượng từ:", len(delivery_note.split()))
        print("Ghi chú chữ thường:", delivery_note.lower())
        print("Ghi chú chữ hoa:", delivery_note.upper())

    elif choice == "2":
        if order_code.strip() == "":
            print("Chưa có mã đơn hàng")
            continue

        normalized_order_code = order_code.strip().upper()
        normalized_order_code = normalized_order_code.replace(" ", "-")

        if not normalized_order_code.startswith("GRAB-"):
            normalized_order_code = "GRAB-" + normalized_order_code

        print("Mã đơn hàng ban đầu:", order_code)
        print("Mã đơn hàng chuẩn hóa:", normalized_order_code)

    elif choice == "3":
        if not sender_phone.isdigit():
            print("Số điện thoại người gửi không hợp lệ")
            continue

        if len(sender_phone) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            continue

        if not receiver_phone.isdigit():
            print("Số điện thoại người nhận không hợp lệ")
            continue

        if len(receiver_phone) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            continue

        hidden_sender_phone = sender_phone[:3] + "*****" + sender_phone[-2:]
        hidden_receiver_phone = receiver_phone[:3] + "*****" + receiver_phone[-2:]

        print("SĐT người gửi:", hidden_sender_phone)
        print("SĐT người nhận:", hidden_receiver_phone)

    elif choice == "4":
        if delivery_note.strip() == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue

        find_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")

        if find_keyword in delivery_note:
            count = delivery_note.count(find_keyword)
            delivery_note = delivery_note.replace(find_keyword, replace_keyword)

            print("Số lần xuất hiện của từ khóa:", count)
            print("Ghi chú giao hàng sau khi thay thế:")
            print(delivery_note)
        else:
            print("Không tìm thấy từ khóa trong ghi chú giao hàng")

    elif choice == "5":
        print("Thoát chương trình")
        break