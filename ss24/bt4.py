class MenuItem:

    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value > 0:
            self.__base_price = value
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return int(
            self.__base_price
            + self.__base_price * MenuItem.service_charge
        )

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_id):

        if len(item_id) != 4:
            return False

        if not item_id[:2].isalpha():
            return False

        if not item_id[:2].isupper():
            return False

        if not item_id[2:].isdigit():
            return False

        return True


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]


def show_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")


def find_item(item_id):

    for item in menu_db:
        if item.item_id == item_id:
            return item

    return None


def display_menu():

    print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")

    for index, item in enumerate(menu_db, 1):

        status = "Đang bán"

        if not item.is_available:
            status = "Hết hàng"

        print(
            f"{index}. "
            f"Mã: {item.item_id} | "
            f"Tên: {item.item_name:<18} | "
            f"Trạng thái: {status:<10} | "
            f"Giá niêm yết: {item.calculate_selling_price():,} VNĐ"
        )


def add_new_item():

    print("\n--- THÊM MÓN MỚI VÀO MENU ---")

    item_id = input("Nhập mã món: ")

    if not MenuItem.is_valid_item_id(item_id):
        print("\nMã món không hợp lệ!")
        print("Mã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
        return

    if find_item(item_id) is not None:
        print("\nMã món đã tồn tại!")
        return

    item_name = input("Nhập tên món: ")
    base_price = int(input("Nhập giá gốc: "))

    if base_price <= 0:
        print("Giá đồ uống phải lớn hơn 0!")
        return

    menu_db.append(MenuItem(item_id, item_name, base_price))

    print("\nThêm món mới thành công!")


def update_status():

    print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")

    item_id = input("Nhập mã món cần cập nhật: ")

    item = find_item(item_id)

    if item is None:
        print("Không tìm thấy món!")
        return

    item.toggle_availability()

    if item.is_available:
        print(f">> Đã cập nhật {item.item_name} thành ĐANG BÁN!")
    else:
        print(f">> Đã cập nhật {item.item_name} thành HẾT HÀNG!")


def update_price():

    print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")

    item_id = input("Nhập mã món cần đổi giá: ")

    item = find_item(item_id)

    if item is None:
        print("Không tìm thấy món!")
        return

    new_price = int(input("Nhập giá tiền mới: "))

    item.base_price = new_price


def update_service_charge():

    print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")

    print(
        f"Phụ phí hiện tại: {MenuItem.service_charge * 100:.0f}%"
    )

    new_rate = float(
        input("Nhập phụ phí mới (Ví dụ 0.1 tương ứng 10%): ")
    )

    MenuItem.update_service_charge(new_rate)

    print("Cập nhật phụ phí dịch vụ thành công!")


def main():

    while True:

        show_menu()

        choice = input("Chọn chức năng (1-6): ")

        match choice:

            case "1":
                display_menu()

            case "2":
                add_new_item()

            case "3":
                update_status()

            case "4":
                update_price()

            case "5":
                update_service_charge()

            case "6":
                print("\nCảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()