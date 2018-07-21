# Test program for object properties in Python

# Properties provide a way of customizing access to instance attributes
# They are created by butting the property decorator above a method, which means when the instance
# attribute with the same name as the method is accessed, the method will be called instead

# A common use of a property is to make an attribute read-only

'''
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
'''

# Properties can also be set by defining setter/getter functions


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "passw0rd":
                self.pineapple_allowed = True
            else:
                raise ValueError("Invalid Password")


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print("here")
print(pizza.pineapple_allowed)
