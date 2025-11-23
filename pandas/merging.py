import pandas as pd

#customer dataframe
customer={
    'Cust_id':[1,2,3],
    'Cust_name':['sita','gita','rita']
}
df_cust=pd.DataFrame(customer)

orders={
    'Cust_id':[1,2,4],
    'OrderAmount':[250,450,350]
}
df_ord=pd.DataFrame(orders)

#Merge
##syntax=pd.merge(df1,df2,on='colm_name',how='inner,outer,left,right,cross)
# df_merged=pd.merge(df_cust,df_ord,on='Cust_id',how='inner')
# print('inner join')
# print(df_merged)

# df_merged=pd.merge(df_cust,df_ord,on='Cust_id',how='outer')
# print('outer join')
# print(df_merged)


# df_merged=pd.merge(df_cust,df_ord,on='Cust_id',how='left')
# print('Left join')
# print(df_merged)


# df_merged=pd.merge(df_cust,df_ord,on='Cust_id',how='right')
# print('Right join')
# print(df_merged)


# df_merged=pd.merge(df_cust,df_ord,how='cross')
# print('Cross join')
# print(df_merged)