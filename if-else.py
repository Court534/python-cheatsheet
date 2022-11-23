# if else statement are used to check the condition and execute the code

if True:
    print("true")
    
hungry = True
if hungry:
    print("feed me") # Will print "feed me" because hungry is true
    
hungry = False
if hungry:
    print("feed me") # Will not print anything because hungry is false
    
hungry = False
if hungry:
    print("feed me")
else:
    print("I am not hungry") # Will print "I am not hungry" because hungry is false

hungry = True
if hungry:
    print("feed me")
else:
    print("I am not hungry") # Will print "feed me" hungry because hungry is false
    
loc = 'Bank'
if loc == 'Auto Shop':
    print("Cars are cool")
else:
    print("I do not know much") # Will print "I do not know much" because loc is not equal to "Auto Shop"

loc == 'Bank'   
if loc == "auto shop":
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool")
else:
    print("I do not know much") # Will print "Money is cool" because loc is equal to "Bank"

loc = "Store"      
if loc == "Auto Shop":
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool")
elif loc == "Store":
    print("Welcome to the store")
else:
    print("I do not know much") # Will print "Welcome to the store" because loc is equal to "Store"
    
name = "Sammy" 
if name == "Frankie":
    print("Hello Frankie")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print("What is your name?") # Will print "Hello Sammy" because name is equal to "Sammy"