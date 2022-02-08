import requests as req
import os
import json
response=req.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1000")
json_response=response.json()
with open('C:/Users/emartinez14/Documents/searchjson202202/data_ml.json', 'w') as json_file:
         json.dump(json_response, json_file)
