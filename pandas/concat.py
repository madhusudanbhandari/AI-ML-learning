###vertical=row_wise
##horizontal==collumn_wise

##syntax==pd.concat([df1,df2],axis=0,ignore_indx=True)


import pandas as  pd

df_region1=pd.DataFrame(
    {
        'Cust_id':[1,2],
        'Name':['ram','sam']
    }
)


df_region2=pd.DataFrame(
    {
        'Cust_id':[3,4],
        'Name':['ben','tom']
    }
)

# ##Vertical concatenation  axis=0

# df_concat=pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
# print(df_concat)

##Vertical concatenation  axis=1

df_concat=pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concat)