def num1(a,b,c):
    print("sum:",a+b+c)

num1(2,4,4,)


def test(*num):
    sum = 0

    for n in num:
        sum = sum+n

    print("sum:", sum)

test(2,4,2,2,10,50,100,30,800)

def intro(**data):
    print("\ndata type of argument:", type(data))
    
    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname="sita", lastname="sharma", Age=22, number=1234567)