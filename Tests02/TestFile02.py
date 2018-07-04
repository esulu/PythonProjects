# Day 3 of python
# Program made by Eren Sulutas

import random
from math import pi # Imports only the pi function from the math module

# Initializing a function
def spam_func():
    for i in range(3):
        print(i)

# Calling the functions
spam_func()

# Prints 2 random numbers between 1 and 10
for j in range(2):
    print(random.randint(1, 10))

print(pi)
