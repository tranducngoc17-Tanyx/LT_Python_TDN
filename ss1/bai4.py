# Phân tích Input/Output:
# Input:
# Mã bệnh nhân: String
# Nhiệt độ cơ thể: nhập từ bàn phím (String ép sang Float)
# Nhịp tim: nhập từ bàn phím (String ép sang Integer)

# Output:
# Hiển thị thông tin bệnh nhân
# Xác nhận kiểu dữ liệu đã chuẩn hóa

print('--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---')

ma_benh_nhan = input('Nhập mã bệnh nhân: ')
nhiet_do = float(input('Nhập nhiệt độ cơ thể: '))
nhip_tim = int(input('Nhập nhịp tim: '))

print('Mã bệnh nhân:', ma_benh_nhan)
print('Nhiệt độ cơ thể:', nhiet_do, 'độ C')
print('=> Kiểu dữ liệu hệ thống ghi nhận:', type(nhiet_do))

print('Nhịp tim:', nhip_tim, 'nhịp/phút')
print('=> Kiểu dữ liệu hệ thống ghi nhận:', type(nhip_tim))

print('Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!')