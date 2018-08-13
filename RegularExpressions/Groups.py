# Introduction to groups in Python

# Created by surrounding part of a regular expression with ()'s

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

# (spam) represents a  group in the example pattern shown above

# Example: '([^aeiou][aeiou][^aeiou])+' would match one or more repetitions of a non-vowel, a vowel and a non-vowel

# The content of groups in a match can be accessed using the <group> function
# group(0) / group() returns the whole match
# group(n) where n is larger than 0, returns the nth group from the left
# groups() returns all groups up from 1
