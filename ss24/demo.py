class PTITStudent:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa
        self.age = 19

    @property
    def name(self):
         return self.name   
    
    @property
    def gpa(self):
         return self.__gpa
    
    @gpa.setter
    def update_gpa(self, new_gpa: float):
        if new_gpa < 0:
              raise ValueError("Điểm không được nhỏ hơn 0")
        self.__gpa = new_gpa          

    def say_hi(self, class_name):
            print(f"Tôi là {self.name}, tôi chào lớp {class_name} nha!")

    def rate_gpa(self):
            if (self.__gpa) > 3.6:
                print("Xuất sắc")
            elif (self.__gpa) > 3.2:
                print("Giỏi")
            elif (self.__gpa) > 3.0:
                print("Khá")
            else:
                print("Trung bình")

    @staticmethod
    def say_goodbye():
         print("Tạm biệt")

student_rikkei = PTITStudent("Khiêm", 3.2)
student_tuxa = PTITStudent("Trứ", 3.7)
student_chinhquy = PTITStudent("Khoa", 4.0)

# print(student_rikkei.name, student_rikkei.gpa)
student_rikkei.say_hi()