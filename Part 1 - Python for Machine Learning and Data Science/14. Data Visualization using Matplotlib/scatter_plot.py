'''
A Scatter Plot is used to analyze the relationship or correlation between two numerical variables. It answers questions like: "Do employees with higher performance scores also earn higher salaries?" or "Does experience correlate with income?"
'''

import matplotlib.pyplot as plt
import pandas as pd

# Load the employee data
emp = pd.read_csv('employees_raw.csv')

# Clean data: Fill missing values
emp['Salary'] = emp['Salary'].fillna(emp['Salary'].median())
emp['Score'] = emp['Score'].fillna(0.0)

# Extract numerical variables
salaries = emp['Salary'].tolist()
scores = emp['Score'].tolist()

# Generate the Scatter Plot
plt.figure(figsize=(9, 6))
plt.scatter(
    salaries, 
    scores, 
    color='purple', 
    marker='.', 
    s=100,            # Marker size
    alpha=0.7,        # Transparency (helps see overlapping dots)
    edgecolors='black'# Border color for each dot
)

# Customizing Grid and Layout
plt.grid(True, linestyle='--', alpha=0.5)

# Set labels and titles
plt.xlabel('Employee Salary (INR)')
plt.ylabel('Performance Score (Out of 10)')
plt.title('Salary vs. Performance Score Correlation', fontsize=14, pad=15)

# Show the chart
plt.show()
