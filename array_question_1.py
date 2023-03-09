def Arraychallenge(arr):
    min_i = list1[0]
    max_profit = 0
    a = []



    for i in arr:
        if i < min_i:
            min_i = i
        elif i - min_i > max_profit:
            max_profit = i - min_i
        if i - min_i >= max_profit:
            a.append(i)
        if i - min_i >= max_profit:
            c = min_i

    b = a[-1]
    print("Greatest number is:",b)
    print("Least number is:",c)

    print(min_i)
    print("Greatest profit is:", max_profit)

list1 = [44,30,24,32,35,30,40,38,15]
Arraychallenge(list1)




