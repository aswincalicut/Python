list1 = [19,19,5,5,5,15,3,2]
count_19 = 0
count_5 = 0

for i in list1:
    if i == 19:
        count_19 = count_19+1
    if i == 5:
        count_5 = count_5+1
if count_19 == 2 and count_5 == 3:
    print("True")
else:
    print("False")

print(count_19)











