import logging

# Cấu hình logging để in ra các cảnh báo nội bộ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def show_devices(device_list):
    """Chức năng 1: Hiển thị danh sách thiết bị dưới dạng bảng."""
    if not device_list:
        print("Danh sách thiết bị hiện đang trống.")
        return
        
    print(f"\n{'Mã TB':<8} | {'Vị trí':<20} | {'Chỉ số cũ':<12} | {'Chỉ số mới':<12} | {'Trạng thái'}")
    print("-" * 75)
    for d in device_list:
        print(f"{d['id']:<8} | {d['location']:<20} | {d['old_index']:<12.1f} | {d['new_index']:<12.1f} | {d['status']}")
    print("-" * 75)

def update_indices(device_list):
    """Chức năng 2: Cập nhật chỉ số điện năng với validation."""
    device_id = input("Nhập mã thiết bị cần cập nhật: ").strip()
    
    # Tìm kiếm thiết bị
    target_device = next((d for d in device_list if d['id'] == device_id), None)
    
    if not target_device:
        print("ERR-E01: Không tìm thấy mã thiết bị trong hệ thống.")
        return

    while True:
        try:
            old_idx = float(input("Nhập chỉ số cũ: "))
            if old_idx < 0:
                print("Lỗi: Chỉ số cũ phải lớn hơn hoặc bằng 0. Vui lòng nhập lại.")
                continue

            new_idx = float(input("Nhập chỉ số mới: "))
            if new_idx < 0:
                print("Lỗi: Chỉ số mới phải lớn hơn hoặc bằng 0. Vui lòng nhập lại.")
                continue

            if new_idx < old_idx:
                print("ERR-E02: Chỉ số mới không được nhỏ hơn chỉ số cũ. Vui lòng nhập lại.")
                continue
                
            # Cập nhật dữ liệu
            target_device['old_index'] = old_idx
            target_device['new_index'] = new_idx
            print(f"Cập nhật thành công chỉ số cho thiết bị {device_id}.")
            break

        except ValueError:
            print("Lỗi: Dữ liệu nhập vào phải là định dạng số hợp lệ. Vui lòng thử lại.")

def activate_overload_warning(device_list):
    """Chức năng 3: Kích hoạt cảnh báo quá tải nếu vượt ngưỡng 5,000 kWh."""
    device_id = input("Nhập mã thiết bị cần kiểm tra cảnh báo: ").strip()
    target_device = next((d for d in device_list if d['id'] == device_id), None)
    
    if not target_device:
        print("ERR-E01: Không tìm thấy mã thiết bị trong hệ thống.")
        return

    if target_device['status'] == 'Overload':
        print("ERR-E04: Thiết bị này đã ở trạng thái Overload từ trước.")
        return

    consumption = target_device['new_index'] - target_device['old_index']
    
    if consumption > 5000:
        target_device['status'] = 'Overload'
        logging.warning(f"Thiết bị {device_id} tiêu thụ {consumption} kWh (vượt 5,000 kWh). Đã chuyển trạng thái sang Overload!")
        print(f"Đã kích hoạt cảnh báo quá tải thành công cho {device_id}.")
    else:
        print(f"Thiết bị {device_id} tiêu thụ {consumption} kWh, vẫn nằm trong mức an toàn.")

def calculate_energy_financials(device_list):
    """
    Chức năng 4: Tính toán tài chính.
    Chỉ trả về Tuple: (tổng_điện, phần_trăm_chiết_khấu, tổng_tiền_sau_chiết_khấu)
    """
    total_consumption = sum((d['new_index'] - d['old_index']) for d in device_list)
    base_price_per_kwh = 3000
    
    # Áp dụng chiết khấu 3% nếu tổng tiêu thụ >= 50,000 kWh
    discount_percent = 0.03 if total_consumption >= 50000 else 0.0
    
    total_cost_before_discount = total_consumption * base_price_per_kwh
    total_cost_after_discount = total_cost_before_discount * (1 - discount_percent)
    
    return (total_consumption, discount_percent, total_cost_after_discount)

def main():
    """Hàm điều phối chính, quản lý vòng lặp Menu."""
    # Dữ liệu khởi tạo mặc định
    devices = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
    ]
    
    while True:
        print("\n=== SMART ENERGY MONITOR ===")
        print("1. Xem danh sách thiết bị")
        print("2. Cập nhật chỉ số điện")
        print("3. Kích hoạt cảnh báo quá tải")
        print("4. Tính tổng lượng điện & Chi phí")
        print("5. Thoát")
        print("============================")
        
        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên từ 1 đến 5.")
            continue

        if choice == 1:
            show_devices(devices)
        elif choice == 2:
            update_indices(devices)
        elif choice == 3:
            activate_overload_warning(devices)
        elif choice == 4:
            # Nhận kết quả từ hàm dưới dạng Tuple và tự in ra màn hình
            consumption, discount, total_cost = calculate_energy_financials(devices)
            print("\n--- BÁO CÁO TÀI CHÍNH NĂNG LƯỢNG ---")
            print(f"Tổng lượng điện tiêu thụ: {consumption:,.1f} kWh")
            print(f"Mức chiết khấu áp dụng: {discount * 100}%")
            print(f"Tổng tiền thanh toán (sau chiết khấu): {total_cost:,.0f} VND")
            print("------------------------------------")
        elif choice == 5:
            print("Hệ thống đã đóng. Tạm biệt và hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 5.")

if __name__ == "__main__":
    main()