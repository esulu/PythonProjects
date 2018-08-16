# Same usage of regular expressions in Python

import re

str = "Please contact info@apple.com for assistance"

# Basic email address:
# word,, may include a dot or dash, followed by @ and domain name

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"


match = re.search(pattern, str)

if match:
    print("Email: {}".format(match.group()))
