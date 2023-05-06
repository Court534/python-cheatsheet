# Example error

# def add(n1, n2):
#     print(n1 + n2)
    
# add(10, 20)
# Output 30

# number1 = 10
# number2 = input("Please provide a number: ")
# This will throw an error because the input in a string, this will stop your code from running stright away
# add(number1 + number2)

# We can use a try to tell the computer to try this code but it might fail
try:
    10 + 10 # It will run this code because it's not encountered any errors
except:
    print("It looks like you are not adding correctly")
    
# We can use a try to tell the computer to try this code but it might fail
try:
    10 + "10"
except:
    print("It looks like you are not adding correctly") # It will run this code as it has incountered an error. You can't add an int and string together this way

# This is handy because the code keeps running even though it encountered an error that would have broken it otherwise.

# You can also add an else to this
try:
    result = 10 + 10
except:
    print("It looks like you are not adding correctly")
else:
    print("Add went well") # The else block will be the output for this as the try was successful it skips the except goes straight to the else.
    print(result)
    
# You can also use a finally block
try:
    f = open("testfile", "r")
    f.write("Write a test line")
except TypeError:                   # You can use multiple excepts
    print("There was a type error") 
except OSError:                     # In this example we are looking for specific errors like "TypeError" and "OSError" 
    print("there was an OSRrror")
finally:
    print("I always run no matter what") # The finally block will always run
    
# Example with a function
def ask_for_int():
    try:
        result = int(input("Please provide a number: "))
        print(f"You chose the number {result}")
    except:
        print("Whoops, thats not a number!")
    finally:
        print("This is the end of the try/except/finally")
        
ask_for_int()

# Example with a function and a loop
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops, thats not a number!")
            continue
        else:
            print(f"You chose the number {result}")
            break
        finally:
            print("This is the end of the try/except/finally")
        
ask_for_int()