order_amount = int(input("How many items are you getting"))
item_price = int(input("How much is the item you are getting?"))
state = str(input("What state do you live in?"))
tax = 1
if state == "Ca" or 'CA' or 'ca' or 'cA' or "California":
    tax = 1.0875
    cost = (order_amount * item_price) * tax
    print("The total cost is ${:.2f}".format(cost))


































































