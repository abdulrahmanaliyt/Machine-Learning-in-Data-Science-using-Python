import matplotlib.pyplot as plt
import pandas as pd

# Load the employee data
emp = pd.read_csv('employees_raw.csv')

# 1. Clean the data (Fix Department casing issues and fill missing salaries)
emp['Department'] = emp['Department'].str.upper()
emp['Salary'] = emp['Salary'].fillna(emp['Salary'].median())

# 2. Group by Department and calculate total salary for each
dept_salary = emp.groupby('Department')['Salary'].sum()

# Extracting labels (Department Names) and values (Total Salaries)
labels = dept_salary.index.tolist()
sizes = dept_salary.values.tolist()

# 3. Customizations for a professional look
# 'explode' pulls out a specific slice. Here, we pop out the 1st slice (Finance) slightly.
explode_settings = [0.1 if i == 0 else 0 for i in range(len(labels))]
colors_list = ['#4CAF50', '#2196F3', '#FF9800', '#E91E63']

# 4. Generate the Pie Chart
plt.figure(figsize=(8, 6))  # Sets width and height aspect ratio
plt.pie(
    sizes, 
    explode=explode_settings, 
    labels=labels, 
    colors=colors_list,
    autopct='%1.1f%%',       # Displays percentages on slices automatically
    shadow=True,             # Adds a subtle 3D shadow depth effect
    startangle=140           # Rotates the start of the pie chart
)

# Set title and equalize layout aspect ratio
plt.title('Total Salary Distribution by Department (Oracle Corp)', pad=20)
plt.axis('equal')            # Ensures the pie chart renders perfectly as a circle

# Show the chart
plt.show()