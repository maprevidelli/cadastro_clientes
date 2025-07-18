# Simula consulta em um BD externo
import pymongo
import datetime
from pprint import pprint
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
# Cria o BD:
db = cliente.softorama_database
# Cria uma Collection no BD:
cadastro_coll = db.cadastro

for cadastros in cadastro_coll.find():
    pprint(cadastros)
