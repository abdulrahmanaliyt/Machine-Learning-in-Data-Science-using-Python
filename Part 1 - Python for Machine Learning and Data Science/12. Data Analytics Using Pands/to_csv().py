import pandas as pd

data = {'Name': ['Amit', 'Priya'], 'Age': [23, 21]}
df = pd.DataFrame(data)

# Saves a file named 'employees.csv' in your working folder
df.to_csv('employees.csv' ,index=False)

# df.to_csv(r"D:\Downloads\my_analyzed_data.csv", index=False)