# Collection of useful string functions in Python

# Join: joins a list of strings with another string as a separator
print(", ".join(["this", "is", "a", "sentence"]))

# Replace, replaces one substring in a string with another
print("This.is.a.sentence".replace(".", " "))

# startswith and endswith determines whether there is a substring at the start/end of a string
print("This is a sentence".startswith("This"))

# upper and to change the case of a sting
print("hello world!".upper())

# Split turns a string with a certain separator into a list
print("this,is,a,sentence".split(","))