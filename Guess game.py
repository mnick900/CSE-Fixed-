import random
type = input("Do you want to manually change what the bounds are?\n Answer with(y/n)").upper()
while type != "Y" and type != "N":
    type = input("Do you want to manually change what the bounds are?\n Answer with(y/n)").upper()
if type == "Y":
    up = int(input("What do you want the upper bound to be?"))
    low = int(input("What do you want the lower bound to be?"))
    num = random.randint(low, up)
    print(num)
    guess = int(input("Guess a number between your ranges"))
    gum = 0
    for i in range(4):
        if guess < num:
            print("Guess higher")
            gum = gum + 1
            guess = int(input("Guess a number between your ranges"))
        elif guess > num:
            print("Guess lower")
            gum = gum + 1
            guess = int(input("Guess a number between your ranges"))
if type == "N":
    mode = input("Type EASY if you wish to play easy, or HARD if you wish to play hard")
    while mode != "HARD" and mode != "EASY":
        mode = input("Type EASY if you wish to play easy, or HARD if you wish to play hard")
    if mode == "EASY":
        num = random.randint(1, 10)
        print(num)
        guess = int(input("Guess a number from 1-10"))
        gum = 0
        for i in range (4):
            if guess < num:
                print("Guess higher")
                gum = gum + 1
                guess = int(input("Guess a number from 1-10"))
            elif guess > num:
                print("Guess lower")
                gum = gum + 1
                guess = int(input("Guess a number from 1-10"))
    if mode == "HARD":
        num = random.randint(1,100)
        print(num)
        guess = int(input("Guess a number from 1-100"))
        gum = 0
        for i in range (4):
            if guess < num:
                print("Guess higher")
                gum = gum + 1
                guess = int(input("Guess a number from 1-100"))
            elif guess > num:
                print("Guess lower")
                gum = gum + 1
                guess = int(input("Guess a number from 1-100"))
    if gum == 4:
        print("That's too many tries")
    if gum < 4:
        print("You did it, good job!")
    print("It took you ",gum + 1,"tries to answers correct.")




































