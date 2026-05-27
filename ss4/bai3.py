total_bill = int(input("Nhập số lượng hóa đơn trong ca: "))
max_bill = 0
min_bill = 0

for i in range(1, total_bill+1):
    bill_value = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))

    if i == 1:
        max_bill = bill_value
        min_bill = bill_value

    if bill_value > max_bill:
        max_bill = bill_value

    if bill_value < min_bill:
        min_bill = bill_value

print("Hóa đơn có giá trị cao nhất:", max_bill)
print("Hóa đơn có giá trị thấp nhất:", min_bill)