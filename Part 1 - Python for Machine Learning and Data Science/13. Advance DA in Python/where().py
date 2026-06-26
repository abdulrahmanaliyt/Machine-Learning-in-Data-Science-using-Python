''' 
The df.where() method in pandas checks a condition and keeps the original values where the condition is True, but replaces values where the condition is False (by default with NaN if not specified)


In real-world data analysis, .where() is incredibly valuable for capping outliers (limiting extreme data spikes) and masking sensitive rows without breaking the underlying structure of your DataFrame.

Scenario: Cleaning E-Commerce Transaction Data
We have a dataset of transaction amounts. We need to:

Identify and cap extreme luxury/fraud spikes (any amount above $500) down to a flat maximum threshold of $500.

Flag or clean up low-value invalid test entries (amounts less than $10) by replacing them with 0.

'''

import pandas as pd

# Realistic transaction data (with outliers and bad entries)
data = {
    'Transaction_ID': ['T101', 'T102', 'T103', 'T104', 'T105', 'T106'],
    'User': ['Amit', 'Priya', 'Vijay', 'Rohan', 'Ananya', 'Suresh'],
    'Amount': [250, 4200, 15, 3, 480, 8]  # 4200 is a massive outlier, 3 and 8 are low test values
}

df = pd.DataFrame(data)
print("--- Raw Transaction Data ---")
print(df)
print("\n" + "="*45 + "\n")

# Use Case 1: Capping High Outliers
# Condition: Keep value if Amount <= 500. If False, replace with 500.
df['Amount_Capped'] = df['Amount'].where(df['Amount'] <= 500, other=500)

# Use Case 2: Masking Low-Value Test Transactions
# Condition: Keep value if Amount >= 10. If False, replace with 0.
df['Amount_Cleaned'] = df['Amount_Capped'].where(df['Amount_Capped'] >= 10, other=0)

print("--- After Professional .where() Cleaning ---")
print(df)
