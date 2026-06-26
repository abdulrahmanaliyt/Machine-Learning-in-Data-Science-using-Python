# Intance vars and method -v2.0
class Student:
    # this is a constructor 
    def __init__(self,n='',m=0):
        self.name = n
        self.marks = m
        
    # This is an instance method
    def display(self):
        print('Hi',self.name)
        print('Your marks is:',self.marks)
        
# Constructor is called without any arguements
s = Student()
s.display()
print('---------------------------------')

# Constructor is called with 2 arguements
s1 = Student('Lakshmi Roy',880)
s1.display()
print('----------------------------------')