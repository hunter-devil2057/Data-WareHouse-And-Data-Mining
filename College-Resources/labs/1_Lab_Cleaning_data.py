import pandas as pd
import numpy as np

data = pd.read_csv('D:/python_projects/employees.csv')
print("Original Data")
print(data[0:25])

# Removing missing values
data=data.dropna(axis=0)

# Removing duplicate rows
data.drop_duplicates(keep='first',inplace=True)

# Removing column Boonus %
del data['Bonus %']

# Correcting Inconsitencies among values
data['Team']=data['Team'].str.replace('Fin','Finance')
data['Team']=data['Team'].str.replace('Mkt','Marketing')
data['Team']=data['Team'].str.replace('Financeance','Finance')

print("Cleaned Data")
print(data[0:25])
data.to_csv('D:/python_projects/employees_cleaned.csv', index=False)
print("Successfully Cleaned...")
