import pandas as pd
import json 
import csv

#leer csv file
ruta_csv='C:/Users/emartinez14/visits.csv'
df_csv= pd.read_csv(ruta_csv)


#leer json file
ruta_json='C:/Users/emartinez14/MPE1004.json'
with open(ruta_json,'r') as file:
    tabla_json = json.load(file)

#CREACION DEL DF VACIO
df_json=pd.DataFrame()
#RECORRIDO DE LA LISTA DE JSON

for elemento in tabla_json["results"]:
    dic_json={ 
               'itemId':elemento["id"],
               'soldQuantity':elemento["sold_quantity"]
               #'availableQuantity':elemento["available_quantity"]
              }
    df_json=df_json.append(dic_json, ignore_index=True)
    #df_json["rowid"]=df_json.index
    


#joinear ambos df
df_final=df_csv.merge(df_json)
df_difcero=df_final[df_final['soldQuantity']!=0]

    
    
    
    
    
    
    
    
    
    