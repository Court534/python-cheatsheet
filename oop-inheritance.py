class Animal():
    def __init__(self):
        print("Animal crated!")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")
        
myanimal = Animal()

myanimal.who_am_i()

myanimal.eat()


# This class is inheriting from the above class Animal
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
     
     # We can overwrite the existing fuctions we've inherited simply by calling them the same name   
    def who_am_i(self):
        print("I am a dog")
    
    # Created a new function    
    def bark(self):
        print("WOOF!")
        
mydog = Dog()

# Calling the the renamed function
mydog.who_am_i()

# We can also call new functions
mydog.bark()
    
        