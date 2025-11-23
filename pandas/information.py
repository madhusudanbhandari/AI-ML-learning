import pandas as pd
df=pd.read_csv('sales_data_sample.csv',encoding='latin1')

print('Displaying the details of the dataset')
print(df.info())


ab=pd.read_json('sample_Data.json')
print(ab.info())