'''
To display a scatter plot with a regression line, the easiest and most professional tool is Seaborn's sns.regplot() or sns.lmplot(). It automatically calculates the linear regression line and draws a shaded confidence interval around it.
'''


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the employee dataset
emp = pd.read_csv(r'E:\Git coding\employees_raw.csv')

# Clean missing values to avoid plotting errors
emp['Salary'] = emp['Salary'].fillna(emp['Salary'].median())
emp['Score'] = emp['Score'].fillna(0.0)

# Set styling background grid
sns.set_theme(style="whitegrid")

plt.figure(figsize=(9, 6))

# Plot scatter dots with a linear regression line
sns.regplot(
    data=emp,
    x='Salary',
    y='Score',
    scatter_kws={'color': 'purple', 's': 80, 'alpha': 0.7, 'edgecolor': 'black'},
    line_kws={'color': 'red', 'linewidth': 2, 'label': 'Regression Line'}
)

# Customizing titles and labels
plt.xlabel('Employee Salary (INR)', fontsize=11)
plt.ylabel('Performance Score (Out of 10)', fontsize=11)
plt.title('Salary vs. Performance Score with Regression Line', fontsize=14, pad=15)
plt.legend()


#----------------------------------------------------------

# Load dataset
mpg = sns.load_dataset('mpg')

plt.figure(figsize=(9, 6))

# Generate scatter plot with linear regression line
sns.regplot(
    data=mpg,
    x='horsepower',
    y='acceleration',
    scatter_kws={'color': 'blue', 'alpha': 0.6, 's': 50},
    line_kws={'color': 'red', 'linewidth': 2}
)

# Customizing titles and labels
plt.xlabel('Horsepower')
plt.ylabel('Acceleration')
plt.title('Horsepower vs. Acceleration with Regression Line')

# Show the chart
plt.show()