list1 = []

a = int(input("Enter the total num of elements you want : "))

for i in range(a):
    result = input("Enter the words : ")
    list1.append(result)
print(list1)

#max_word = max(list1, key=len)
#print("The largest word in list1 is :", max_word, len(max_word))
#print("len of largest word is :", len(max_string))

max_length = 0

for i in list1:
    length = len(i)
    if length > max_length:
        max_length = length
print(max_length)
