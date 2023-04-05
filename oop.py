# Brief over view of what a class looks like
class NameOfClass():
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
    def some_method(self):
        # perfrom some action
        print(self.param1)
        
class Dog():
    
    # Class Object Attribute
    # Same for any instance of a class
    species = 'mammal'
    
    def __init__(self, breed, name, spots):
        # Expecting breed and name to be a string
        self.breed = breed
        self.name = name
        # Exspecting spots to be a boolean (True/False)
        self.spots = spots
       
my_dog = Dog(breed = 'Bichon', name = 'Pippin', spots = False)

print(my_dog.name)
print(my_dog.breed)
print(my_dog.spots)
print(my_dog.species)
        