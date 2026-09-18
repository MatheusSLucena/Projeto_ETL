import pandas

#Pega algum tipo de dado e transforma em outro
class Transform:    

    def __init__(self):
        pass

    def transform_pnadc(self,data):
        # Navega pela resposta Json, encontra a série de tempo e faz uma tabela do pandas com o resultado
        serie = data[1]['resultados'][0]['series'][0]['serie']
        df = pandas.DataFrame.from_dict(serie, orient='index',columns=['valor'])
        df.index.name = 'periodo'
        df = df.reset_index()

        # Transforma a coluna temporal em um formato útil, transforma o resultado em uma série temporal e retorna
        # O resultado total em formato de DataFrame pronto pro SQLite
        df['valor'] = df['valor'].replace('...','0')
        df['valor'] = df['valor'].astype(float)
        df['periodo']=df['periodo'].astype(str)
        df['ano'] = df['periodo'].str[:4]
        df['tri'] = df['periodo'].str[-1:]
        df['periodo'] = pandas.PeriodIndex(df['ano']+'Q'+df['tri'], freq='Q')
        df['periodo'] = df['periodo'].dt.to_timestamp()
        return df