# Phần 1 phân tích:
# Câu 1:
# "from math import *" là Anti-pattern vì import toàn bộ hàm vào namespace,
# dễ gây xung đột tên, khó đọc và khó bảo trì code.
# Nên dùng:
# import math
# hoặc
# from math import sqrt

# câu 2:
# Để biến thư mục thành Package cần file __init__.py
# Vai trò:
# - Đánh dấu thư mục là Package Python
# - Cho phép import các module bên trong
# - Có thể chứa mã khởi tạo package

# câu 3:
# rikkeiLogistics/
# │
# ├── main.py
# │
# ├── core/
# │   ├── __init__.py
# │   ├── geo_calculator.py
# │   └── time_estimator.py
# │
# └── utils/
#     ├── __init__.py
#     └── file_helper.py


