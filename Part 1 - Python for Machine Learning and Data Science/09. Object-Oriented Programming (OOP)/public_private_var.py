# understanding public and private variables

class MyClass:
    # this is constructor to initialize vars.
    def __init__(self):
        self.x = 1       # public var
        self.__y = 2     # private var (added double underscore)
    
    # instance method to access variables
    def display(self):
        print(self.x)    # x is available directly 
        print(self.__y)  # name mangling not required inside the class

# Driver code (Moved outside the class)
print('Accessing variables through method :')
m = MyClass()
m.display()
    
print('Accessing variables through instance:')
print(m.x)               # x is available directly
print(m._MyClass__y)     # name mangling required outside the class