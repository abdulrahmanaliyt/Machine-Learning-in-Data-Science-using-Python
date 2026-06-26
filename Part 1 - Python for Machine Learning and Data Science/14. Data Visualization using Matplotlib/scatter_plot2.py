'''
A Scatter Plot maps individual data points along an X and Y axis to inspect relationships or correlations between two numerical variables.
'''
'''
1. Basic Scatter Plot
To plot vehicle weight (weight) against fuel efficiency (mpg):
'''
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')
plt.figure(figsize=(9, 6))

sns.scatterplot(data=mpg, x='weight', y='mpg')

plt.xlabel('Weight of Car')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Weight vs. MPG')
plt.show()

'''
2. Grouping Variables (hue and style)
To segment data point distributions by category (e.g., origin country or cylinders):
'''

plt.figure(figsize=(9, 6))
# hue alters colors; style alters marker shapes per category
sns.scatterplot(
    data=mpg, 
    x='horsepower', 
    y='mpg', 
    hue='origin', 
    style='origin', 
    s=100
)

plt.xlabel('Horsepower')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Horsepower vs. MPG by Origin')
plt.show()

'''
3. Continuous Sizing Adjustments (size)
To scale marker sizes proportionally based on a continuous numerical third variable:
'''
plt.figure(figsize=(9, 6))
# size maps marker area dimensions relative to the variable array values
sns.scatterplot(
    data=mpg, 
    x='acceleration', 
    y='mpg', 
    hue='origin', 
    size='weight', 
    sizes=(40, 400), 
    alpha=0.7
)

plt.xlabel('Acceleration')
plt.ylabel('Miles Per Gallon (mpg)')
plt.title('Acceleration vs. MPG (Marker Size = Weight)')
plt.show()