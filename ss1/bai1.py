# Phân tích lỗi
print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ');
name_patient = input('Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input('Mời bạn nhập triệu chứng bệnh: ');

print(' -- PHIẾU KHÁM BỆNH -- '); 
print('Tên bệnh nhân: ', symptom); # symptom lưu triệu chứng nhưng lại hiển thị ở mục "Tên bệnh nhân"
print('Tuổi: ', name_patient); # name_patient lưu tên bệnh nhân nhưng lại hiển thị ở mục "Tuổi"
print('Triệu chứng: ', age); # age lưu tuổi nhưng lại hiển thị ở mục "Triệu chứng"

# Các biến được sử dụng sai vị trí khi xuất dữ liệu
# Chương trình không lỗi cú pháp nhưng sai logic xử lý

# Sửa lại
print(' -- PHIẾU KHÁM BỆNH -- ');
print('Tên bệnh nhân: ', name_patient);
print('Tuổi: ', age);
print('Triệu chứng: ', symptom);
