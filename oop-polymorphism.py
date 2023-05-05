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