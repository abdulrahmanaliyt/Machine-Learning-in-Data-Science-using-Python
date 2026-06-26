'''A Pair Plot (sns.pairplot()) creates a matrix of scatter plots for every pair of numerical features in a dataset, along with univariate distributions (histograms or KDEs) on the diagonal. It is a powerful tool for discovering patterns and correlations across multiple dimensions simultaneously.

1. Basic Pair Plot
To plot all numerical features in the Iris dataset:
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
iris = sns.load_dataset('iris')

# Generates a grid for all numerical features
sns.pairplot(data=iris)

'''2. Grouping by Category (hue)
To color-code data points by species and change the diagonal to smooth KDE plots'''

# 'hue' groups data points and adds a legend automatically
sns.pairplot(data=iris, hue='species', palette='Set2', diag_kind='kde')

'''3. Customizing Markers and Visual Layout
To use different marker shapes for each species, add a regression trend line to the scatter plots, and clean up the matrix layout by keeping only the lower triangle:'''

sns.pairplot(
    data=iris, 
    hue='species', 
    markers=['o', 's', 'D'], 
    kind='reg',              # Adds a regression line to non-diagonal plots
    corner=True,             # Hides duplicate upper-triangle subplots
    palette='bright'
)
plt.show()