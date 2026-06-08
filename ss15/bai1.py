"""
Phân tích Local và Global
Biến Global

Khai báo ngoài hàm:

inventory_stock = 100
total_revenue = 0.0

Ý nghĩa:

inventory_stock: tồn kho hiện tại
total_revenue: tổng doanh thu

Mọi hàm đều có thể đọc được.

Nếu muốn sửa giá trị thì phải dùng:

global inventory_stock
global total_revenue
Biến Local

Chỉ tồn tại bên trong hàm:

subtotal
discount
vat
final_total
quantity
price

Ví dụ:

def calculate_final_price(quantity, price):
    subtotal = quantity * price

subtotal chỉ dùng trong hàm này.
"""

# ==========================
# GLOBAL VARIABLES
# ==========================
inventory_stock = 100
total_revenue = 0.0


def add_stock(amount):
    """
    Thêm sản phẩm vào kho.

    Parameters:
        amount (int): số lượng muốn nhập thêm

    Returns:
        None
    """
    global inventory_stock

    inventory_stock += amount

    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def calculate_final_price(quantity, price):
    """
    Tính tổng tiền cuối cùng của hóa đơn.

    Parameters:
        quantity (int): số lượng mua
        price (float): đơn giá

    Returns:
        tuple:
            subtotal
            discount
            vat
            final_total
    """

    subtotal = quantity * price

    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.10

    after_discount = subtotal - discount

    vat = after_discount * 0.08

    final_total = after_discount + vat

    return subtotal, discount, vat, final_total


def process_sale(quantity):
    """
    Kiểm tra kho có đủ hàng hay không.

    Parameters:
        quantity (int): số lượng khách mua

    Returns:
        bool
    """

    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. "
            f"Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return False

    return True


def print_report():
    """
    Hiển thị báo cáo kinh doanh hiện tại.

    Bao gồm:
    - Số lượng tồn kho
    - Tổng doanh thu
    """

    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")


def main():
    global inventory_stock
    global total_revenue

    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        # ==================
        # CHỨC NĂNG 1
        # ==================
        if choice == "1":
            print("\n--- NHẬP HÀNG ---")

            try:
                amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))

                if amount <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue

                add_stock(amount)

            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

        # ==================
        # CHỨC NĂNG 2
        # ==================
        elif choice == "2":
            print("\n--- BÁN HÀNG ---")

            try:
                quantity = int(input("Nhập số lượng mua: "))
                price = float(input("Nhập đơn giá ($): "))

                if quantity <= 0 or price <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue

                if not process_sale(quantity):
                    continue

                subtotal, discount, vat, final_total = (
                    calculate_final_price(quantity, price)
                )

                inventory_stock -= quantity
                total_revenue += final_total

                print("\n-> Hóa đơn chi tiết:")
                print(
                    f"Số lượng: {quantity} | "
                    f"Đơn giá: ${price}"
                )
                print(f"Tạm tính: ${subtotal}")
                print(f"Giảm giá (10%): ${discount}")
                print(f"Thuế VAT (8%): ${vat}")
                print(f"Tổng thanh toán: ${final_total}")
                print("Đã bán thành công!")

            except ValueError:
                print("Vui lòng nhập đúng định dạng số.")

        # ==================
        # CHỨC NĂNG 3
        # ==================
        elif choice == "3":
            print_report()

        # ==================
        # CHỨC NĂNG 4
        # ==================
        elif choice == "4":
            print("Đã lưu dữ liệu. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ.")


main()