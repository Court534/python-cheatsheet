mylist = [1,2,3]
print(len(mylist))

# Create a simple class
class Sample():
    pass

# Try the same method again
mysample = Sample()

# We get this "error TypeError: object of type 'Sample' has no len()"
# print(len(mysample))

# If we try and print mysample
print(mysample)
# We get this output "<__main__.Sample object at 0x0000014C40D6B5E0>"

# How can we get these to act like normal? 
class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
        
    b = Book("Python rocks", "Courtney", 200)
    
    print(b)

        

