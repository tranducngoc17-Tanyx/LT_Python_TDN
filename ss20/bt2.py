# 1 phân tích lỗi

# 1. IndexError xảy ra vì SofM chỉ có 2 phần tử:
# ("SofM", 150) nhưng code lại truy cập p[2] để lấy MMR
# Levi có đủ 3 phần tử nên chạy được

# 2. Nếu sửa SofM thành đủ dữ liệu, đến Optimus sẽ gặp ValueError
# Nguyên nhân là int("N/A") không thể chuyển chuỗi "N/A" thành số nguyên

# 3. Lệnh print("Đang xử lý:", p) giúp biết chương trình
#  đang xử lý tuyển thủ nào trước khi bị sập, hỗ trợ debug

# 4. Tên biến cũ như ds, p, t, m, r, b khó hiểu
# Nên đổi thành player_records, record, name, matches, mmr, bonus để dễ đọc hơn


# 2 sửa code

player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)


def process_players(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        name = record[0]

        try:
            matches = record[1]
            mmr = int(record[2])

            bonus = calculate_bonus(matches, mmr)

            print(f"Tuyển thủ {name} nhận được {bonus} RP")

        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue
        

process_players(player_records)