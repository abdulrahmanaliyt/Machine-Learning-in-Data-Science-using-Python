import pandas as pd
import numpy as np

# Structured dataset: (ID, Name, Dept, Join_Date, Salary, Performance_Score)
raw_data = [
    (101, 'Amit Sharma', 'IT', '2022-01-15', 85000, 8.5),
    (102, 'Priya Rao', 'HR', '2023-03-22', 60000, np.nan), # Missing performance score
    (103, 'Vijay Kumar', 'Finance', '2021-11-05', 95000, 9.2),
    (104, 'Rohan Das', 'it', '2024-05-10', 72000, 7.0),    # Inconsistent 'it' casing
    (105, 'Ananya Singh', 'Marketing', '2022-08-19', np.nan, 6.8), # Missing salary
    (106, 'Suresh Raina', 'Finance', '2020-02-01', 98000, 9.5),
    (107, 'Megha Gupta', 'HR', '2023-07-12', 62000, 7.8),
    (108, 'Rahul Verma', 'IT', '2019-12-25', 110000, 9.9),
    (109, 'Kriti Malhotra', 'Marketing', '2025-01-10', 58000, np.nan),
    (110, 'Nitin Malhotra', 'IT', '2024-04-15', 72000, 8.0)
]

# Configure pandas to display all rows and columns
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)

# Column names
clm = ['Emp_ID', 'Name', 'Department', 'Join_Date', 'Salary', 'Score']

# Initialize DataFrame
df = pd.DataFrame(raw_data, columns=clm)
print("Initial DataFrame Loaded Successfully.")
print(df)