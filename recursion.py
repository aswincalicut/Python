# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         x = n*factorial(n-1)
#         return x
#
# print(factorial(3))

# fibinocci
# def fibinocci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibinocci(n-1) + fibinocci(n-2))
#
# c = 10
# if c <= 0:
#     print("Enter a positive number")
# else:
#     for i in range(c):
#         print(fibinocci(i))


a = input("Enter a string: ")
b = input("Enter a substring: ")
count = 0

for i in a:
    if i in b:
        count += 1
    else:
        count = 1
print(count)

