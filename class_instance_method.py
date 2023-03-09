# instance method
import codecs


# class student():
#     school = "arrow"
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def average(self):
#         return(self.m1+self.m2+self.m3)/3
#
# a = student(10,15,20)
# b = student(100,222,333)
#
# print(a.average())
# print(b.average())

#class method

# class student():
#     school = "arrow" #class variable
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1 #instance variable
#         self.m2 = m2
#         self.m3 = m3
#     def avg(self):
#         return(self.m1+self.m2+self.m3)/3
#     @classmethod
#     def info(cls):
#         return(self.m1+self.m2+self.m3)/3
#     def name(cls):
#         return cls.school
#
# a = student(5,10,20)
# b = student(100,500,1000)

# print(a.avg())
# #print(a.info())
# print(a.name())
# print(b.avg())

# static method

# class student():
#     school = "Arrow"
#     @staticmethod
#     def name():
#         print("This is static method")
#
# a = student()
# print(a.name())

# innerclass method

class student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.laptop() #calling innerclass

    def show(self):
        print(self.name,self.rollno)
        self.laptop.show1()

    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show1(self):
            print(self.brand,self.cpu,self.ram)


s1 = student("Arjun", 8)
lap1 = student.laptop()

print(s1.laptop.brand)
print(s1.show())
print(lap1.show1())
print(s1.laptop.ram)








