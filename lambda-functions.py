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

# Lambda function example with map() and list()
mynums = [1, 2, 3, 4, 5]

print(list(map(lambda num: num**2, mynums))) # prints [1, 4, 9, 16, 25]

# Lambda function example with filter() and list()
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda num: num%2 == 0, mylist))) # prints [2, 4, 6, 8, 10]

