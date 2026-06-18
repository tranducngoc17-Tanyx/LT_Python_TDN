# (1) PHÂN TÍCH LỖI (CODE REVIEW)
# Câu 1. Tại sao dòng print(f"Chiến binh {w1.name} xuất trận!") lại phát sinh lỗi AttributeError?

# Lỗi xảy ra do đối tượng w1 thuộc lớp Warrior không có thuộc tính name.

# Trong lớp cha Character, các thuộc tính:

# self.name = name
# self.hp = hp
# self.attack_power = attack_power

# được khởi tạo bên trong hàm:

# def __init__(self, name, hp, attack_power):

# Tuy nhiên, trong lớp Warrior, lập trình viên đã ghi đè (override) hàm __init__() nhưng lại không gọi hàm khởi tạo của lớp cha:

# class Warrior(Character):
#     def __init__(self, name, hp, attack_power, bonus_armor):
#         self.bonus_armor = bonus_armor

# Do đó khi tạo đối tượng:

# w1 = Warrior("Arthur", 1000, 150, 50)

# đối tượng chỉ có thuộc tính:

# self.bonus_armor

# mà không có:

# self.name
# self.hp
# self.attack_power

# Khi chương trình thực hiện:

# print(f"Chiến binh {w1.name} xuất trận!")

# Python không tìm thấy thuộc tính name nên phát sinh lỗi:

# AttributeError: 'Warrior' object has no attribute 'name'
# Cú pháp còn thiếu

# Để kế thừa đầy đủ thuộc tính từ lớp cha cần gọi:

# super().__init__(name, hp, attack_power)
# Câu 2. Nếu không dùng super().__init__(...), có thể gọi constructor của Character bằng cách nào?

# Có thể gọi trực tiếp hàm khởi tạo của lớp cha:

# Character.__init__(self, name, hp, attack_power)

# Ví dụ:

# class Warrior(Character):
#     def __init__(self, name, hp, attack_power, bonus_armor):
#         Character.__init__(self, name, hp, attack_power)
#         self.bonus_armor = bonus_armor

# Cách này vẫn hoạt động nhưng không được khuyến khích vì kém linh hoạt khi làm việc với đa kế thừa (Multiple Inheritance). Thực tế nên sử dụng:

# super().__init__(...)
# Câu 3. Nếu đã sửa lỗi kế thừa, chương trình sẽ gặp lỗi gì tại dòng if w1 > w2:?

# Sau khi bổ sung super().__init__(...), chương trình sẽ chạy được đến đoạn:

# if w1 > w2:

# Lúc này Python sẽ phát sinh lỗi:

# TypeError: '>' not supported between instances of 'Warrior' and 'Warrior'

# Nguyên nhân là Python không biết tiêu chí để so sánh hai đối tượng Warrior.

# Câu 4. Tại sao dấu > không hoạt động với hai đối tượng Warrior?

# Toán tử > hoạt động sẵn với các kiểu dữ liệu cơ bản như:

# 10 > 5

# Tuy nhiên w1 và w2 là các đối tượng do người dùng tự định nghĩa.

# Python không biết cần so sánh theo:

# Máu (hp)
# Sát thương (attack_power)
# Giáp (bonus_armor)
# Hay tổng sức mạnh chiến đấu

# Do đó nếu không được định nghĩa trước, Python không thể xử lý phép so sánh và sẽ phát sinh TypeError.

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


# Lớp con: Chiến binh cận chiến
class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        return self.get_total_power() > other.get_total_power()


# --- KỊCH BẢN MATCHMAKING ---

w1 = Warrior("Arthur", 1000, 150, 50)
w2 = Warrior("Lancelot", 900, 180, 10)

print(f"Chiến binh {w1.name} xuất trận!")

if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")