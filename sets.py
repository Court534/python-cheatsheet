# A set is an unordered collection with no duplicate elements.

myset = set()
print(myset) # prints set()

myset.add(1)
print(myset) # prints {1}

myset.add(2) # This will add 2 to the set
print(myset) # prints {1, 2}

myset.add(2) # This will not add 2 to the set because it is already in the set

mylist = [1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist)) # This will remove the duplicates from the list and return a set