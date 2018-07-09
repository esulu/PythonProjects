# Python generators
# Type of iterable like lists or tuples
# Don't allow indexing with arbitrary indices, but can be iterated with a for loop
# Can be used with the yield statement


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)


print("\n")

# The yield statement is used to define a generator

# EXAMPLE: Generator that generates even numbers


def even_generator(j):
    for i in range(j):
        if i % 2 == 0:
            yield i


print(list(even_generator(11)))