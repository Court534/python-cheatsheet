# String slicing is a way to get a substring from a string.

mystring = "Hello World"

print(mystring)
print(mystring[0])
print(mystring[1])
print(mystring[2])
print(mystring[3])
print(mystring[4])

abcstring = "abcdefghijklmnopqrstuvwxyz"
print(abcstring[:2]) # Prints the first two characters of the string
print(abcstring[2:]) # Prints the string after the first two characters
print(abcstring[2:5]) # Prints the string from the third character to the fifth character
print(abcstring[0] + abcstring[-1]) # print the first and last character of the string
print(abcstring[::2]) # print every second character of the string
print('tinker'[1:4]) # prints ink