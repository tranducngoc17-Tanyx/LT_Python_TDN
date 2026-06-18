# I. PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. Sơ đồ lớp

# Hệ thống được xây dựng theo mô hình kế thừa từ một lớp trừu tượng.

#             Champion (ABC)
#                   |
#         ---------------------
#         |                   |
#      Warrior             Mage
# Champion là lớp cha trừu tượng, chứa các thuộc tính chung của mọi quân cờ như mã tướng, tên, máu và sát thương cơ bản.
# Warrior và Mage là các lớp con kế thừa từ Champion.
# Mỗi lớp con sẽ có cách tính sát thương kỹ năng riêng.
# 2. Phân tích tính Đa hình (Polymorphism)

# Trong lớp Champion có phương thức trừu tượng:

# calculate_skill_damage()

# Phương thức này được các lớp con ghi đè theo đặc điểm riêng:

# Warrior: base_atk * 2 + shield_bonus
# Mage: base_atk * ability_power

# Nhờ tính đa hình, khi duyệt danh sách quân cờ:

# for champion in champion_pool:
#     champion.calculate_skill_damage()

# chương trình sẽ tự động gọi đúng hàm của từng loại tướng mà không cần sử dụng nhiều câu lệnh if-else.

# Điều này giúp hệ thống dễ mở rộng. Nếu sau này thêm Assassin hoặc Ranger thì chỉ cần tạo lớp mới kế thừa Champion và cài đặt lại phương thức calculate_skill_damage().

# 3. Phân tích nạp chồng toán tử (add)

# Đề bài yêu cầu sử dụng toán tử + để tính tổng chiến lực đội hình.

# Do đó lớp Champion sẽ nạp chồng toán tử:

# __add__()

# để hỗ trợ:

# Champion + Champion

# và

# Champion + int/float

# Ví dụ:

# total_power = 0

# for champion in team:
#     total_power = champion + total_power

# Nhờ vậy việc cộng dồn chiến lực đội hình trở nên đơn giản và trực quan hơn.

# 4. Các kiến thức OOP được áp dụng
# Abstract Base Class (ABC)

# Lớp Champion được xây dựng dưới dạng lớp trừu tượng nhằm ngăn việc tạo trực tiếp một quân cờ không thuộc hệ nào.

# Inheritance

# Warrior và Mage kế thừa các thuộc tính chung từ Champion để tránh lặp lại mã nguồn.

# Polymorphism

# Các lớp con cùng sử dụng phương thức calculate_skill_damage() nhưng có cách xử lý khác nhau.

# Operator Overloading

# Nạp chồng toán tử:

# __add__()
# __gt__()

# để cộng và so sánh chiến lực giữa các quân cờ.

# Encapsulation

# Thông tin và hành vi của mỗi quân cờ được đóng gói trong một đối tượng riêng.

# 5. Xử lý các trường hợp đặc biệt (Edge Cases)
# Trường hợp 1: Khởi tạo Champion trực tiếp

# Do Champion là lớp trừu tượng nên:

# Champion(...)

# sẽ phát sinh lỗi TypeError.

# Trường hợp 2: HP hoặc ATK nhỏ hơn hoặc bằng 0

# Nếu người dùng nhập giá trị không hợp lệ thì hệ thống tự động đưa về giá trị mặc định là 100.

# Trường hợp 3: Mã tướng không tồn tại

# Khi so sánh hoặc tính chiến lực đội hình, nếu mã tướng không có trong danh sách thì hệ thống sẽ thông báo lỗi và bỏ qua thay vì làm chương trình bị dừng.

# Trường hợp 4: Trùng mã tướng

# Khi thêm quân cờ mới, hệ thống kiểm tra mã tướng đã tồn tại hay chưa. Nếu trùng sẽ từ chối thêm mới để đảm bảo dữ liệu không bị xung đột.
from abc import ABC, abstractmethod
class Champion(ABC):
    """
    Lớp trừu tượng đại diện cho một quân cờ trong hệ thống Auto-Battler.
    Chứa các thuộc tính và hành vi chung của mọi Champion.
    """

    def __init__(self, champion_id, name, base_hp, base_atk):
        """
        Khởi tạo Champion.

        Args:
            champion_id (str): Mã quân cờ.
            name (str): Tên tướng.
            base_hp (int): Máu cơ bản.
            base_atk (int): Sát thương cơ bản.
        """
        self.champion_id = champion_id
        self.name = name

        # Edge Case 2
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Phương thức trừu tượng.
        Mỗi lớp con phải tự định nghĩa cách tính sát thương kỹ năng.
        """
        pass

    def get_combat_power(self):
        """
        Tính chiến lực tổng hợp.

        Công thức:
        Chiến lực = HP + (Skill Damage × 1.5)

        Returns:
            float
        """
        return self.base_hp + (self.calculate_skill_damage() * 1.5)

    def __add__(self, other):
        """
        Nạp chồng toán tử +

        Hỗ trợ:
        Champion + Champion
        Champion + int
        Champion + float
        """
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()

        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other

        return NotImplemented

    def __gt__(self, other):
        """
        Nạp chồng toán tử >
        So sánh chiến lực giữa hai Champion.
        """
        if isinstance(other, Champion):
            return self.get_combat_power() > other.get_combat_power()

        return NotImplemented


class Warrior(Champion):
    """
    Lớp Warrior (Chiến binh).
    """

    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        """
        Khởi tạo Warrior.
        """
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        """
        Công thức:
        base_atk * 2 + shield_bonus
        """
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    """
    Lớp Mage (Pháp sư).
    """

    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        """
        Khởi tạo Mage.
        """
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        """
        Công thức:
        base_atk * ability_power
        """
        return self.base_atk * self.ability_power


def find_champion_by_id(champion_pool, champion_id):
    """
    Tìm Champion theo mã.
    """
    for champion in champion_pool:
        if champion.champion_id.upper() == champion_id.upper():
            return champion
    return None


def display_champions(champion_pool):
    """
    Hiển thị danh sách Champion.
    """
    print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")

    print(
        f"{'Mã':<8} | {'Tên tướng':<20} | {'Hệ':<10} | "
        f"{'HP':<6} | {'ATK':<6} | {'Chỉ số riêng':<20} | {'Chiến lực'}"
    )

    print("-" * 110)

    for champion in champion_pool:

        if isinstance(champion, Warrior):
            champion_type = "Warrior"
            special = f"Armor: {champion.shield_bonus}"

        elif isinstance(champion, Mage):
            champion_type = "Mage"
            special = f"Mana: {champion.ability_power}"

        else:
            champion_type = "Unknown"
            special = "-"

        print(
            f"{champion.champion_id:<8} | "
            f"{champion.name:<20} | "
            f"{champion_type:<10} | "
            f"{champion.base_hp:<6} | "
            f"{champion.base_atk:<6} | "
            f"{special:<20} | "
            f"{champion.get_combat_power():.0f}"
        )

    print("-" * 110)


def add_champion(champion_pool):
    """
    Thêm Champion mới.
    """

    print("\n1. Warrior")
    print("2. Mage")

    choice = input("Chọn hệ tướng: ").strip()

    champion_id = input("Nhập mã tướng: ").strip()

    # Edge Case 4
    if find_champion_by_id(champion_pool, champion_id):
        print("Mã tướng đã tồn tại!")
        return

    name = input("Nhập tên tướng: ").strip()

    try:
        base_hp = int(input("Nhập HP: "))
        base_atk = int(input("Nhập ATK: "))
    except ValueError:
        print("Dữ liệu không hợp lệ!")
        return

    if choice == "1":

        try:
            shield_bonus = int(input("Nhập Armor: "))
        except ValueError:
            print("Armor không hợp lệ!")
            return

        champion = Warrior(
            champion_id,
            name,
            base_hp,
            base_atk,
            shield_bonus
        )

        champion_pool.append(champion)

        print("\nThêm tướng Warrior thành công!")
        print(
            f"Mã: {champion.champion_id} | "
            f"Tên: {champion.name} | "
            f"Chiến lực: {champion.get_combat_power():.0f}"
        )

    elif choice == "2":

        try:
            ability_power = float(input("Nhập Mana (Ability Power): "))
        except ValueError:
            print("Mana không hợp lệ!")
            return

        champion = Mage(
            champion_id,
            name,
            base_hp,
            base_atk,
            ability_power
        )

        champion_pool.append(champion)

        print("\nThêm tướng Mage thành công!")
        print(
            f"Mã: {champion.champion_id} | "
            f"Tên: {champion.name} | "
            f"Chiến lực: {champion.get_combat_power():.0f}"
        )

    else:
        print("Lựa chọn không hợp lệ!")


def compare_champions(champion_pool):
    """
    So sánh sức mạnh giữa hai Champion.
    """

    print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")

    id1 = input("Nhập mã tướng thứ nhất: ").strip()
    id2 = input("Nhập mã tướng thứ hai: ").strip()

    champion1 = find_champion_by_id(champion_pool, id1)
    champion2 = find_champion_by_id(champion_pool, id2)

    # Edge Case 3
    if champion1 is None:
        print(f"Mã tướng {id1} không hợp lệ, bỏ qua!")
        return

    if champion2 is None:
        print(f"Mã tướng {id2} không hợp lệ, bỏ qua!")
        return

    print("\nThông tin so sánh:")

    type1 = champion1.__class__.__name__
    type2 = champion2.__class__.__name__

    print(
        f"{champion1.champion_id} - {champion1.name} | "
        f"Hệ: {type1} | "
        f"Chiến lực: {champion1.get_combat_power():.0f}"
    )

    print(
        f"{champion2.champion_id} - {champion2.name} | "
        f"Hệ: {type2} | "
        f"Chiến lực: {champion2.get_combat_power():.0f}"
    )

    if champion1 > champion2:
        print(
            f"\nKết quả: {champion1.champion_id} - "
            f"{champion1.name} mạnh hơn "
            f"{champion2.champion_id} - {champion2.name}."
        )
    else:
        print(
            f"\nKết quả: {champion2.champion_id} - "
            f"{champion2.name} mạnh hơn "
            f"{champion1.champion_id} - {champion1.name}."
        )


def calculate_team_power(champion_pool):
    """
    Tính tổng chiến lực đội hình.
    """

    print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")

    ids = input(
        "Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: "
    ).split(",")

    team = []

    for champion_id in ids:

        champion_id = champion_id.strip()

        champion = find_champion_by_id(
            champion_pool,
            champion_id
        )

        # Edge Case 3
        if champion is None:
            print(
                f"Mã tướng {champion_id} không hợp lệ, bỏ qua!"
            )
            continue

        team.append(champion)

    if not team:
        print("Không có quân cờ hợp lệ!")
        return

    print("\nDanh sách đội hình:")

    total_power = 0

    for index, champion in enumerate(team, start=1):

        print(
            f"{index}. "
            f"{champion.champion_id} - "
            f"{champion.name} | "
            f"Chiến lực: "
            f"{champion.get_combat_power():.0f}"
        )

        total_power = champion + total_power

    print(
        f"\nTổng chiến lực đội hình: "
        f"{total_power:.0f}"
    )


def create_default_pool():
    """
    Khởi tạo bể tướng mặc định.
    """

    return [
        Warrior(
            "WAR01",
            "Rikkei Knight",
            1200,
            300,
            150
        ),
        Warrior(
            "WAR02",
            "Steel Guardian",
            1500,
            250,
            200
        ),
        Mage(
            "MAG01",
            "Rikkei Wizard",
            800,
            500,
            2.0
        )
    ]

def main():
    """
    Hàm điều khiển chương trình.
    """

    champion_pool = create_default_pool()

    while True:

        print("\n===== RIKKEI RPG - AUTO BATTLER MANAGER =====")
        print("1. Hiển thị bể tướng")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực đội hình")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:

            case "1":
                display_champions(champion_pool)

            case "2":
                add_champion(champion_pool)

            case "3":
                compare_champions(champion_pool)

            case "4":
                calculate_team_power(champion_pool)

            case "5":
                print(
                    "Cảm ơn bạn đã sử dụng "
                    "Rikkei RPG - Auto-Battler Manager!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()