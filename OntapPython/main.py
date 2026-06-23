class Product:
    def __init__(self, id, name, import_price, quantity, storage_fee):
        self.id = id
        self.name = name
        self.import_price = import_price
        self.quantity = quantity
        self.storage_fee = storage_fee
        
        self.total_value = 0
        self.stock_status = ""
        
        self.calculate_total_value()
        self.classify_stock_status()
         
        
    def calculate_total_value(self):
        self.total_value = (self.import_price * self.quantity) + self.storage_fee
        
    def classify_stock_status(self):
        if self.total_value < 9000000:
            self.stock_status = "Thấp (An toàn)"
        elif self.total_value < 15000000:
            self.stock_status = "Trunh bình"
        elif self.total_value < 30000000:
            self.stock_status = "Cao (Cần chú ý)"
        else:
            self.stock_status = "Rất cao (Rủi ro ứ đọng vốn)"
            

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        print("\n===== THÊM SẢN PHẨM =====")

        id = input("Nhập mã sản phẩm: ").strip()
        name = input("Nhập tên sản phẩm: ").strip()

        if id == "" or name == "":
            print("Mã hoặc tên sản phẩm không được trống")
            return

        for product in self.products:
            if product.id == id:
                print("Mã sản phẩm đã tồn tại")
                return

        try:
            import_price = float(input("Nhập giá nhập: "))
            quantity = int(input("Nhập số lượng: "))
            storage_fee = float(input("Nhập chi phí kho: "))
        except ValueError:
            print("Bạn nhập sai kiểu dữ liệu!")
            return

        if import_price <= 0:
            print("Giá nhập phải lớn hơn 0")
            return

        if storage_fee <= 0:
            print("Chi phí kho phải lớn hơn 0")
            return

        if quantity < 0 or quantity > 1000:
            print("Số lượng phải từ 0 đến 1000")
            return

        product = Product(
            id,
            name,
            import_price,
            quantity,
            storage_fee
        )

        self.products.append(product)

        print("Thêm sản phẩm thành công!")
            
    def show_all(self):
        if len(self.products) == 0:
            print("Danh sách sản phẩm trống!")
            return

        print("-" * 120)
        print(f"{'Mã SP':<10} | {'Tên sản phẩm':<20} | {'Giá nhập':<15} | {'SL':<10} | {'Phí kho':<15} | {'Tổng giá trị':<20} | {'Trạng thái'}")
        print("-" * 120)

        for product in self.products:
            print(f"{product.id:<10} | {product.name:<20} | {product.import_price:<15,.0f} | {product.quantity:<10} | {product.storage_fee:<15,.0f} | {product.total_value:<20,.0f} | {product.stock_status}")

    def update_product(self):
        id = input("Nhập mã sản phẩm cần cập nhật: ")

        for product in self.products:
            if product.id == id:
                try:
                    product.import_price = float(input("Nhập giá nhập mới: "))
                    product.quantity = int(input("Nhập số lượng mới: "))
                    product.storage_fee = float(input("Nhập chi phí kho mới: "))
                except ValueError:
                    print("Bạn nhập sai kiểu dữ liệu!")
                    return

                if product.import_price <= 0:
                    print("Giá nhập phải lớn hơn 0")
                    return

                if product.storage_fee <= 0:
                    print("Chi phí kho phải lớn hơn 0")
                    return

                if product.quantity < 0 or product.quantity > 1000:
                    print("Số lượng phải từ 0 đến 1000")
                    return

                product.calculate_total_value()
                product.classify_stock_status()

                print("Cập nhật thành công!")
                return

        print("Không tìm thấy sản phẩm!")

    def delete_product(self):
        id = input("Nhập mã sản phẩm cần xóa: ")

        for product in self.products:
            if product.id == id:
                choice = input("Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ")

                if choice.lower() == "y":
                    self.products.remove(product)
                    print("Đã xóa sản phẩm!")
                else:
                    print("Đã hủy thao tác!")

                return

        print("Không tìm thấy sản phẩm!")

    def search_product(self):
        keyword = input("Nhập tên sản phẩm cần tìm: ").lower()

        found = False

        for product in self.products:
            if keyword in product.name.lower():
                print("-" * 100)
                print(f"Mã: {product.id}")
                print(f"Tên: {product.name}")
                print(f"Giá nhập: {product.import_price:,.0f}")
                print(f"Số lượng: {product.quantity}")
                print(f"Chi phí kho: {product.storage_fee:,.0f}")
                print(f"Tổng giá trị: {product.total_value:,.0f}")
                print(f"Trạng thái: {product.stock_status}")
                found = True

        if not found:
            print("Không tìm thấy sản phẩm phù hợp!")




def menu():
    print('MENU')
    print('''
=====================================
1. Hiển thị danh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
=====================================
''')
    
def main():
    manager = ProductManager()

    while True:
        menu()
        choice = input('Nhập lựa chọn của bạn: ')

        match choice:
            case "1":
                manager.show_all()

            case "2":
                manager.add_product()

            case "3":
                manager.update_product()

            case "4":
                manager.delete_product()

            case "5":
                manager.search_product()

            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng!")
                break

            case _:
                print("Nhập lại lựa chọn!")
main()