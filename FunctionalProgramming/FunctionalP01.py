# Functional programming

# Higher order functions
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

# Prints 20
print(apply_twice(add_five, 10))
