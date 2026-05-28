price = int(input('Nhập đơn giá:'))
quantity = int(input('Nhập số lượng:'))
total = price * quantity

if(total >= 1000000):
    total = total * 0.9
    
print('Số tiền khách hàng phải thanh toán: ',total)