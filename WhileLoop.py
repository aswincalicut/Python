list1 = []
list2 = []

a = int(input("Enter the limit for list1 : "))

for i in range(a):
    result1 = int(input("Enter the numbers for list1 : "))
    list1.append(result1)

b = int(input("Enter the limit for list2 : "))
for i in range(b):
    result2 = int(input("Enter the numbers for list2 : "))
    list2.append(result2)
print(list1)
print(list2)

if len(list1) == len(list2):
    print("Both list are same length")
else:
    print("Both list are not same length")

if sum(list1) == sum(list2):
    print("Sum of both list are same ")
else:
    print("Sum of both list are not same ")

b = 0
for i in list1:
    for j in list2:
        if i == j:
            b = i
            print("Same value occurs in both list ", i)
        if b == 0:
            print("No same value occurs in both list ")
print(b)
