import random
import time
c1 = 0
c2 = 0
c3 = 0
win = 0
lose = 0
draw = 0
play = "y"
playnum = 1
l_ratio = 0
w_ratio = 0
c_choice = ""
while play == "y":
    time.sleep(1)
    u_choice = input("Choose Rock, Paper, or scissors").lower()
    time.sleep(7/2)
    while u_choice != "rock" and u_choice != "paper" and u_choice != "scissors":
        u_choice = input("Choose Rock, Paper, or scissors").lower()
        print("The player failed to answer the question")
        time.sleep(1)
    if playnum < 5:
        c_choice = random.randint(1,3)
    elif playnum >= 5:
        if c1 > c2 and c1 > c3:
            c_choice = 2
        elif c2 > c1 and c2 > c3:
            c_choice = 3
        elif c3 > c1 and c3 > c2:
            c_choice = 1
        elif c1 == c2:
            c_choice = random.randint(2,3)
        elif c2 == c3:
            c_choice = random.randint(1,3)
            while c_choice == 2:
                c_choice = random.randint(1,3)
        elif c1 == c3:
            c_choice = random.randint(1,2)
        elif c1 == c2 == c3:
            c_choice = random.randint(1,3)
        else:
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
            print("      /        \                   ")
            print("     /          \__                ")
            print("     |             \               ")
            print("     \           _|                  ")
            print("      |         |                   ")
            print("       \_______/                           ")
            print("vs")
            print("      /        \                   ")
            print("     /          \__                ")
            print("     |             \               ")
            print("     \           _|                  ")
            print("      |         |                   ")
            print("       \_______/                           ")
            time.sleep(2)
        if u_choice == "paper":
            win = win + 1
            print("The computer chose {}".format(c_choice))
            print("You won!")
            print("      /        \                   ")
            print("     /          \__                ")
            print("     |             \               ")
            print("     \           _|                  ")
            print("      |         |                   ")
            print("       \_______/                           ")
            print("vs")
            print("    ___________                          ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |              ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |                ")
            print("   |___________|                           ")
            time.sleep(2)
        if u_choice == "scissors":
            lose = lose + 1
            print("The computer chose {}".format(c_choice))
            print("You lost :(")
            print("      /        \                   ")
            print("     /          \__                ")
            print("     |             \               ")
            print("     \           _|                  ")
            print("      |         |                   ")
            print("       \_______/                           ")
            print("vs")
            print("  /\                    ")
            print("  \/ \ ______________                  ")
            print("       |_____________\        ")
            print("       |_____________/          ")
            print("  /\  /                  ")
            print("  \/                  ")
            time.sleep(2)
    if c_choice == 2:
        c_choice = "Paper"
        if u_choice == "rock":
            lose = lose + 1
            print("The computer chose {}".format(c_choice))
            print("You lost :(")
            print("    ___________                          ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |              ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |                ")
            print("   |___________|                           ")
            print("vs")
            print("       ________                           ")
            print("      /        \                   ")
            print("     /          \__                ")
            print("     |             \               ")
            print("     \           _|                  ")
            print("      |         |                   ")
            print("       \_______/                           ")
            time.sleep(2)
        if u_choice == "paper":
            draw = draw + 1
            print("The computer chose {}".format(c_choice))
            print("The round was a draw")
            print("    ___________                          ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |              ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |                ")
            print("   |___________|                           ")
            print("vs")
            print("    ___________                          ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |              ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |                ")
            print("   |___________|                           ")
            time.sleep(2)
        if u_choice == "scissors":
            win = win + 1
            print("The computer chose {}".format(c_choice))
            print("You won!")
            print("    ___________                          ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |              ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |                ")
            print("   |___________|                           ")
            print("vs")
            print("  /\                    ")
            print("  \/ \ ______________                  ")
            print("       |_____________\        ")
            print("       |_____________/          ")
            print("  /\  /                  ")
            print("  \/                  ")
            time.sleep(2)
    if c_choice == 3:
        c_choice = "Scissors"
        if u_choice == "rock":
            win = win + 1
            print("The computer chose {}".format(c_choice))
            print("You won!")
            print("  /\                    ")
            print("  \/ \ ______________                  ")
            print("       |_____________\        ")
            print("       |_____________/          ")
            print("  /\  /                  ")
            print("  \/                  ")
            print("vs")
            print("       ________                           ")
            print("      /        \                   ")
            print("     /          \__                ")
            print("     |             \               ")
            print("     \           _|                  ")
            print("      |         |                   ")
            print("       \_______/                           ")
        time.sleep(2)
        if u_choice == "paper":
            lose = lose + 1
            print("The computer chose {}".format(c_choice))
            print("You lost :(")
            print("  /\                    ")
            print("  \/ \ ______________                  ")
            print("       |_____________\        ")
            print("       |_____________/          ")
            print("  /\  /                  ")
            print("  \/                  ")
            print("vs")
            print("    ___________                          ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |              ")
            print("   |           |                ")
            print("   |           |               ")
            print("   |           |                ")
            print("   |___________|                           ")
            time.sleep(2)
        if u_choice == "scissors":
            draw = draw + 1
            print("The computer chose {}".format(c_choice))
            print("The round was a draw")
            print("  /\                    ")
            print("  \/ \ ______________                  ")
            print("       |_____________\        ")
            print("       |_____________/          ")
            print("  /\  /                  ")
            print("  \/                  ")
            print("vs")
            print("  /\                    ")
            print("  \/ \ ______________                  ")
            print("       |_____________\        ")
            print("       |_____________/          ")
            print("  /\  /                  ")
            print("  \/                  ")
    time.sleep(2)
    w_ratio = (win / playnum) * 100
    l_ratio = (lose / playnum) * 100
    print("The player wins {:.2f}% of the time, and loses {:.2f}% of the time".format(w_ratio, l_ratio))
    time.sleep(1)
    play = input("Do you want to play again? Answer with (y/n)").lower()
    while play != "y" and play != "n":
        play = input("Do you want to play again? Answer with (y/n)").lower()
        print("The player failed to answer the question")
    if play == "y":
        playnum = playnum + 1
        print("The player decided to play again")
print("The player quits, BOOO")


print("                      ")
print("  /\                    ")
print("  \/ \ ______________                  ")
print("       |_____________\        ")
print("       |_____________/          ")
print("  /\  /                  ")
print("  \/                  ")
print("                      ")
print("    ___________                          ")
print("   |           |                ")
print("   |           |               ")
print("   |           |              ")
print("   |           |                ")
print("   |           |               ")
print("   |           |                ")
print("   |___________|                           ")
print("       ________                           ")
print("      /        \                   ")
print("     /          \__                ")
print("     |             \               ")
print("     \           _|                  ")
print("      |         |                   ")
print("       \_______/                           ")














































































