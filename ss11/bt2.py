# Phân tích lỗi 
# dictionary employee gồm 4 key là employee_id, full_name, department, status

# employee_id = employee[0]
# Dictionary truy cập dữ liệu bằng key, không truy cập bằng index như list
# muốn lấy mã nhân viên "NV001", cần viết lệnh employee_id = employee["employee_id"]

# full_name = employee["name"]
# vì dictionary không có key "name"
# key đúng là "full_name"

# employee["employee_status"] = "official"
# dict đang có key là "status". Nhưng đoạn code lại tạo key mới "employee_status" -> trạng thái cũ còn và chưa cập nhật
# muốn cập nhật trạng thái nhân viên, cần dùng key "status"

# employee.append("base_salary", 15000000)
# append() chỉ dùng cho list, không dùng cho dict
# muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh employee["base_salary"] = 15000000

# del employee["team"]
# Vì dict không có key "team"
# muốn xóa thông tin phòng ban, cần dùng key "department", có thể dùng del hoặc .pop()


# Sửa lỗi
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]
full_name = employee["full_name"]
employee["status"] = "official"
employee["base_salary"] = 15000000

del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)