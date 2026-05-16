import pandas as pd

data={
    'Name':['arun','varun','karun','sita','gita'],
    'Age':[56,53,43,53,43],
    'Salary':[10000,40000,45000,67000,20000]
}
df=pd.DataFrame(data)
print(df)

##grouping data based on the age and calculating the salary in single column

# grouped=df.groupby('Age')['Salary'].sum()
# print(grouped)



##grouping data based on the age and calculating the salary in multiple column

# grouped=df.groupby(['Age','Name'])['Salary'].sum()
# print(grouped)

###Aggregation Methods
#1.sum
#2.mean
#3.count
#4.min
#5.max
#6.sd