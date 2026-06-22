#Phần 1: Phân tích và Thiết kế Giải pháp (Design Document)1. Sơ đồ cấu trúc kiến trúc & MROBaseLesson (Abstract Class): Lớp gốc định nghĩa khung sườn (thuộc tính chung, toán tử nạp chồng, hàm trừu tượng). Không thể khởi tạo trực tiếp.VideoLesson & CodingChallenge: Kế thừa trực tiếp từ BaseLesson, triển khai các hàm trừu tượng theo nghiệp vụ riêng.HybridAssessment: Đa kế thừa từ cả VideoLesson và CodingChallenge.Giải quyết xung đột (MRO): Python sử dụng thuật toán C3 Linearization để tạo ra danh sách Method Resolution Order (MRO). Thứ tự tìm kiếm của HybridAssessment sẽ là: HybridAssessment $\rightarrow$ VideoLesson $\rightarrow$ CodingChallenge $\rightarrow$ BaseLesson $\rightarrow$ object. Nhờ MRO, khi gọi một phương thức bị trùng tên, Python sẽ ưu tiên lấy phương thức ở lớp cha được khai báo trước (từ trái sang phải), giúp tránh lỗi "Diamond Problem" (Vấn đề kim cương).2. Phân tích cơ chế Duck TypingDuck Typing là phong cách lập trình không quan tâm đến "kiểu" (type/class) của đối tượng mà chỉ quan tâm đến hành vi (method/property) của nó.Lợi ích: Hàm sync_to_cloud chỉ gọi cloud_service.upload_lesson(lesson). Nhờ vậy, trong tương lai Rikkei Academy muốn thêm AzureBlobStorage, chỉ cần tạo class có chứa hàm upload_lesson() mà không cần sửa đổi bất kỳ dòng code nào trong lõi hệ thống LMS hay hàm đồng bộ. Điều này đảm bảo tính mở (Open/Closed Principle) của hệ thống.Phần 2: Triển khai Code Python Hoàn chỉnhDưới đây là toàn bộ mã nguồn xử lý mượt mà cả logic tính toán lẫn các Edge Cases (bẫy dữ liệu). Bạn có thể sao chép code này vào một file main.py để chạy.Pythonfrom abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACT BASE CLASS & CORE LOGIC
# ==========================================
class BaseLesson(ABC):
    platform_name = "Rikkei Academy LMS"
    base_completion_points = 10

    def __init__(self, lesson_code, title, duration_minutes):
        # Edge Case 1: ABC tự động ném TypeError nếu khởi tạo trực tiếp BaseLesson
        
        # Kiểm tra mã bài học hợp lệ
        if not self.validate_lesson_code(lesson_code):
            raise ValueError("Mã bài học không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng LMS.")
        
        # Edge Case 2: Bẫy dữ liệu thời lượng âm hoặc bằng 0
        if duration_minutes <= 0:
            raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")

        self.lesson_code = lesson_code
        self._title = title.strip().upper()  # Chuẩn hóa in hoa qua thuộc tính ẩn
        self.__duration_minutes = duration_minutes # Đóng gói private

    # @property: Biến một phương thức thành thuộc tính (chỉ đọc), chặn can thiệp từ bên ngoài
    @property
    def duration_minutes(self):
        return self.__duration_minutes

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.strip().upper()

    # @abstractmethod: Ép buộc các lớp con phải triển khai hàm này (Tính đa hình)
    @abstractmethod
    def calculate_completion_score(self):
        pass

    @abstractmethod
    def update_content(self, new_data):
        pass

    # Operator Overloading: Nạp chồng toán tử +
    def __add__(self, other):
        # Edge Case 3: Kiểm tra tính hợp lệ khi Overloading
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes + other.duration_minutes

    # Operator Overloading: Nạp chồng toán tử <
    def __lt__(self, other):
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes < other.duration_minutes

    # @staticmethod: Hàm tĩnh không cần truy cập thuộc tính của class/instance (không cần self/cls)
    @staticmethod
    def validate_lesson_code(lesson_code):
        return isinstance(lesson_code, str) and len(lesson_code) == 10 and lesson_code.startswith("LMS")

    # @classmethod: Tác động lên biến cấp Class, dùng chung cho toàn bộ object
    @classmethod
    def update_base_points(cls, new_points):
        cls.base_completion_points = new_points

# ==========================================
# 2. SUBCLASSES (KẾ THỪA & ĐA KẾ THỪA)
# ==========================================
class VideoLesson(BaseLesson):
    def __init__(self, lesson_code, title, duration_minutes, video_quality="1080p"):
        super().__init__(lesson_code, title, duration_minutes)
        self.video_quality = video_quality
        self.view_count = 0

    def calculate_completion_score(self):
        return self.base_completion_points + (self.duration_minutes * 0.5)

    def update_content(self, new_data):
        if isinstance(new_data, str):
            if new_data.endswith("p"):
                self.video_quality = new_data
            else:
                self.title = new_data
    
    def play_video(self):
        self.view_count += 1
        print(f"Ghi nhận thành công! Học viên đã xem video bài học.\nTổng số lượt xem hiện tại: {self.view_count} lượt.")

class CodingChallenge(BaseLesson):
    def __init__(self, lesson_code, title, duration_minutes, number_of_testcases, difficulty_multiplier=1.0):
        super().__init__(lesson_code, title, duration_minutes)
        if number_of_testcases <= 0:
            raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        return self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier

    def update_content(self, new_data):
        if isinstance(new_data, int) and new_data > 0:
            self.number_of_testcases = new_data
        else:
            print("Lỗi: Số lượng testcase không hợp lệ.")

class HybridAssessment(VideoLesson, CodingChallenge):
    def __init__(self, lesson_code, title, duration_minutes, video_quality="1080p", number_of_testcases=5, difficulty_multiplier=1.5):
        # Khởi tạo BaseLesson trực tiếp để kiểm soát dữ liệu đầu vào trong đa kế thừa
        BaseLesson.__init__(self, lesson_code, title, duration_minutes)
        self.video_quality = video_quality
        self.view_count = 0
        
        if number_of_testcases <= 0:
            raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        # Tích hợp cơ chế tính điểm của cả 2 lớp cha
        video_score = self.duration_minutes * 0.5
        coding_score = self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier
        return self.base_completion_points + video_score + coding_score

    def update_content(self, new_data):
        if isinstance(new_data, int) and new_data > 0:
            self.number_of_testcases = new_data
        elif isinstance(new_data, str) and new_data.endswith("p"):
            self.video_quality = new_data

# ==========================================
# 3. DUCK TYPING SERVICES
# ==========================================
class AWSS3StorageService:
    def upload_lesson(self, lesson):
        print(f"[Hệ thống AWS S3]: Đang khởi tạo luồng băng thông kết nối tới LMS...")
        print(f"Hệ thống lưu trữ đám mây đã upload toàn bộ tài nguyên của bài học {lesson.lesson_code} lên cụm máy chủ an toàn.")

class GoogleCloudStorageService:
    def upload_lesson(self, lesson):
        print(f"[Hệ thống Google Cloud Storage]: Đang thiết lập API...")
        print(f"Hệ thống lưu trữ đám mây đã upload tài nguyên của {lesson.lesson_code} thành công.")

class InvalidStorageService:
    pass # Cố tình tạo class lỗi để test Edge Case 4

def sync_to_cloud(cloud_service, lesson):
    try:
        cloud_service.upload_lesson(lesson)
        print("Xác thực dịch vụ bằng Duck Typing thành công!")
    except AttributeError:
        # Edge Case 4: Lỗi khi không có hàm upload_lesson
        print("Dịch vụ lưu trữ đám mây không hợp lệ hoặc chưa ký kết chứng chỉ API liên thông")


# ==========================================
# 4. CHƯƠNG TRÌNH CHÍNH (MENU CLI)
# ==========================================
def main():
    lessons = []
    current_lesson = None

    while True:
        print("\n===== RIKKEI ACADEMY LMS SIMULATOR PRO =====")
        print("1. Khởi tạo bài học mới (Chọn loại bài học nội dung)")
        print("2. Xem thông tin bài học & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Cập nhật thời lượng & Nội dung bài học (Tính đa hình)")
        print("4. Xem chi tiết điểm thưởng hoàn thành bài học")
        print("5. Kiểm tra gộp thời lượng & So sánh độ dài bài học (Overloading)")
        print("6. Đồng bộ bài giảng lên Nền tảng Đám mây (Duck Typing)")
        print("7. Thoát chương trình")
        print("============================================")
        
        choice = input("Chọn chức năng (1-7): ")

        if choice == '1':
            print("--- CHỌN LOẠI BÀI HỌC KHỞI TẠO ---")
            print("1. Video Lesson (Bài học Video Lý Thuyết)")
            print("2. Coding Challenge (Bài tập Thực Hành Code)")
            print("3. Hybrid Assessment (Bài Kiểm Tra Tổng Hợp)")
            type_choice = input("Chọn loại bài học (1-3): ")
            
            code = input("Nhập mã bài học 10 ký tự: ")
            title = input("Nhập tiêu đề bài học: ")
            
            try:
                if type_choice == '1':
                    duration = int(input("Nhập thời lượng (phút): "))
                    current_lesson = VideoLesson(code, title, duration)
                    lessons.append(current_lesson)
                    print("Khởi tạo bài học Video thành công!")
                    print(f"Tiêu đề bài học: {current_lesson.title}")
                elif type_choice == '2':
                    duration = int(input("Nhập thời lượng (phút): "))
                    tests = int(input("Nhập số lượng testcase: "))
                    current_lesson = CodingChallenge(code, title, duration, tests)
                    lessons.append(current_lesson)
                    print("Khởi tạo bài học Coding thành công!")
                elif type_choice == '3':
                    duration = int(input("Nhập thời lượng (phút): "))
                    current_lesson = HybridAssessment(code, title, duration)
                    lessons.append(current_lesson)
                    print("Khởi tạo bài học Hybrid thành công!")
                else:
                    print("Loại bài học không hợp lệ.")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"Có lỗi xảy ra: {e}")

        elif choice == '2':
            if not current_lesson:
                print("Vui lòng khởi tạo bài học trước!")
                continue
            
            print("\n--- THÔNG TIN BÀI HỌC HIỆN TẠI ---")
            print(f"Loại bài học: {current_lesson.__class__.__name__}")
            print(f"Nền tảng: {current_lesson.platform_name}")
            print(f"Mã bài học: {current_lesson.lesson_code}")
            print(f"Tiêu đề bài học: {current_lesson.title}")
            print(f"Thời lượng bài học: {current_lesson.duration_minutes} phút")
            
            if isinstance(current_lesson, VideoLesson):
                print(f"Chất lượng video: {current_lesson.video_quality}")
            if isinstance(current_lesson, CodingChallenge):
                print(f"Số lượng testcase lập trình: {current_lesson.number_of_testcases} bài")
            
            print("\n[Kiểm tra MRO (Thứ tự phân giải phương thức)]:")
            for m in current_lesson.__class__.__mro__:
                print(" ->", m.__name__)

        elif choice == '3':
            if not current_lesson:
                print("Vui lòng khởi tạo bài học trước!")
                continue
                
            print("--- CẬP NHẬT NỘI DUNG & THỜI LƯỢNG ---")
            print("1. Giả lập học viên tăng lượt xem video (Chỉ dành cho Video/Hybrid)")
            print("2. Cập nhật thông số bài học (Thời lượng, testcase...)")
            sub_choice = input("Chọn tác vụ (1-2): ")
            
            if sub_choice == '1':
                if isinstance(current_lesson, VideoLesson):
                    current_lesson.play_video()
                else:
                    print("Chức năng chỉ áp dụng cho Video/Hybrid Lesson.")
            elif sub_choice == '2':
                if isinstance(current_lesson, CodingChallenge) or isinstance(current_lesson, HybridAssessment):
                    try:
                        new_tests = int(input("Nhập số lượng testcase kiểm thử mới bổ sung: "))
                        current_lesson.update_content(new_tests)
                        print("Cập nhật thông số thành công!")
                        print(f"Số lượng testcase hiện tại: {current_lesson.number_of_testcases} testcases.")
                    except ValueError:
                        print("Vui lòng nhập số nguyên.")
                else:
                    # VideoLesson
                    new_quality = input("Nhập chất lượng video mới (vd: 4K, 720p): ")
                    current_lesson.update_content(new_quality)
                    print(f"Chất lượng video đã cập nhật: {current_lesson.video_quality}")

        elif choice == '4':
            if not current_lesson:
                print("Vui lòng khởi tạo bài học trước!")
                continue
            
            print("\n--- CHI TIẾT ĐIỂM THƯỞNG HOÀN THÀNH ---")
            print(f"Bài học: {current_lesson.title} (Loại: {current_lesson.__class__.__name__})")
            print(f"Điểm cơ sở hệ thống: {current_lesson.base_completion_points} XP")
            print(f"Tổng điểm kinh nghiệm (XP) nhận được khi hoàn thành: {current_lesson.calculate_completion_score()} XP")

        elif choice == '5':
            if len(lessons) < 2:
                print("Hệ thống cần ít nhất 2 bài học để thực hiện so sánh. Hãy khởi tạo thêm (Chức năng 1)!")
                continue
            
            print("--- ĐỒNG BỘ & SO SÁNH THỜI LƯỢNG ---")
            lesson_A = lessons[0]
            lesson_B = lessons[1]
            print(f"Bài học hiện tại (A): {lesson_A.title} (Thời lượng: {lesson_A.duration_minutes} phút)")
            print(f"Bài học đối ứng (B): {lesson_B.title} (Thời lượng: {lesson_B.duration_minutes} phút)")
            
            if lesson_A < lesson_B:
                print("[Kết quả So sánh (__lt__)]: Thời lượng bài học A NGẮN HƠN thời lượng bài học B.")
            else:
                print("[Kết quả So sánh (__lt__)]: Thời lượng bài học A KHÔNG NGẮN HƠN thời lượng bài học B.")
                
            total_duration = lesson_A + lesson_B
            print(f"[Kết quả Tổng hợp (__add__)]: Tổng thời lượng học tập của cả 2 bài học là: {total_duration} phút.")

        elif choice == '6':
            if not current_lesson:
                print("Vui lòng khởi tạo bài học trước!")
                continue
                
            print("--- ĐỒNG BỘ BÀI GIẢNG LÊN NỀN TẢNG ĐÁM MÂY ---")
            print("1. Đồng bộ lên máy chủ AWS S3 Storage")
            print("2. Đồng bộ lên máy chủ Google Cloud Storage")
            print("3. Test Bẫy Lỗi (Truyền dịch vụ ảo không hợp lệ)")
            cloud_choice = input("Chọn dịch vụ lưu trữ (1-3): ")
            
            if cloud_choice == '1':
                sync_to_cloud(AWSS3StorageService(), current_lesson)
            elif cloud_choice == '2':
                sync_to_cloud(GoogleCloudStorageService(), current_lesson)
            elif cloud_choice == '3':
                sync_to_cloud(InvalidStorageService(), current_lesson)

        elif choice == '7':
            print("Cảm ơn bạn đã trải nghiệm hệ thống Quản lý Bài học Rikkei Academy LMS Pro!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 7.")

if __name__ == "__main__":
    main()