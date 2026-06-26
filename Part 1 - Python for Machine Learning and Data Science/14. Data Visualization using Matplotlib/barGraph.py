import matplotlib.pyplot as plt
import pandas as pd

emp = pd.read_csv('employees_raw.csv')
# print(emp)

x = emp['Emp_ID']
y = emp['Salary']

#create bar graph
plt.bar(x,y, label = 'Employee data', color = 'red')

# set x and y axis labels
plt.xlabel('Employee ID')
plt.ylabel('Employee Salaries')

# set company title
plt.title('MicroBond Inc')

#show legend
plt.legend()

#displat the graph
plt.show()

maxSal = emp['Salary'].idxmax()

# print(emp.loc[maxSal,['Name','Emp_ID','Salary']])