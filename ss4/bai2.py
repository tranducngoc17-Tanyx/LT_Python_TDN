total = 0; count_day = 0; number_day = 7
for i in range(1, (number_day+1)):
    day_work = int(input(f"Nhập doanh thu Ngày {i}: "))
    total += day_work
    if (day_work >= 5000000):
        count_day += 1
avg = total / number_day

print('\n---BÁO CÁO DOANH THU---')
print("Tổng doanh thu cả tuần:", total)
print("Doanh thu trung bình mỗi ngày:", avg)
print("Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND):", count_day, "ngày")