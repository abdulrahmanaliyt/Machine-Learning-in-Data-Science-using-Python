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

# concat()
concatination = pd.concat([df1,df2])
print(concatination)


print("------------------ignore_Index = True ---------------")
# concat()
concatination2 = pd.concat([df1,df2], ignore_index=True)
print(concatination2)

print("------------------ignore_Index = false , axix=1---------------")
# concat()
concatination3 = pd.concat([df1,df2], ignore_index=False , axis=1)
print(concatination3)