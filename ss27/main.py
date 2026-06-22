class Student:
    def __init__(self,id,name,theory_score, practice_score,project_score ):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = ""
    
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def theory_score(self):
        return self.__theory_score
    @property
    def practice_score(self):
        return self.__practice_score
    @property
    def project_score(self):
        return self.__project_score
    @property
    def final_score(self):
        return self.__final_score
    @property
    def academic_rank(self):
        return self.__academic_rank
    def update_theory_score(self,theory_score ):
        self.__theory_score = theory_score
    def update_practice_score(self,practice_score):
        self.__practice_score = practice_score
    def update_project_score(self,project_score):
        self.__project_score = project_score
    def calculate_final_score(self):
        self.__final_score = (self.__theory_score * 0.2) + (self.__practice_score * 0.3) + (self.__project_score*0.5)
    def classify_academic_rank(self):
        if self.__final_score >= 8.5:
            self.__academic_rank = "giỏi"
        elif self.__final_score >= 7 :
            self.__academic_rank = "khá"
        elif self.__final_score >= 5:
            self.__academic_rank = "trung bình"
        elif self.__final_score < 5 and self.__final_score >= 0:
            self.__academic_rank = "yếu"
class StudentManager :
    def __init__(self):
        self.students : list[Student] = []

       

    def add_student(self):
       stu_id = input("nhập MaSV: ")
       if not stu_id:
           print("không có mã SV") 
           return
       for stu in self.students:
           if stu.id == stu_id:
               print("mã SV đã tồn tại")
               return
       stu_name = input("nhập Tên SV:")
       if not stu_name:
            print("không có tên SV") 
            return
       stu_theory_score = float(input("nhập điểm lý thuyết: "))
       stu_practice_score = float(input("nhập điểm thực hành: "))
       stu_project_score = float(input("nhập điểm đồ án: "))
       if not stu_theory_score >= 0 and  stu_theory_score <= 10:
           print("điểm không hợp lệ")
       if not stu_practice_score >= 0 and  stu_practice_score <= 10:
            print("điểm không hợp lệ")
       if not stu_project_score >= 0 and  stu_project_score <= 10:
           print("điểm không hợp lệ")
       new_student = Student(stu_id,stu_name,stu_theory_score,stu_practice_score,stu_project_score)
       new_student.calculate_final_score()
       new_student.classify_academic_rank()
       self.students.append(new_student)
       print("thêm sinh viên thành công")
    def show_all(self):
        print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<20} | {'Điểm Thực Hành':<20} | {'Điểm Đồ Án':<20} | {'Điểm Tổng Kết':<20} | {'Học Lực':<10}")
        for stu in self.students:
            print(f"{stu.id :<10} | {stu.name :<20} | {stu.theory_score :<20} | {stu.practice_score :< 20}| {stu.project_score :<20} | {stu.final_score :< 20} | {stu.academic_rank :<10} ")
    def update_student(self):
        stu_id = input("nhập mã SV cần cập nhật: ")
        for stu in self.students:
            if stu.id == id:
                stu_theory_score = float(input("nhập điểm lý thuyết: "))
                stu_practice_score = float(input("nhập điểm thực hành: "))
                stu_project_score = float(input("nhập điểm đồ án: "))
                if not stu_theory_score >= 0 and  stu_theory_score <= 10:
                    print("điểm không hợp lệ")
                    return
                if not stu_practice_score >= 0 and  stu_practice_score <= 10:
                        print("điểm không hợp lệ")
                        return
                if not stu_project_score >= 0 and  stu_project_score <= 10:
                    print("điểm không hợp lệ")
                    return
                stu.update_theory_score(stu_theory_score)
                stu.update_practice_score(stu_practice_score)
                stu.update_project_score(stu_project_score)
                print("cập nhật thành công")
        else: 
                print("không tìm thấy SV")
                return
            
    def delete_student(self):
        stu_id = input("nhập mã SV cần xóa")
        for stu in self.students:
            if stu.id == stu_id:
             choice = input("Bạn có chắc muốn xóa sinh viên này không? (Y/N): ")
             if choice.lower() == "y" : 
                 self.students.remove(stu) 
                 print("đã xóa thành công")
             elif  choice.lower() == "n" :
                 print("đã hủy bỏ thao tác xóa")
                 return
        else: 
            print("không tìm thấy SV")
            return
    def search_student(self): 
        name_input = input("nhập tên cần tìm kiếm: ")
        find_list_stu  = StudentManager()
        for stu in self.students:
            if name_input in stu.name:
                find_list_stu.append(stu)
        
        if not find_list_stu:
            print("không có sinh viên nào được tìm thấy")
        else: 
            find_list_stu.show_all()
        

