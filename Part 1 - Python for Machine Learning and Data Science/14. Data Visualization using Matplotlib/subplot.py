import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
mpg = sns.load_dataset('mpg')

# Create a 2x3 grid of subplots with a 15x10 inch canvas frame size
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# 1. Top-Left (0,0): Scatter Plot
sns.scatterplot(data=mpg, x='weight', y='mpg', hue='origin', ax=axes[0, 0])
axes[0, 0].set_title('1. Scatter Plot (Weight vs MPG)')

# 2. Top-Middle (0,1): Line Plot
sns.lineplot(data=mpg, x='horsepower', y='acceleration', ax=axes[0, 1], color='red')
axes[0, 1].set_title('2. Line Plot (Horsepower vs Acceleration)')

# 3. Top-Right (0,2): Bar/Count Plot
sns.countplot(data=mpg, x='origin', ax=axes[0, 2], palette='Set2')
axes[0, 2].set_title('3. Count Plot (Cars by Origin)')

# 4. Bottom-Left (1,0): Box Plot
sns.boxplot(data=mpg, x='origin', y='mpg', ax=axes[1, 0], palette='Pastel1')
axes[1, 0].set_title('4. Box Plot (MPG Distribution by Origin)')

# 5. Bottom-Middle (1,1): Histogram with KDE Overlay
sns.histplot(data=mpg, x='mpg', bins=15, kde=True, ax=axes[1, 1], color='purple')
axes[1, 1].set_title('5. Histogram + KDE (MPG Distribution)')

# 6. Bottom-Right (1,2): ECDF Plot
sns.ecdfplot(data=mpg, x='displacement', ax=axes[1, 2], color='green')
axes[1, 2].set_title('6. ECDF Plot (Displacement Proportion)')

# Optimize spacing layout to prevent overlapping labels and titles
plt.tight_layout()

# Single show function call to render the entire canvas figure matrix
plt.show()