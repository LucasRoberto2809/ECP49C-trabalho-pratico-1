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
cliente.connect(('127.0.0.1',50000))

opcao = None
while opcao != 0:
    opcao = int(input(f'Digite um numero'))