for i in range(0, 5):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i, 5):
        print("*", end=" ")
    for l in range(i):
        print(" ", end=" ")
    for s in range(i, 5):
        print("*", end=" ")
    print()

for i in range(0, 5):
    for j in range(i+1, 5):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    for l in range(i+1, 5):
        print(" ", end=" ")
    for f in range(i+1):
        print("*", end=" ")
    print()