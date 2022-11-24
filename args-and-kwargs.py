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
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
        
myfunc(fruit='apple', veggie='lettuce')