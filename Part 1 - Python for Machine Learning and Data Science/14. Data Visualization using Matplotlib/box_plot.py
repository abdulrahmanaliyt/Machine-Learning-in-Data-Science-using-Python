'''
A Box Plot (or Box-and-Whisker Plot) is used to show the distribution of a numerical dataset based on its five-number summary: Minimum, First Quartile ($Q_1$), Median, Third Quartile ($Q_3$), and Maximum. It is highly effective for identifying outliers and comparing distributions across different categories.
'''

'''
1. Basic Box Plot
To see the distribution of miles per gallon (mpg) across the entire dataset:
'''
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')

# Create a basic vertical box plot
sns.boxplot(data=mpg, y='mpg', color='lightblue')

plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Distribution of MPG')
plt.show()

'''
2. Categorical Comparison Box Plot
To compare the distribution of mpg across cars from different countries of origin:
'''
plt.figure(figsize=(8, 5))

# x is categorical, y is numerical
sns.boxplot(data=mpg, x='origin', y='mpg', palette='Set2')

plt.xlabel('Country of Origin')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('MPG Distribution by Country of Origin')
plt.show()

'''
3. Horizontal Box Plot
To flip the layout horizontally, switch your assignment of x (numerical) and y (categorical):
'''
# Assigning numerical to x and categorical to y makes it horizontal
sns.boxplot(data=mpg, x='mpg', y='origin', orient='h')

plt.xlabel('Miles Per Gallon (mpg)')
plt.ylabel('Country of Origin')
plt.title('Horizontal Box Plot of MPG by Origin')
plt.show()
