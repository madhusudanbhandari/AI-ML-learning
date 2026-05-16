
## Series===one dimensional labeled array used to store any data type ....each element in the series has unique label called index

##Dataframe==multi dimensional data storage..used to store the data in the form of rows and columns

##creating dataset
import pandas as pd

data={
    'name':['ram','shyam','gita'],
    'age':[23,45,66],
    'address':['ktm','pkr','mnr']

}

df=pd.DataFrame(data)

print(df)

df.to_csv("details.csv",index=False)