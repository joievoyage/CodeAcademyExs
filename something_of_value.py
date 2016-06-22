prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total = 0

for key in prices:
# Always remember left side of value not = right side like maths!
# So CAN NOT write something like total + prices[key] * stock[key] = total!! That will error!!!
    total = prices[key] * stock[key] + total
    print total

