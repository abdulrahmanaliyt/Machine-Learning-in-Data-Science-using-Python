import pandas as pd

# Configure pandas to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv(r"D:\Downloads\company_clean_data.csv")
print(df)