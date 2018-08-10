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

# The pattern [aeiou] in the search function matches all strings
#  that contain any one of the characters defined.

# Character classes can also match ranges of characters
# Ex:
# [a-z] matches any lowercase alphabetic character
# [G-P] matches any uppercase character from G to P
# [0-9] matches any digit
# Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter
# of any case

pattern = r"[A-Z][A-Z][0-9]"

# The pattern above matches strings that contain two alphabetic uppercase letters
# followed by a digit

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")
    
# if a ^ is placed at the start of a character class it becomes inverted
# This causes it to match any character other than the ones included

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")

# Rest of code will be added asap
