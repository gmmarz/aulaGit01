import pandas as pd

#Criando um data frame como exemplo.
#Para este utilizei um dicionario
data = {'nome':['João','maria','Pedro','Ana','Carlos'],
        'Idade':[25,30,18,19,35],
        'Cidade':['São Paulo','Rio de Janeiro','Belo Horizonte','São Paulo','São Bernardo']
        }
df = pd.DataFrame(data)
print(f"Data frame original\n {df}, \n------------")

#Exemplo para mostrar a funcionalidade do FOR
pessoas_acima_20 = []
for index, row in df.iterrows():
    if row['Idade'] > 20:
        pessoas_acima_20.append(row)

#Convertendo a lista em um novo dataframe
df_filtrado = pd.DataFrame(pessoas_acima_20)

print(f"Data frame final filtrado\n {df_filtrado}\n----------------")
#--------------------------------------------------------------------------

#Filtrando diretamente com o pandas
df_filtrado2 = df[df['Idade'] >= 30]

print(f'Exemplo filtrando utiliando diretamente o dataframe\n{df_filtrado2}\n---------------')

print('Criando um novo branch para testes')