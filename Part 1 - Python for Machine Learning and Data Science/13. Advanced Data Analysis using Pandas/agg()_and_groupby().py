import pandas as pd

# Sample dataset
data = {
    'Employee': ['Amit', 'Priya', 'Vijay', 'Rohan', 'Ananya', 'Suresh'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
    'Salary': [85000, 60000, 90000, 75000, 65000, 98000],
    'Projects': [4, 2, 5, 3, 2, 6]
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
print("\n" + "="*40 + "\n")

# 1. df.value_counts() -> Count how many employees are in each department
print("--- 1. df['Department'].value_counts() ---")
dept_counts = df['Department'].value_counts()
print(dept_counts)
print("\n" + "-"*30 + "\n")

# 2. df.groupby('col').mean() -> Get the average values for each department
# Note: numeric_only=True ignores non-numeric columns like 'Employee'
print("--- 2. df.groupby('Department').mean() ---")
dept_means = df.groupby('Department').mean(numeric_only=True)
print(dept_means)
print("\n" + "-"*30 + "\n")

# 3. df.groupby().agg() -> Apply multiple different operations simultaneously
print("--- 3. df.groupby('Department').agg(...) ---")
dept_summary = df.groupby('Department').agg(
    Total_Employees=('Employee', 'count'),
    Average_Salary=('Salary', 'mean'),
    Max_Projects=('Projects', 'max')
)
print(dept_summary)