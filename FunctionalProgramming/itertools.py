# itertools demo program
# Standard library

from itertools import count, accumulate, takewhile, product, permutations

'''
Functions:
count: counts up infinitely from a value
cycle: infinitely iterates through an iterable (ex a string)
repeat: repeats an object, either infinitely or a specific number of times

takewhile: takes items from an iterable while a predicate function (boolean) remains true
chain: combines several iterables into one long one
accumulate: returns a running total of values in an iterable (sum of all previous values)

product: all possible combinations between multiple sets of data
permutations: all possible combination of a single set of data
'''

for i in count(3):
    print(i)
    if i == 11:
        break


nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

letters = ("A", "B")
numbers = (0, 1)

print(list(product(letters, numbers)))
print(list(permutations(letters)))


