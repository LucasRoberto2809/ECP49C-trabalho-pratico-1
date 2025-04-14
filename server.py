import socket
import bd

class CRUD:
    def __init__(self):
        self.banco = bd.Banco()
        self.escutador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.escutador.bind(('',50001))

    def esperarConexao(self):
        self.escutador.listen(1)
        socket_cliente, dados_cliente = self.escutador.accept()
        self.processarPedidos(socket_cliente)
    
    def adicionar(self, album, banda, ano,review, nota):
        id = self.banco.adicionar(album, banda, ano,review, nota)
        return id
    
    def ler_tudo(self):
        print(self.banco.retorna_tudo())

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
                        self.ler_tudo()


def main():
    c = CRUD()
    while True:
        c.esperarConexao()

if __name__ == '__main__':
    main()