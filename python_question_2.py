dict1 = {"place": "calicut", "game": "pes", }
dict2 = {"player": "messi", "sport": "football"}
print(dict1)
print(dict2)

for i in dict2:
    dict1.update(dict2)
print(dict1)


