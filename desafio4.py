import pandas as pd
import json

#cargar json



ruta='C:/Users/emartinez14/MPE1004.json'
with open(ruta) as file:
    tabla_json = json.load(file)

#CREACION DEL DF VACIO
df=pd.DataFrame()
#RECORRIDO DE LA LISTA DE JSON

for elemento in tabla_json["results"]:
    dic_json={ #'rowId':elemento[],
               'itemId':elemento["id"],
               'soldQuantity':elemento["sold_quantity"],
               'availableQuantity':elemento["available_quantity"]
              }
    df=df.append(dic_json, ignore_index=True)
    df["rowid"]=df.index
  




