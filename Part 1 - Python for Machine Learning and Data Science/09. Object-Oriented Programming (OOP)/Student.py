# a class is an example for encapsulation
class Student:
    # to declare and initialize the variables 
    def __init__(self):
        self.id = 10
        self.name = 'Raju'
    
    # display students details 
    def display(self):
        print('ID:', self.id)
        print('Name:', self.name)
    
# Creating object and calling method outside the class
p1 = Student()
p1.display()