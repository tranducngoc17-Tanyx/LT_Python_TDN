express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

# Hiển thị kết quả
print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)