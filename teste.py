from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os.path import join, dirname
import pandas
import os
import json

uri = "mongodb+srv://DB_USER:<DB_PASSWORD>@cluster0.qoks7uh.mongodb.net/?appName=Cluster0"
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Create a new client and connect to the server
client = MongoClient(os.environ[uri], server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['dados_ibge']
dados_ibge = db['dados_ibge'].find()
print(dados_ibge[1]['resultados'][0]['series'][0]['serie'])

serie = dados_ibge[1]['resultados'][0]['series'][0]['serie']
df = pandas.DataFrame.from_dict(serie, orient='index',columns=['valor'])
df.index.name = 'periodo'
df = df.reset_index()
df.head()
print(df)