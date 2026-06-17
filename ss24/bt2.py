class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0
        self.points = points

    # Getter
    @property
    def points(self):
        return self.__points

    # Setter kiểm tra dữ liệu
    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    # Cộng điểm
    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print("Điểm cộng không hợp lệ!")

    # Static Method kiểm tra voucher
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000

# Kịch bản kiểm thử
card1 = MemberCard("Le Van C", 100)

print("Điểm ban đầu:", card1.points)

# Thử gán điểm âm
card1.points = -50

print("Điểm sau khi gán sai:", card1.points)

# Gọi trực tiếp từ Class
result = MemberCard.is_eligible_for_voucher(250000)

print("Khách hàng:", card1.customer_name)
print("Điểm hiện tại:", card1.points)
print("Hóa đơn 250000 có được tặng Voucher không?", result)