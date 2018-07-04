# This program is to demo the use of the file reader/writer

try:
    file = open("file.txt")
    print(file.read())
finally:
    # Ensures that the file is always closed, even if an error occurs
    file.close()


# with statement creates a temporary variable
with open("file.txt") as f:
    print(f.read())