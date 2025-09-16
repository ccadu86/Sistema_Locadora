# 🎬🎮 Sistema de Locadora

Um sistema de gerenciamento de locadora desenvolvido em Python para controle de aluguel de filmes e jogos.

## 📋 Descrição

O **Sistema de Locadora** é uma aplicação console em Python que permite gerenciar uma locadora de filmes e jogos de forma simples e eficiente. O sistema oferece funcionalidades completas para cadastro de clientes, cadastro de itens (filmes e jogos), controle de locações e devoluções.

## ✨ Funcionalidades

- **👥 Gerenciamento de Clientes**
  - Cadastro de novos clientes
  - Listagem de clientes cadastrados
  - Visualização de itens locados por cliente

- **📚 Gerenciamento de Itens**
  - Cadastro de filmes (título, gênero, duração)
  - Cadastro de jogos (título, plataforma, faixa etária)
  - Listagem de todos os itens disponíveis
  - Controle de disponibilidade

- **🔄 Sistema de Locação**
  - Alugar itens para clientes
  - Devolver itens locados
  - Controle automático de disponibilidade

## 🛠️ Requisitos do Sistema

- **Python**: 3.10 ou superior
- **Sistema Operacional**: Windows (utiliza comandos `cls` e `pause`)

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ccadu86/Sistema_Locadora.git
   cd Sistema_Locadora
   ```

2. **Verifique se o Python está instalado:**
   ```bash
   python --version
   ```

3. **Execute a aplicação:**
   ```bash
   python app.py
   ```

## 🚀 Como Usar

### Menu Principal

Ao executar a aplicação, você verá o menu principal:

```
--BEM VINDO A LOCADORA--
1 - CADASTRAR CLIENTE
2 - CADASTRAR FILME
3 - CADASTRAR JOGO
4 - LISTAR ITENS
5 - LISTAR CLIENTES
6 - ALUGAR ITEM
7 - DEVOLVER ITEM
0 - SAIR
```

### Exemplos de Uso

#### 1. Cadastrando um Cliente
- Escolha a opção `1`
- Informe o nome do cliente
- Informe o CPF (apenas números)

#### 2. Cadastrando um Filme
- Escolha a opção `2`
- Informe o título do filme
- Informe o gênero
- Informe a duração em minutos

#### 3. Cadastrando um Jogo
- Escolha a opção `3`
- Informe o título do jogo
- Informe a plataforma (ex: PlayStation, Xbox, PC)
- Informe a faixa etária

#### 4. Alugando um Item
- Escolha a opção `6`
- Selecione o item desejado pelo ID
- Informe o CPF do cliente

#### 5. Devolvendo um Item
- Escolha a opção `7`
- Informe o CPF do cliente
- Selecione o item a ser devolvido

## 🏗️ Estrutura do Projeto

```
Sistema_Locadora/
│
├── app.py          # Arquivo principal da aplicação
├── classes.py      # Definição das classes do sistema
├── funcoes.py      # Funções do sistema
└── README.md       # Documentação do projeto
```

### Arquivos Principais

- **`app.py`**: Ponto de entrada da aplicação, contém o loop principal e controle do menu
- **`classes.py`**: Define as classes principais do sistema:
  - `Locadora`: Gerencia clientes e itens
  - `Item`: Classe base para filmes e jogos
  - `Filme`: Especialização de Item para filmes
  - `Jogo`: Especialização de Item para jogos
  - `Cliente`: Representa os clientes da locadora
- **`funcoes.py`**: Contém todas as funções de interface e operações do sistema

## 🔧 Arquitetura do Sistema

### Classes Principais

#### Locadora
```python
class Locadora:
    - __clientes: list
    - __itens: list
    + cadastrarCliente(cliente)
    + cadastrarItem(item)
    + listarClientes()
    + listarItens()
```

#### Item (Classe Base)
```python
class Item:
    - __codigo: int
    - __titulo: str
    - __disponivel: bool
    + alugar()
    + devolver()
    + getCodigo()
    + getTitulo()
    + getDisponivel()
```

#### Filme (Herda de Item)
```python
class Filme(Item):
    - __genero: str
    - __duracao: int
    + getGenero()
    + getDuracao()
```

#### Jogo (Herda de Item)
```python
class Jogo(Item):
    - __plataforma: str
    - __faixa_etaria: int
    + getPlataforma()
    + getFaixa()
```

#### Cliente
```python
class Cliente:
    - __nome: str
    - __cpf: int
    - __itens_locados: list
    + locar(item)
    + devolver(item)
    + listarItens()
    + getNome()
    + getCpf()
```

## 🎯 Características Técnicas

- **Paradigma**: Programação Orientada a Objetos
- **Padrões**: Herança, Encapsulamento
- **Interface**: Console/Terminal
- **Armazenamento**: Em memória (dados são perdidos ao fechar a aplicação)

## 📝 Notas Importantes

- O sistema atualmente armazena dados apenas em memória
- Todos os dados são perdidos quando a aplicação é fechada
- Os comandos `cls` e `pause` são específicos do Windows
- CPF deve ser informado apenas com números (sem pontos ou hífens)

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

- **ccadu86** - *Desenvolvimento inicial* - [ccadu86](https://github.com/ccadu86)

## 🔮 Melhorias Futuras

- [ ] Persistência de dados em arquivo ou banco de dados
- [ ] Interface gráfica
- [ ] Sistema de autenticação
- [ ] Relatórios de locação
- [ ] Controle de multas por atraso
- [ ] API REST
- [ ] Compatibilidade com Linux/macOS

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!