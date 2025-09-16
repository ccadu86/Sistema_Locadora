class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []
    
    def cadastrarCliente(self,cliente):
        self.__clientes.append(cliente)

    def cadastrarItem(self, item):
        self.__itens.append(item)
    
    def listarClientes(self):
        return self.__clientes

    def listarItens(self):
        return self.__itens

locadora_senai = Locadora()

class Item:
    def __init__(self, titulo):
        self.__codigo = len(locadora_senai.listarItens()) + 1
        self.__titulo = titulo
        self.__disponivel = True
    
    def alugar(self):
        self.__disponivel = False

    def devolver(self):
        self.__disponivel = True

    def getCodigo(self):
        return self.__codigo
    
    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel

class Jogo(Item):
    def __init__(self, titulo, plataforma, faixa_etaria):
        super().__init__(titulo=titulo)
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria

    def getPlataforma(self):
        return self.__plataforma
    
    def getFaixa(self):
        return self.__faixa_etaria
    
    
class Filme(Item):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo=titulo)
        self.__genero = genero
        self.__duracao = duracao
    
    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao

class Cliente():
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = []

    def locar(self, item):
        item.alugar()
        self.__itens_locados.append(item)

    def devolver(self, item):
        item.devolver()
        self.__itens_locados.remove(item)

    def listarItens(self):
        return self.__itens_locados

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf