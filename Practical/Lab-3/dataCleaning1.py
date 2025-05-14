# Data Cleaning by Handling Missing Value and Handling Inconsistent Value 
import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Sheewakoti-Manish\Documents\My-Codes\Data-Warehouse-And-Data-Mining\Practical\Lab-3\employees.csv')
print("Original Data")
print(data[0:25])

# Removing missing values
data=data.dropna(axis=0)

# Removing duplicate rows
data.drop_duplicates(keep='first',inplace=True)

# Removing column Bonus
del data['Bonus']

# Correcting Inconsitencies among values
data['Team']=data['Team'].str.replace('Fin','Finance')
data['Team']=data['Team'].str.replace('Mkt','Marketing')
data['Team']=data['Team'].str.replace('Financeance','Finance')

print("Cleaned Data")
print(data[0:25])