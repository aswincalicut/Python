#class computer():
#    def hello(self):
#        print("This is method")
#    def hello2(self):
#        print("This is method 2")
#    def hello3(self):
#        print("Good morning")

#com1 = computer()
#com2 = computer()
#windows = computer()
#mac = computer()

#com1.hello2()
#com1.hello()
#windows.hello2()
#windows.hello3()

#com1.hello3()
#com2.hello()
#com1.hello()
#mac.hello2()
#
# class computer():
#     def __init__(self,cpu,name):
#         self.cpu=cpu
#         self.name=name
#     def config(self):
#         print("config is ", self.cpu,self.name)
#     def config2(self):
#         print("config is ",self.name)
# com1 = computer("i5 ", "game")
#
#
# com1.config()
# com1.config2()


#class person():
#    def __init__(self):
#        self.name = "aswin"
#        self.age = 21

#    def update(self):
#        self.age = 50

#c1 = person()

#print("name is:", c1.name)
#print("age is:", c1.age)

#c1.update()
#print("updated age is:", c1.age)


class check():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def r(self,other):
        if self.b > other.b:
            return True
        else:
            return False

a1 = check("hello", 40)
a2 = check("hi", 100)

if a1.r(a2):
    print("self.b is greatest")
else:
    print("other.b is greatest")




