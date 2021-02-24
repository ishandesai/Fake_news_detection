"""
using pandas created two dataframes for true news and fake news load datasets
"""
from import_libs import *

df_true=pd.read_csv("True.csv")
df_fake=pd.read_csv("Fake.csv")
print("True news:")
print(df_true)
print("Fake news:")
print(df_fake)

