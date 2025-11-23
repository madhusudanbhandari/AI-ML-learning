##Head and tail methods
#head(n)or 5 views first n or 5 rows
#tail(n) or 5 views last 5 or n rows


import pandas as pd

df = pd.read_csv('sales_data_sample.csv',encoding='latin1')

#printing first 10 rows of the dataset
print(df.head(10))

print('Last 10 rows of the dataset')
print(df.tail(10))