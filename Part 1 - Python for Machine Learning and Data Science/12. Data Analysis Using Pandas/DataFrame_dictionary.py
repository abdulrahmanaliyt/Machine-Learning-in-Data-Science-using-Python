import pandas as pd

# Employee dictionary dataset
employee_data = {
    'Emp_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Amit Sharma', 'Priya Rao', 'Vijay Kumar', 'Rohan Das', 'Ananya Singh', 
             'Suresh Raina', 'Megha Gupta', 'Rahul Verma', 'Kriti Malhotra', 'Nitin Malhotra'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing', 
                   'Finance', 'HR', 'IT', 'Marketing', 'IT'],
    'Salary': [85000, 60000, 95000, 72000, 55000, 
               98000, 62000, 110000, 58000, 72000],
    'Experience_Years': [5, 3, 8, 4, 2, 9, 3, 10, 2, 4],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Noida', 
             'Bangalore', 'Mumbai', 'Delhi', 'Noida', 'Delhi']
}

# Configure pandas to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Create DataFrame
df = pd.DataFrame(employee_data)

# Display the DataFrame
print(df)

# Useful Practice Operations
print(df[df['Salary'] > 70000])
print(df.groupby('Department')['Salary'].mean())
print(df['City'].value_counts())
print(df.duplicated().sum())