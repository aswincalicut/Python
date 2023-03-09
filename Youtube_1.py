# class Cars:
#     condition = "Good"
#     def __init__(self,name, price, colour):
#         self.name = name
#         self.price = price
#         self.colour = colour
#     def start(self,n):
#         return self.name + " Engine started " + n
#         # print(self.name +" Engine started " + n
#     def accident(self,n):
#         return self.name + " Got crashed " + n
#
# car1 = Cars("Lamborgini", 4000000, "Green")
# car2 = Cars("Supra MK4", 80000000, "Orange")
#
# print(car1.name, car1.price, car1.colour, car1.condition)
#
# print(car1.start("That's Cool"))
# print(car2.start("Yeah boy"))
# print(car1.accident(":Oh No"))
# print(car2.accident(":Noooooooooooooooooooooooooooooooooo"))
# print(car2.condition)

# class Parent():
#     def feature1(self):
#         return "Feature1"
#     def feature2(self):
#         return "Feature2"
# class child(Parent):
#     def feature3(self):
#         return "Feature3"
#     def feature4(self):
#         return "Feature4"
#
# a = child()
# b = Parent()
# print(a.feature1())
# print(a.feature4())
# print(b.feature1())
# print(b.feature2())
# print(a.feature3())

# class A():
#     def __init__(self):
#         r = 7
#     def feature1(self):
#         return "Feature1"
#     def feature2(self,n):
#         return "Feature2" + n
# class B():
#     def __init__(self):
#         g = 6
#     def feature3(self):
#         return "Feature3"
#     def feature4(self):
#         return "Feature4"
# class C(A,B):
#     def __init__(self):
#         k = 3
#     def feature5(self):
#         return "Feature5"
#     def feature6(self):
#         return "Feature6"
#
# s = C()
# d = C()
#
#
# print(s.feature1())
# print(s.feature6())
# print(s.__init__())
# print("THis is " + s.feature2(" Hello"))
# print("Hello" + " " + s.feature3())
# print(d.feature5())

# class A():
#     def number1(self):
#         return "This is number 1"
#     def number2(self):
#         return "This is number 2"
# class B():
#     def number3(self):
#         return "This is number 3"
#     def number4(self):
#         return "This is number 4"
# class C():
#     def number5(self):
#         return "This is number 5"
#     def number6(self):
#         return "This is number 6"
# class D(A,B,C):
#     def number7(self):
#         return "This is number 7"
#     def number8(self):
#         return "This is number 8"
#
# k = D()
# s = D()
# print(k.number1())
# print(k.number2())
# print(k.number3())

class Person():
    def __init__(self,name, number):
        self.name = name
        self.number = number
    def adress(self):
        print(self.name, self.number)
class Doctor(Person):
    pass
class Patient(Person):
    pass

Doc1 = Doctor("Anil kumar", 22468)
Pat1 = Patient("Aswin", 1234)

Doc1.adress()
Pat1.adress()






