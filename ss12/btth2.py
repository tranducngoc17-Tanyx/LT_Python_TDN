playlist = []

while True:
    print("\n===== QUẢN LÝ DANH SÁCH PHÁT =====")
    print("1. Thêm bài hát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát")
    print("4. Sắp xếp / Trích xuất")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ")

    # Thêm bài hát
    if choice == "1":
        print("\n--- THÊM BÀI HÁT ---")
        print("1. Thêm vào cuối")
        print("2. Chèn vào vị trí")

        sub_choice = input("Nhập lựa chọn: ")

        if sub_choice == "1":
            song_name = input("Nhập tên bài hát: ")
            playlist.append(song_name)
            print("Đã thêm thành công!")

        elif sub_choice == "2":
            song_name = input("Nhập tên bài hát: ")

            while True:
                position = int(input("Nhập vị trí muốn chèn: "))

                if position < 0 or position > len(playlist):
                    print("Vị trí không hợp lệ!")
                else:
                    break

            playlist.insert(position, song_name)
            print("Đã chèn bài hát thành công!")

        else:
            print("Lựa chọn không hợp lệ!")

    # Xem danh sách
    elif choice == "2":
        print("\n--- DANH SÁCH PHÁT ---")

        if len(playlist) == 0:
            print("Danh sách đang trống!")
        else:
            for i in range(len(playlist)):
                print(f"{i + 1}. {playlist[i]}")

            print(f"\nTổng số bài hát: {len(playlist)}")

    # Xóa bài hát
    elif choice == "3":
        print("\n--- XÓA BÀI HÁT ---")
        print("1. Xóa theo tên")
        print("2. Xóa theo vị trí")

        sub_choice = input("Nhập lựa chọn: ")

        if sub_choice == "1":
            song_name = input("Nhập tên bài hát cần xóa: ")

            if song_name in playlist:
                playlist.remove(song_name)
                print("Đã xóa thành công!")
            else:
                print("Không tìm thấy bài hát!")

        elif sub_choice == "2":
            position = int(input("Nhập vị trí cần xóa: "))

            if position < 1 or position > len(playlist):
                print("Vị trí không hợp lệ!")
            else:
                playlist.pop(position - 1)
                print("Đã xóa thành công!")

        else:
            print("Lựa chọn không hợp lệ!")

    # Sắp xếp và trích xuất
    elif choice == "4":

        if len(playlist) == 0:
            print("Danh sách đang trống!")
            continue

        print("\n--- SẮP XẾP VÀ TRÍCH XUẤT ---")
        print("1. Sắp xếp A-Z")
        print("2. Hiển thị 3 bài đầu tiên")

        sub_choice = input("Nhập lựa chọn: ")

        if sub_choice == "1":
            playlist.sort()

            print("\nDanh sách sau khi sắp xếp:")
            for i in range(len(playlist)):
                print(f"{i + 1}. {playlist[i]}")

        elif sub_choice == "2":
            print("\n3 bài hát đầu tiên:")

            for i in range(min(3, len(playlist))):
                print(f"{i + 1}. {playlist[i]}")

        else:
            print("Lựa chọn không hợp lệ!")

    # Thoát
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!")