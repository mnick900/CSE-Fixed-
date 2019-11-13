print("Basic Print Testing")
# This is a comment
print("Hello World")
print("NSM")
print("this is a string")
print("123abc")  # yet another comment
print('12')  # apostrophe works too!
print("123a")
print("")
print("Numbers")
# printing numbers
print(7)  # this is an integer
print(3.14159265359)  # I'm a float
print(-3.14159265359)
print("")
print("Booleans")
# printing booleans
print(True)
print(False)

"""
this is a 
multi-line
comment
"""
# error catching
print("")
print("Variables")

# variables
spam = 40
print(spam+20)
greg = 'hello'
print(greg)
name = "John Dee"
print(name)
print("Welcome", name)

# Variable Changing
price = 7
print(price)
price += 3
print(price)
print()
cost = 50
print(cost)
cost -= 10
print(cost)

# Basic Math
print("")
print("Math")
print(6+3)
print(5-3)
print(3*4)
print(10/6)
print("")
print(1**3)
print(3**1)
print(4//3)
print(11//5)
print(412//50)
print(11 % 5)
print(79 % 10)

# Writing some code
small = 12
medium = 15
large = 20
print(small)
print()

# Semi-advanced Math
print("code tracing")
small = large - medium
large = large % small
medium = large - small
print(small)
print(medium)
print(large)
print()
print("Comparison")
# Comparison
print(8 < 4)
print(8 > 4)
print(6 <= 4)
print(6 >= 4)
print(5 == 5)
print(7 == 5)
print(5 != 5)
print(7 != 5)

name = input("Name:")
print("Welcome to our humble abode {name}")