print([1, 2, 3]) # prints [1, 2, 3]

print([1, 2, 3]) # prints 1 2 3
print([4, 5, 6]) # prints 4 5 6
print([7, 8, 9]) # prints 7 8 9

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

display(row1, row2, row3)

row2[1] = "X"

display(row1, row2, row3)

# Accepting user input
result = input("Please enter a value: ")
print(result) # The output will always be a string
print(type(result))

# If you wanted the output to be another value type, you would have to convert it
result_int = int(result)
print(result_int)
print(type(result_int))
