bovine = 6.25
poultry = 5.25
soy = 5.75
c1 = 0
c2 = 0
c3 = 0
c4 = 0
sandt = input("What kind of sandwich do you want? \n Chicken $5.25 \n Beef $6.25 \n Tofu $5.75").upper()
bev = input("Would you like a beverage? Answer with (y/n)").upper()
while sandt != "CHICKEN" and "sandt" != "BEEF" and sandt != "TOFU":
    print("That is not a valid option.")
    sandt = input("What kind of sandwich do you want? \n Chicken $5.25 \n Beef $6.25 \n Tofu $5.75").upper()
    if sandt == "CHICKEN":
        c1 = poultry
    elif sandt == "BEEF":
        c1 = bovine
    elif sandt == "TOFU":
        c1 = soy
    while bev != "Y" and bev != "N":
        bev = input("Would you like a beverage? Answer with (y/n)").upper()
    if bev == "Y":
        bevs = input("What size would you like? \n Small $1.00 \n Medium $1.75 \n Large $2.25").upper()

print("You chose {}, and the cost will be {}".format(sandt, c1))










































































































































