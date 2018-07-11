# Day 4 of Python
# Exceptions and Files by Eren Sulutas

# Using a try/except block to handle errors
try:
    num1 = 7
    num2 = 0
    print("Calculating...")
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred due to zero division")

# Note: using except with no values will catch any error
try:
    var = 10
    print(var + "Hello")
except(TypeError, ValueError):
    print("An Error Occurred")
finally: # Finally statement insures a part of the code will run no matter what
    print("This code will still run")

# Raising exceptions
'''
print(1)
raise ValueError("Error: Invalid value")
print(2)
'''

# Assertions are used to check the validity of an expression
# An Assertion Error occurs when the expression is false
try:
    print(1)
    assert 2 + 2 == 4
    print(2)
    assert (1 + 1 == 3), "The statement is false"
    print(3)
except AssertionError:
    print("Error: A statement is invalid")
