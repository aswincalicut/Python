class car:
    wheel = 8

    def __init__(self, milage, name, colour):
        self.milage = milage
        self.name = name
        self.colour = colour

    def change(self):
        self.milage = 27
        self.name = "Lambo"
        self.colour = "White"
        self.wheel = self.wheel

c1 =car(15, "BMW","Black")
c2 =car(10, "TATA", "Black")
c3 =car(40, "Audi", "blue")


c1.change()
print(c1.milage, c1.name, c1.wheel,c1.colour,)

c2.change()
print(c2.wheel, c2.name, c2.colour)

c1.change()
print(c2.name, c2.colour)
print(c3.milage,c1.milage,c3.name, c1.name,"this is class", c1.wheel)

c3.change()
print(c3.name, c3.milage, c1.colour, c1.wheel)





