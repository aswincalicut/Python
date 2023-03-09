# increment triangle

# for i in range(0, 5):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()


# decrement triangle

#for i in range(0, 5):
#    for j in range(i):
#        print(" ", end=" ")
#    for k in range(i, 5):
#        print("*", end=" ")
#    print()

# full pyramid

for i in range(0, 5):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    for n in range(i+1):
        print("*", end=" ")
    print()
# full pyramid inverted
print()
for i in range(0, 5):
    for j in range(i):
        print(" ", end=" ")
    for n in range(i, 5):
        print("*", end=" ")
    for k in range(i, 5):
        print("*", end=" ")
    print()


