fris = 0
bevs = 0
mega = "n"
c1 = 0
c2 = 0
c3 = 0
c4 = 0
bev = "n"
fri = "n"
sandt = input("What kind of sandwich do you want? \n Chicken $5.25 \n Beef $6.25 \n Tofu $5.75").upper()
while sandt != "CHICKEN" and sandt != "BEEF" and sandt != "TOFU":
    print("That is not a valid option.")
    sandt = input("What kind of sandwich do you want? \n Chicken $5.25 \n Beef $6.25 \n Tofu $5.75").upper()
    if sandt == "CHICKEN":
        c1 = 5.25
    elif sandt == "BEEF":
        c1 = 6.25
    elif sandt == "TOFU":
        c1 = 5.75
bev = input("Would you like a beverage? Answer with (y/n)").upper()
while bev != "Y" and bev != "N":
    bev = input("Would you like a beverage? Answer with (y/n)").upper()
if bev == "Y":
    bevs = input("What size would you like of drink? \n Small $1.00 \n Medium $1.75 \n Large $2.25").upper()
    while bevs != "SMALL" and bevs != "MEDIUM" and bevs != "LARGE":
        bevs = input("What size would you like of drink? \n Small $1.00 \n Medium $1.75 \n Large $2.25").upper()
    if bevs == "SMALL":
        c2 = 1.00
    elif bevs == "MEDIUM":
        c2 = 1.75
    elif bevs == "LARGE":
        c2 = 2.25
fri = input("Would you like fries? Answer with (y/n)").lower()
while fri != "y" and fri != "n":
    fri = input("Would you like fries? Answer with (y/n)").lower()
if fri == "y":
    fris = input("What size would you like of fries? \n Small $1.00 \n Medium $1.50 \n Large $2.00").lower()
    while fris != "small" and fris != "medium" and fris != "large":
        fris = input("What size would you like of fries? \n Small $1.00 \n Medium $1.50 \n Large $2.00").lower()
    if fris == "small":
        c3 = 1.00
        mega = input("Would you like to mega-size your fries? Answer with (y/n)").lower()
        while mega != "y" and mega != "n":
            mega = input("Would you like to mega-size your fries? Answer with (y/n)").lower()
        if mega == "y":
            c3 = 2.00
        fris = "MEGA"
    elif fris == "medium":
        c3 = 1.50
    elif fris == "large":
        c3 = 2.00

print("You chose {} for your sandwich".format(sandt))
if bev == "Y":
    print("You chose the {} size for your drink.".format(bevs))
if fri == "y":
    print("You chose the {} size for your fries.".format(fris))
cost = c1 + c2 + c3 + c4
print("The cost is ${:.2f}".format(cost))








































































































































