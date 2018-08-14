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

# Note: <(.+) /1> != <(.+)(.+)> because /1 refers to the first group's subexpression, which is the matched expression
# itself, and not the regex pattern

# More useful special sequences are \d, \s, and \w
# These match digits, whitespace, and word characters respectively

# ASCII equivalent: [0-9], [\t\n\r\f\v], and [a-zA-Z0-9_]
# The upper case version of the special sequences mean the opposite of the lower case versions
# Ex: /D matches anything that isn't a digit
