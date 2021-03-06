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

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 2187!")
if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, "! $?")
if match:
    print("Match 3")

# (\D+\d) matches one or more non-digits followed by a digit

# Additional special sequences are \A, \Z, and \b
# \A and \Z match the beginning and the end of a string respectively
# \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string
# \B matches the empty string anywhere else

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print("Match 2")

match = re.search(pattern, "We scattered?")
if match:
    print("Match 3")

# <\b(cat)\b> matches the word "cat" surrounded by word boundaries
