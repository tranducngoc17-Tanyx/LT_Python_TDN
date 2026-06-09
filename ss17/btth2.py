list_bus = []
def classify_status(empty_chair, total_chair):
    if empty_chair == 0:
        return "Hết vé"

    ratio = empty_chair / total_chair

    if ratio < 0.15:
        return "Hút khách"
    elif ratio <= 0.80:
        return "Bình thường"
    else:
        return "Ế khách"

def calculate_revenue(ticket_price, total_chair, empty_chair):
    sold_seat = total_chair - empty_chair
    return sold_seat * ticket_price


def find_bus_by_code(code):
    for bus in list_bus:
        if bus["ma_xe"] == code:
            return bus
    return None

def show_bus():
    if not list_bus:
        print("Danh sách chuyến xe trống!")
        return

    print("-" * 120)
    print(
        f"{'Mã CX':<10}"
        f"{'Tuyến đường':<30}"
        f"{'Giá vé':<15}"
        f"{'Ghế trống':<12}"
        f"{'Tổng ghế':<12}"
        f"{'Doanh thu':<15}"
        f"{'Trạng thái':<15}"
    )
    print("-" * 120)

    for bus in list_bus:
        print(
            f"{bus['ma_xe']:<10}"
            f"{bus['tuyen_duong']:<30}"
            f"{bus['gia_ve']:<15}"
            f"{bus['ghe_trong']:<12}"
            f"{bus['tong_ghe']:<12}"
            f"{bus['doanh_thu']:<15}"
            f"{bus['trang_thai']:<15}"
        )

def add_bus():
    code = input("Nhập mã CX: ").strip()

    if code == "":
        print("Mã chuyến xe không được để trống!")
        return

    if find_bus_by_code(code):
        print("Mã chuyến xe đã tồn tại!")
        return

    route = input("Nhập tuyến đường: ").strip()

    if route == "":
        print("Tuyến đường không được để trống!")
        return

    try:
        ticket_price = int(input("Nhập giá vé: "))
        total_chair = int(input("Nhập tổng số ghế: "))

        if ticket_price <= 0 or total_chair <= 0:
            print("Giá vé và tổng số ghế phải lớn hơn 0!")
            return

    except ValueError:
        print("Dữ liệu nhập không hợp lệ!")
        return

    empty_chair = total_chair
    revenue = 0
    status = classify_status(empty_chair, total_chair)

    bus = {
        "ma_xe": code,
        "tuyen_duong": route,
        "gia_ve": ticket_price,
        "ghe_trong": empty_chair,
        "tong_ghe": total_chair,
        "doanh_thu": revenue,
        "trang_thai": status
    }

    list_bus.append(bus)

    print("Thêm chuyến xe thành công!")

def book_ticket():
    code = input("Nhập mã chuyến xe: ").strip()

    bus = find_bus_by_code(code)

    if bus is None:
        print("Không tìm thấy chuyến xe!")
        return

    try:
        quantity = int(input("Nhập số vé cần đặt: "))

        if quantity <= 0:
            print("Số vé phải lớn hơn 0!")
            return

    except ValueError:
        print("Số vé không hợp lệ!")
        return

    if quantity > bus["ghe_trong"]:
        print("Không đủ ghế trống!")
        return

    bus["ghe_trong"] -= quantity

    bus["doanh_thu"] = calculate_revenue(
        bus["gia_ve"],
        bus["tong_ghe"],
        bus["ghe_trong"]
    )

    bus["trang_thai"] = classify_status(
        bus["ghe_trong"],
        bus["tong_ghe"]
    )

    print("Đặt vé thành công!")

def delete_bus():
    code = input("Nhập mã chuyến xe cần xóa: ").strip()

    bus = find_bus_by_code(code)

    if bus is None:
        print("Không tìm thấy chuyến xe!")
        return

    confirm = input(
        "Bạn có chắc muốn xóa chuyến xe này khỏi lịch trình không? (Y/N): "
    ).upper()

    if confirm == "Y":
        list_bus.remove(bus)
        print("Đã xóa chuyến xe!")
    else:
        print("Đã hủy thao tác.")

def search_bus():
    keyword = input(
        "Nhập mã CX hoặc tuyến đường cần tìm: "
    ).strip().lower()

    found = False

    print("-" * 120)

    for bus in list_bus:
        if (
            keyword == bus["ma_xe"].lower()
            or keyword in bus["tuyen_duong"].lower()
        ):
            found = True

            print(
                f"{bus['ma_xe']:<10}"
                f"{bus['tuyen_duong']:<30}"
                f"{bus['gia_ve']:<15}"
                f"{bus['ghe_trong']:<12}"
                f"{bus['tong_ghe']:<12}"
                f"{bus['doanh_thu']:<15}"
                f"{bus['trang_thai']:<15}"
            )

    if not found:
        print("Không tìm thấy chuyến xe!")

def statistic_status():
    het_ve = 0
    hut_khach = 0
    binh_thuong = 0
    e_khach = 0

    for bus in list_bus:
        status = bus["trang_thai"]

        if status == "Hết vé":
            het_ve += 1
        elif status == "Hút khách":
            hut_khach += 1
        elif status == "Bình thường":
            binh_thuong += 1
        elif status == "Ế khách":
            e_khach += 1

    print("\nTHỐNG KÊ TRẠNG THÁI")
    print("Hết vé:", het_ve)
    print("Hút khách:", hut_khach)
    print("Bình thường:", binh_thuong)
    print("Ế khách:", e_khach)

def refresh_status():
    for bus in list_bus:
        bus["trang_thai"] = classify_status(
            bus["ghe_trong"],
            bus["tong_ghe"]
        )

    print("Đã cập nhật trạng thái cho toàn bộ chuyến xe!")

def main():
    while True:
        print("\n===== QUẢN LÝ CHUYẾN XE =====")

        choice = input("""
1. Hiển thị danh sách chuyến xe
2. Khai báo chuyến xe mới
3. Cập nhật đặt vé
4. Hủy chuyến xe
5. Tìm kiếm chuyến xe
6. Thống kê trạng thái
7. Phân loại trạng thái tự động
8. Thoát chương trình

Nhập lựa chọn (1-8): """)

        match choice:
            case "1":
                show_bus()
            case "2":
                add_bus()
            case "3":
                book_ticket()
            case "4":
                delete_bus()
            case "5":
                search_bus()
            case "6":
                statistic_status()
            case "7":
                refresh_status()
            case "8":
                print("Cảm ơn đã sử dụng chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
main()