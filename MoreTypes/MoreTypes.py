# None object - represents the absence of a value, aka null
print(None)

# Dictionaries are use to assign keys to values
ages = {"Eren": 17}
print(ages["Eren"])
colour = {
    "Red": [255, 0, 0],
    "Green": [0, 255, 0],
    "Blue": [0, 0, 255]
}
print(colour["Red"])

# Can reassign values and assign new ones
squares = {1: 1, 2: 4, 3: "error", 4: 16}
squares[8] = 64
squares[3] = 9
print(squares)

# Can use "in" and "not in" to see if a key is in a dictionary
print(1 in squares)
print(1 not in squares)

# Can use "get" for indexing
print(squares.get(8))
print(squares.get(9))
print(squares.get(123, "Not in dictionary"))

# Tuples are similar to lists, except there are immutable. an also be done without brackets
words = ("hello", "world", "eren")
print(words[0])
# words[1] = "cheese" # This creates an error

