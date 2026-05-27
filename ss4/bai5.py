i = 1
total = 0
count_bill = 0
count_big_bill = 0

while True:
    cus_bill = int(input(f'Khách hàng {i} - Nhập giá trị hóa đơn: '))
    total += cus_bill
    count_bill += 1

    if (cus_bill >= 1000000):
        count_big_bill += 1
    continue_chose = input('Có muốn nhập tiếp không? (C/K): ')

    if continue_chose.lower() == 'k':
        break
    i += 1

if (count_bill > 0):
    percent = (count_big_bill / count_bill) * 100
else:
    percent = 0

print('--BÁO CÁO DOANH THU CUỐI NGÀY---')
print('Tổng hóa đơn đã xử lí:', count_bill)
print('Tổng doanh thu ngày hôm nay:', total)
print('Tổng hóa đơn lớn hơn 1 củ:', count_big_bill)
print('Tỷ lệ hóa đơn lớn:', percent, '%')