# Phân tích lỗi:
# Chương trình đang cho phép nhập số âm hoặc số 0.
# Điều này không hợp lệ vì số lượng nhân sự mới phải lớn hơn 0.
# Cần dùng vòng lặp để bắt người dùng nhập lại nếu dữ liệu sai.

print('--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---')
so_luong_nhan_su = 0

while so_luong_nhan_su <= 0:

    so_luong_nhan_su = int(input('Vui lòng nhập số lượng nhân sự mới trong tháng này: '))

    if so_luong_nhan_su <= 0:
        print('[LỖI] Số lượng không hợp lệ! Vui lòng nhập số lớn hơn 0')

print(f'[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {so_luong_nhan_su} nhân sự mới!')

print('CHƯƠNG TRÌNH KẾT THÚC')