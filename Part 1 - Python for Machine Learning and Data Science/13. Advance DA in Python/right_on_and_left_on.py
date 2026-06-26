import pandas as pd

# DataFrame 1: Uses 'Emp_ID'
df1 = pd.DataFrame({
    'Emp_ID': [101, 102, 103],
    'Name': ['Amit', 'Priya', 'Vijay'],
    'Department': ['IT', 'HR', 'Finance']
})

# DataFrame 2: Uses 'Employee_Identifier' instead of 'Emp_ID'
df2 = pd.DataFrame({
    'Employee_Identifier': [101, 102, 103],
    'Salary': [85000, 60000, 95000],
    'Location': ['Delhi', 'Mumbai', 'Bangalore']
})

# Merge using left_on and right_on
print('----------------------how = join------------------')
merged_inner = pd.merge(df1, df2, left_on='Emp_ID', right_on='Employee_Identifier', how='inner')
print(merged_inner)

print('----------------------how = left------------------')
merged_left = pd.merge(df1, df2, left_on='Emp_ID', right_on='Employee_Identifier', how='left')
print(merged_left)

print('----------------------how = right------------------')
merged_right = pd.merge(df1, df2, left_on='Emp_ID', right_on='Employee_Identifier', how='right')
print(merged_right)

print('----------------------how = outer------------------')
merged_outer = pd.merge(df1, df2, left_on='Emp_ID', right_on='Employee_Identifier', how='outer')
print(merged_outer)