# Test file day 2
# Program by Eren Sulutas
'''
entry = input("Welcome to day 2 of Python, enter your name: ")
print("Welcome, " + entry)

entry = input("Enter your age: ")

if int(entry) > 18:
    print("You are an adult")
else:
    print("You are a child")

i = 0
while i < 5 :
    print(i)
    i += 1
    if i == 2:
        print("Skipping 2")
        continue
    elif i == 5 :
        break
'''
# List demo
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

# Can use keyword "in" to check if the list contains an item. Can also use "not"
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

print()

# Iterating through a list using a while loop
i = 0
maxIndex = len(words)
while i < maxIndex:
    print(words[i] + "!")
    i += 1

print()

# Iterating through a list using a more effecient for loop
for word in words:
    print(word + "!")

print()

# For loop for printing a message x amount of times
x = 2
for i in range(x):
    print("Hello!")

# Appending lists
nums = [1, 2, 3]
nums.append(4)
print(nums)

# Inserting elements to lists
nums2 = [1, 2, 3]
nums2.insert(1, 4)
print(nums2)

# Getting the index of lists
print(nums.index(1))

print("\nEnd of program")
