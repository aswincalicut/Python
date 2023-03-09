#def message(name):
#    print(f"Hello " + name)

#message("Aswin")
#message("Amal")

#def find_sum(num1, num2):
#    print(num1 + num2)

#find_sum(10, 6)

#def find_square(num):
#    return num * num
#
#print(find_square(10))


#def recursion(n):
#    if n <= 1:
#        return n
#    else:
#        return n + recursion(n - 1)
#s = recursion(4)
#print(s)

#list1 = [1, 2, 3, 4, 5, 6, 7, 8]

#def even(x):
#    if x % 2 == 0:
#        return x
#f = filter(even, list1)
#print(list(f))

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

f = filter(lambda x: x % 2 == 0, list1)
print(list(f))

