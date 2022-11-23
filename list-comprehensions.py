# Lists comprehensions are a way to create lists in a single line of code

mystring = 'hello'

mylist = []

for letter in mystring:
    mylist.append(letter)
    
print(mylist) # This will print ['h', 'e', 'l', 'l', 'o']

# Braking down the above code into one line

mylist2 = [letter for letter in mystring]

print(mylist2) # This will print ['h', 'e', 'l', 'l', 'o']

mylist3 = [x for x in 'word']
print(mylist3) # This will print ['w', 'o', 'r', 'd']

mylist4 = [num for num in range(0,11)]
print(mylist4) # This will print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist5 = [num**2 for num in range(0,11)]
print(mylist5) # This will print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist6 = [x for x in range(0,11) if x%2 == 0]
print(mylist6) # This will print [0, 2, 4, 6, 8, 10]

celcius = [0, 10, 20, 34.5]

fahrenheight = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheight) # This will print [32.0, 50.0, 68.0, 94.1]