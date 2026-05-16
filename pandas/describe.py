import pandas as pd

data={
    'Name':['ram','hari','sita','gita','rita','tina','mina','sina'],
    'Age':[23,None,23,54,66,44,33,33],
    'Salary':[30000,40000,50000,20000,40000,50000,60000,80000],
    'Performance Score':[4,3,2,5,6,7,3,2]

}      

df=pd.DataFrame(data)
print(df)

print(df.describe())

pd=df.to_csv('details1.csv',index=False)