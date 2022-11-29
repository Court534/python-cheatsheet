# Lambda functions are small anonymous functions.

# Example function
def square(num):
    result = num**2
    return result

print(square(3)) # prints 9

# Example function simplified
def square(num):
    return num**2

print(square(3)) # prints 9

# Lambda function example
square = lambda num: num**2

print(square(3)) # prints 9


