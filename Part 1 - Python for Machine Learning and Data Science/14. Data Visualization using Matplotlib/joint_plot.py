"""A Joint Plot (sns.jointplot()) combines a bivariate plot (like a scatter plot) with two univariate plots (histograms or density plots) on the outer margins. This allows you to view the relationship between two numerical variables and their individual distributions simultaneously.

1. Basic Joint Plot (Scatter + Histogram)
To plot vehicle weight (weight) against fuel efficiency (mpg):"""

import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')

# Generates scatter plot in center and histograms on top/right margins
sns.jointplot(data=mpg, x='weight', y='mpg', color='purple')
plt.show()

'''2. Hexagonal Binning (kind='hex')
When you have overlapping data points, you can group them into hexagonal bins. Darker hexagons represent a higher density of data points.'''

sns.jointplot(data=mpg, x='horsepower', y='mpg', kind='hex', color='blue')
plt.show()

'''3. Kernel Density Estimate (kind='kde')
Changes both the central and marginal plots to smooth KDE curves for a continuous probability layout.'''

sns.jointplot(data=mpg, x='acceleration', y='mpg', kind='kde', fill=True, color='green')
plt.show()

'''4. Categorical Grouping (hue)
Segments the data point distribution by a categorical variable across both the central scatter and marginal density lines.'''

sns.jointplot(data=mpg, x='weight', y='mpg', hue='origin')
plt.show()