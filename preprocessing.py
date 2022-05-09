import pandas as pd
import numpy as np

class Processing:

    def __init__(self,data):
        self.data=data

    # checking missing values
    def checking_missing_value(self):
        
        try:
            missing_value= self.data.isnull().sum()
            return missing_value
        except Exception as e:
            return Exception ()
    
    # Remve the catagorical columns 

    def remove_cat(self):
        try:
            categorical_features=[feature for feature in self.data.columns
                     if self.data[feature].dtypes=="O"]
            print(categorical_features)
            self.data.drop(labels=categorical_features,axis=1,inplace=True)
            return self.data
        except Exception as e:
            return Exception()


    
