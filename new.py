x=lambda a,b: a**b
print(x(2,4))

# map function
def addition(n):
    return n + n

numbers = [1, 2, 3, 4]

result = map(addition, numbers)

print(list(result))