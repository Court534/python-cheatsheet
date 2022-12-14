# The range function is used to generate a sequence of numbers

mylist = [1,2,3]

for num in range(10):
    print(num) # This will print 0 to 9

for num in range(3,10):
    print(num) # This will print 3 to 9

for num in range(3,10,2): # This will print 3 to 9 with a step size of 2
    print(num) # This will print 3, 5, 7, 9
    
print(list(range(0,11,2))) # This will print [0, 2, 4, 6, 8, 10]

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1 # This prints the index and the letter at that index

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1 # This prints the letter at the index
    

# The enumerate function is used to keep track of the index and the letter at that index

word = 'abcde'

for item in enumerate(word):
    print(item) # This prints the index and the letter at that index

word = 'abcde'

for index, letter in enumerate(word):
    print (index) # This prints the index
    print (letter) # This prints the letter at that index
    print('\n') # This prints a new line
    
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]


# The zip function will zip together the two lists

print(zip(mylist1, mylist2)) # This will print a zip object

for item in zip(mylist1, mylist2, mylist3):
    print(item) # This will print the zipped lists
   
print(list(zip(mylist1, mylist2, mylist3))) # This will print a list of the zipped lists


# How to quickly check if an item is in a list

print('x' in [1,2,3]) # This will return False
print('x' in ['x', 'y', 'z']) # This will return True
print('a' in 'a world') # This will return True
print('mykey' in {'mykey':345}) # This will return True

dict = {'mykey':345}
print(345 in dict.values()) # This will return True
print(345 in dict.keys()) # This will return False


mylist = [10, 20, 30, 40, 100]

# The min function will return the minimum value in a list
print(min(mylist)) # This will print 10

# The max function will return the maximum value in a list
print(max(mylist)) # This will print 100


# The random library is used to generate random numbers
from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(mylist) # This will shuffle the list

print(mylist) # This will print the shuffled list

from random import randint
print(randint(0,100)) # This will return a random integer between 0 and 100

# The input function is used to get user input
result = input('Enter a number here: ') # This will prompt the user to enter a number 

result = input('What is your name? ') # This will prompt the user to enter their name
print('Hello {}'.format(result)) # This will print Hello and the user's name