# Program that analyzes the frequency of substrings in a file

def char_count(text, char):
    count = 0

    # Iterates through every character
    for c in text:
        if c.lower() == char.lower():
            count += 1
    return count

def percentage(text, char):
    return 100 * char_count(text.lower(), char.lower()) / len(text.lower())

filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()

# Prints the percentage of the character frequency
for char in "abcdefghijklmnopqrstuvwxyz":
    print("{0}: - {1}x - {2}%".format(char.upper(), char_count(text, char), round(percentage(text, char),2)))

