# Test file for file operations

# Write mode
file = open("file.txt", "w")

file.write("A new line has been added!")
file.close()

# Read mode (Can also add 'r')
file = open("file.txt")

cont = file.read() # Reads the file (Can also specify the number of bytes to read in the brackets
print(cont)

# Iterating through each line (can also use .readline() method)
for line in file:
    print(line)

# Note: adding "b" to the end of a mode opens the file in binary - used for sounds/images

#  the file
file.close()