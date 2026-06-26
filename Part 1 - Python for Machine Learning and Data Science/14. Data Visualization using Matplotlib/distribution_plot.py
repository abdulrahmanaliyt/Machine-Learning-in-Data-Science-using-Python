import matplotlib.pyplot as plt
import seaborn as sns

# Load the mpg dataset into a dataframe 
mpg = sns.load_dataset('mpg')

# 1. Distribution plot (Histogram) with 5 bins
# Added a label parameter inside the plot function
sns.displot(data=mpg, x='cylinders', bins=5, color='blue', facecolor='blue')
plt.xlabel('No of Cylinders')
plt.legend(['Histogram of Cylinders'])
plt.show()

# 2. Distribution plot with both Histogram and KDE curve overlay
sns.displot(data=mpg, x='cylinders', bins=5, kde=True, color='purple')
plt.xlabel('No of Cylinders')
plt.legend(['Histogram with KDE Overlay'])
plt.show()

# 3. Pure KDE Distribution plot
sns.displot(data=mpg, x='cylinders', kind='kde', fill=True, color='red')
plt.xlabel('No of Cylinders')
plt.legend(['Pure KDE Plot'])
plt.show()