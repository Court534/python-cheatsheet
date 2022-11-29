# map is a built in function in python that takes a function and a list as arguments
def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]

map(square, my_nums) # returns a map object

for item in map(square, my_nums):
    print(item) # prints 1, 4, 9, 16, 25
 
# you can use list to convert the map object to a list   
list(map(square, my_nums)) # prints [1, 4, 9, 16, 25]


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
 
# you can use map with multiple lists   
names = ['Andy', 'Eve', 'Sally']
list(map(splicer, names)) # prints ['EVEN', 'E', 'S']


def check_even(num):
    return num % 2 == 0

mynums = [1, 2, 3, 4, 5, 6]

filter(check_even, mynums) # returns a filter object

for n in filter(check_even, mynums):
    print(n) # prints 2, 4, 6



    
