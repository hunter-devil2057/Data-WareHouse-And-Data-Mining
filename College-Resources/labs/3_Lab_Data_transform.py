import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
  
df = pd.read_csv("D:/python_projects/student-data.csv")

print(df)
#Sort by name
sorted = df.sort_values(by=['name'])
print(sorted)

#Filter rows
just_students = df.query('is_student==True')
print(just_students)


#Filter columns
no_birthday = df.filter(['name','is_student','target'])
print(no_birthday)

#Remove duplicates
print(df.duplicated())
dups_removed = df.drop_duplicates()
print(dups_removed)
