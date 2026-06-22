# Phần 1: Phân tích và thiết kế giải pháp (Design Document)
# 1. Sơ đồ cấu trúc kiến trúc (Kế thừa & Đa kế thừa)

# Hệ thống được thiết kế dựa trên mô hình phân cấp từ tổng quát đến chi tiết:

# BaseEmployee (Abstract Base Class): Lớp gốc định nghĩa khung chuẩn cho mọi nhân sự (mã nhân sự, tên, giờ làm). Các thuộc tính cốt lõi được đóng gói (Encapsulation) để bảo vệ dữ liệu.

# ↳ Lecturer (Subclass 1): Kế thừa BaseEmployee, bổ sung số ca dạy.

# ↳ AdmissionStaff (Subclass 2): Kế thừa BaseEmployee, bổ sung doanh số.

# ↳ HybridManager (Multiple Inheritance Subclass): Đa kế thừa từ cả Lecturer và AdmissionStaff. Lớp này hội tụ đặc tính của cả hai dòng nhân sự trên.

# 2. Báo cáo kỹ thuật

# Cơ chế MRO (Method Resolution Order) trong đa kế thừa:
# Khi HybridManager gọi một phương thức (ví dụ __init__), Python sẽ tìm kiếm theo thứ tự MRO: HybridManager -> Lecturer -> AdmissionStaff -> BaseEmployee -> object. Nhờ MRO, Python giải quyết triệt để các xung đột (Diamond Problem) nếu có hai thuộc tính hay hàm trùng tên ở lớp cha. Hàm super() sẽ chạy dọc theo chuỗi MRO này để đảm bảo mọi class cha đều được khởi tạo đúng 1 lần.

# Lợi ích của Duck Typing trong thanh toán lương:
# Duck Typing ("Nếu nó đi như vịt và kêu như vịt, thì nó là vịt") cho phép hàm giải ngân execute_payroll không cần quan tâm tham số truyền vào thuộc class Vietcombank hay Techcombank. Nó chỉ cần biết object đó có hàm transfer_salary() hay không. Nhờ vậy, sau này nếu hệ thống tích hợp thêm MoMo hay ZaloPay, bạn chỉ cần tạo class mới có hàm transfer_salary() mà không phải sửa lại code cốt lõi của HR.

# Phần 2: Triển khai code Python hoàn chỉnh
# Dưới đây là file script mã nguồn hoàn chỉnh. Code đã được áp dụng chuẩn đặt tên snake_case cho hàm/biến, PascalCase cho class, và có đầy đủ comment giải thích các decorator cũng như bẫy lỗi (Edge Cases).

# Python
from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACT BASE CLASS
# ==========================================
class BaseEmployee(ABC):
    # Class attributes
    company_name = "Rikkei Education"
    base_salary_rate = 3000000

    def __init__(self, emp_code, name):
        if not self.validate_employee_code(emp_code):
            raise ValueError("Mã nhân sự không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng RKE.")
        self.emp_code = emp_code
        self.name = name  # Sẽ gọi @name.setter để chuẩn hóa
        self.__working_hours = 0  # Private attribute

    # @property: Biến method thành một thuộc tính read-only để lấy giá trị __working_hours
    @property
    def working_hours(self):
        return self.__working_hours

    # Hàm nội bộ (protected) để cộng giờ làm an toàn, thay vì dùng setter mở
    def _add_working_hours(self, hours):
        if hours > 0:
            self.__working_hours += hours

    @property
    def name(self):
        return self._name

    # Setter để tự động chuẩn hóa họ tên khi khởi tạo hoặc thay đổi
    @name.setter
    def name(self, value):
        self._name = value.strip().upper()

    # @abstractmethod: Ép buộc tất cả các class con phải ghi đè (override) hàm này
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def update_kpi(self, progress):
        pass

    # Operator Overloading: Nạp chồng toán tử cộng (+)
    def __add__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented # Bẫy 3: Báo lỗi nếu cộng với kiểu dữ liệu lạ
        return self.working_hours + other.working_hours

    # Operator Overloading: Nạp chồng toán tử so sánh nhỏ hơn (<)
    def __lt__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours < other.working_hours

    # @staticmethod: Hàm tĩnh, không cần tham chiếu đến self hay cls, dùng như hàm tiện ích
    @staticmethod
    def validate_employee_code(emp_code):
        return isinstance(emp_code, str) and emp_code.startswith("RKE") and len(emp_code) == 10

    # @classmethod: Tác động lên toàn bộ class, đổi lương cơ sở của mọi nhân viên
    @classmethod
    def update_base_salary_rate(cls, new_rate):
        cls.base_salary_rate = new_rate


# ==========================================
# 2. SUBCLASSES
# ==========================================
class Lecturer(BaseEmployee):
    def __init__(self, emp_code, name):
        super().__init__(emp_code, name)
        self.teaching_slots = 0

    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000)

    def update_kpi(self, progress):
        # Giả lập cập nhật tiến độ giáo án
        print(f"Tiến độ hoàn thành khung chương trình: {progress}%")

    def conduct_class(self):
        self.teaching_slots += 1
        self._add_working_hours(2)


class AdmissionStaff(BaseEmployee):
    def __init__(self, emp_code, name):
        super().__init__(emp_code, name)
        self.revenue_generated = 0
        self.kpi_target = 100000000

    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.revenue_generated * 0.05)

    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0") # Bẫy 2
        self.revenue_generated += progress


class HybridManager(Lecturer, AdmissionStaff):
    # Tự động thừa kế __init__ qua chuỗi MRO: HybridManager -> Lecturer -> AdmissionStaff -> BaseEmployee
    def __init__(self, emp_code, name):
        super().__init__(emp_code, name)

    def calculate_salary(self):
        # Tính toán tích hợp: Lương theo giờ + Ca dạy (Lecturer) + Hoa hồng doanh số (AdmissionStaff)
        base_and_teaching = (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000)
        commission = self.revenue_generated * 0.05
        return base_and_teaching + commission

    def update_kpi(self, progress):
        # Ưu tiên tính năng cập nhật doanh số cho Hybrid Manager
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        self.revenue_generated += progress


# ==========================================
# 3. DUCK TYPING SERVICES
# ==========================================
class VietcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print("[Hệ thống VCB Corporate]: Đang kết nối tới cổng chi trả Rikkei...")
        print(f"Xác thực đối tác bằng Duck Typing thành công!\nNgân hàng đối tác đã giải ngân thành công số tiền: {amount:,.0f} VND tới nhân sự {employee.emp_code}.")

class TechcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print("[Hệ thống TCB Doanh Nghiệp]: Xử lý giao dịch 24/7...")
        print(f"Giải ngân TCB thành công số tiền {amount:,.0f} VND cho {employee.name}.")

# Hàm giải ngân độc lập - Thể hiện tính Duck Typing
def execute_payroll(payment_service, employee, amount):
    try:
        payment_service.transfer_salary(employee, amount)
    except AttributeError:
        # Bẫy 4: Object truyền vào không có hàm transfer_salary
        print("Cổng dịch vụ ngân hàng doanh nghiệp không hợp lệ hoặc chưa được liên kết liên thông kỹ thuật.")


# ==========================================
# 4. HỆ THỐNG MENU (CLI)
# ==========================================
def main_menu():
    employees = []
    current_employee = None

    while True:
        print("\n===== RIKKEI EDUCATION HR SIMULATOR PRO =====")
        print("1. Tuyển dụng nhân sự mới (Chọn loại hợp đồng nhân sự)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Ghi nhận công nhật & Cập nhật KPI (Tính đa hình)")
        print("4. Tổng hợp quỹ lương và ngân sách chi trả")
        print("5. Kiểm tra gộp giờ làm việc & So sánh hiệu suất (Overloading)")
        print("6. Giải ngân lương qua Cổng thanh toán đối tác (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ")

        if choice == '1':
            print("--- CHỌN LOẠI NHÂN SỰ KHỞI TẠO ---")
            print("1. Lecturer (Giảng viên chuyên trách)")
            print("2. Admission Staff (Nhân viên Tuyển sinh)")
            print("3. Hybrid Manager (Quản lý kiêm Giảng dạy)")
            emp_type = input("Chọn loại nhân sự (1-3): ")
            emp_code = input("Nhập mã nhân sự 10 ký tự: ")
            name = input("Nhập họ và tên: ")

            try:
                if emp_type == '1':
                    new_emp = Lecturer(emp_code, name)
                elif emp_type == '2':
                    new_emp = AdmissionStaff(emp_code, name)
                elif emp_type == '3':
                    new_emp = HybridManager(emp_code, name)
                else:
                    print("Lựa chọn không hợp lệ.")
                    continue
                
                employees.append(new_emp)
                current_employee = new_emp
                print(f"Tuyển dụng thành công!\nTên nhân sự: {new_emp.name}")
            except ValueError as e:
                print(e)
            except TypeError as e:
                # Bẫy 1: Ngăn chặn khởi tạo trực tiếp BaseEmployee
                print(f"Lỗi khởi tạo: {e}")

        elif choice == '2':
            if not current_employee:
                print("Vui lòng tuyển dụng hoặc chọn nhân sự trước.")
                continue
            
            print("\n--- THÔNG TIN NHÂN SỰ HIỆN TẠI ---")
            print(f"Loại nhân sự: {current_employee.__class__.__name__}")
            print(f"Tổ chức: {current_employee.company_name}")
            print(f"Mã nhân sự: {current_employee.emp_code}")
            print(f"Họ và tên: {current_employee.name}")
            print(f"Số giờ làm việc: {current_employee.working_hours} giờ")
            
            if hasattr(current_employee, 'teaching_slots'):
                print(f"Số ca đã dạy: {current_employee.teaching_slots} ca")
            if hasattr(current_employee, 'revenue_generated'):
                print(f"Doanh số mang về: {current_employee.revenue_generated:,.0f} VND")
            
            print("\n[MRO - Thứ tự phân giải phương thức]:")
            for m in current_employee.__class__.__mro__:
                print(f" - {m.__name__}")

        elif choice == '3':
            if not current_employee:
                print("Vui lòng tuyển dụng hoặc chọn nhân sự trước.")
                continue

            print("--- GHI NHẬN CÔNG NHẬT & HIỆU SUẤT ---")
            print("1. Ghi nhận tham gia đứng lớp (Chỉ dành cho Giảng viên/Hybrid)")
            print("2. Cập nhật tiến độ KPI / Doanh số")
            action = input("Chọn tác vụ (1-2): ")

            if action == '1':
                if hasattr(current_employee, 'conduct_class'):
                    current_employee.conduct_class()
                    print(f"Ghi nhận thành công! Thầy/Cô đã hoàn thành thêm 1 ca dạy.\nSố ca dạy hiện tại: {current_employee.teaching_slots} ca.\nSố giờ làm việc tích lũy: {current_employee.working_hours} giờ.")
                else:
                    print("Nhân sự này không có chức năng đứng lớp.")
            elif action == '2':
                try:
                    progress = float(input("Nhập giá trị tiến độ/doanh số hợp đồng mới: "))
                    current_employee.update_kpi(progress)
                    print("Cập nhật KPI thành công!")
                except ValueError as e:
                    print(f"Lỗi: {e}")

        elif choice == '4':
            if not current_employee:
                print("Vui lòng tuyển dụng hoặc chọn nhân sự trước.")
                continue

            salary = current_employee.calculate_salary()
            print("\n--- CHI TIẾT QUỸ LƯƠNG NHÂN SỰ ---")
            print(f"Nhân sự: {current_employee.name} (Loại: {current_employee.__class__.__name__})")
            print(f"Mức lương cơ sở hệ thống: {current_employee.base_salary_rate:,.0f} VND")
            print(f"Số giờ làm việc tích lũy: {current_employee.working_hours} giờ")
            print(f"Lương cứng tính theo giờ: {current_employee.working_hours * current_employee.base_salary_rate:,.0f} VND")
            print(f"Tổng lương thực nhận tháng này: {salary:,.0f} VND")

        elif choice == '5':
            if len(employees) < 2:
                print("Hệ thống cần ít nhất 2 nhân sự để thực hiện so sánh.")
                continue
            
            print("\n--- ĐỒNG BỘ & SO SÁNH GIỜ CÔNG (OPERATOR OVERLOADING) ---")
            emp_A = current_employee
            print(f"Nhân sự hiện tại (A): {emp_A.name} (Giờ công: {emp_A.working_hours} giờ)")
            
            # Đơn giản hóa việc chọn nhân sự B (lấy người đầu tiên khác người hiện tại)
            emp_B = next((e for e in employees if e != emp_A), employees[0])
            print(f"Nhân sự đối ứng (B) từ danh sách: {emp_B.emp_code} ({emp_B.name} - Giờ công: {emp_B.working_hours} giờ)")

            is_less = emp_A < emp_B
            total_hours = emp_A + emp_B

            result_str = "ÍT HƠN" if is_less else "KHÔNG ÍT HƠN"
            print(f"[Kết quả So sánh (__lt__)]: Giờ công cống hiến của nhân sự A {result_str} nhân sự B.")
            print(f"[Kết quả Tổng hợp (__add__)]: Tổng số giờ làm việc của cả 2 nhân sự là: {total_hours} giờ.")

        elif choice == '6':
            if not current_employee:
                print("Vui lòng tuyển dụng hoặc chọn nhân sự trước.")
                continue

            print("--- CHI TRẢ LƯƠNG QUA CỔNG ĐỐI TÁC TRUNG GIAN ---")
            print("1. Chi trả qua tài khoản Doanh nghiệp Vietcombank")
            print("2. Chi trả qua tài khoản Doanh nghiệp Techcombank")
            bank_choice = input("Chọn cổng ngân hàng (1-2): ")
            
            try:
                amount = float(input("Nhập số tiền giải ngân: "))
                if bank_choice == '1':
                    service = VietcombankCorporateService()
                else:
                    service = TechcombankCorporateService()
                
                execute_payroll(service, current_employee, amount)
            except ValueError:
                print("Số tiền không hợp lệ.")

        elif choice == '7':
            print("Cảm ơn đã sử dụng hệ thống Quản lý Nhân sự Rikkei Education Pro!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()