"""
# 1
user = input("Enter a username")
e = 0
while len(user) == 0:
    print("Please input a username")
    user = input("Enter a username")
    e = e + 1
if e > 5:
    print("See, it wasn't that hard to input a username")

# 2
passs = input("Input a password that is more than 9 and less than 15 characters")
while len(passs) < 9 or len(passs) > 15:
    print("Please input a password")
    passs = input("Input a password that is more than 9 and less than 15 characters")
# 3
user1 = input("What is your username")
pass1 = input("What is your password")
while user1 != user:
        print("Wrong")
        user1 = input("What is your username")
while pass1 != passs:
        print("Wrong")
        pass1 = input("What is your password")
print("That's it")
"""
# 4
color = input("color guess time").upper()
s = 0
while color != "GREEN":
    color = input("Color guess time").upper()
    if color == "BLUE":
        print("Add yellow")
        s = s + 1
    elif color == "YELLOW":
        print("Add Blue")
        s = s + 1
    elif color == "RED":
        print("Add other primaries")
        s = s + 1
    else:
        print("Nope")
print("güt")
print("You used {} tries".format(s))

"""
num = int(input("Enter a number from 1 - 10"))
while num < 1 or num > 10:
    print("It isn't hard")
    num = int(input("Enter a number from 1 - 10"))
print("Correct")
"""



















































































