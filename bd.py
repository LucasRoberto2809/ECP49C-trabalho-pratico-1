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
    
    def modificar(self, album, novo_review, nova_nota):
        cursor = self.conexao.cursor()
        cursor.execute("""
            UPDATE teste
            SET review = ?, nota = ?
            WHERE album = ?
        """, (novo_review, nova_nota, album))
        self.conexao.commit()
        linhas_afetadas = cursor.rowcount
        cursor.close()
        if linhas_afetadas == 0:
            print(f"Nenhum álbum com nome '{album}' encontrado.")
        else:
            print(f"Registro do álbum '{album}' atualizado com sucesso.")
        return linhas_afetadas
    
    def retorna_tudo(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM teste')
        retorno = cursor.fetchall()
        cursor.close()
        return retorno
    
    def busca_por_banda(self, banda: str):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM teste WHERE banda = ?', (banda,))
        retorno = cursor.fetchall()
        cursor.close()
        return retorno
    
    def busca_por_album(self, album: str):
        cursor = self.conexao.cursor()
        # LIKE por case-insensitive 
        cursor.execute('SELECT * FROM teste WHERE album LIKE ?', (f'%{album}%',))
        retorno = cursor.fetchall()
        cursor.close()
        return retorno
    
    def deleta(self, album: str):
        cursor = self.conexao.cursor()
        cursor.execute('DELETE FROM teste WHERE album LIKE ?', (f'%{album}%',))
        self.conexao.commit()
        linhas_afetadas = cursor.rowcount
        cursor.close()
        if linhas_afetadas == 0:
            print(f"Nenhum álbum com nome '{album}' encontrado.")
        else:
            print(f"Album '{album}' removido com sucesso.")
        return linhas_afetadas