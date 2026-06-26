'''
A countplot in Seaborn is essentially a histogram for categorical variables. Instead of distributing continuous numbers into bins, it counts the number of occurrences (frequency) for each unique category and displays them as bars.
'''
# To see how many cars in the dataset belong to each country of origin:

import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')

# Create a basic countplot
sns.countplot(data=mpg, x='origin')

plt.xlabel('Country of Origin')
plt.ylabel('Count of Cars')
plt.title('Number of Cars by Origin')
plt.show()

#----------------------------------

mpg = sns.load_dataset('mpg')

plt.figure(figsize=(8, 5))

# 'hue' splits the bars into sub-categories
sns.countplot(data=mpg, x='origin', hue='cylinders')

plt.xlabel('Country of Origin')
plt.ylabel('Count of Cars')
plt.title('Number of Cars by Origin and Cylinder Count')
plt.legend(title='Cylinders')
plt.show()

'''
If your category names are long, flip the graph horizontally by assigning your categorical variable to y instead of x:
'''
plt.figure(figsize=(8, 5))

# Assigning to y makes the bars horizontal
sns.countplot(data=mpg, y='origin', palette='Set2')

plt.ylabel('Country of Origin')
plt.xlabel('Count of Cars')
plt.title('Horizontal Car Count by Origin')
plt.show()
