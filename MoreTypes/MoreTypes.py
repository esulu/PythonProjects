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

# Tuples are similar to lists, except there are immutable. Can also be done without brackets
words = ("hello", "world", "eren")
print(words[0])
# words[1] = "cheese" # This creates an error

# List slices allow you to return values of lists contain the values between specified indices
sample_list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sample_list[2:6])
print(sample_list[:9:2]) # Step value of 2 is added

# List comprehensions are lists that obey simple rules
cubes = [i**3 for i in range(5)]
print(cubes)

# String formatting
# Each argument of the format function is placed in the string at the corresponding position,
# which is determined using the curly brackets
nums = [4, 5, 6]
print("Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2]))

# List functions

# all or any
numbers = [55, 44, 33, 22, 11]

if all([i > 5 for i in numbers]):
    print("All numbers are larger than 5")

if any([i % 2 == 0 for i in numbers]):
    print("At least one number is even")

# enumerate iterates through the values and indices of a list
for i in enumerate(numbers):
    print(i)