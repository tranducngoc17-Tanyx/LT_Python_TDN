class CoffeeOrder:
    # Class Attribute
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    # Chỉ đọc tổng tiền
    @property
    def total_amount(self):
        return self.__total_amount

    # Thêm món
    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    # Tính hóa đơn
    def calculate_final_bill(self):
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    # Cập nhật VAT cho toàn hệ thống
    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate

# Kiểm chứng chương trình
order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

# Gọi món
order_table1.add_item(50000)
order_table2.add_item(30000)

print("Tổng tiền bàn 1:", order_table1.total_amount)
print("Tổng tiền bàn 2:", order_table2.total_amount)

# Thử sửa trực tiếp
try:
    order_table1.total_amount = 0
except AttributeError:
    print("\nKhông thể sửa trực tiếp total_amount!")

# Cập nhật VAT toàn hệ thống
CoffeeOrder.update_vat_rate(0.08)

print("\nVAT mới của bàn 1:", order_table1.vat_rate)
print("VAT mới của bàn 2:", order_table2.vat_rate)

print("\nHóa đơn bàn 1:", order_table1.calculate_final_bill())
print("Hóa đơn bàn 2:", order_table2.calculate_final_bill())