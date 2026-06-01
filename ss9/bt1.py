delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000")

# Cập nhật mã đơn hàng GE002
delivery_orders[2] = "GE002-UPDATED"

# Xóa đơn hàng bị khách hủy
delivery_orders.remove("GE003-CANCEL")

# Lấy đơn hàng cuối cùng ra để bàn giao
transferred_order = delivery_orders.pop()

# Hiển thị kết quả
print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)