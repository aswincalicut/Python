word = " the quick brown fox jumps over the lazy dog"
dict1 = {}

a = word.split()
print(a)

for i in a:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)










