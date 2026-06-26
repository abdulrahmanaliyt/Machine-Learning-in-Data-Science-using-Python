'''
To create an ECDF (Empirical Cumulative Distribution Function) plot in Seaborn, you use the parameter kind='ecdf' inside sns.displot().

An ECDF plot shows the proportion or percentage of data points that are less than or equal to a particular value on the X-axis.
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
mpg = sns.load_dataset('mpg')

# Bivariate distribution plot
sns.displot(data=mpg, x='cylinders', y='mpg', hue='origin')

# Customizing titles and labels
plt.xlabel('No of Cylinders')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Bivariate Distribution of Cylinders vs. MPG')

# Show the chart
plt.show()

#-------------------cbar=True----------------------------
# Bivariate distribution plot
sns.displot(data=mpg, x='cylinders', y='mpg', cbar=True, hue='origin')

# Customizing titles and labels
plt.xlabel('No of Cylinders')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Bivariate Distribution of Cylinders vs. MPG')

# Show the chart
plt.show()

#-------------------kind='kde'----------------------------
# Bivariate distribution plot
sns.displot(data=mpg, x='cylinders', y='mpg', cbar=False, hue='origin', kind='kde')

# Customizing titles and labels
plt.xlabel('No of Cylinders')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Bivariate Distribution of Cylinders vs. MPG')

# Show the chart
plt.show()