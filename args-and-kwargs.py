# Args are passed as a tuple and kwargs as a dictionary

def myfunc(a, b):
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05   

print(myfunc(40, 60))

# args allows us to pass multiple arguments without having to define them ot throwing an error and stores them in a tuple
def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(40, 60, 100, 1, 34))


def myfunc(*args):
    for item in args:
        print(item)
        
myfunc(40, 60, 100, 1, 34)

# kwargs allows us to pass multiple arguments without having to define them ot throwing an error and stores them in a dictionary
def myfunc(**kwargs):
    print (kwargs) # prints a dictionary
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
        
myfunc(fruit='apple', veggie='lettuce')

# you can also pass both args and kwargs
def myfunc(*args, **kwargs):
    print(args) # This is just to show that args is a tuple
    print(kwargs) # This is just to show that kwargs is a dictionary
    print('I would like {} {}'.format(args[0], kwargs['food']))
    
myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog') # prints I would like 10 eggs