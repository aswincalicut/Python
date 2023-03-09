def limit(n):
    print()

    for i in range(0, n):
        for j in range(i+1):
            print("*", end=" ")
        print()
    for k in range(0, n):
        for b in range(k, n):
            print("*", end=" ")
        print()

limit(10)


def sum1(a, b):
    print(a + b)

sum1(5,10)

