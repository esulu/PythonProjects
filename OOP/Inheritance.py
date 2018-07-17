# Test file for inheritance in Python


class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def jump(self):
        print("Jump!")


class Cat(Animal):
    def meow(self):
        print("Meow!")
        super().jump()


class Dog(Animal):
    def bark(self):
        print("Bark!")


fido = Dog("Fido", "White")
jim = Cat("Jim", "Black")
print(fido.colour)
fido.bark()
jim.meow()


