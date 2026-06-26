import matplotlib.pyplot as plt
import pandas as pd

# Load the employee data
emp = pd.read_csv('employees_raw.csv')

# 1. Clean and convert the Join_Date column to datetime
emp['Join_Date'] = pd.to_datetime(emp['Join_Date'])

# 2. Extract only the Year from the date to track annual growth
emp['Join_Year'] = emp['Join_Date'].dt.year

# 3. Group by Year and count how many employees joined each year
hiring_trend = emp.groupby('Join_Year')['Emp_ID'].count()

# Extracting years (X-axis) and employee count (Y-axis)
years = hiring_trend.index.tolist()
employee_counts = hiring_trend.values.tolist()

# 4. Generate the Line Graph
plt.figure(figsize=(9, 5))

# Plot line with marker dots at data points
plt.plot(years, employee_counts, color='red', marker='o', linestyle='-', linewidth=2, label='New Hires')

# Customizing Grid and Axes
plt.grid(True, linestyle='--', alpha=0.6)  # Adds clean background grid lines
plt.xticks(years)  # Ensures every year is clearly marked on the X-axis

# Set labels and titles
plt.xlabel('Year of Joining', fontsize=11)
plt.ylabel('Number of Employees Hired', fontsize=11)
plt.title('Hiring Growth Trend Over Time (Oracle Corp)', fontsize=14, pad=15)
plt.legend()

# Show the chart
plt.show()