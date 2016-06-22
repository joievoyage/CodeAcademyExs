shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    # This is a for loop here!!
    for item in food:
        # A while loop inside a for loop :P
        #But I believe won't do it in normally.
        if stock[item] > 0:
            # Add the prices for the total
            total += prices[item]
            #Here we minus the stock
            stock[item] -= 1
    return total
    print total

