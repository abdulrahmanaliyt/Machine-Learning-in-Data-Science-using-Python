'''sns.catplot() (Categorical Plot) is a figure-level function in Seaborn used to visualize relationships between numerical and categorical variables.

Instead of memorizing different functions like sns.boxplot(), sns.barplot(), or sns.violinplot(), you can create all of them using sns.catplot() by changing the kind parameter.'''

import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
mpg = sns.load_dataset('mpg')

# 1. Categorical Scatter: Swarm Plot (Points do not overlap)
sns.catplot(data=mpg, x='origin', y='mpg', kind='swarm', hue='cylinders')
plt.title('Swarm Plot via catplot')

# 2. Categorical Distribution: Box Plot 
sns.catplot(data=mpg, x='origin', y='mpg', kind='box', palette='Set2')
plt.title('Box Plot via catplot')

# 3. Categorical Estimate: Bar Plot (Shows the Mean value + error bar)
sns.catplot(data=mpg, x='origin', y='mpg', kind='bar', errorbar=None)
plt.title('Bar Plot via catplot')


#_____________________________________________________________
'''Why use catplot instead of standard axes-level plots?
The main advantage of catplot() is its ability to easily create multi-plot grids across rows or columns using the col and row parameters:'''

# Creates separate side-by-side subplot columns for each country of origin
sns.catplot(
    data=mpg, 
    x='cylinders', 
    y='mpg', 
    kind='box', 
    col='origin'
)




# Display all open figures
plt.show()