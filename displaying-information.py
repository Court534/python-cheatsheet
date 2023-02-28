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

#result = input("Please enter a value: ")
#print(result) # The output will always be a string
# print(type(result))

# If you wanted the output to be another value type, you would have to convert it

# result_int = int(result)
# print(result_int)
# print(type(result_int))

# How to control user input

# def user_choice():
    
#     choice = input("Please neter an number (0-10): ")
    
#     return int(choice)

# The issue with the above is that it will accept any input, even if it is not a number, and in that case will throw an error

# We can use a while loop to keep asking the user for input until they give us a valid input

# def user_choice():
    
#     choice = "WRONG"
    
#     while choice.isdigit() == False:
#         choice = input("Please enter an number (0-10): ")
    
#         if choice.isdigit() == False:
#             print("Sorry that is not a digit!")
        
#     return int(choice)

# user_choice()

# Now the above code is better but not perfect. It will accept any number, even if it is outside of the range we want

# Lets now add a range check to make sure we get a number between 0 and 10

def user_choice():
    
    choice = "WRONG"
    acceptable_range = range(0, 11)
    within_range = False

    
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter an number (0-10): ")
    
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10")
                within_range = False
        
    return int(choice)

user_choice()