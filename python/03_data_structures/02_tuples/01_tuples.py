'''
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, 
Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''

# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
type()

# What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)