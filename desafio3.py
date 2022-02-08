import pandas as pd
import json

#cargar json

ruta='C:/Users/emartinez14/Sellers.json'
with open(ruta) as file:
    tabla_json = json.load(file)
#CREACION DEL DF VACIO
df=pd.DataFrame()
#RECORRIDO DE LA LISTA DE JSON
for elemento in tabla_json :
    dic_json={'siteId':elemento["body"]["site_id"],
              'sellerId':elemento["body"]["id"],
              'sellerNickname':elemento["body"]["nickname"],
              'sellerPoints':elemento["body"]["points"]
             }
    df=df.append(dic_json, ignore_index=True)
    

#Filtrar el df por seller point

df_positivos=df[df['sellerPoints']>0]
df_negativos=df[df['sellerPoints']<0]
df_ceros=df[df['sellerPoints']==0]



df_positivos.to_csv('C:/Users/emartinez14/MPE/2022/02/06/positivo/seller_posi.csv')
df_negativos.to_csv('C:/Users/emartinez14/MPE/2022/02/06/negativo/seller_nega.csv')
df_ceros.to_csv('C:/Users/emartinez14/MPE/2022/02/06/ceros/seller_cero.csv')