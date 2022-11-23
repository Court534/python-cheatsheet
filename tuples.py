# Tuples are immutable lists, they cannot be changed

t = (1, 2, 3) # This is a tuple
mylist = [1, 2, 3] # This is a list

print(type(t)) # prints <class 'tuple'>
print(type(mylist)) # prints <class 'list'>

t = ('one', 2)
print(t[0]) # prints 'one'
print(t[-1]) # prints 2

t = ('a', 'a', 'b')
print(t.count('a')) # counts the number of times 'a' appears in the tuple
print(t.index('a')) # prints 0, the index of the first 'a' in the tuple

mylist[0] = 'NEW'
print(mylist) # prints ['NEW', 2, 3]

t[0] = 'NEW' # This will throw an error because tuples are immutable