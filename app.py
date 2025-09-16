from funcoes import *
import os

while True:
    os.system("cls")
    match menu():
        case 1:
            cadastrar_cliente()
        case 2:
            cadastrar_filme()
        case 3:
            cadastrar_jogo()
        case 4:
            listar_itens()
        case 5:
            listar_clientes()
        case 6:
            alugar_itens()
        case 7:
            devolver_itens()
        case 0:
            break
        case _:
            print("OPÇÃO INVALIDA")
            os.system('pause')