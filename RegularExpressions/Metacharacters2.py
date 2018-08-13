# More metacharacters in Python

# Some more metacharacters:
# * : zero or more repetitions of the previous thing
# The "previous thing" can be a single character, a class, or a group of characters in ()

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggsspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

# + : one or more repetitions

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "ggg"):
    print("Match 2")

if re.match(pattern, "abc"):
    print("Match 3")

# ? : zero or one repetition

pattern = r"ice(-)?cream"

if re.match(pattern, "icecream"):
    print("Match 1")

if re.match(pattern, "ice-cream"):
    print("Match 2")

if re.match(pattern, "sausages"):
    print("Match 3")

if re.match(pattern, "ice--ice"):
    print("Match 4")

# {} : used to represent the number of repetitions between two numbers
# {x, y} means between x and y repetitions
# Hence {0, 1} is the same as ?

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")
