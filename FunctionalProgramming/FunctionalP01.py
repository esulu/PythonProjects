# Functional programming

# Higher order functions
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

# Prints 20
print(apply_twice(add_five, 10))

# Named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

# Lambda (anonymous) function
print((lambda x: x**2 + 5*x + 4)(-4))