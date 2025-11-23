##Sorting Data
#Sorting datas iin one column

import pandas as pd

# data={
#     'Name':['arun','varun','karun'],
#     'Age':[56,23,43],
#     'Salary':[10000,40000,20000]
# }
# df=pd.DataFrame(data)
# print(df)


##Sorting
# #sorting by single Column
# df.sort_values(by='Age', ascending= False ,inplace=True)
# print(df)

# #Sorting by multiple columns
# df.sort_values(by=['Age','Salary'], ascending= [False,False] ,inplace=True)
# print(df)



####Aggregation


# data={
#     'Name':['arun','varun','karun'],
#     'Age':[56,23,43],
#     'Salary':[10000,40000,20000]
# }
# df=pd.DataFrame(data)
# print(df)


# avg_salary=df['Salary'].mean()
# print(avg_salary)