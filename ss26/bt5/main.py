# class Animal():
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

#     def breed(self):
#         print("Cho tôi ăn, cho tôi ăn")

# class Dog(Animal):
#     def __init__(self, name, type, sound):
#         super().__init__(name, type)
#         self.sound = sound
    
#     # def breed(self):
#     # return super().breed()

#     # ghi đè phương thức - overwrite
#     def breed(self):
#         print("Gâu Gâu")
# class Cat(Animal):
#     def __init__(self, name, type):
#         super().__init__(name, type)

# dog_1 = Dog("Corgi", "Chó cảnh", "ẳng ẳng")
# # print(f"Dây là {dog_1.name} Thuộc giống {dog_1.type} kêu {dog_1.sound}")
# dog_1.breed()


class a:
    def show(self):
        print("Đây là lớp a")

class b(a):
    def show(self):
        return super().show()
    # def show(self):
    #     print("Đây là lớp b")
    # pass
class c(a):
    def show(self):
        print("Đây là lớp c")

class d(b, c):
    # def show(self):
    #     print("Đây là lớp d")
    pass
obj_d = d()
print(d.mro)
obj_d.show()