x = 5
y = "John"
print(x)
print(y)

y = 4       # x is of type int
y = "Sally" # x is now of type str
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

a = "John"
# is the same as
b = 'John'

a = 4
A = "Sally"
#A will not overwrite a

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John" # CAMEL CASE

MyVariableName = "John" # PASCAL CASE

my_variable_name = "John" # SNAKE CASE

# MULTIPLE VARIABLES
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# ONE VALUE TO MULTIPLE VARIABLES
x = y = z = "Orange"
print(x)
print(y)
print(z)

# UNPACK A LIST
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# OUTPUT VARIABLES
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

# GOLBAL VARIABLES
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

x = "Awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)