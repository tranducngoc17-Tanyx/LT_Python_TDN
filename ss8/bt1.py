while True:
    print("HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK")
    print("1. Nhập và phân tích thông tin video")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra tính hợp lệ của hashtag")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")
    choice = input("> Mời bạn chọn chức năng (1-5): ")
    
    if choice == "1":
        user_name = input('Nhâp tên tài khoản: ')
        title = input('Nhập tiêu đề video: ')
        description = input('Mô tả video: ')
        list_hashtag = input('Nhập danh sách hashởi dấu ptag (cách nhau bhẩy): ')
        
        print('===Đã qua xử lí, hiển thị!===')
        print(f"Tên tài khoản: {user_name.strip()}")
        print(f"Tên tiêu đề: {title.title().strip()}")
        print(f"Mô tả: {description.strip()}")
        print(f"Độ dài mô tả: {len(description)}")
        count_space = description.count(" ") + 1
        print(f"Số lượng từ trong mô tả: {count_space}")    

        list_temp = list_hashtag.split(",")
        new_lits_hashtag = "".join(list_temp)     
        print(f"Danh sách hashtag: {new_lits_hashtag}")
        
        count_hashtag = len(list_temp)
        print(f"Số lượng hashtag là: {count_hashtag}")
        print(f"Mô tả video chuyển thành thường: {description.lower()}")
        print(f"Mô tả video chuyển thành hoa: {description.upper()}")

    elif choice == "2":
        print(f"Tên tài khoản ban đầu: {user_name}")
        print("Tên tài khoản sau khi được chuẩn hóa:", "@" + user_name.lower())
    
    elif choice == "3":
        hashtag = input('Nhập hashtag: ')
        if (hashtag == ""):
            print("Không được rỗng!")
        elif (not hashtag.startswith("#")):
            print("phải bắt đầu bằng #")
        elif (" " in hashtag):
            print("Không được chứa khoảng trắng")
        elif (len(hashtag) < 2):
            print("Phải chúa tối thiểu 2 kí tự")
        else:
            print("Hashtag hợp lệ!")
            list_hashtag = list_hashtag + hashtag
            print(f"Danh sách hashtag mới: {list_hashtag}")
    
    elif choice == "4":
        find_word = input("Nhập từ khóa cần tìm: ")
        count_word = description.count(find_word)
        if (count_word > 0):
            description = description.replace(find_word, "Từ khóa mới")
            print(f"Mô tả sau khi thay thế: {description}")
            print(f"Số lần xuất hiện từ khóa: {count_word}")
        else:
            print("Từ khóa không tìm thấy!")
    
    elif choice == "5":
        print("Thoát chương trinh")
        break
    else:
        print("Vui lòng nhập lại!")