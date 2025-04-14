import sqlite3

class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect("teste.db")
        cursor = self.conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS teste(id INTEGER PRIMARY KEY, album, banda, ano, review, nota)")
        self.conexao.commit()
        cursor.close()

    def adicionar(self, album, banda, ano, review, nota):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO teste(album, banda, ano, review, nota) VALUES(?,?,?,?,?)', (album, banda, ano, review, nota))
        if(cursor.rowcount > 0):
            id = cursor.lastrowid
        else:
            id = None
        self.conexao.commit()
        cursor.close()
        return id

    def retorna_tudo(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM teste')
        retorno = cursor.fetchall()
        cursor.close()
        return retorno
