a = ["red", "blue", "black", "white", "yellow", "orange"]
b = ["red", "blue", "black", "white", "yellow"]
c = []
for i in a:
    print(i)
    if i not in b:
        c.append(i)

print("color from a is not in b", c)
