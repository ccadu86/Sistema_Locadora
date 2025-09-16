from classes import *
import os

def menu():
    print("--BEM VINDO A LOCADORA--")
    print("1 - CADASTRAR CLIENTE")
    print("2 - CADASTRAR FILME")
    print("3 - CADASTRAR JOGO")
    print("4 - LISTAR ITENS")
    print("5 - LISTAR CLIENTES")
    print("6 - ALUGAR ITEM")
    print("7 - DEVOLVER ITEM")
    print("0 - SAIR")
    escolha = int(input("--> "))
    return escolha

def cadastrar_cliente():
    os.system("cls")
    print("--CADASTRO DE CLIENTE--")
    nome = input("Informe seu nome\n--> ")
    cpf = int(input("Informe seu CPF\n--> "))
    cliente = Cliente(nome=nome, cpf=cpf)
    locadora_senai.cadastrarCliente(cliente)
    print("CLIENTE CADASTRADO COM SUCESSO")
    os.system("pause")

def cadastrar_filme():
    os.system("cls")
    print("--CADASTRO DE FILME--")
    titulo = input("Informe o titulo do filme\n--> ")
    genero = input("Informe o genero do filme\n--> ")
    duracao = int(input("Informe a duração do filme\n--> "))
    filme = Filme(titulo=titulo, genero=genero, duracao=duracao)
    locadora_senai.cadastrarItem(filme)
    print("FILME CADASTRADO COM SUCESSO")
    os.system("pause")

def cadastrar_jogo():
    os.system("cls")
    print("--CADASTRO DE JOGO--")
    titulo = input("Informe o titulo do jogo\n--> ")
    plataforma = input("Informe a plataforma do jogo\n--> ")
    faixa = int(input("Informe a faixa etaria do jogo\n--> "))
    jogo = Jogo(titulo=titulo, plataforma=plataforma, faixa_etaria=faixa)
    locadora_senai.cadastrarItem(jogo)
    print("JOGO CADASTRADO COM SUCESSO")
    os.system("pause")

def listar_itens():
    os.system("cls")
    print("--LISTA DE ITENS--")
    for itens in locadora_senai.listarItens():
        try:
            itens.getPlataforma()
            print("Tipo : JOGO")
        except:
             print("Tipo : FILME")

        print(f"Codigo: {itens.getCodigo()}")
        print(f"Titulo: {itens.getTitulo()}")
        if itens.getDisponivel() == True:
            print(f"Disponivel: Disponivel para locação")
        else:
            print(f"Disponivel: Indisponivel para locação")
           
        try:
            print(f"Plataforma: {itens.getPlataforma()}")
            print(f"Faixa Etaria: {itens.getFaixa()}")
        except:
            print(f"Genero: {itens.getGenero()}")
            print(f"Duração: {itens.getDuracao()}")
        print("-------------------------------------\n")
    os.system("pause")

def listar_clientes():
    os.system("cls")
    print("--LISTA DE CLIENTES--")
    for cliente in locadora_senai.listarClientes():
        print(f"Nome: {cliente.getNome()}")
        print(f"CPF: {cliente.getCpf()}")
        if len(cliente.listarItens()) != 0:
            print(f"\nITENS LOCADOS")
            for itens in cliente.listarItens():
                try:
                    itens.getPlataforma()
                    print("Tipo : JOGO")
                except:
                    print("Tipo : FILME")

                print(f"Codigo: {itens.getCodigo()}")
                print(f"Titulo: {itens.getTitulo()}")
                
                try:
                    print(f"Plataforma: {itens.getPlataforma()}")
                    print(f"Faixa Etaria: {itens.getFaixa()}")
                except:
                    print(f"Genero: {itens.getGenero()}")
                    print(f"Duração: {itens.getDuracao()}")
                print("-------------------------------------\n")
        else:
            print("\nNENHUM ITEM LOCADO")    
        print("\n-------------------------------------\n")
    os.system("pause")

def alugar_itens():
    os.system("cls")
    listar_itens()
    item = int(input("Informe o ID do item\n--> "))

    if item <= len(locadora_senai.listarItens()):
        os.system("cls")
        listar_clientes()

        cliente = int(input("Informe o CPF do cliente\n--> "))
        for clie in locadora_senai.listarClientes():
            if cliente == clie.getCpf():
                clie.locar(locadora_senai.listarItens()[item - 1])
                print("ITEM LOCADO COM SUCESSO")
                break
        else:
            print("CLIENTE INVALIDO")    
    else:
        print("CODIGO INVALIDO")
    os.system("pause")

def devolver_itens():
    os.system("cls")
    listar_clientes()

    cliente = int(input("Infome o CPF do Cliente\n--> "))

    for clie in locadora_senai.listarClientes():
        if cliente == clie.getCpf():
            cont = 0
            if len(clie.listarItens()) != 0:
                for itens in clie.listarItens():
                    cont += 1
                    print(f"Produto locado {cont}")
                    try:
                        itens.getPlataforma()
                        print("Tipo : JOGO")
                    except:
                        print("Tipo : FILME")

                    print(f"Codigo: {itens.getCodigo()}")
                    print(f"Titulo: {itens.getTitulo()}")
                    if itens.getDisponivel() == True:
                        print(f"Disponivel: Disponivel para locação")
                    else:
                        print(f"Disponivel: Indisponivel para locação")
                    
                    try:
                        print(f"Plataforma: {itens.getPlataforma()}")
                        print(f"Faixa Etaria: {itens.getFaixa()}")
                    except:
                        print(f"Genero: {itens.getGenero()}")
                        print(f"Duração: {itens.getDuracao()}")
                    print("-------------------------------------\n")
                
                devolucao = int(input("Informe o valor da locação que deseja devolver\n--> "))

                clie.devolver(clie.listarItens()[devolucao - 1])
                print("ITEM DEVOLVIDO COM SUCESSO")
            else:
                print("NENHUM ITEM ALUGADO")
    os.system('pause')       