#Python range() function is a shortcut for generationg a list, so can use ranges in all the same places we can use lists.

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0,3,1)) # Add your range between the parentheses!


#range function has three different versions:
#range(6) --> [0,1,2,3,4,5]
#range(1,6) --> [1,2,3,4,5]
#range(1,6,3) --> [1,4]
#the first one is range(stop)
#the second one is range(start, stop)
#the last one is range(start, stop, step)

## in all case, the range() function returns a list of number 