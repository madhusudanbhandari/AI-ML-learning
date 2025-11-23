#1=how big is your dataset
#2-what are the names of columns

##shape and column methods

import pandas as pd

data={
    'Name':['ram','sam','curan','hari','sita','rita','raj','simran'],
    'Age':[54,45,60,34,68,36,67,53],
    'Salary':[34500,70000,490000,50000,45000,65000,34000,67000],
    'Performance Score':[45,98,37,89,46,67,81,78]

}
df=pd.DataFrame(data)
print(df)

print('Shape: ',df.shape)
print('Columns: ',df.columns)

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