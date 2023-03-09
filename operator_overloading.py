# operator overloading
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __sub__(self, other):
#         m1 = self.m1 * other.m1
#         m2 = self.m2 * other.m2
#         s3 = Student(m1, m2)
#         return s3
#
# s1 = Student(34, 45)
# s2 = Student(67, 57)
#
# s4 = s1 - s2
#
# print(s4.m1)
# print(s4.m2)

#method overloading

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def sum(self, a=None, b=None, c=None):
#         s = 0
#         if a!=None and  b!=None and c!=None:
#             s = a+b+c
#             return s
#         elif a!=None and b!=None:
#             s = a+b
#             return s
#
#         else:
#             s = a
#             return s
#
# s1 = Student(5,3)
#
# print(s1.sum(4,5,5))
# print(s1.sum(5))
# print(s1.sum(2,1))
# print(s1.sum())

# polymorphism
# class a():
#     def show(self):
#         return "This is A"
# class b(a):
#     def show(self):
#         return "This is B"
# c = a()
#
# print(c.show())

# Python program to
# demonstrate protected members
class Base():
    def __init__(self):
        self._a = 2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protector member of base class:", self._a)

        self._a = 3
        print("Calling modified protector member outside the class:", self._a)



obj1 = Derived()
obj2 = Base()

print("Accessing protected member of obj1:",obj1._a)
print("Acessing protected member of obj2:", obj2._a)
print(obj1._a)
print(obj2._a)