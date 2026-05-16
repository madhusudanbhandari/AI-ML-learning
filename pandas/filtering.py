
# ###Filtering rows
# 1-select specific column
# 2-filter rows
# 3-combine multiple conditions

# 1-square bracket
# 2-boolean conditions

# #selecting columns
# 1-a series
# 2-dataframe multiple columns of data

# column=df['Column name']
# subset=df['col1','col2',..]

# filtering rows
# boolean indexing

# #based on a single condition
# filtered_row=df[df['Salary']>50000]

# #combine multiple conditioons
# filtered_row=df[(df['column']>value) & (df['column2']<8000)]

import pandas as pd


data={
    'Name':['ram','sam','curan','hari','sita','rita','raj','simran'],
    'Age':[54,45,60,34,68,36,67,53],
    'Salary':[34500,70000,490000,50000,45000,65000,34000,67000],
    'Performance_Score':[45,98,37,89,46,67,81,78]

}
df=pd.DataFrame(data)
print('sample dataframe')
print(df)

# ##filtering columns
# print('Names (single column return series)')
# name=df['Name']
# print(name)

# ###selecting multiple columns
# print('Multiple columns with Name and salry')
# subset=df[['Name','Salary']]
# print(subset)



##Filtering rows
##Single Condition
# high_salary=df[df['Salary']>50000]
# print('Employees with salary greater then 50000')
# print(high_salary)

##Multiple Conditions
# sorted=df[(df['Salary']>50000) & (df['Age']>40)]
# print('Employees with Salary greater them 50000 and with age above 40')
# print(sorted)

print('Employees with either salary greater then 50000 or performance greater then 50')
filtered=df[(df['Salary']>50000)  |  (df['Performance_Score']>50)]
print(filtered)