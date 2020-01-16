"""
order_amount = int(input("How many items are you getting"))
item_price = int(input("How much is the item you are getting?"))
state = str(input("What state do you live in?"))
tax = 1
cost = (order_amount * item_price)
if state == "Ca" or state == 'CA' or state == 'ca' or state == 'cA' or state == "California":
    tax = 1.08
    cost *= tax
    print("The total cost is ${:.2f}".format(cost))

print("The password for the user person1 is 090909")
user = input()
pas = "090909"
entered = input("What is the password for {}".format(user))
if entered == pas:
    print("Welcome")
else:
    print("Sorry, that is the wrong password")

x = 0
age = int(input("What is your age?"))
if age >= 16:
    x = "You are able to drive"
elif 16 > age > 0:
    x = "You are not able to drive"
else:
    x = "Enter a valid age"
print(x)

scale = input("Press C for Celsius or F for Fahrenheit")
temp = int(input("What is the temperature?"))
if scale == "f" or scale == "F":
    temp = (temp-32)*5/9
elif scale == "c" or scale == "C":
    temp = (temp * 9 / 5) + 32
print(temp)
"""
height = int(input("How many inches tall are you?"))
weight = int(input("What is your weight in pounds?"))
bmi = int((weight / (height * height)) * 703)
if 18.5 <= bmi <= 25:
    print("You are at an ideal BMI")
elif 0 < bmi < 18.5:
    print("You are at an underweight BMI")
elif 25 < bmi:
    print("You are at an overweight BMI")






















































