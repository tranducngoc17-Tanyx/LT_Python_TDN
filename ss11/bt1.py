# Phân tích

# Thông tin sản phẩm ban đầu
# product_info = ("SP001", "Áo polo nam", "Size L", 299000)
# Tuple product_info ban đầu có 4 phần tử

# product_code = product_info[1]
# Phần tử "SP001" đang nằm ở index[0]
# Vì dòng này lấy sai mã sản phẩm ở index[1]

# product_name = product_info[2]
# Phần tử "Áo polo nam" đang nằm ở index[1]
# Vì dòng này lấy sai tên sản phẩm ở index[2]

# product_length = product_info.length()
# Vì dòng này không có thuộc tính .length()
# Muốn đếm số phần tử trong tuple, cần dùng hàm len()

# product_info[3] = 279000
# vì tuple không hỗ trợ gán phần tử
# tuple không cho phép sửa trực tiếp phần tử
# muốn cập nhật gái bán từ 299000 thành 279000, có thể chuyển thành list để thay đổi giá trị tại vị trí, chuyển ngược lại

# sửa lỗi
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)

product_list = list(product_info)
product_list[3] = 279000
new_product_info = tuple(product_list)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", new_product_info)