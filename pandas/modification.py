import pandas as pd

# data={
#     'Name':['ram','sam','curan','hari','sita','rita','raj','simran'],
#     'Age':[54,45,60,34,68,36,67,53],
#     'Salary':[34500,70000,490000,50000,45000,65000,34000,67000],
#     'Performance Score':[45,98,37,89,46,67,81,78]

# }
# df=pd.DataFrame(data)
# print(df)

#1##Adding columns
# df['Bonus']=df['Salary']*0.1
# print(df)


# ##Next method using the insert()
# df.insert(0,'Employee_id',[1,2,3,4,5,6,7,8])
# print(df)


##Updating Values
#df.loc[row_indx,'col_name']=5000

# df.loc[0,'Salary']=5500
# print(df)

##Increasing salary by 5 percent
# df['Salary']=df['Salary']*1.05
# print(df)

#2##Removing Columns Using Drop method

# df.drop(columns=['Performance Score','Age'],inplace=True)
# print('Dataset after  removing Column')
# print(df)


#3##Handling the missing data
# NaN=not a number
# None=For object datatypes

# isnull()
# True=NaN is missing
# False=Value is Present



# data={
#     'Name':['ram','sam','siri','hari','sita','rita','raj','simran'],
#     'Age':[54,45,34,36,54,None,67,53],
#     'Salary':[34500,70000,490000,50000,45000,65000,34000,67000],
#     'Performance Score':[45,98,37,89,None,67,81,78]

# }
# df=pd.DataFrame(data)
# print(df)

#For finding the missing values
#print(df.isnull())
 

#For counting the total number of missing values
# print(df.isnull().sum())


##Handling the missing values
    #Drop whole row or column
    #Fill value if required

# df.dropna(inplace=True)  ##axis=0 for deleting the missing values from the row and axis=1 for deleting the missing values from the dataset
# print(df)

# df.fillna(0,inplace=True) ## 0 is the value to be placed in the missing place
# print(df)

# df['Age'].fillna(df['Age'].mean(),inplace=True)
# print(df)



#######Interpolation==process of filling missing value with the estimted value
        #preserves data integrity
        #avoid data loss
        #smoooth trends
##types:
        #1:linear
        #2:polynomial
        #3:time
        

# data={
#     'Name':['ram','sam','siri','hari','sita','rita','raj','simran'],
#     'Age':[54,45,34,36,54,None,67,53],
#     'Salary':[34500,None,490000,50000,45000,65000,34000,67000],
#     'Performance Score':[45,98,37,89,None,67,81,78]

# }
# df=pd.DataFrame(data)
# print(df)


# df.interpolate(type='linear',axis=0,inplace=True)
# print(df)


##Example 2
# data={
#     'Name':['ram','gita','shyam','hari'],
#     'Age':[34,None,67,None]
# }

# df=pd.DataFrame(data)
# print('Before Interpolation',df)

# df['Age']=df['Age'].interpolate(method='linear')
# print('After interpolation',df)


