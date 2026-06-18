# # RPG BLACKSMITH SYSTEM - DESIGN DOCUMENT

# ## 1. Vai trò Equipment (ABC)

# Equipment là lớp trừu tượng đại diện cho mọi trang bị trong game.

# ### Mục đích:
# - Ép tất cả trang bị phải có:
#   → calculate_total_damage()

# ### Lợi ích:
# - Ngăn tạo class không có logic tính sát thương
# - Ví dụ:
#   class Bow(Equipment): pass  -> bị chặn ngay

# => Đảm bảo mọi vũ khí đều "có công thức damage rõ ràng"

# ---

# ## 2. Polymorphism

# Inventory chứa nhiều loại object:
# - Weapon
# - MagicSword

# Khi duyệt:

# for item in inventory:
#     item.calculate_total_damage()

# => Không cần biết object là gì
# => Đây là runtime polymorphism (Duck typing + ABC)

# ---

# ## 3. Multiple Inheritance & MRO

# MagicSword kế thừa:

# class MagicSword(Weapon, MagicMixin)

# ### MRO:
# MagicSword → Weapon → MagicMixin → Equipment → object

# ### Nguyên tắc init:
# - Weapon init: name, base_damage, upgrade_level
# - MagicMixin init: magic_power

# => dùng super() theo MRO để không mất attribute

# ---

# ## 4. Operator Overloading

# ### __gt__:
# So sánh sức mạnh dựa trên:
# calculate_total_damage()

# Return:
# → True / False

# ---

# ### __add__:
# Dung hợp 2 Weapon:

# Input:
# - other: Equipment

# Output:
# - Weapon mới

# Công thức:
# - name = self.name
# - base_damage = self.base_damage + other.base_damage
# - upgrade_level = self.upgrade + other.upgrade

# ---

# ## 5. Edge Cases

# - Không cho instantiate Equipment
# - Không cho + hoặc > với number
# - MagicSword phải đủ magic_power
from abc import ABC, abstractmethod
class Equipment(ABC):

    @abstractmethod
    def calculate_total_damage(self):
        pass

class MagicMixin:
    def __init__(self, magic_power=0, **kwargs):
        self.magic_power = magic_power
        super().__init__(**kwargs)

    def cast_glow(self):
        print(f"{self.name} phát sáng ánh phép thuật!")

class Weapon(Equipment):

    def __init__(self, name, base_damage, upgrade_level=0):
        if base_damage <= 0 or upgrade_level < 0:
            raise ValueError("Giá trị phải lớn hơn 0!")

        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể so sánh giữa các trang bị!")
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể dung hợp giữa các trang bị!")

        if not isinstance(other, Weapon):
            raise TypeError("Chỉ Weapon mới có thể dung hợp!")

        new_name = self.name
        new_base = self.base_damage + other.base_damage
        new_upgrade = self.upgrade_level + other.upgrade_level

        return Weapon(new_name, new_base, new_upgrade)

class MagicSword(Weapon, MagicMixin):

    def __init__(self, name, base_damage, upgrade_level, magic_power):
        super().__init__(
            name=name,
            base_damage=base_damage,
            upgrade_level=upgrade_level,
            magic_power=magic_power
        )

    def calculate_total_damage(self):
        return self.base_damage + (self.upgrade_level * 10) + self.magic_power

inventory = []

def input_positive_int(msg):
    while True:
        try:
            value = int(input(msg))
            if value <= 0:
                print("Giá trị phải lớn hơn 0!")
                continue
            return value
        except:
            print("Dữ liệu không hợp lệ!")

def show_inventory():
    if not inventory:
        print("\nKho vũ khí hiện đang trống.")
        return

    print("\n--- KHO VŨ KHÍ ---")
    print("STT | Tên | Loại | Cấp | Sát thương")
    print("-" * 50)

    for i, item in enumerate(inventory, 1):
        print(f"{i} | {item.name} | {type(item).__name__} | "
              f"{getattr(item, 'upgrade_level', 0)} | "
              f"{item.calculate_total_damage()}")

def forge_weapon():
    print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")

    name = input("Tên: ")
    base = input_positive_int("Sát thương gốc: ")
    level = input_positive_int("Cấp: ")

    w = Weapon(name, base, level)
    inventory.append(w)

    print(">> Rèn thành công!")
    print(f"{w.name} | Weapon | {w.calculate_total_damage()}")


def forge_magic():
    print("\n--- RÈN KIẾM MA THUẬT ---")

    name = input("Tên: ")
    base = input_positive_int("Sát thương gốc: ")
    level = input_positive_int("Cấp: ")
    magic = input_positive_int("Sức mạnh phép: ")

    m = MagicSword(name, base, level, magic)
    inventory.append(m)

    print(">> Rèn thành công!")
    print(f"{m.name} | MagicSword | {m.calculate_total_damage()}")


def compare():
    print("\n--- THẨM ĐỊNH ---")

    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí!")
        return

    a, b = inventory[0], inventory[1]

    print(f"A: {a.name} | {a.calculate_total_damage()}")
    print(f"B: {b.name} | {b.calculate_total_damage()}")

    if a > b:
        print("Kết quả: Vũ khí A mạnh hơn")
    elif b > a:
        print("Kết quả: Vũ khí B mạnh hơn")
    else:
        print("Kết quả: Hai vũ khí ngang nhau")


def fuse():
    print("\n--- DUNG HỢP ---")

    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí!")
        return

    a = inventory.pop(0)
    b = inventory.pop(0)

    new_item = a + b
    inventory.append(new_item)

    print(">> Dung hợp thành công!")
    print(f"Fusion: {new_item.name} | {new_item.calculate_total_damage()}")

def main():
    while True:
        print("\n===== LÒ RÈN =====")
        print("1. Xem kho vũ khí và sát thương tổng")
        print("2. Rèn vũ khí vật lý (tạo Weapon)")
        print("3. Rèn kiếm ma thuật (tạo MagicSword)")
        print("4. Thẩm định vũ khí (so sánh lớn hơn)")
        print("5. Dung hợp vũ khí (Cộng dồn cấp độ)")
        print("6. Thoát game")

        choice = input("Chọn: ")

        match choice:
            case "1":
                show_inventory()
            case "2":
                forge_weapon()
            case "3":
                forge_magic()
            case "4":
                compare()
            case "5":
                fuse()
            case "6":
                print("Thoát lò rèn. Hẹn gặp lại Anh Hùng!")
                break
            case _:
                print("Sai lựa chọn!")


if __name__ == "__main__":
    main()