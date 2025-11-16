import pymongo

def conectar():
    cliente = pymongo.MongoClient("mongodb://localhost:27017/")
    banco = cliente["sistema_gestao"]
    return banco

def pegar_colecao(nome):
    banco = conectar()
    return banco[nome]