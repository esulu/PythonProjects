# Test file for class methods in Python


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    # Class methods are called by a class, which is passed into the cls parameter
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())

# Static methods are similar to class methods. except they don't receive any additional arguments


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    # Static methods behave like functions, except that you can call them from an instance of the class
    @staticmethod
    def valid_topping(topping):
        if topping == "pineapple":
            raise ValueError("Pineapples are not allowed on pizza")
        else:
            return True


ingredients = ["cheese", "onions", "peperoni"]
if all(Pizza.valid_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
