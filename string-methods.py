# A string is a sequence of characters. Strings are immutable, meaning they cannot be changed once created.

name = 'Sam'
last_letters = name[1:] # Assigns the string 'am' to the variable last_letters
print(last_letters) # Prints 'am'
new_name = 'P' + last_letters # Assigns the string 'Pam' to the variable new_name
print(new_name) # Prints 'Pam'

x = 'Hello World'
print(x + ' it is beautiful outside') # Concatenates the string 'Hello World' with the string ' it is beautiful outside'

letter = 'z'
print(letter * 10) # Prints 'zzzzzzzzzz'

print(2 + 3) # Prints 5
print('2' + '3') # Prints 23

x = 'Hello World'
print(x.upper()) # Prints 'HELLO WORLD'
print(x.lower()) # Prints 'hello world'
print(x.split()) # Prints ['Hello', 'World']

# .split() splits the string into a list of strings
x = 'Hi this is a string'
print(x.split(' ')) # Prints ['Hi', 'this', 'is', 'a', 'string']