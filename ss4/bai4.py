secert_number = 79
for i in range(5):
    number = int(input('Nhập số lucky của bạn: ')); 
    if(number == secert_number):
        print('Chúc bạn đã trúng số!'); 
    elif(number > secert_number):
        print('Số bạn nhập lớn hơn!'); 
    else:
        print('Số bạn nhập nhỏ hơn!'); 
    
if(number != secert_number):
    print('Bạn đã hết lượt!'); 
