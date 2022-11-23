# A functions is a block of code that is called by name. It can be passed data to operate on (i.e. the parameters) 
# and can optionally return data (the return value). All data that is passed to a function is explicitly passed.

# def is a keyword that marks the start of a function header. The header always consists of the function name 
# e.g.

def my_function():
    '''
    Docstring: Documentation about the function.
    '''
    print("Hello from a function")


# Calling a function
my_function() # This prints "Hello from a function"


# Functions that take arguments
def my_function_with_args(name):
    print("Hello " + name)
    
my_function_with_args("John Smith") # This prints "Hello John Smith"


# Using return instead of print
def add_function(num1, num2):
    return num1 + num2 # Return allows us to assign the result of the function to a variable

result = add_function(1, 2)
print(result) # This prints 3

result2 = add_function(5, 10)
print(result2) # This prints 15


def say_hello(name):
    return f"Hello {name}"
print(say_hello("John")) # This prints "Hello John"
# print(say_hello()) You will get a TypeError: say_hello() missing 1 required positional argument: 'name'


# You can provide a default value to an argument by using the assignment operator (=).
def say_hello(name="Default"):
    return f"Hello {name}"
print(say_hello("John")) # This prints "Hello John"
print(say_hello()) # This prints "Hello Default"


# Functions with logic and conditionals
def even_check(number):
    return number % 2 == 0

print(even_check(20)) # This prints True
print(even_check(21)) # This prints False

# Create a function that returns true if any number is even inside a list
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False
        
print(check_even_list([1, 3, 5])) # This returns False
print(check_even_list([2, 4, 5])) # This returns True

# Create a function that returns all the even numbers in a list 
def check_even_num_list(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

print(check_even_num_list([1, 2, 3, 4, 5, 6])) # This returns [2, 4, 6]
print(check_even_num_list([1, 3, 6, 7, 10, 16 ])) # This returns [6, 10, 16]

