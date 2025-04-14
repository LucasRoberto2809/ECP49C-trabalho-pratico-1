import sqlite3

class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect("teste.db")
        cursor = self.conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS teste(id INTEGER PRIMARY KEY, nome, idade, endereco, cep)")
        self.conexao.commit()
        cursor.close()