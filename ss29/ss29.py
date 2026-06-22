import logging
from abc import ABC, abstractmethod
logging.basicConfig(
    filename="smart_factory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
class BaseDevice(ABC):
    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1000000

    def __init__(self, device_code, device_name, operating_hours=0):
        # Kiểm tra tính hợp lệ của mã thiết bị thông qua Static Method
        if not self.validate_device_code(device_code):
            print("[Lỗi] (ERR-IOT-01): Mã thiết bị không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng tiền tố quy định.")
            logging.error(f"ERR-IOT-01: Khởi tạo thất bại với mã {device_code}")
            raise ValueError("ERR-IOT-01")

        self.device_code = device_code
        self._device_name = device_name.strip().upper()  # Chuẩn hóa tự động qua Encapsulation
        self.__operating_hours = operating_hours        # Biến Private nghiêm ngặt

    @property
    def operating_hours(self):
        return self.__operating_hours

    # Hàm hỗ trợ cập nhật số giờ chạy nội bộ
    def _add_hours(self, hours):
        if hours <= 0:
            print("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
            logging.error("ERR-IOT-03: Nhập sai định dạng số giờ vận hành.")
            raise ValueError("ERR-IOT-03")
        self.__operating_hours += hours

    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value.strip().upper()

    @abstractmethod
    def track_performance(self):
        pass

    @abstractmethod
    def run_diagnostic(self):
        pass
    def __add__(self, other):
        if not isinstance(other, BaseDevice):
            print("[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")
            logging.error("ERR-IOT-04: Xung đột kiểu dữ liệu khi thực hiện toán tử __add__")
            return NotImplemented
        return self.operating_hours + other.operating_hours

    # OPERATOR OVERLOADING: Nạp chồng toán tử so sánh nhỏ hơn (<)
    def __lt__(self, other):
        if not isinstance(other, BaseDevice):
            print("[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")
            logging.error("ERR-IOT-04: Xung đột kiểu dữ liệu khi thực hiện toán tử __lt__")
            return NotImplemented
        return self.operating_hours < other.operating_hours

    @staticmethod
    def validate_device_code(device_code):
        # Mã 10 ký tự và bắt đầu bằng chữ cái (Ví dụ: IOT0012345)
        return isinstance(device_code, str) and len(device_code) == 10 and device_code[0].isalpha()

    @classmethod
    def update_maintenance_cost(cls, new_cost):
        cls.base_maintenance_cost = new_cost
        logging.info(f"Hệ thống cập nhật chi phí bảo trì cơ sở thành: {new_cost} VND")


# ==========================================
# 2. CÁC LỚP CON TIÊU CHUẨN (SUBCLASSES)
# ==========================================
class ProductionRobot(BaseDevice):
    def __init__(self, device_code, device_name, operating_hours=0, completed_products=0):
        super().__init__(device_code, device_name, operating_hours)
        self.completed_products = completed_products

    def track_performance(self):
        # Tính toán hiệu suất OEE mô phỏng theo số liệu đầu ra thực tế
        if self.operating_hours == 0:
            return 0.0
        oee = (self.completed_products / (self.operating_hours * 2.166667))
        return round(oee, 1)

    def run_diagnostic(self):
        if self.completed_products > 10000:
            return f"[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!\nKết quả chẩn đoán: Nguy hiểm: Sản lượng vượt 10,000 sản phẩm! Cần bảo dưỡng cánh tay robot."
        return "Kết quả chẩn đoán: Hệ thống cơ khí hoạt động an toàn."


class ThermalSensor(BaseDevice):
    def __init__(self, device_code, device_name, operating_hours=0, current_temperature=25.0, safety_threshold=80.0):
        super().__init__(device_code, device_name, operating_hours)
        self.current_temperature = current_temperature
        self.safety_threshold = safety_threshold

    def track_performance(self):
        # Biên độ nhiệt an toàn
        return self.safety_threshold - self.current_temperature

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return f"[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!\nKết quả chẩn đoán: Nguy hiểm: Vượt ngưỡng nhiệt! (Nhiệt độ hiện tại: {self.current_temperature} độ C / Ngưỡng an toàn: {self.safety_threshold} độ C)"
        return "Kết quả chẩn đoán: Nhiệt độ cảm biến trong phạm vi an toàn."

class HybridSmartActuator(ProductionRobot, ThermalSensor):
    def __init__(self, device_code, device_name, operating_hours=0):
        # Khởi tạo tường minh tránh xung đột tham số trong kiến trúc Kim Cương
        BaseDevice.__init__(self, device_code, device_name, operating_hours)
        self.completed_products = 0
        self.current_temperature = 25.0
        self.safety_threshold = 80.0

    def track_performance(self):
        # Đa hình phức hợp tích hợp
        oee = ProductionRobot.track_performance(self)
        margin = ThermalSensor.track_performance(self)
        return f"OEE: {oee}% | Biên độ nhiệt: {margin}°C"

    def run_diagnostic(self):
        # Ưu tiên kiểm tra lỗi nghiêm trọng từ cảm biến nhiệt trước, sau đó tới robot
        if self.current_temperature > self.safety_threshold:
            return ThermalSensor.run_diagnostic(self)
        return ProductionRobot.run_diagnostic(self)


# ==========================================
# 4. DUCK TYPING GATEWAYS (CỔNG NGOẠI VI)
# ==========================================
class MQTTEngineGateway:
    def process_stream(self, device_object):
        print("[Hệ thống MQTT Engine]: Đang khởi tạo băng thông kết nối dữ liệu IoT...")

class ERPReportGateway:
    def process_stream(self, device_object):
        print("[Hệ thống ERP Report Gateway]: Đang đồng bộ số liệu vào hệ thống quản trị ERP...")

class InvalidGateway:
    pass # Cố tình tạo để test lỗi kiểm thử hệ thống

def export_telemetry_data(data_gateway, device_object):
    try:
        if not hasattr(data_gateway, 'process_stream'):
            raise AttributeError()
        
        data_gateway.process_stream(device_object)
        print("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
        print(f"Dữ liệu của thiết bị {device_object.device_code} đã được đóng gói và xuất chuỗi luồng thành công.")
        logging.info(f"Xuất telemetry thành công cho thiết bị {device_object.device_code}")
    except AttributeError:
        print("[Lỗi] (ERR-IOT-05): Xung đột kiến trúc! Không thể xuất dữ liệu do cấu hình cổng ngoại vi không tương thích.")
        logging.error("ERR-IOT-05: Cổng ngoại vi không tương thích phương thức process_stream.")


# ==========================================
# 5. CLI INTERFACE MENU (GIAO DIỆN ĐIỀU HÀNH)
# ==========================================
def main():
    devices_list = []
    current_device = None

    while True:
        print("\n===== Rikkei Smart Factory IoT Simulator =====")
        print("1. Đăng ký & Khởi tạo thiết bị IoT mới")
        print("2. Xem thông tin thiết bị & Thứ tự kế thừa (MRO)")
        print("3. Check-in giờ vận hành & Cập nhật chỉ số hiệu suất (Đa hình)")
        print("4. Thực thi quy trình tự chẩn đoán kỹ thuật (Diagnostic)")
        print("5. Cộng gộp thời gian tải & So sánh hao mòn (Operator Overloading)")
        print("6. Xuất dữ liệu vận hành ra Cổng ngoại vi (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        if choice == '1':
            print("\n--- ĐĂNG KÝ THIẾT BỊ IOT MỚI ---")
            print("1. Production Robot (Robot sản xuất lắp ráp)")
            print("2. Thermal Sensor (Cảm biến nhiệt độ)")
            print("3. Hybrid Smart Actuator (Thiết bị truyền động lai)")
            type_choice = input("Chọn phân loại thiết bị (1-3): ").strip()
            
            code = input("Nhập mã thiết bị 10 ký tự: ").strip()
            name = input("Nhập tên thiết bị: ")
            
            try:
                if type_choice == '1':
                    current_device = ProductionRobot(code, name)
                    print(f"[Thành công]: Đăng ký Robot sản xuất thành công!")
                elif type_choice == '2':
                    current_device = ThermalSensor(code, name)
                    print(f"[Thành công]: Đăng ký Cảm biến nhiệt độ thành công!")
                elif type_choice == '3':
                    current_device = HybridSmartActuator(code, name)
                    print(f"[Thành công]: Đăng ký Thiết bị truyền động lai thành công!")
                else:
                    print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")
                    continue
                
                devices_list.append(current_device)
                print(f"Tên thiết bị: {current_device.device_name}")
            except ValueError:
                # Lỗi ERR-IOT-01 đã được in phía trong constructor của BaseDevice
                continue

        elif choice in ['2', '3', '4', '5', '6']:
            # Kiểm tra bẫy thao tác rỗng (ERR-IOT-02)
            if current_device is None:
                print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                logging.warning("ERR-IOT-02: Truy cập thiết bị khi danh sách trống.")
                continue

            if choice == '2':
                print("\n--- THÔNG TIN THIẾT BỊ HIỆN TẠI ---")
                print(f"Loại thiết bị: {current_device.__class__.__name__}")
                print(f"Nhà máy: {current_device.factory_name}")
                print(f"Mã thiết bị: {current_device.device_code}")
                print(f"Tên thiết bị: {current_device.device_name}")
                print(f"Số giờ vận hành: {current_device.operating_hours} giờ")
                
                if hasattr(current_device, 'completed_products'):
                    print(f"Sản phẩm hoàn thành: {current_device.completed_products} sản phẩm")
                if hasattr(current_device, 'current_temperature'):
                    print(f"Nhiệt độ hiện tại: {current_device.current_temperature} độ C")
                
                # In chuỗi MRO chuẩn hóa quy định
                mro_chain = " -> ".join([m.__name__ for m in current_device.__class__.__mro__ if m.__name__ != 'ABC'])
                print(f"[Hệ thống MRO]: {mro_chain}")

            elif choice == '3':
                print("\n--- GHI NHẬN SỐ LIỆU VẬN HÀNH ---")
                try:
                    hours_input = input("Nhập số giờ chạy mới phát sinh: ").strip()
                    if not hours_input.isdigit() or int(hours_input) <= 0:
                        raise ValueError()
                    hours = int(hours_input)

                    if isinstance(current_device, HybridSmartActuator):
                        prod_input = input("Nhập số lượng sản phẩm hoàn thành mới bổ sung: ").strip()
                        temp_input = input("Nhập thông số nhiệt độ hiện thời mới ghi nhận: ").strip()
                        if not prod_input.isdigit() or int(prod_input) <= 0:
                            raise ValueError()
                        current_device.completed_products += int(prod_input)
                        current_device.current_temperature = float(temp_input)
                    elif isinstance(current_device, ProductionRobot):
                        prod_input = input("Nhập số lượng sản phẩm hoàn thành mới bổ sung: ").strip()
                        if not prod_input.isdigit() or int(prod_input) <= 0:
                            raise ValueError()
                        current_device.completed_products += int(prod_input)
                    elif isinstance(current_device, ThermalSensor):
                        temp_input = input("Nhập thông số nhiệt độ hiện thời mới ghi nhận: ").strip()
                        current_device.current_temperature = float(temp_input)

                    current_device._add_hours(hours)
                    print("[Thành công]: Đã cập nhật số liệu vận hành.")
                    print(f"Tổng số giờ chạy tích lũy: {current_device.operating_hours} giờ.")
                    
                    # Gọi phương thức đa hình đồng nhất track_performance()
                    perf_result = current_device.track_performance()
                    if isinstance(current_device, ProductionRobot) and not isinstance(current_device, HybridSmartActuator):
                        print(f"Chỉ số hiệu suất thiết bị tổng thể (OEE): {perf_result}%")
                    else:
                        print(f"Báo cáo hiệu suất: {perf_result}")
                        
                except ValueError:
                    print("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
                    logging.error("ERR-IOT-03: Nhập sai định dạng kiểu dữ liệu số.")

            elif choice == '4':
                print("\n--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
                diag_msg = current_device.run_diagnostic()
                print(diag_msg)
                print(f"Định mức chi phí bảo trì hệ thống dự kiến: {current_device.base_maintenance_cost:,} VND")

            elif choice == '5':
                print("\n--- KIỂM KÊ & SO SÁNH TẢI (OPERATOR OVERLOADING) ---")
                if len(devices_list) < 2:
                    print("[Thông báo]: Cần đăng ký thêm ít nhất một thiết bị đối ứng khác (Chức năng 1) để thực hiện so sánh.")
                    continue
                
                print(f"Thiết bị hiện tại (A): {current_device.device_code} (Số giờ chạy: {current_device.operating_hours} giờ)")
                print("Danh sách thiết bị đối ứng sẵn có:")
                for idx, dev in enumerate(devices_list):
                    if dev != current_device:
                        print(f"[{idx}] Mã: {dev.device_code} | Tên: {dev.device_name} | Giờ chạy: {dev.operating_hours} giờ")
                
                try:
                    target_idx = int(input("Chọn số thứ tự thiết bị đối ứng (B): "))
                    device_B = devices_list[target_idx]
                    
                    if current_device < device_B:
                        print("[Kết quả So sánh (__lt__)]: Hao mòn (số giờ chạy) của thiết bị A ÍT HƠN thiết bị B.")
                    else:
                        print("[Kết quả So sánh (__lt__)]: Hao mòn (số giờ chạy) của thiết bị A KHÔNG ÍT HƠN thiết bị B.")
                    
                    total_hours = current_device + device_B
                    print(f"[Kết quả Tổng hợp (__add__)]: Tổng thời gian tải vận hành của cả 2 thiết bị là: {total_hours} giờ.")
                except (ValueError, IndexError):
                    print("[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")

            elif choice == '6':
                print("\n--- XUẤT DỮ LIỆU VẬN HÀNH RA CỔNG NGOẠI VI ---")
                print("1. Xuất dữ liệu qua cổng MQTT (Cloud Stream)")
                print("2. Đồng bộ số liệu vào hệ thống quản trị ERP")
                print("3. Test Cổng lỗi (Kiểm tra bẫy ngoại vi không tương thích)")
                gt_choice = input("Chọn cổng kết nối ngoại vi (1-3): ").strip()
                
                if gt_choice == '1':
                    export_telemetry_data(MQTTEngineGateway(), current_device)
                elif gt_choice == '2':
                    export_telemetry_data(ERPReportGateway(), current_device)
                elif gt_choice == '3':
                    export_telemetry_data(InvalidGateway(), current_device)
                else:
                    print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")

        elif choice == '7':
            print("\nCảm ơn bạn đã sử dụng hệ thống Quản lý Thiết bị Rikkei Smart Factory IoT Pro!")
            break
        else:
            print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")
            logging.warning("ERR-IOT-06: Người dùng nhập sai lựa chọn Menu chính.")

if __name__ == "__main__":
    main()