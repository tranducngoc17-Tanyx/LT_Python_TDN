class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    @staticmethod
    def is_valid_card_id(card_id):
        if len(card_id) != 4:
            return False

        if card_id[:2] != "RC":
            return False

        if not card_id[2:].isdigit():
            return False

        return True

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned

        upgraded = False

        if self.__points >= 100 and self.__tier == "Standard":
            self.__tier = "VIP"
            upgraded = True

        return earned, upgraded

    def redeem_points(self, points_to_use):
        if points_to_use <= 0:
            return False, 0

        if points_to_use > self.__points:
            return False, 0

        self.__points -= points_to_use

        discount = points_to_use * MemberCard.point_value_vnd

        return True, discount

    @classmethod
    def update_point_value(cls, new_value):
        if new_value > 0:
            cls.point_value_vnd = new_value


cards_database = []

card1 = MemberCard("RC01", "Nguyen Van A")
card1.earn_points(1500000)

card2 = MemberCard("RC02", "Tran Thi B")
card2.earn_points(200000)

cards_database.append(card1)
cards_database.append(card2)


while True:

    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")

    choice = input("Chọn chức năng (1-6): ")

    match choice:

        case "1":

            print("\nDANH SÁCH THẺ THÀNH VIÊN")

            if len(cards_database) == 0:
                print("Chưa có dữ liệu.")
            else:
                for i, card in enumerate(cards_database, 1):
                    print(
                        f"{i}. Mã: {card.card_id} | "
                        f"Tên: {card.name} | "
                        f"Điểm: {card.points} | "
                        f"Hạng: {card.tier}"
                    )

        case "2":

            print("\n--- ĐĂNG KÝ THẺ MỚI ---")

            card_id = input("Nhập mã thẻ: ").upper()

            if not MemberCard.is_valid_card_id(card_id):
                print("Mã thẻ không hợp lệ!")
                continue

            exist = False

            for card in cards_database:
                if card.card_id == card_id:
                    exist = True
                    break

            if exist:
                print("Mã thẻ đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên khách hàng: ")

            new_card = MemberCard(card_id, name)

            cards_database.append(new_card)

            print("\nĐăng ký thành công!")
            print("Mã thẻ:", new_card.card_id)
            print("Tên:", new_card.name)
            print("Điểm:", new_card.points)
            print("Hạng:", new_card.tier)

        case "3":

            print("\n--- KHÁCH MUA HÀNG ---")

            card_id = input("Nhập mã thẻ: ").upper()

            target = None

            for card in cards_database:
                if card.card_id == card_id:
                    target = card
                    break

            if target is None:
                print("Không tìm thấy thẻ.")
                continue

            bill = int(input("Nhập tổng tiền hóa đơn: "))

            earned, upgraded = target.earn_points(bill)

            print("\nKhách hàng:", target.name)
            print(f"Hóa đơn: {bill:,} VNĐ")
            print("Điểm được tích:", earned)
            print("Tổng điểm:", target.points)

            if upgraded:
                print("Chúc mừng! Khách hàng đã được nâng hạng VIP.")

            print("Hạng:", target.tier)

        case "4":

            print("\n--- ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

            card_id = input("Nhập mã thẻ: ").upper()

            target = None

            for card in cards_database:
                if card.card_id == card_id:
                    target = card
                    break

            if target is None:
                print("Không tìm thấy thẻ.")
                continue

            use = int(input("Nhập số điểm muốn dùng: "))

            success, discount = target.redeem_points(use)

            if success:
                print(f"\nĐã trừ {use} điểm.")
                print(f"Khách hàng được giảm giá {discount:,} VNĐ.")
                print("Số điểm còn lại:", target.points)
                print("Hạng:", target.tier)
            else:
                print("\nKhông thể đổi điểm!")
                print("Số điểm muốn sử dụng vượt quá số điểm hiện có hoặc không hợp lệ.")
                print("Điểm hiện tại:", target.points)

        case "5":

            print("\n--- CẬP NHẬT TỶ GIÁ ---")
            print(
                f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
            )

            value = int(input("Nhập tỷ giá mới: "))

            MemberCard.update_point_value(value)

            print("Cập nhật thành công!")
            print(
                f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
            )

        case "6":

            print("\nCảm ơn bạn đã sử dụng hệ thống!")
            break

        case _:

            print("Lựa chọn không hợp lệ!")