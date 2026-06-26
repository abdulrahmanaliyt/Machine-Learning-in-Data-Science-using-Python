import pandas as pd

# df1 contains basic info
df1 = pd.DataFrame({
    'Emp_ID': [101, 102, 103,104],
    'Name': ['Amit', 'Priya', 'Vijay','Virat']
})

# df2 contains payroll info
df2 = pd.DataFrame({
    'Emp_ID': [101, 102, 103,105],
    'Salary': [85000, 60000, 95000,50000]
})

# The 'key' here is 'Emp_ID'
print('----------------------how = join------------------')
merged_inner = pd.merge(df1, df2, on='Emp_ID', how='inner')
print(merged_inner)

print('----------------------how = left------------------')
merged_left = pd.merge(df1, df2, on='Emp_ID', how='left')
print(merged_left)

print('----------------------how = right------------------')
merged_right = pd.merge(df1, df2, on='Emp_ID', how='right')
print(merged_right)

print('----------------------how = outer------------------')
merged_outer = pd.merge(df1, df2, on='Emp_ID', how='outer')
print(merged_outer)