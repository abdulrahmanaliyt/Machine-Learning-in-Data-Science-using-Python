class Person:
    # attributes / class variables
    name = 'Raju'
    age = 30
    
    # actions / instance methods
    def talk(self):
        print('Name:',self.name)
        print('Age:',self.age)

# Object creation (outside the class)
p1 = Person()
p1.talk()