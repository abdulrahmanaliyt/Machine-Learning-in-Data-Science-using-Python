'''To create a line plot mapping horsepower on the X-axis and acceleration on the Y-axis using Seaborn, use sns.lineplot().

Because multiple data points can share the exact same horsepower value, Seaborn automatically aggregates them, draws a line through their mean values, and displays a shaded 95% confidence interval boundary.'''

import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
mpg = sns.load_dataset('mpg')

plt.figure(figsize=(9, 5))

# Generate the line plot
sns.lineplot(data=mpg, x='horsepower', y='acceleration', color='blue', linewidth=2)

# Customizing labels and titles
plt.xlabel('Horsepower')
plt.ylabel('Acceleration')
plt.title('Horsepower vs. Acceleration Trend')
plt.grid(True, linestyle='--', alpha=0.5)

# Show the chart
plt.show()

'''Sorting Optimization Hint
If your underlying data arrays are unordered and you wish to disable Seaborn's internal sorting calculation along the X-axis timeline, you can pass sort=False inside the function:'''

sns.lineplot(data=mpg, x='horsepower', y='acceleration', sort=False)
plt.show()
