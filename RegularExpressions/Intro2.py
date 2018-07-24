# Intro to regular expressions 2

import re

pattern = r"pam"

'''
Methods list:
- group: returns the string matched
- start / end: return the start and end positions of the first match
- span: returns the start and end positions as a tuple'''

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

# The sub method replaces all occurrences of the pattern in a string with repl, substituting
# all occurrences, unless max provided

# Syntax: re.sub(pattern, repl, string, max = 0)

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)
