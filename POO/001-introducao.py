from rich.traceback import install # view de erro amigável no terminal
from rich import inspect # inspecionar a classe ou objeto
install()

# Declaração de Classes
class Funcionario:
    '''
    Classe que representa um funcionario.
    '''

    # Atributos de Classe
    empresa: str = 'Grupo DSB'
    subempresas: dict = {
        'principal': 'Data Science Brigade',
        'fabrica': 'F22 Tech Factory',
        'labs': 'DSB Labs',
    }
    localizacao: str = 'Av. Praia de Belas, 1212 - Sala: 1619'
    ANO_ATUAL: int = 2026

    # Atributos de instâncias 
    def __init__(self, nome: str, idade: int, anos_empresa: int, cargo: str):
        self.nome = nome            
        self.idade = idade  
        self.tempo_empresa = anos_empresa                 
        self.cargo = cargo         

    # Métodos de Instância
    def apresentacao_funcionario(self) -> str:
        '''retorna a apresenção de funcionári'''            
        return f'Olá, eu me chamo {self.nome} e tenho {self.idade} anos. Trabalho no {Funcionario.empresa} há {self.tempo_empresa} anos como {self.cargo}.'

    def ano_nascimento(self) -> int:
        '''retorna o ano de nascimento'''
        return Funcionario.ANO_ATUAL - self.idade

    # Métodos de Classe
    @classmethod
    def apresentacao_empresa(cls): # self aqui nao funciona
        '''retorna a apresenção da empresa'''
        return f'O {cls.empresa} trabalha há mais de 8 anos com desenvolvimento de projetos e produtos de ciência de dados e inteligência artificial.'

    @classmethod
    def criar_zerado(cls):
        '''retorna a criação de atributos de instâncias zerados'''
        return cls('Desconhecido', 0, 0, 'Desconhecido') # é igual a isso -> Conta('Desconhecido', 0, 0, 'Desconhecido')

dados1 = ['Patrick', 23, 2, 'Assistente']
dados2 = {'nome': 'Pedro', 'idade': 26, 'anos_empresa': 3, 'cargo': 'Gerente'} # chave = atributo de instância

# desempacotamento e criação de instâncias
patrick = Funcionario(*dados1)
pedro = Funcionario(**dados2)

# criação de instância zerada
funcio_desc = Funcionario.criar_zerado()

print(f"-> {patrick.apresentacao_funcionario()}") # instância
print(f"-> {Funcionario.apresentacao_empresa()}") # classe
print(f"-> {patrick.ano_nascimento()}")
print(f"-> {patrick.localizacao}") # acessar atributos de classe via objeto0
inspect(pedro)
del patrick.cargo
inspect(pedro)


