from utilies import Utilies

uti=Utilies()
path="Iris.csv"
data=uti.data_loader(path)

print(data.head())