
def function_sample(s1,s2,n):
    a = s1.lower()
    b = s2.lower()
    c = (a + b)*100

    dictionary = c[:10]

    print(dictionary)

    dict1 = {}

    for i in dictionary:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    print(dict1)

function_sample("Abc", "cDe",10)












