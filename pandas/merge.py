import pandas as pd


# customer={
#     'Cust_id':[1,2,3],
#     'Cust_name':['sita','gita','rita']
# }
# df_cust=pd.DataFrame(customer)


# orders={
#     'Cust_id':[1,2,4],
#     'OrderAmount':[250,450,350]
# }

# df_ord=pd.DataFrame(orders)

# df_merged=pd.merge(df_cust,df_ord, on="Cust_id",how='inner')
# print(df_merged)



# df_merged=pd.merge(df_cust,df_ord, on="Cust_id",how='outer')
# print(df_merged)

# df_merged=pd.merge(df_cust,df_ord, on="Cust_id",how='left')
# print(df_merged)

# df_merged=pd.merge(df_cust,df_ord, on="Cust_id",how='right')
# print(df_merged)


##cross join




customer1={
    'Cust_id':[1,2,3],
    'Cust_name':['sita','gita','rita']
}
df_cust1=pd.DataFrame(customer1)

customer2={
    'Cust_id':[4,5,6],
    'Cust_name':['mita','nita','jita']
}
df_cust2=pd.DataFrame(customer2)


df_concat=pd.concat([df_cust1,df_cust2],axis=1, ignore_index=True)
print(df_concat)