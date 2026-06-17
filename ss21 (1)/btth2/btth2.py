import logging

# Cấu hình logging in ra Terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dữ liệu thực đơn mặc định
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

# --- CUSTOM EXCEPTIONS ---
class ItemNotFoundError(Exception):
    """Ngoại lệ khi mã đồ uống không tồn tại trong thực đơn."""
    pass

class InvalidQuantityError(Exception):
    """Ngoại lệ khi số lượng nhập vào nhỏ hơn hoặc bằng 0."""
    pass

# --- LOGIC FUNCTIONS ---
def add_to_order(current_order, drink_code, quantity_input):
    """
    Xử lý thêm món vào giỏ hàng.
    Kiểm tra mã đồ uống hợp lệ và số lượng nhập vào.
    """
    # Xử lý nhập chữ thường và khoảng trắng thừa
    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {drink_code}")
        raise ItemNotFoundError("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")

    try:
        quantity = int(quantity_input)
    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        raise ValueError("Vui lòng nhập số lượng là một số nguyên!")

    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise InvalidQuantityError("Số lượng phải lớn hơn 0!")

    item_info = DRINK_MENU[drink_code]
    
    # Kiểm tra xem món đã có trong giỏ chưa để cộng dồn, nếu chưa thì thêm mới
    item_found = False
    for order_item in current_order:
        if order_item['code'] == drink_code:
            order_item['quantity'] += quantity
            item_found = True
            break
            
    if not item_found:
        current_order.append({
            'code': drink_code,
            'name': item_info['name'],
            'price': item_info['price'],
            'quantity': quantity
        })

    logging.info(f"Added {quantity} of {drink_code} to order")
    return item_info['name']

def calculate_total(current_order):
    """
    Tính toán tổng tiền của các món có trong giỏ hàng.
    """
    return sum(item['price'] * item['quantity'] for item in current_order)

def view_order(current_order):
    """
    In chi tiết giỏ hàng ra Terminal và trả về tổng tiền.
    """
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return 0

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<5} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    print("-" * 64)
    for item in current_order:
        thanh_tien = item['price'] * item['quantity']
        print(f"{item['code']:<5} | {item['name']:<20} | {item['price']:<8,} | {item['quantity']:<8} | {thanh_tien:,} VNĐ")
    print("-" * 64)
    
    total = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    return total

import logging
from pos_logic import (
    DRINK_MENU, 
    add_to_order, 
    view_order, 
    ItemNotFoundError, 
    InvalidQuantityError
)

def show_menu():
    """Hiển thị thực đơn hiện có."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():
        print(f"[{code}] - {info['name']} - {info['price']:,} VNĐ")

def main():
    current_order = []

    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            show_menu()

        elif choice == '2':
            print("\n--- THÊM MÓN VÀO GIỎ ---")
            drink_code = input("Nhập mã đồ uống: ")
            quantity = input("Nhập số lượng: ")
            try:
                item_name = add_to_order(current_order, drink_code, quantity)
                print(f"Đã thêm {quantity} x {item_name} vào giỏ hàng.")
            except ItemNotFoundError as e:
                print(e)
            except ValueError as e:
                print(e)
            except InvalidQuantityError as e:
                print(e)

        elif choice == '3':
            view_order(current_order)

        elif choice == '4':
            if not current_order:
                print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
                continue
                
            print("\n--- THANH TOÁN ---")
            total = view_order(current_order)
            confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()
            
            if confirm == 'y':
                print("Thanh toán thành công.")
                logging.info("Checkout successful")
                current_order.clear()
                print("Giỏ hàng đã được làm trống.")
            elif confirm == 'n':
                print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
            else:
                print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")

        elif choice == '5':
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break

        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()