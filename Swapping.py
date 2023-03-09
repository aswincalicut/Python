# 1st question

#a = 30
#b = 20
#c = 10

#if(a>b) and (a>c):
 #   print("a is greatest")
#elif (b>a) and (b>c):
 #   print("b is greatest")
#else:
 #   print("c is greatest")

# 2nd question
#n = input("Enter a number :")
#a = n+n
#b = n+n+n

#print(int(n)+ int(a)+ int(b))

# 3rd question

#a = "Python"
#b = list(a)
#print(b)
#b.remove("P")
#b.remove("n")
#b.append("P")
#b.insert(0, "n")
#print(b)
#for i in b:
 #   print(i,end="")


# 4th question

#a = []
#b = int(input("Enter the number of elements:"))

#for i in range(b):
 #   c = int(input("Enter the values : "))
  #  if c <= 100:
   #     a.append(c)
    #else:
     #   a.append("over")
#print(a)

# 5th question

#list1 = ["aswin.a", "amal", "binu", "aravind", "anuvind", "carter", "aaaaaaaaaa"]
#count = 0
#print(list)
#for i in list1:
    #print(i)
 #   for j in i:
        #print(j)
  #      if j == "a":
   #         count += 1
#print(count)


# 6th question

list1 = []
list2 = []

while True:
    number = int(input("Enter the numbers for list1 : "))
    list1.append(number)

    choice = input("Enter another number? (y/n): ")
    if choice == "n":
        break

while True:
    number2 = int(input("Enter numbers for list2 : "))
    list2.append(number2)

    choice2 = input("Enter another number? (y/n) : ")
    if choice2 == "n":
        break
print(list1)
print(list2)

#print(len(list1) and len(list2))

if len(list1) == len(list2):
    print("Both list are same Length ")
else:
    print("Both list are not same Length ")

if sum(list1) == sum(list2):
    print("Sum of values of both list are same ")
else:
    print("Sum of values of both list are not same ")

#if set(list1) == set(list2):
 #   print("Same value occurs in both list ")
#else:
 #   print("No same value occurs in both list ")
b = 0
for i in list1:
    #print(i)
    for j in list2:
        #print(j)
        if i == j:
            b = i
            print("Same value occurs in both list", b)
    if b == 0:
        print("No same value occurs in both list ")



























