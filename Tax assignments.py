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
"""
print("The password for the user person1 is 090909")
user = input()
pas = "090909"
entered = input("What is the password for {}".format(user))
if entered == pas:
    print("Welcome")
else:
    print("Sorry, that is the wrong password")


































































