# Brief over view of what a class looks like
class NameOfClass():
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
    def some_method(self):
        # perfrom some action
        print(self.param1)
        
class Dog():
    def __init__(self, breed):
       self.breed = breed
       
pippin = Dog(breed = 'Bichon')

print(pippin.breed)
        