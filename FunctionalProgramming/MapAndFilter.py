# Map and filter demo
def add_five(x):
    return x + 5

# Map functions takes a function and an iterable as arguments, and returns a new iterable
# with the function applied to each argument
nums = [11, 22, 33, 44, 55]
print(list(map(add_five, nums)))

# "filter" filters and iterable by removing items that don't match a predicate (function that returns boolean)
nums2 = [11, 22, 33, 44, 55]
result = list(filter(lambda x: x % 2 == 0, nums2))
print(result)
