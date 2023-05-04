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

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
mydog = Dog()
    
        