# for loops are used to iterate over a sequence (list, tuple, string) or other iterable objects

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print(num) # prints 1 2 3 4 5 6 7 8 9 10
    
for num in mylist:
    if num % 2 == 0:
        print(num) # prints 2 4 6 8 10
    else:
        print(f'Odd Number: {num}') # prints Odd Number: 1 Odd Number: 3 Odd Number: 5 Odd Number: 7 Odd Number: 9
        
list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    
print(list_sum) # prints 55 the total sum of the list

for letter in 'Hello World':
    print(letter) # prints H e l l o   W o r l d
    print(letter * 3) # prints HHH eee lll lll ooo   WWWW ooo rrr lll ddd
    
tup = (1, 2, 3)

for item in tup:
    print(item) # prints 1 2 3
    
# Tuple unpacking is a way to iterate through a list of tuples

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]

len(mylist) # prints 4

for item in mylist:
    print(item) # prints (1, 2) (3, 4) (5, 6) (7, 8)
    
for a, b in mylist:
    print(a) # prints 1 3 5 7
    print(b) # prints 2 4 6 8
    
mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for item in mylist:
    print (item) # prints (1, 2, 3) (4, 5, 6) (7, 8, 9)
    
for a,b,c in mylist:
    print(a) # prints 1 4 7
    print(b) # prints 2 5 8
    print(c) # prints 3 6 9
  
# Dictionary unpacking is a way to iterate through a dictionary
  
d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item) # prints k1 k2 k3
    
for item in d.items():
    print(item) # prints ('k1', 1) ('k2', 2) ('k3', 3)
    
for key, value in d.items():
    print(value) # prints 1 2 3
    

    