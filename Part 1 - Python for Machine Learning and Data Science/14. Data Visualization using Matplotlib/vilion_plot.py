'''A Violin Plot (sns.violinplot()) combines a Box Plot and a Kernel Density Plot (KDE) into a single visualization.

While a box plot only shows summary statistics (like the median and quartiles), a violin plot displays the entire distribution shape and density of the data at different values. This makes it much easier to see if your data has multiple peaks (bimodal distributions).

1. Basic Violin Plot
To see the distribution density of miles per gallon (mpg) across the entire dataset:'''

import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')

# Standard vertical violin plot
sns.violinplot(data=mpg, y='mpg', color='lightgreen')

plt.ylabel('Miles Per Gallon (mpg)')
plt.title('MPG Distribution Density')

#________________________________________
'''2. Grouped Violin Plot
To compare the density distributions of mpg across different countries of origin:'''

plt.figure(figsize=(8, 5))

# x is categorical, y is numerical
sns.violinplot(data=mpg, x='origin', y='mpg', palette='Set2')

plt.xlabel('Country of Origin')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('MPG Distribution by Country')
#__________________________________________________
'''3. Split Violin Plot (Using hue and split=True)
When comparing a binary category (like two specific groups), you can split the left and right halves of the violin to directly contrast their shapes:'''

# Filtering for 4 and 6 cylinder cars from USA/Japan to make a clean comparison
filtered_mpg = mpg[mpg['cylinders'].isin([4, 6]) & mpg['origin'].isin(['usa', 'japan'])]

plt.figure(figsize=(8, 5))

# split=True merges the two hue categories into a single violin
sns.violinplot(
    data=filtered_mpg, 
    x='origin', 
    y='mpg', 
    hue='cylinders', 
    split=True, 
    inner='quart',
    palette='muted'
)

plt.xlabel('Country of Origin')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Split Violin Plot Comparison')
plt.show()