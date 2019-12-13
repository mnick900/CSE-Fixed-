"""
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

this is a 
multi-line
comment

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

# Typecasting

value = int(input("enter a number"))
cost = 12
print(value + cost)

print("7" + "5")
print(int("7") + int("5"))

print(str("7") + str("5"))

# Rounding with .format
# Method 1: Storing value in a variable
value = 12.3456789
print("Value = {}".format(value))
print("Value to two decimal places {:.2f}".format(value))
print("Value to three decimal places {:.3f}".format(value))
print("Value to ten decimal places {:.10f}".format(value))
print("Value to ten decimal places {:.0f}".format(value))

# Method 2: Calculating while rounding
print("The answer is {:.4f}".format(3.141592/6))
cost = 100
tax_rate = .0725
print("You actually owe ${:.2f} for your purchase".format(cost*tax_rate))


# Escape characters

sent1 = "This actually does exist"
print(sent1)
# New Line
sent1 = "This \nactually \ndoes exist"
print(sent1)
# Intent (tab)
sent1 = "This \tactually \tdoes exist"
print(sent1)

sent2 = "She said \"yes\" to her mom "
print(sent2)

sent3 = 'Jack\'s dog'
print(sent3)

sent4 = "Jill's dog"
print(sent4)

sent5 = 'my "dog"'
print(sent4)

print("This \t is \t my \t string.")

print("This \n is \n SPARTA.")

print("Sally said \"no\" about the jacket.")
print("Sally said \"no\" about the jacket.")

print('This is Sally\'s jacket.')
print('This is Sally\'s jacket.')

print("I used years \\ months")
print(1/2)


perimeter = 30
print("We need", perimeter, "feet of fencing for the yard,")
"""
t = 5
r = 5

t = float(input("input a number"))
print(t)