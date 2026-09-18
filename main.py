import requests
import json
import os
from src.extract import Extract
from src.load import Load
from src.transform import Transform


#Pega a resposta Json direto do MongoDB
extractor = Extract()
pnadc = extractor.extract_collection_from_mongo("dados_ibge","dados_ibge")

""" with open('pernambuco.json','r') as file:
    data = json.load(file) """

#transforma o resultado JSON em uma DataFrame formatada para ser jogada em um banco de dados
transformer = Transform()
df = transformer.transform_pnadc(pnadc)

#Coloca a DataFrame em um banco de dados SQLite
loader = Load()
loader.load_sqlite(df,'pnadc_total')

#loader.load_sqlite(pnadc,"pnadc_total")

#print(data[0]['resultados'][0]['series'][0]['serie'])



