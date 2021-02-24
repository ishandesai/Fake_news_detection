from load_data import *

"""
insert new column in two dataframes is_fake if news is fake then is_fake=0 and if news is true is_fake=1
concatenate two dataframes into one dataframe (merge)
drop unnecessary columns from merged dataframe like date
concatenate title and text columns and assign it to brand new column original in dataframe

"""

df_true['is_fake']=1
df_fake['is_fake']=0

print(df_true.head())

print(df_fake.head())

dataframe=pd.concat([df_true,df_fake]).reset_index(drop=True)

print(dataframe)

dataframe.drop(columns=['date'],inplace=True)

dataframe['original'] = dataframe['title'] + ' ' +dataframe['text']

print(dataframe.head())

print(dataframe["original"][0])
