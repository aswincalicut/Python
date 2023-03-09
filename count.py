count_sweets = [15,20,18,23,21]

n = len(count_sweets)
for i in range(n):
    for j in range(0, n - i - 1):
        if count_sweets[j] > count_sweets[j + 1]:
            count_sweets[j], count_sweets[j + 1] = count_sweets[j + 1], count_sweets[j]

print(count_sweets)
