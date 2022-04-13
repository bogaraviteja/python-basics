'''
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
'''

# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
type()

# What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
