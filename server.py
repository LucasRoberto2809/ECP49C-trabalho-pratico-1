import socket
import bd

class CRUD:
    def __init__(self):
        self.banco = bd.Banco()
        self.escutador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.escutador.bind(('',50000))

    def esperarConexao(self):
        self.escutador.listen(1)
        socket_cliente, dados_cliente = self.escutador.accept()
        self.processarPedidos(socket_cliente)
    
    def adicionar(self, album, banda, ano,review, nota):
        id = self.banco.adicionar(album, banda, ano,review, nota)
        return id
    
    def ler_tudo(self):
        print(self.banco.retorna_tudo())

    def modificar(self, album, review, nota):
        id = self.banco.modificar(album, review, nota)

    def envia_msg(self, socket_cliente:socket.socket, conteudo):
        # lista tuplas: id, album, banda, ano, review, nota
        num_linhas = len(conteudo)
        msg = num_linhas.to_bytes(1, 'big')
        id =  socket_cliente.send(msg)
        #for linhas in conteudo:
           # print(linhas)
        for linhas in conteudo:
            # para criar a mensagem o id é ignorado
            msg = (len(linhas[1].encode()).to_bytes(1, 'big') + linhas[1].encode()
                + len(linhas[2].encode()).to_bytes(1, 'big') + linhas[2].encode()
                + linhas[3].encode()
                + len(linhas[4].encode()).to_bytes(1, 'big') + linhas[4].encode()
                + linhas[5].to_bytes(1, 'big'))
            id =  socket_cliente.send(msg)
    
    def busca_banda(self, banda: str):
       return self.banco.busca_por_banda(banda)

    def busca_album(self, album: str):
        return self.banco.busca_por_album(album)
    
    def remover(self, album: str) -> int:
        return self.banco.deleta(album)

    def processarPedidos(self, socket_cliente:socket.socket):
        cliente_conectado = True
        while cliente_conectado:
            opcode = socket_cliente.recv(1)
            if not opcode:
                cliente_conectado = False
            else:
                opcode = int.from_bytes(opcode, 'big')
                match opcode:
                    case 1:
                        tam_album = socket_cliente.recv(1)
                        tam_album = int.from_bytes(tam_album, 'big')
                        album = socket_cliente.recv(tam_album).decode()

                        tam_banda = socket_cliente.recv(1)
                        tam_banda = int.from_bytes(tam_banda, 'big')
                        banda = socket_cliente.recv(tam_banda).decode()

                        ano = socket_cliente.recv(4).decode()

                        tam_review = socket_cliente.recv(1)
                        tam_review = int.from_bytes(tam_review, 'big')
                        review = socket_cliente.recv(tam_review).decode()

                        nota = socket_cliente.recv(1)
                        nota = int.from_bytes(nota, 'big')

                        self.adicionar(album, banda, ano, review, nota)
                    
                    case 2:
                        cod_opc = int.from_bytes(socket_cliente.recv(1), 'big')
                        print(f"Codigo: {cod_opc}")
                        if cod_opc == 1: # retorna tudo
                            conteudo = self.banco.retorna_tudo() 
                            self.envia_msg(socket_cliente, conteudo)
    
                        elif cod_opc == 2: # busca por banda
                            tam_banda = int.from_bytes(socket_cliente.recv(1), 'big')
                            banda = socket_cliente.recv(tam_banda).decode()
                            conteudo = self.busca_banda(banda)
                            self.envia_msg(socket_cliente, conteudo)
                            
                        else: # busca por album
                            tam_album = int.from_bytes(socket_cliente.recv(1), 'big')
                            album = socket_cliente.recv(tam_album).decode()
                            conteudo = self.busca_album(album)
                            self.envia_msg(socket_cliente, conteudo)
                        print("Busca realizada com sucesso")

                    case 3:
                        tam_album = socket_cliente.recv(1)
                        tam_album = int.from_bytes(tam_album, 'big')
                        album = socket_cliente.recv(tam_album).decode()

                        tam_review = socket_cliente.recv(1)
                        tam_review = int.from_bytes(tam_review, 'big')
                        review = socket_cliente.recv(tam_review).decode()

                        nota = socket_cliente.recv(1)
                        nota = int.from_bytes(nota, 'big')
                        
                        self.modificar(album, review, nota)

                    case 4:
                        tam_album = int.from_bytes(socket_cliente.recv(1), 'big')
                        album = socket_cliente.recv(tam_album).decode()
                        # envia resposta da operação para cliente
                        resp = self.remover(album)
                        msg = resp.to_bytes(1, 'big')
                        socket_cliente.send(msg)

def main():
    c = CRUD()
    while True:
        c.esperarConexao()

if __name__ == '__main__':
    main()