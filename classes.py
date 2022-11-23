# A class is a blueprint for creating objects. An object has properties and methods (functions) associated with it. 
# Almost everything in Python is an object.

class Animal():
    
    def __init__(self):
        print("Animal created")
        
    def who_am_i(self):
        print("I am an Animal")
        
    def eat(self):
        print("I am eating")
        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
    def who_am_i(self):
        print("I am a dog")
        
    def bark(self):
        print("Woof!")
        
mydog = Animal()