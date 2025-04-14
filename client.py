import socket

"""
1 - create
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

4 -
pelo album
"""


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1',50001))

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

            cliente.send(msg)

        case 5:
            opcao = 0
            break

            
            
