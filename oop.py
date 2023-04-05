# Brief over view of what a class looks like
class NameOfClass():
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
    def some_method(self):
        # perfrom some action
        print(self.param1)

# Example 1
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
    
    # Operation/Actions --> Methods    
    def bark(self, number):
        print('Woof! My name is {} and I am {} years old'.format(self.name, number))
       
my_dog = Dog('Bichon', 'Pippin', False)

print(my_dog.name)
print(my_dog.breed)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark(10))


# Example 2
class Circle():

    # Class Object Attribute
    pi = 3.14 
    
    def __init__(self, radius=1):
        
        self.radius = radius
        
    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle()
    
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
