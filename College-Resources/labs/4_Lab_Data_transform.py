import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#New Variable
from dateutil.relativedelta import *
from datetime import *

df = pd.read_csv("D:/python_projects/student-data.csv")  
def get_age(dob):
    now = datetime.now()
    age = relativedelta(now, dob).years
    return age
  
df['age'] = pd.to_datetime(df['dob']).apply(get_age)

data = df.filter(['name','dob','age','is_student','target'])

print(data)
