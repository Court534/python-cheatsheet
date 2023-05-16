#Counter is a subclass of dict that's specially designed for counting hashable objects in Python
# import counter module
from collections import Counter 

# Here we have a list and we need to find out how many of each item there is in the list
mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]

# We can use counter for this
print(Counter(mylist))
# Output: Counter({1: 6, 2: 5, 3: 5, 4: 5})