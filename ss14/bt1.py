# Phân tích
# câu 1:
# calculate_final_price(price, discount, shipping_fee)
# Ban đầu: calculate_final_price(100000, 15000, 0.1)
# => 100000 được gán cho price
# => 15000 được gán cho discount
# => 0.1 được gán cho shipping_fee
# Phải là discount là 0.1 và shipping_fee là 15000

# Câu 2:
# Do truyền sai vị trí tham số nên discount = 15000
# Chương trình tính: 100000 - (100000 * 15000) + 0.1
# => kết quả bị âm rất lớn

# Câu 3:
# Dòng: final_payment = order_total + 5000
# bị lỗi vì order_total không phải số

# Câu 4:
# order_total nhận giá trị None
# Vì trong hàm chỉ có print() mà không có return

# Câu 5:
# print() chỉ hiển thị kết quả ra màn hình
# return dùng để trả kết quả về cho chương trình tiếp tục sử dụng

# Câu 6: cần sửa
# Truyền đúng thứ tự tham số
# Thêm return total trong hàm
# Khi đó order_total sẽ nhận được tổng tiền đúng

# sửa lỗi
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total

order_total = calculate_final_price(100000, 0.1, 15000)
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)