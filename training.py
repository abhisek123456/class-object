from utilies import Utilies
from preprocessing import Processing

#data load
uti=Utilies()
path="Iris.csv"
data=uti.data_loader(path)

#print(data.head())

#Preprocess
## Checking missing values
process=Processing(data)

mis= process.checking_missing_value()
print("The missiong values are ",mis)

