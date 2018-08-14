# Introduction to special sequences in Python

# Syntax: \<character>

# One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17
# This matches the expression of the group of that number

import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc def")
if match:
    print("Match 3")
