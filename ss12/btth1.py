cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]

while True:
    choice = input("""
==== SHOPEE CART MANAGEMENT SYSTEM =====
1. Xem chi tiêt giỏ hàng & Tính tổng tiên
2. Thêm sản phẩm mới / Cộng dôn sô ượng
3. Cập nhật sô lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chưong trinh
========================================
Mời bạn chọn chức năng (1-5):""")
    match (choice):
        case '1':
            stt = 1
            count = 0
            sum = 0
            print('---- Chi tiết giỏ hàng-----')
            print('-' * 30)
            print(f"{'STT':<3} | {"Mã SP":<5} | {"Tên sản phẩm":<30} | {"SL":<4} | {"Đơn giá":<10} | {"Thành tiền":<12}")
            for item in cart_items:
                
                print(f"{stt:<3} | {item['id']:<5} | {item["name"]:<30} | {item["number"]:<4} | {item["price"]:<10} | {(item['price'] * item['number']):<12}")
                count += item["number"]
                sum += (item['price'] * item['number'])
                stt += 1
            print(f'Tổng số lượng sản phẩm mua: {count}')
            print(f"TỔNG TIỀN THANH TOÁN {sum}đ")
        case '2':
            is_exists_id = True

            id = input('Nhập mã sản phẩm:').strip().upper()
    
            
            
            for i in range(len(cart_items)):
                if(id == cart_items[i]["id"] ):
                    is_exists_id = False
                    number = int(input('Nhập số lượng của sản phẩm:'))
                    if(number <= 0):
                        print('Không được nhập số lượng <= 0')
                        continue
                    cart_items[i]["number"] += number
                    
                    print('Sản phẩm đã có nên cập nhật lên số lượng')
                    break

            
            if is_exists_id == True:
                name = input('Nhập tên sản phẩm:').strip().title()
                number = int(input('Nhập số lượng của sản phẩm:'))
                if(number <= 0):
                    print('Không được nhập số lượng <= 0')
                    continue
                price = int(input('Nhập giá sản phẩm:'))
                if (price < 0):
                    print('Giá không được nhỏ hơn 0')
                    continue
                cart_items.append({"id" : id, "name" : name, "number" : number, "price" : price })
                print('Thêm sản phẩm thành công!')
        case '3':
            is_exists_id = True
            id = input("Nhập Mã sản phẩm để cập nhật số lượng: ")
            for i in range(len(cart_items)):
                if(id == cart_items[i]["id"] ):
                    is_exists_id = False

            if(is_exists_id == True):
                print('Mã sản phẩm không tồn tại trong giỏ hàng.')
                continue
            number = int(input('Nhập số lượng cập nhật của sản phẩm:'))
            if(number <= 0):
                print('Không được nhập số lượng <= 0')
                continue
            is_exists_id = 0 
            for i in range(len(cart_items)):
                if(id == cart_items[i]["id"] ):
                    cart_items[i]["number"] = number
                    is_exists_id = 1
                    print('Sản phẩm đã được cập nhật số lượng')
                    break
            if is_exists_id == 0:
                print('Không tìm thấy mã sản phẩm')

        case '4':
            is_exists_id = True
            id = input("Nhập Mã sản phẩm để cập nhật số lượng: ")
            for i in range(len(cart_items)):
                if(id == cart_items[i]["id"] ):
                    is_exists_id = False

            if(is_exists_id == True):
                print('Mã sản phẩm không tồn tại trong giỏ hàng.')
                continue

            for i in range(len(cart_items)):
                if (id == cart_items[i]["id"]):
                    del cart_items[i]
                    print('Đã xóa thành công!')
                    break
                
        case '5':
            print('Thanks for used me!')

        case _ :
            print("vui lòng nhập đúng lựa chọn")       