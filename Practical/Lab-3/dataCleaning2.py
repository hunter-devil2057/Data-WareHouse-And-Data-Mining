import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Sheewakoti-Manish\Documents\My-Codes\Data-Warehouse-And-Data-Mining\Practical\Lab-3\employees.csv')
print("Original Data")
print(data[0:25])
# Filling missing values with interpolate 
data['Salary']=data['Salary'].interpolate(method="linear")
print("Cleaned Data")
print(data[0:25])