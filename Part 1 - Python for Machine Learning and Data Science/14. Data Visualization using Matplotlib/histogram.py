import matplotlib.pyplot as plt
import pandas as pd

emp = pd.read_csv('employees_raw.csv')
emp['Salary'] = emp['Salary'].fillna(emp['Salary'].median())

x = emp['Salary'].tolist()

# 'bins=10' creates 10 even mathematical salary ranges automatically
plt.hist(x, bins=10, histtype='bar', rwidth=0.8, color='blue', label='Salary Frequency')

plt.xlabel('Employee Salaries')
plt.ylabel('Number of Employees')  # Histograms plot count frequency on Y-axis

plt.title('Oracle Corp')
plt.legend()
plt.show()