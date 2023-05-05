# Dog class with a speak function 
class Dog():
    
    def __init__(self, name):
        self.name = name 
        
    def speak(self):
        return self.name + " says Woof!"
    
# Cat class that is identical to the dog class    
class Cat():
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says Meow!"
    
niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

# Example of polymorphism with these two classes
# for pet in [niko, felix]:
    # print(type(pet))
    # print(type(pet.speak()))
    
# Althoug the classes are identical, you can see they're different types

# output
# <class '__main__.Dog'>
# <class 'str'>
# <class '__main__.Cat'>
# <class 'str'>

# Another example of polymorphism
for pet in [niko, felix]:
    def pet_speak(pet):
        print(pet.speak())
        
    pet_speak(niko)
    pet_speak(felix)
    
class Animal():
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
