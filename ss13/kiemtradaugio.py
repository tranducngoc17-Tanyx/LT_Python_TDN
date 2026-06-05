list_car = []

while True:
    print('QUẢN LÝ BÃI XE - SMART PARKING')
    print('1. Thêm mới vào bãi')
    print('2. Hiển thị danh sách xe trong bãi')
    print('3. Xóa xe khỏi bãi (khi xe ra)')
    print('4. Thoát chương trình')
    choice = input('Nhập lựa chọn: ')
    
    if choice == "1":
        list_id = int(input("Nhập danh sách: "))
        for i in range (list_id):
            type_car = input("Nhập loại xe: ")
            owner = input("Nhập chủ xe: ")
    elif choice == "2":
        print("ID  |Loại xe    |Chủ xe",
              f"{i+1}   |{type_car} |{owner}")        
        
    elif choice == "4":
        print("Thoát chương trình")
        break
    else:
        print("Vui lòng nhập lại")
        
