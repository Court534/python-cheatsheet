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