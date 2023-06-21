"""Menu (list) of 4 items"""
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

"""Stock dictionary"""
stock = {
    "Coffee": 10,
    "Tea": 15,
    "Sandwich": 5,
    "Cake": 8
}

"""Price dictionary"""
price = {
    "Coffee": 2.5,
    "Tea": 1.75,
    "Sandwich": 4.25,
    "Cake": 3.0
}

"""Variable total stock worth"""
total_stock_worth = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

print("Total stock worth:", total_stock_worth)