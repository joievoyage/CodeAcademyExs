def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0: ## drop notes here.
       return cube(number)
       print "number is divisable by 3" ##print should after return
    else:
        return False
        print "number is  not divisable by 3" 