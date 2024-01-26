""" A 50% discount applies to all pizza prices on Tuesdays. This discount does not apply to any delivery cost
(see below).

Delivery costs £2.50, unless there are five or more pizzas in the order, in which case it is free.

A discount of 25% of the total price (pizzas plus delivery, if required) is applied if the customer orders via the new
BPP App.

This is in addition to the Tuesday Discount, and is applied after that discount."""
PIZZA_COST = 12  # declaring constant values
DELIVERY_PRICE = 2.50
print("WELCOME TO BPP")
def pizza_deliv(quantity_pizza, day, delivery, app):
    
    total_cost_of_pizza = quantity_pizza * PIZZA_COST

    if delivery == "y" and quantity_pizza < 5:
        delivery_cost = DELIVERY_PRICE
    else:
        delivery_cost = 0

    total_cost = total_cost_of_pizza + delivery_cost

    # 50% discount on Tuesday
    if day == "y":
        total_cost = total_cost * 0.5

    # 25% discount if app is used
    if app == "y":
        total_cost = total_cost * 0.75

    print ('The total cost of the pizzas is £.',total_cost,)

quantity_pizza = int(input("How many pizzas would you like:"))
while quantity_pizza < 0:
    quantity_pizza = int(input("How many pizzas would you like:"))

day = input("Is the pizza ordered on a Tuesday (y/n):").lower()
while day != "y" and day != "n":
    day = input("Is the pizza ordered on a Tuesday (y/n):").lower()

delivery = input("Do you need delivery (y/n):").lower()
while delivery != "y" and delivery != "n":
    delivery = input("Do you need delivery (y/n):").lower()

app = input("Is the app used (y/n):").lower()
while app != "y" and app != "n":
    app = input("Is the app used (y/n):").lower()

pizza_deliv(quantity_pizza, day, delivery, app)