# Test file for an introduction to regular expressions ih Python

# Regular expressions area powerful tool for string manipulation
# Two main tasks:
# - verifying that string match a pattern (ex: email address format)
# - performing substitutions in a string (ex: changing american spellings to british

# Accessed using the re module
# re.match function determines whether it matches the beginning of a string
# If it does, match returns an object representing the match, otherwise it returns None

import re

pattern = r"spam"  # raw string

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

# re.search finds a match of a pattern anywhere in the string
# re.findall returns a list of all substrings that match a pattern

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

print(re.findall(pattern, "eggspamsausagespam"))
