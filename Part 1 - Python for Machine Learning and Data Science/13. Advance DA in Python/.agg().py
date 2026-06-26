import pandas as pd
import numpy as np

data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Electronics'],
    'Sales': [12000, 4500, 8000, 3200, 6000, 15000],
    'Profit': [3000, 900, 2000, 400, 1500, 4500],
    'Units_Sold': [40, 90, 25, 12, 120, 50]
}

df = pd.DataFrame(data)
print(df)

print('-'*40)

'''
2. Common Ways to Apply Aggregate Functions
Method A: Applying Multiple Functions Across the Entire DataFrame
You can pass a list of strings representing built-in functions (like 'sum', 'mean', 'min', 'max', 'count', 'std') to run them on all numeric columns.

'''

# Calculate the total, average, and maximum for all numeric columns
summary = df[['Sales', 'Profit', 'Units_Sold']].agg(['sum', 'mean', 'max'])
print(summary)

print('-'*40)
'''
Method B: Applying Specific Functions to Specific Columns
You can pass a dictionary to map specific mathematical operations to selected columns.
'''
# Total sales, average profit, and the highest units sold
specific_summary = df.agg({
    'Sales': 'sum',
    'Profit': 'mean',
    'Units_Sold': 'max'
})
print(specific_summary)


print('-'*40)
'''
Method C: Aggregating Groups (groupby + agg)
This is the most common data analysis workflow. It splits the dataset by a categorical column and runs custom aggregates on each group.
'''
# Group by Category and apply named aggregations
category_analysis = df.groupby('Category').agg(
    Total_Revenue=('Sales', 'sum'),
    Average_Profit=('Profit', 'mean'),
    Total_Units=('Units_Sold', 'sum')
)
print(category_analysis)

print('-'*40)