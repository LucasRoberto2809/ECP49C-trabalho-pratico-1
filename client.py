import socket

"""
1 - Create
Album - char ate 255
Banda - char ate 255
Ano - char 4
Review - char ate 500
Nota - char 1

2 - Read
1 - retorna tudo prioridade
2 - por banda
3 - album

3 - Update 
Review 
Nota

4 - Delete
pelo album
"""


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1',50000))

opcao = None
while opcao != 0:
    print(f'Entre com a operacao desejada\n 1 - Criar registro\n 2 - Ler registro\n 3 - Alterar registro\n 4- Deletar registro\n 5 - Sair')
    opcao = int(input())
    match opcao:
        case 1:  
            album = input('Entre com o nome do album ')
            banda = input('Entre o nome da banda ')
            ano = input('Entre o ano de lancamento do album ')
            review = input('Entre com sua review ')
            nota = int(input('Entre com sua nota (0 a 5) '))
            while (nota < 0  or nota > 5):
                nota = int(input('Entre com sua nota (0 a 5) '))
            msg = opcao.to_bytes(1, 'big')
            msg = msg + len(album.encode()).to_bytes(1, 'big') + album.encode()
            msg = msg + len(banda.encode()).to_bytes(1, 'big') + banda.encode()
            msg = msg + ano.encode()
            msg = msg + len(review.encode()).to_bytes(1, 'big') + review.encode()
            msg = msg + nota.to_bytes(1, 'big')

            id = cliente.send(msg)
            print(id)

        case 2:
            cod_opc = 0
            while cod_opc>3 or cod_opc<=0:
                print("Digite 1 para retornar tudo\n" \
                "Digite 2 para buscar por banda\n" \
                "Digite 3 para buscar por album")
                cod_opc = int(input())
            busca = ""
            if cod_opc == 2:
                busca = input('Digite a banda ')
            if cod_opc == 3:
                busca = input('Digite o album ')
            msg = (opcao.to_bytes(1,'big') 
                   + cod_opc.to_bytes(1,'big') 
                   + len(busca.encode()).to_bytes(1, 'big') + busca.encode())
            cliente.send(msg)
            #linhas = cliente.recv(1)
            linhas = int.from_bytes(cliente.recv(1),'big')
            #print(f"Numero de linhas: {linhas}")
            if linhas==0:
                print("Nenhum resultado encontrado\n")
            else:
                for _ in range(linhas):
                    tam_album = int.from_bytes(cliente.recv(1), 'big')
                    album = cliente.recv(tam_album).decode()

                    tam_banda = int.from_bytes(cliente.recv(1), 'big')
                    banda = cliente.recv(tam_banda).decode()

                    ano = cliente.recv(4).decode()

                    tam_review = int.from_bytes(cliente.recv(1), 'big')
                    review = cliente.recv(tam_review).decode()

                    nota = int.from_bytes(cliente.recv(1), 'big')

                    print(f"{album}, {banda}, {ano}, {review}, {nota}")
                
        case 3:
            album = input('Entre com o album que deseja mudar a review ')
            review = input('Entre com a review para modificar ')
            nota = int(input('Entre com a nota para modificar '))

            msg = opcao.to_bytes(1, 'big')
            msg = msg + len(album.encode()).to_bytes(1, 'big') + album.encode()
            msg = msg + len(review.encode()).to_bytes(1, 'big') + review.encode()
            msg = msg + nota.to_bytes(1, 'big')

            cliente.send(msg)

        case 4:
            album = input('Entre com o album que deseja remover ')
            msg = (
                opcao.to_bytes(1, 'big')
                + len(album.encode()).to_bytes(1, 'big') + album.encode()
            )
            cliente.send(msg)
            resp = int.from_bytes(cliente.recv(1), 'big')
            if resp == 0:
                print(f"Nenhum álbum com nome '{album}' encontrado.")
            else:
                print(f"Álbum '{album}' removido com sucesso.")

        case 5:
            opcao = 0
            break

            
            
