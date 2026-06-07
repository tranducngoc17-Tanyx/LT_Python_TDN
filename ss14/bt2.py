# phân tích
# Câu 1:
# total_points được khai báo bên ngoài hàm
# nên đây là biến toàn cục (Global Variable)

# Câu 2:
# Python thấy có phép gán: total_points = total_points + points_earned
# nên tự hiểu total_points bên trong hàm là biến cục bộ
# Nhưng biến này chưa được tạo giá trị trước đó
# nên phát sinh lỗi UnboundLocalError

# Câu 3:
# Nếu chỉ đọc hoặc print(total_points) thì chương trình không bị lỗi
# Vì Python được phép đọc biến toàn cục bên trong hàm

# Câu 4:
# Từ khóa dùng để thay đổi biến toàn cục là: global
# Ví dụ: global total_points

# Câu 5:
# Cách làm tốt hơn là truyền dữ liệu vào hàm
# và dùng return để trả kết quả về
# Hàm sẽ nhận tổng điểm hiện tại và điểm được thưởng
# Sau đó return tổng điểm mới



# sửa lỗi
total_points = 100
def add_reward_points(current_points, points_earned):
    total = current_points + points_earned
    return total

total_points = add_reward_points(total_points, 50)

print("Đã cộng thêm 50 điểm.")
print("Tổng điểm hiện tại của khách hàng:", total_points)