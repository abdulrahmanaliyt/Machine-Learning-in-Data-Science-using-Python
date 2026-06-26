# Instance vars and method -v2.0
class Student:
    def __init__(self, n='', m=0):
        self.name = n
        self.marks = m
        
    def display(self):
        print('Hi', self.name)
        print('Your marks is:', self.marks)
    
    def calculate(self):    
        if self.marks >= 600:
            print('You have got first grade')
        elif self.marks >= 500:
            print("You have got second position")
        elif self.marks >= 350:
            print('You have got third position')
        else:
            print('You are failed')

# 1. Create an empty list to store all student objects
all_students = []

n = int(input('How many students are there : '))

# Receiving and saving data
for i in range(1, n + 1):
    name = input(f'Enter name of student {i}: ')
    marks = int(input(f'Enter marks of Student {i}: '))
    
    s = Student(name, marks)
    
    # 2. Append the current student object to the list
    all_students.append(s)
    print("-" * 30)

# 3. Accessing and displaying all stored data after the loop completes
print("\n--- Displaying All Students Data ---")
for s in all_students:
    s.display()
    s.calculate()
    print("-" * 30)