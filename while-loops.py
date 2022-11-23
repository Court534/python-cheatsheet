# A while loops is used to iterate over a block of code as long as the test expression (condition) is true.

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print('x is not less than 5') # This will run when the while loop is finished
    
x = [1,2,3]

for item in x:
    # comment
    pass # This is a placeholder for future code. It does nothing.
print('end of my script')
    
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue # This will skip the current iteration of the loop
    print(letter)

for letter in mystring:
    if letter == 'a':
        break # This will break out of the current closest enclosing loop
    print(letter)
    
x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

