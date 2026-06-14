# 1 phần tích lỗi
# 1. ZeroDivisionError xảy ra vì ShowMaker có Deaths = 0.
# Khi tính (kills + assists) / deaths sẽ thành chia cho 0,
# làm chương trình bị dừng ngay lập tức.

# 2. Nếu bỏ ShowMaker, đến Chovy sẽ gặp ValueError.
# Nguyên nhân là int("ba") không thể chuyển chuỗi "ba" thành số nguyên.

# 3. Tên biến cũ như ds, x, n, k, d, a khó hiểu.
# Nên đổi thành players_data, player_stats, name,
# kills, deaths, assists để dễ đọc hơn.

# 4. Tách công thức KDA thành hàm riêng giúp tránh lặp code,
# dễ sửa đổi và tái sử dụng sau này.


# 2 sửa code

players_data = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths


def process_players(players_data):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player_stats in players_data:
        name = player_stats[0]
        kills = player_stats[1]
        deaths = player_stats[2]
        assists = player_stats[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA: {kda}")

        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
            continue

        except ValueError:
            print(f"Tuyển thủ{name}: Lỗi dữ liệu không hợp lệ!")
            continue

process_players(players_data)