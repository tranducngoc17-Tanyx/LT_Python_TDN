total_money = int(input('Nhập tổng tiền hóa đơn ban đầu: '))
if(total_money >= 500000):
    dis_money = total_money * 0.1
    total_money = total_money - dis_money
    
print('---HÓA ĐƠN THANH TOÁN RIKKEI STORE---')
print('Số tiền được giảm giá:', dis_money, 'VND')
print('Tổng tiền khách phải trả: ', total_money, 'VND')