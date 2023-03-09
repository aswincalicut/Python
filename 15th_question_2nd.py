list1 = []

limit = input("Enter the limit : ")

a = list(limit.split(' '))
print(a)
max1 = len(a[0])
word = ""

for i in a:
    if len(i) > max1:
        max1 = len(i)
        word = i
print(word)










