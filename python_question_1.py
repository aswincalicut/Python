list1 = [-1, -2, -3, -4, 5, 6, 7, 8, 9, 10]

x = list(i for i in list1 if i > 0)
print(x)

a = list(i*i for i in x)
print(a)

str1 = "aswin.a"
a = ["a", "e", "i", "o", "u"]
b = list(i for i in str1 if i in a)
print(b)

print(ord("A"))


