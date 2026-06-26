# accessor and mutator methods
class Students():
    #mutator method
    def setName(self,name):
        self.name = name
        
    # accessor method
    def getName(self):
        return self.name
    
    # mutator method
    def setMarks(self,marks):
        self.marks = marks
    
    # accessor method 
    def getMarks(self):
        return self.marks
    
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
 
# create instance with some data from keyboard
n = int(input('How many students are there : '))   
# create instances with some data from keyboard
for i in range(1, n + 1):
    # create student class instance
    s = Students()
    
    
    #store name and marks into s using setter methods
    name = input(f'Enter name of student {i}: ')
    s.setName(name)
    marks = int(input(f'Enter marks of Student {i}: '))
    s.setMarks(marks)
    
    # 2. Append the current student object to the list
    all_students.append(s)
    print("-" * 30)
    
# retriving data from s using gette methods
print("\n--- Displaying All Students Data ---")
for s in all_students:
    print('Hi',s.getName())    
    print('Your marks:',s.getMarks())
    s.calculate()
    print("-" * 15)
    
   