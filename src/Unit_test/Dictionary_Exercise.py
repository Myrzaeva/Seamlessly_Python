# Task 1:
from random import choice
food = choice(["cheese pizza", "apple", "apricot","coffee"])
bakery_stock = {
    "almond" : 12,
    "toffee-fee": 5,
    "apple": 1,
    "coffee":100
}
if food in bakery_stock:
        print(f"{bakery_stock[food]} left")
else :
    print("We don't have that")


if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("Dont make that")


quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")

