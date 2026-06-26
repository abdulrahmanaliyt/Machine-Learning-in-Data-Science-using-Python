import pandas as pd
import numpy as np

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 1000)

# 1. GENERATE THE DATASET (30 Employees)
raw_employee_data = [
    (101, 'Amit Sharma', 'IT', '2022-01-15', 85000, 8.5, 'Delhi'),
    (102, 'Priya Rao', 'HR', '2023-03-22', 60000, np.nan, 'Mumbai'),
    (103, 'Vijay Kumar', 'Finance', '2021-11-05', 95000, 9.2, 'Bangalore'),
    (104, 'Rohan Das', 'it', '2024-05-10', 72000, 7.0, 'Delhi'),
    (105, 'Ananya Singh', 'Marketing', '2022-08-19', np.nan, 6.8, 'Noida'),
    (106, 'Suresh Raina', 'Finance', '2020-02-01', 98000, 9.5, 'Bangalore'),
    (107, 'Megha Gupta', 'HR', '2023-07-12', 62000, 7.8, 'Mumbai'),
    (108, 'Rahul Verma', 'IT', '2019-12-25', 110000, 9.9, 'Delhi'),
    (109, 'Kriti Malhotra', 'Marketing', '2025-01-10', 58000, np.nan, 'Noida'),
    (110, 'Nitin Malhotra', 'IT', '2024-04-15', 72000, 8.0, 'Delhi'),
    (111, 'Rajesh Patel', 'Finance', '2021-06-18', 105000, 8.9, 'Mumbai'),
    (112, 'Sunita Williams', 'HR', '2022-09-05', 64000, 7.2, 'Bangalore'),
    (113, 'Vikram Malhotra', 'IT', '2023-11-20', 88000, 8.3, 'Noida'),
    (114, 'Neha Dhupia', 'Marketing', '2024-02-14', 53000, 6.1, 'Delhi'),
    (115, 'Alok Nath', 'Finance', '2020-07-29', 115000, np.nan, 'Mumbai'),
    (116, 'Deepika Padukone', 'HR', '2023-01-01', 61000, 7.5, 'Bangalore'),
    (117, 'Ranveer Singh', 'Marketing', '2022-05-12', 67000, 8.1, 'Noida'),
    (118, 'Siddharth Malhotra', 'it', '2024-08-22', 71000, 7.4, 'Delhi'),
    (119, 'Kiara Advani', 'Finance', '2021-03-30', 92000, 9.0, 'Mumbai'),
    (120, 'Varun Dhawan', 'HR', '2025-02-17', 59000, 6.5, 'Bangalore'),
    (121, 'Alia Bhatt', 'IT', '2022-10-10', 94000, 8.8, 'Noida'),
    (122, 'Ranbir Kapoor', 'Marketing', '2023-04-05', 73000, 7.9, 'Delhi'),
    (123, 'Katrina Kaif', 'Finance', '2019-05-14', 125000, 9.7, 'Mumbai'),
    (124, 'Vicky Kaushal', 'HR', '2024-06-01', 63000, 7.1, 'Bangalore'),
    (125, 'Ayushmann Khurrana', 'IT', '2023-08-15', 82000, 8.2, 'Noida'),
    (126, 'Kriti Sanon', 'Marketing', '2021-12-20', 70000, 8.4, 'Delhi'),
    (127, 'Kartik Aaryan', 'Finance', '2020-10-11', 102000, 8.6, 'Mumbai'),
    (128, 'Sara Ali Khan', 'HR', '2022-11-03', 65000, np.nan, 'Bangalore'),
    (129, 'Janhvi Kapoor', 'IT', '2025-03-01', 69000, 7.0, 'Noida'),
    (130, 'Pankaj Tripathi', 'Marketing', '2018-09-15', 140000, 9.8, 'Delhi')
]

clm = ['Emp_ID', 'Name', 'Department', 'Join_Date', 'Salary', 'Score', 'City']
df_initial = pd.DataFrame(raw_employee_data, columns=clm)

# Save to CSV
df_initial.to_csv('employees_raw.csv', index=False)

# 2. READ CSV BACK INTO PANDAS
df = pd.read_csv('employees_raw.csv')

print("=== 1. DATA INSPECTION ===")
print(df.head(10))
print(f"\nShape of Dataset: {df.shape}")
print(f"\nMissing values per column:\n{df.isnull().sum()}")
print("-" * 50)

print("\n=== 2. DATA CLEANING ===")
# Fix casing in Department ('it' -> 'IT')
df['Department'] = df['Department'].str.upper()

# Handle Missing Values
salary_median = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(salary_median)
df['Score'] = df['Score'].fillna(0.0)

# Convert Date to Datetime Object
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
print("Cleaning complete. Data types updated:")
print(df.dtypes)
print("-" * 50)

print("\n=== 3. SELECTION AND SELECTION WITH CONDITION (.loc & .iloc) ===")
# View Row index 2 to 4 using .iloc (Exclusive of stop)
print("\nSlicing positional rows [2:5] via .iloc:")
print(df.iloc[2:5, 0:3])

# Filter via .loc: IT employees earning more than 80,000
print("\nFiltering high earners in IT via .loc:")
high_it = df.loc[(df['Department'] == 'IT') & (df['Salary'] > 80000), ['Name', 'Salary', 'City']]
print(high_it.head(3))
print("-" * 50)

print("\n=== 4. VALUE COUNTS ===")
print(df['Department'].value_counts())
print("-" * 50)

print("\n=== 5. AGGREGATE FUNCTIONS & GROUPBY ===")
# Custom Aggregation per Department
dept_analysis = df.groupby('Department').agg(
    Total_Employees=('Emp_ID', 'count'),
    Average_Salary=('Salary', 'mean'),
    Max_Score=('Score', 'max')
).reset_index()
print(dept_analysis)
print("-" * 50)

print("\n=== 6. NUMERICAL TRANSFORMATION WITH .where() ===")
# Cap Salaries over 110,000 to a max threshold of 110,000
df['Salary_Capped'] = df['Salary'].where(df['Salary'] <= 110000, other=110000)
print(df[['Name', 'Salary', 'Salary_Capped']].loc[df['Salary'] > 105000].head(4))
print("-" * 50)

print("\n=== 7. EXPORTING FINAL WORK TO CSV ===")
df.to_csv('employees_analyzed_clean.csv', index=False)
print("Saved final file as: 'employees_analyzed_clean.csv'")