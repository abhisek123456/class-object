from cProfile import label
from calendar import c
import pandas as pd

df= pd.read_csv("Iris.csv")

print(df.shape)
#categorical_features=[feature for feature in df.columns
                     #if df[feature].dtypes=="O"]
#print(categorical_features)

def remove_cat(data):
    categorical_features=[feature for feature in data.columns
                     if data[feature].dtypes=="O"]
    print(categorical_features)
    data.drop(labels=categorical_features,axis=1,inplace=True)

remove_cat(df)
print(df.shape)