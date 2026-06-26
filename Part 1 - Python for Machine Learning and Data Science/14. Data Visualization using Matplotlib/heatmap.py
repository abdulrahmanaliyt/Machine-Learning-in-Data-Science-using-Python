'''A Heatmap (sns.heatmap()) is a graphical representation of data where individual values contained in a matrix are represented as colors. It is primarily used to visualize correlation matrices to see relationships between multiple numerical variables at a glance.'''

import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
iris = sns.load_dataset('iris')

# Drop the categorical 'species' column to calculate numeric correlation
numeric_iris = iris.drop(columns=['species'])
correlation_matrix = numeric_iris.corr()

plt.figure(figsize=(8, 6))

# Generate the Heatmap
sns.heatmap(
    data=correlation_matrix, 
    annot=True,             # Displays the correlation value numbers inside squares
    cmap='coolwarm',        # Color palette gradient (blue to red)
    linewidths=0.5,         # Adds white grid dividing lines between boxes
    vmin=-1, vmax=1         # Sets the colorbar limits to match correlation boundaries
)

plt.title('Correlation Heatmap of Iris Dataset Features', fontsize=14, pad=15)

# Slice the dataframe: first 10 rows (0 to 9) and first 4 columns (0 to 3)
subset = iris.iloc[:10, :4]

plt.figure(figsize=(8, 6))

# Generate the Heatmap for the data values
sns.heatmap(
    data=subset, 
    annot=True,             # Displays the exact cell values inside the squares
    cmap='YlGnBu',          # Yellow-Green-Blue color gradient
    linewidths=0.5,         # Adds a clear grid line between cells
    cbar=True               # Shows the color scale bar
)
# Customizing layout labels
plt.title('Heatmap of First 10 Rows & First 4 Columns (Iris)', fontsize=14, pad=15)
plt.xlabel('Features', fontsize=12)
plt.ylabel('Row Index', fontsize=12)

# Show the chart
plt.show()

print(iris['species'].value_counts())