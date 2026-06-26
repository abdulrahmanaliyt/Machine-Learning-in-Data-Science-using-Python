import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Vijay', 'Rohan'],
    'Age': [23, 21, 25, 22],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Noida']
}

# Creating a DataFrame with custom row index names
df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4'])
print(df)

#---------------loc[]------------------------

print('-'*20)
# Find the Age of Priya (row2)
print(df.loc['row2', 'Age'])  # Outputs: 21

print('-'*20)
#Selecting an entire row
# Pass only the row label
print(df.loc['row3'])

print('-'*20)
# Selecting specific rows and columns (Slicing)
# Select rows from 'row1' to 'row3' inclusive, and only 'Name' and 'City'
print(df.loc['row1':'row3', ['Name', 'City']])

print('-'*20)
print('Reverse the rows from index 3 down to 0')
# Reverse the rows from index 3 down to 0
print(df.loc['row3':'row1':-1, :])

print('-'*20)
print('-'*20)
# Find employees who are older than 21 AND live in Delhi or Bangalore
multi_filter = df.loc[(df['Age'] > 21) & (df['City'].isin(['Delhi', 'Bangalore']))]
print(multi_filter)
#-----------------iloc[]-----------------------
print('-'*20)
# Find the Age of Priya (row at index 1, column at index 1)
print(df.iloc[1, 1])  # Outputs: 21

print('-'*20)
# Pass only the numerical row index
print(df.iloc[2])  # Returns the entire row of Vijay

print('-'*20)
# Select index positions 0, 1, and 2 (excludes 3) and columns 0 and 1
print(df.iloc[0:3, 0:2])

print('-'*20)
print(df.describe())