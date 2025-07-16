'''
Cadastro de clientes simples, com simulação de armazenamento de dados em servidor externo para data base
MongoDB

'''
import pymongo
from datetime import datetime
# Link com o Banco de Dados:
cliente = pymongo.MongoClient("mongodb://localhost:27017/")

# usar uma Lista como chaves e depois pedir os valores em um dicionario
lista = ['Nome', 'Sobrenome', 'Data Nascimento', 'Cidade', 'Escolaridade',
'Estado Civil', 'Filhos','Profissão', 'e-mail', 'telefone']
print()

# Declarações:
dictionary = {}
cont = True
data_atual = datetime.now()
# Cria o BD:
db = cliente.softorama_database
# Cria uma Collection no BD:
cadastro_coll = db.cadastro

while cont:
    for chave in lista:
        valor = input(f'Entre com a informação ({chave}): ')
        dictionary[chave] = valor.lower()
    # Inserção de chave fixa e obrigatoria para cada cadastro:
    dictionary["registro"] = data_atual
    print('===' * 10)
    for chave in dictionary:
        print(f'{chave}: {dictionary[chave]}')
    # Adiciona o cadastro na collection do BD:
    cadastro_coll.insert_one(dictionary)
    opcao = input('Deseja cadastrar outro cliente? [s/n]: ')
    if opcao == 's':
        cont = True
    else:
        break
print('Fim do Cadastro!')

