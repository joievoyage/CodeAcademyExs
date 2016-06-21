inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket'] = ['seashell','strange berry', 'lint']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['backpack'].sort()
#remove the 'dagger under 'backpack'
inventory['backpack'].remove('dagger')
#add 50 to the number stored under 'gold'
inventory['gold'] = 500 + 50

