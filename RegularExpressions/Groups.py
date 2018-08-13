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

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")

if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

# The example above also shows that groups can be nested

# There are several kinds of special groups

# named groups : syntax (?P<name>...) | name = name of the group | ... = content
# Behave the same as normal groups, except they can be accessed by <group(name)> in addition to its number

# non-capturing groups : syntax (?:...)
# Not accessible by the <group> method, so they can be added to an existing regular expression  without
# breaking the numbering

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")

if match:
    print(match.group("first"))
    print(match.groups())
