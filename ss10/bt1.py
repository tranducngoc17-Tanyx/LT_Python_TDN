cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n===== MENU =====")
    print("1. Xem gio hang")
    print("2. Them san pham")
    print("3. Cap nhat so luong")
    print("4. Xoa san pham")
    print("5. Thoat")

    choice = input("Nhap lua chon: ")

    if choice == "1":
        tong_so_luong = 0
        tong_tien = 0

        print("\n===== GIO HANG =====")

        for item in cart_items:
            print(item)

            tong_so_luong += item[2]
            tong_tien += item[2] * item[3]

        print("Tong so luong:", tong_so_luong)
        print("Tong tien:", tong_tien)

    elif choice == "2":
        ma_sp = input("Nhap ma san pham: ")
        ten_sp = input("Nhap ten san pham: ")

        so_luong = int(input("Nhap so luong: "))
        don_gia = int(input("Nhap don gia: "))

        if so_luong <= 0 or don_gia < 0:
            print("Du lieu khong hop le!")
            continue

        ton_tai = False

        for item in cart_items:
            if ma_sp == item[0]:
                item[2] += so_luong
                ton_tai = True
                print("Da cong don so luong.")
                break

        if ton_tai == False:
            cart_items.append([ma_sp, ten_sp, so_luong, don_gia])
            print("Them san pham thanh cong.")

    elif choice == "3":
        ma_sp = input("Nhap ma san pham: ")
        so_luong_moi = int(input("Nhap so luong moi: "))

        if so_luong_moi <= 0:
            print("So luong khong hop le!")
            continue

        tim_thay = False

        for item in cart_items:
            if ma_sp == item[0]:
                item[2] = so_luong_moi
                tim_thay = True
                print("Cap nhat thanh cong.")
                break

        if tim_thay == False:
            print("Ma san pham khong ton tai trong gio hang.")

    elif choice == "4":
        ma_sp = input("Nhap ma san pham can xoa: ")

        tim_thay = False

        for item in cart_items:
            if ma_sp == item[0]:
                cart_items.remove(item)
                tim_thay = True
                print("Xoa thanh cong.")
                break

        if tim_thay == False:
            print("Ma san pham khong ton tai trong gio hang.")

    elif choice == "5":
        print("Thoat chuong trinh.")
        break

    else:
        print("Lua chon khong hop le!")