#single level

# class A():
#     def features1(self):
#         k = "feature1"
#         return k
#     def feature2(self):
#         s = "feature2"
#         return s
#
# class B(A):
#     def feature3(self):
#         j = "feature3"
#         return j
#     def feature4(self):
#         l = "feature4"
#         return  l
# class C(B):
#     def feature5(self):
#         n = "feature5"
#         return n

# A = C()
#
# print(A.features1())
# print(A.feature2())
# print(A.feature5())


#multiple inheritance

# class A:
#     def features1(self):
#         k = "feature1"
#         return k
#     def feature2(self):
#         s = "feature2"
#         return s
#
# class B:
#     def feature3(self):
#         j = "feature3"
#         return j
#     def feature4(self):
#         l = "feature4"
#         return  l
# class C(A,B):
#     def feature5(self):
#         n = "feature5"
#         return n

# a = C()
#
# print(a.features1())


# constructor inheritance

# class A():
#     def __init__(self):
#         g = "A init"
#         return g
#     def feature1(self):
#         f1 = "Feature1"
#         return f1
#     def feature2(self):
#         f2 = "feature2"
#         return f2
# class B(A):
#     def __init__(self):
#         super().__init__()
#         #k = "B init"
#         print("B init")
#     def feature3(self):
#         f3 = "feature3"
#         return f3
#     def feature4(self):
#         f4 = "feature4"
#         return f4
#
# a1 = B()
#
# print(a1.feature1())
# print(a1.feature3())
# print(a1.feature4())

# multiple inheritance init

class A:
    def __init__(self):
        r = 7

    def features1(self):
        k = "feature1"
        return k
    def feature2(self):
        s = "feature2"
        return s

class B:
    def __init__(self):
        s = 9

    def feature3(self):
        j = "feature3"
        return j
    def feature4(self):
        l = "feature4"
        return l
class C(A,B):
    def __init__(self):
        super().__init__()
        g = 7

    def feature5(self):
        n = "feature5"
        return n

a = C()
b = C()

print(a.features1())
print(a.__init__())
print(a.feature2())
print(b.feature4())
print(b.feature5())




