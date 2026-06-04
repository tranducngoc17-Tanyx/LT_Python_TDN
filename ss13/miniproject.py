# Cấu trúc dữ liệu chính lưu trữ thông tin bãi xe
parking_lot = {}

# Biến đếm để tự động gán ID tăng dần
current_id = 1

# Đơn giá tính tiền (VNĐ/giờ)
PRICE_MOTO = 5000
PRICE_CAR = 20000

# Vòng lặp chính của chương trình
while True:
    # Hiển thị Menu
    print("\n" + "="*45)
    print(" HỆ THỐNG QUẢN LÝ BÃI XE")
    print("="*45)
    print("1. Quản lý vào bãi (Check-in)")
    print("2. Quản lý ra bãi (Check-out)")
    print("3. Hiển thị danh sách xe đang đỗ")
    print("4. Tìm kiếm phương tiện")
    print("5. Thoát chương trình (Exit)")
    print("="*45)

    # Nhập và kiểm tra lựa chọn từ menu bằng isdigit()
    choice_str = input("Chọn chức năng (1-5): ")
    if not choice_str.isdigit():
        print("ERR-05: [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue

    choice = int(choice_str)

    # Xử lý các chức năng
    if choice == 1:
        # --- 2.1 QUẢN LÝ VÀO BÃI (CHECK-IN) ---
        print("\n--- CHECK-IN ---")
        plate = input("Nhập biển số: ").strip()

        if not plate:
            print("[Lỗi]: Biển số không được để trống!")
            continue

        if plate in parking_lot:
            print("ERR-01: [Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
            continue

        # Nhập và kiểm tra loại xe
        while True:
            type_str = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ")
            if type_str.isdigit():
                vehicle_type = int(type_str)
                if vehicle_type in (1, 2):
                    break
                else:
                    print("ERR-02: [Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
            else:
                print("[Lỗi]: Vui lòng nhập số 1 hoặc 2!")

        # Nhập và kiểm tra giờ vào
        while True:
            entry_str = input("Nhập giờ vào (0-24): ")
            if entry_str.isdigit():
                entry_time = int(entry_str)
                if 0 <= entry_time <= 24:
                    break
                else:
                    print("[Lỗi]: Giờ vào phải nằm trong khoảng từ 0 đến 24!")
            else:
                print("[Lỗi]: Vui lòng nhập một số nguyên hợp lệ!")

        # Lưu dữ liệu vào hệ thống kèm theo ID
        parking_lot[plate] = {
            "id": current_id,
            "type": vehicle_type,
            "entry_time": entry_time
        }

        print(f"[Thành công]: Xe {plate} đã được đăng ký vào bãi với ID: {current_id}.")

        # Tăng ID lên 1 cho phương tiện tiếp theo
        current_id += 1

    elif choice == 2:
        # --- 2.2 QUẢN LÝ RA BÃI (CHECK-OUT) ---
        print("\n--- CHECK-OUT ---")
        if len(parking_lot) == 0:
            print("[Thông báo]: Bãi xe hiện đang trống!")
            continue

        plate = input("Nhập biển số cần check-out: ").strip()

        if plate not in parking_lot:
            print(f"ERR-04: [Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")
            continue

        # Nhập và kiểm tra giờ ra
        while True:
            exit_str = input("Nhập giờ ra (0-24): ")
            if exit_str.isdigit():
                exit_time = int(exit_str)
                if 0 <= exit_time <= 24:
                    break
                else:
                    print("[Lỗi]: Giờ ra phải nằm trong khoảng từ 0 đến 24!")
            else:
                print("[Lỗi]: Vui lòng nhập một số nguyên hợp lệ!")

        record = parking_lot[plate]

        # Kiểm tra logic thời gian
        if exit_time < record["entry_time"]:
            print("ERR-03: [Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
            continue

        # Tính phí
        hours_parked = exit_time - record["entry_time"]

        if record["type"] == 1:
            unit_price = PRICE_MOTO
        else:
            unit_price = PRICE_CAR

        fee = hours_parked * unit_price

        # Xóa bản ghi và xuất hóa đơn
        del parking_lot[plate]
        print(f"[Thành công]: Đã thanh toán cho xe {plate}. Thời gian đỗ: {hours_parked} giờ. Tổng tiền: {fee:,} VND.")

    elif choice == 3:
        # --- 2.3 BÁO CÁO & HIỂN THỊ ---
        print("\n--- DANH SÁCH XE ĐANG ĐỖ ---")
        if len(parking_lot) == 0:
            print("[Bãi xe hiện đang trống...]")
        else:
            # Thêm cột ID vào bảng hiển thị
            print(f"{'ID':<5} | {'Biển số':<15} | {'Loại xe':<10} | {'Giờ vào':<10}")
            print("-" * 50)
            for plate in parking_lot:
                details = parking_lot[plate]
                if details["type"] == 1:
                    type_str = "Xe máy"
                else:
                    type_str = "Ô tô"
                print(f"{details['id']:<5} | {plate:<15} | {type_str:<10} | {details['entry_time']:<10}")

    elif choice == 4:
        # --- TÌM KIẾM XE ---
        print("\n--- TÌM KIẾM XE ---")
        plate = input("Nhập biển số cần tìm: ").strip()
        if plate not in parking_lot:
            print(f"ERR-04: [Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")
        else:
            details = parking_lot[plate]
            if details["type"] == 1:
                type_str = "Xe máy"
            else:
                type_str = "Ô tô"
            print(f"[Thông tin]: Xe {plate} (ID: {details['id']}, Loại: {type_str}) vào bãi lúc {details['entry_time']} giờ.")

    elif choice == 5:
        # --- THOÁT CHƯƠNG TRÌNH ---
        print("[Hệ thống]: Đóng ứng dụng. Tạm biệt!")
        break

    else:
        # Xử lý trường hợp nhập số nguyên hợp lệ nhưng không nằm trong dải 1-5
        print("ERR-05: [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")