# Python sets test program
# Sets are data structures that are similar to lists or dictionaries
# Cannot be indexed, cannot contain duplicate elements, use add instead of append, use remove to remove
# a specific element


num_set = {1, 2, 3, 4, 5}
word_set = set(["hello", "world", "!"])

print(3 in num_set)
print("hello" not in word_set)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

# Operations:
# | union: Combines two sets to form a new one
# & intersection: gets the items only in both sets
# - difference: gets the items in the first set but not in the second
# ^ symmetric difference: gets the items in either set, but not both

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(second - first)
print(first ^ second)

'''
When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a 
  simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.
'''