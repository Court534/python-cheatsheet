# A nested statement is a statement inside another statement. For example, a for loop inside a for loop is a nested statement.
# Scope is the context in which a variable is visible. A variable is only visible in the scope in which it is defined.

x = 25

def printer():
    x = 50
    return x

print(x) # prints 25 because x is defined in the global scope

print(printer()) # prints 50 because x is defined in the local scope of the printer() function

# LEGB Rule is used to determine the order in which Python looks for a variable

# L: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function.
# E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# G: Global (module) - Names assigned at the top-level of a module file, or declared global in a def within the file.
# B: Built-in (Python) - Names preassigned in the built-in names module : open, range, SyntaxError,...

# Local Example
lambda num: num**2 # num is local to the lambda expression

# Enclosing function locals Example

# Global Example
name = 'This is a global name'

def greet():
    
    # Enclosing example
    name = 'Sammy'

    def hello():
        # Local example
        name = 'I am a local'
        print('Hello ' + name)

    hello()
    
greet() # prints Hello Sammy

y = 50

def func(y):
    print(f'Y is {y}')

    # Local reassignment
    y = 200
    print(f'I just locally changed Y to {y}')
    
print(func(y)) # prints Y is 50 and I just locally changed Y to 200
print(y) # prints 50 because y is defined in the global scope

def func():
    global y # global keyword allows us to change the global variable
    print(f'Y is {y}')

    # Local reassignment on a global variable
    y = 'New Value'
    print(f'I just locally changed global Y to {y}')
    
print(y) # prints 50 because y is defined in the global scope
print(func()) # prints Y is 50 and I just locally changed global Y to New Value
print(y) # prints New Value because y is defined in the global scope
