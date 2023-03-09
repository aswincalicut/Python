# def function1(name):
#     print("hello " + name)
#
# function1("bro")
# function1("aswin")
#
# def recursion(n):
#     if n <= 1:
#         return n
#     else:
#         return n + recursion(n - 1)
# s = recursion(2)
# print(s)
#

# lambda function

# a = lambda x: x * x
# print(a(10))

# list1 = [1, 2, 3, 4, 5, 6, 8]

# def even(x):
#     if x % 2 == 0:
#         return x
# f = filter(even, list1)
# print(list(f))

# f = filter(lambda x: x % 2 == 0, list1)
# print(list(f))

# class Cars:
#     def __init__(self,name,price,colour,):
#         self.name = name
#         self.price = price
#         self.colour = colour
#     def start(self):
#         print(self.name + " Engine started")
#
# car1 = Cars("Maruti Swift", 10000, "Red")
# car2 = Cars("Toyota Innova", 20000, "White")
# car1.price = 15000
# car2.colour = "Blue"
# del car1.colour
# del car2
#
# print(car1.name, car1.price)
# print(car2.name, car2.price, car2.colour)

