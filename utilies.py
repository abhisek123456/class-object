import pandas as pd
import numpy as np 

class Utilies:

    def __init__(self):
        pass

# loading data 
    def data_loader(self,path):
        """ Method data_loader
            Descriptions load the given data
            Output Pandas DataFrame  
        """
        try:
            return pd.read_csv(path)
        except Exception as e:
            raise Exception(e)