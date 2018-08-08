# Character classes in Python

# Character classes provide a way to match only one of a specific set of characters

# A character class is created by putting the characters it matches in square brackets

import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")
