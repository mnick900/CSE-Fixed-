import random
c1 = 0
c2 = 0
c3 = 0
win = 0
lose = 0
draw = 0
play = "y"
wr_ratio = 0
while play == "y":
    u_choice = input("Choose Rock, Paper, or scissors").lower()
    while u_choice != "rock" and u_choice != "paper" and u_choice != "scissors":
        u_choice = input("Choose Rock, Paper, or scissors").lower()
    c_choice = random.randint(1,3)
    if u_choice == "rock":
        c1 = c1 + 1
    if u_choice == "paper":
        c2 = c2 + 1
    if u_choice == "scissors":
        c3 = c3 + 1
    if c_choice == 1:
        c_choice = "Rock"
        if u_choice == "rock":
            draw = draw + 1
            print("The computer chose {}".format(c_choice))
            print("The round was a draw")
        if u_choice == "paper":
            win = win + 1
            print("The computer chose {}".format(c_choice))
            print("You won!")
        if u_choice == "scissors":
            lose = lose + 1
            print("The computer chose {}".format(c_choice))
            print("You lost :(")
    if c_choice == 2:
        c_choice = "Paper"
        if u_choice == "rock":
            lose = lose + 1
            print("The computer chose {}".format(c_choice))
            print("You lost :(")
        if u_choice == "paper":
            draw = draw + 1
            print("The computer chose {}".format(c_choice))
            print("The round was a draw")
        if u_choice == "scissors":
            win = win + 1
            print("The computer chose {}".format(c_choice))
            print("You won!")
    if c_choice == 3:
        c_choice = "Scissors"
        if u_choice == "rock":
            win = win + 1
            print("The computer chose {}".format(c_choice))
            print("You won!")
        if u_choice == "paper":
            lose = lose + 1
            print("The computer chose {}".format(c_choice))
            print("You lost :(")
        if u_choice == "scissors":
            draw = draw + 1
            print("The computer chose {}".format(c_choice))
            print("The round was a draw")
    if lose == 0 and win == 0:
        wr_ratio = 0
    elif win == 0:
        wr_ratio = lose * .1
    elif lose == 0:
        wr_ratio = win * .1
    print("Your win to lose ratio in this session is {}".format(wr_ratio))
    play = input("Do you want to play again? Answer with (y/n)").lower()
    while play != "y" and play != "n":
        play = input("Do you want to play again? Answer with (y/n)").lower()








































































































