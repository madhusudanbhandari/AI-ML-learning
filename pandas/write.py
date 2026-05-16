import pandas as pd

data={
    'Name':['Madhu','Sudan','ram'],
    'Age':[21,23,45],
    'Cities':['Ktm','Pkr','mnr']
}
df=pd.DataFrame(data)
print(df)

# ##Saving Data in a csv file
# df.to_csv('Output.csv',index=False)

# ##Saving Data in a JSON file
# df.to_json('Output.json',index=False)

##Saving Data in a Excel file
#df.to_excel('Output.xlsx',index=False)