password = 123456

for i in range(3):
    input_pass = int(input('Nhập mật khẩu: '))
    if(input_pass == password):
        print('Đăng nhập thành công!')
    else:
        print('Mật khẩu sai, vui lòng nhập lại!')
        
if(input_pass != password):
    print('Tài khoản đã bị khóa!')