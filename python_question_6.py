num1 = int(input("Enter a number for multiplication : "))
print(num1)
N = 1

for i in range(1, 11):
    multi = num1 * i
    print(num1, "x", N, "=", multi)
    N += 1


