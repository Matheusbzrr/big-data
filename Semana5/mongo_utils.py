from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

class GerenciadorMongo:
    def __init__(self, uri=None):
        self.uri = uri or os.getenv("URL")
        self.cliente = MongoClient(self.uri, server_api=ServerApi('1'))

    def ref_db(self, db_nome):
        return self.cliente[db_nome]

    def listar_bancos(self):
        return self.cliente.list_database_names()

    def listar_colecoes(self, db_nome):
        db = self.ref_db(db_nome)
        return db.list_collection_names()

    def adicionar_colecao(self, nome_colecao, db_nome):
        db = self.ref_db(db_nome)
        if nome_colecao in db.list_collection_names():
            print(f"A coleção '{nome_colecao}' já existe no banco '{db_nome}'.")
            return db[nome_colecao]
        else:
            colecao = db.create_collection(nome_colecao)
            print(f"Coleção '{nome_colecao}' criada com sucesso no banco '{db_nome}'!")
            return colecao
