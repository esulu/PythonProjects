# Metacharacters in Python

# Metacharacters are what make regular expressions more powerful than normal string methods

# . (dot) : matches any character, other than a new line

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

# The metacharacters ^ and $ match the start and end of a string, respectively

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")
