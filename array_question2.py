list1 = []


limit = int(input("Enter the total number you want : "))

for i in range(limit):
    a = int(input("Enter the values : "))
    list1.append(a)
print(list1)
a = len(list1)
b = list1[4]

count_5 = 0

for j in list1:
    if j == b:
        count_5 += 1
if a == 8 and count_5 >= 3:
    print("True")
else:
    print("False")

#print(len(list1))
print(count_5)
