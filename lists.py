# A list is a collection which is ordered and changeable. Allows duplicate members.

my_list = [1,2,3]
my_list_2 = ['STRING', 100, 23.2]
print(len(my_list)) # Prints the length of the list

my_list_3 = ['one', 'two', 'three']
print(my_list_3[0]) # Prints the first item in the list 
print(my_list_3[1:]) # Prints the list from the second item to the end of the list
print(my_list_3 + my_list_2) # Concatenates the two lists

new_list = my_list_3 + my_list_2 # Assigns the concatenated list to the variable new_list
print(new_list) # Prints the concatenated list

print(new_list) # Prints the list
new_list[0] = 'ONE ALL CAPS' # Assigns the string 'ONE ALL CAPS' to the first item in the list
print(new_list) # Prints the list

new_list.append('append me!') # Appends the string 'append me!' to the end of the list
print(new_list) # Prints the list

new_list.pop() # Removes the last item in the list
print(new_list) # Prints the list
popped_item = new_list.pop() # Assigns the last item in the list to the variable popped_item
print(popped_item) # Prints the last item in the list

new_list.pop(0) # Removes the first item in the list
print(new_list) # Prints the list

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

new_list.sort() # Sorts the list in alphabetical order
num_list.sort() # Sorts the list in numerical order
print(new_list) # Prints the list
print(num_list) # Prints the list

new_list.reverse() # Reverses the list
num_list.reverse() # Reverses the list
print(new_list) # Prints the list
print(num_list) # Prints the list


