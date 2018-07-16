# Classes for Python test program


class Cat:
    def __init__(self, colour, friends):
        self.colour = colour
        self.friends = friends

    def meow(self):
        print("Meow!")


felix = Cat("Ginger", 4)
rover = Cat("Golden", 6)
charles = Cat("Brown", 3)

print(felix.colour)
rover.meow()