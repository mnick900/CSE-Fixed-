c1 = 0
c2 = 0
fizz = int(input("What do you want Fizz to be?"))
buzz = int(input("What do you want Buzz to be?"))
num = int(input("How many numbers do you want the program to count?"))
for i in range(1, num):
    if i % fizz == 0 and i % buzz == 0:
        print("Fizzbuzz")
    elif i % fizz == 0:
        print("fizz")
        c2 = c2 + 1
    elif i % buzz == 0:
        print("buzz")
        c1 = c1 + 1
    else:
        print(i)
print("Fizz was said {} times, and Buzz was said {} times.".format(c2, c1))