import pandas as pd

# Configure pandas to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_excel("d:\\Downloads\\student_dataset_750.xls", sheet_name=0)
print(df)