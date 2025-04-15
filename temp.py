# server
case 2:
                        cod_opc = socket_cliente.recv(1)
                        if cod_opc == 1:
                            # SQL retorna tudo
                        elif cod_opc == 2:
                            # SQL busca por banda
                        else:
                            # SQL por album

#client

case 2:
            cod_opc = 0
            while id>3 or id<=0:
                print("Digite 1 retornar tudo\n" \
                "Digite 2 para buscar por banda\n" \
                "Digite 3 para buscar por album")
                cod_opc = int(input())
            msg = opcao.to_bytes(1,'big') + cod_opc.to_bytes(1,'big')
            cliente.send(msg)
            opcode = cliente.recv(1)
            opcode = int.from_bytes(opcode,'big')
            if (opcode == 6):
                print('Não encontrado')
            else:
                linhas = cliente.recv(1)
                for i in range(linhas):
                    tam_album = cliente.recv(1)
                    tam_album = int.from_bytes(tam_album, 'big')
                    album = cliente.recv(tam_album).decode()

                    tam_banda = cliente.recv(1)
                    tam_banda = int.from_bytes(tam_banda, 'big')
                    banda = cliente.recv(tam_banda).decode()

                    ano = cliente.recv(4).decode()

                    tam_review = cliente.recv(1)
                    tam_review = int.from_bytes(tam_review, 'big')
                    review = cliente.recv(tam_review).decode()

                    nota = cliente.recv(1)
                    nota = int.from_bytes(nota, 'big')
                    print(f"{album}, {banda}, {ano}, {review}, {nota}\n")