import requests
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

# Tira dados de algum lugar
class Extract():

    def __init__(self):
        pass

    def extract_pnadc(self):

        #Usuario seleciona um tipo de taxa para extrair.
        taxas = {'8529' :'8529 - Taxa de informalidade das pessoas de 14 anos ou mais de idade, ocupadas na semana de referência',
                 '4099' : '4099 - Taxa de desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade'}
        print(f"Lista de taxas:")
        for chave,valor in taxas.items():
                    print(f"{valor}")

        while True:
            taxa = input("Selecione uma taxa pelo número:")
            if taxa in taxas.keys():
                 break
            else:
                print("Opção inválida:")
                continue

        # Usuário seleciona quais estados quer extrair.
        estados = {'Todos' : 'all',
                            'Rondônia' : 11,
                            'Acre' : 12,
                            'Amazonas' : 13,
                            'Roraima' : 14,
                            'Pará' : 15,
                            'Amapá' : 16,
                            'Tocantins' : 17,
                            'Maranhão' : 21,
                            'Piauí' : 22,
                            'Ceará' : 23,
                            'Rio Grande do Norte' : 24,
                            'Paraíba' : 25,
                            'Pernambuco' : 26 ,
                            'Alagoas' : 27,
                            'Sergipe' : 28,
                            'Bahia' : 29,
                            'Minas Gerais' : 31,
                            'Espírito Santo' : 32,
                            'Rio de Janeiro' : 33,
                            'São Paulo' : 35,
                            'Paraná' : 41,
                            'Santa Catarina' : 42,
                            'Rio Grande do Sul' : 43, 
                            'Mato Grosso do Sul' : 50,
                            'Mato Grosso' : 51,
                            'Goiás' : 52,
                            'Distrito Federal' : 53}

        
        print(f"Lista de estados:")
        for chave,valor in estados.items():
            print(f"{chave}")
        print(f"Digite 0 para sair.\n","-------------------------------\n")


        lista_estados = []
        while True:
            
            op = input('Informe um estado para selecionar pelo nome:',)
            if op == '0':
                 break
            elif op in estados.keys():
                lista_estados.append(estados[op])
                continue    
            else:
                 print("Opção inválida.")
                 continue

        # Constroi a string com os estados
        if len(lista_estados) > 1:
            estados_url = estados[lista_estados[0]]
            index = len(lista_estados) 
            for item in range(1,index,1):
                estados_url += "," + estados[lista_estados[item]]
        else:
             estados_url = lista_estados[0]
        
        # url é montada
        url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104|202201|202202|202203|202204|202301|202302|202303|202304|202401|202402|202403|202404|202501|202502|202503|202504|202601|202602/variaveis/{taxa}?localidades=N3[{estados_url}]&classificacao=2[all]"
        print(url)
        response = requests.get(url)
        data = response.json()
        return data

    def extract_collection_from_mongo(self, db_name, collection_name):
        mongo_url = os.getenv("MONGO_URL")
        client = MongoClient(mongo_url,server_api= ServerApi('1'))
        db = client["dados_ibge"]
        data = db["dados_ibge"]
        data = list(data.find())
        return data
        

