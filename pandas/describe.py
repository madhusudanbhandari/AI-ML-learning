#step1-sample data frame
import pandas as pd

data={
    'Name':['ram','sam','curan','hari','sita','rita','raj','simran'],
    'Age':[54,45,60,34,68,36,67,53],
    'Salary':[34500,70000,490000,50000,45000,65000,34000,67000],
    'Performance Score':[45,98,37,89,46,67,81,78]

}
df=pd.DataFrame(data)
print('Sample DataFrame')
print(df)
print('Descriptive Statistics')
print(df.describe())