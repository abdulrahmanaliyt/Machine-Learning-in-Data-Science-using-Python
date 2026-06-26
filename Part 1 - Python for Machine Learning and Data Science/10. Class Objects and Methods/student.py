class Student:
    #the below code defines attributes or variables 
    def __init__(self):
        self.name = 'Vishnu'
        self.age = 20
        self.marks = 900
        
    #the  below block defines a method
    def talk(self):
        print('Hi , i am ',self.name)
        print('My age is ',self.age)
        print('I have scored ',self.marks,'marks')
# Create an instance to Student class
s1 = Student()
# call the method using the instance
s1.talk()