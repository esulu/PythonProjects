# Python decorators test program
# Modify functions using other functions


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


def print_text():
    print("Hello World!")


print_text = decor(print_text)
print_text()

print("\n")

# Decorated function by replacing the variable containing the function with a wrapped version

# Alternate way of accomplishing the same result:


@decor
def print_text2():
    print("Hello World!")


print_text()
