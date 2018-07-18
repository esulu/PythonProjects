# Test program for magic methods and overloading in Python

# Magic methods are made with the double underscores
# A common use of them is operator overloading

import random


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


'''
Examples:
__add__ for +
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
'''

# The expression x + y is translated into x.__add__(y).
# However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.


vect1 = Vector2D(5, 7)
vect2 = Vector2D(3, 9)
result_vect = vect1 + vect2
print(result_vect.x)
print(result_vect.y)

'''
Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
'''


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs


'''
There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
'''


class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])