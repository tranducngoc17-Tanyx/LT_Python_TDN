order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]


while True:

    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":

        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("\nDanh sách đơn hàng hiện tại:")

            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")

    elif choice == "2":

        while True:

            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")

            sub_choice = input("Nhập lựa chọn: ").strip()

            if sub_choice == "1":

                order_code = input(
                    "Nhập mã đơn hàng: "
                ).strip().upper()

                status = input(
                    "Nhập trạng thái: "
                ).strip().upper()

                new_order = f"{order_code} - {status}"

                order_list.append(new_order)

                print("Thêm đơn hàng thành công!")

            elif sub_choice == "2":

                position = input(
                    "Nhập vị trí cần sửa: "
                ).strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                index = int(position) - 1

                if index < 0 or index >= len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                order_code = input(
                    "Nhập mã đơn hàng mới: "
                ).strip().upper()

                status = input(
                    "Nhập trạng thái mới: "
                ).strip().upper()

                updated_order = f"{order_code} - {status}"

                order_list[index] = updated_order

                print("Cập nhật đơn hàng thành công!")

            elif sub_choice == "3":

                position = input(
                    "Nhập vị trí cần xóa: "
                ).strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                index = int(position) - 1

                if index < 0 or index >= len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                deleted_order = order_list.pop(index)

                print("Đã xóa đơn hàng:")
                print(deleted_order)

            elif sub_choice == "4":
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


    elif choice == "3":

        pending_count = 0
        delivering_count = 0
        completed_count = 0
        cancelled_count = 0

        for order in order_list:

            parts = order.split(" - ")

            if len(parts) != 2:
                continue

            status = parts[1]

            if status == "PENDING":
                pending_count += 1

            elif status == "DELIVERING":
                delivering_count += 1

            elif status == "COMPLETED":
                completed_count += 1

            elif status == "CANCELLED":
                cancelled_count += 1

        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print("PENDING:", pending_count)
        print("DELIVERING:", delivering_count)
        print("COMPLETED:", completed_count)
        print("CANCELLED:", cancelled_count)
        print("Tổng số đơn hàng:", len(order_list))

    elif choice == "4":

        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")