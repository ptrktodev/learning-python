from rich.traceback import install
install()

class Animal:
    def __init__(self, nome, cor, peso, cont: list[str]):
        self.nome = nome
        self.cor = cor
        self.peso = peso
        self.continente = cont

    # representação do objeto de modo amigável
    def __str__(self):
        return f"{self.nome} e da cor {self.cor}"
    
    # permite o uso do len() direto no objeto
    def __len__(self):
        return len(self.nome)
    
    def __add__(self, other):
        return self.peso + other.peso
    
    def __getitem__(self, index):
        return self.continente[index]
    

cobra = Animal('Mamba Negra', 'Preto', 5, ['África'])   
elefante = Animal('Elefante', 'Cinza', 500, ['África', 'Ásia'])

print(len(cobra)) # obtem o lenght da prpriedade que eu defini 
print(cobra + elefante) # somando as propriedades que eu defini tbm
print(cobra[-1]) # iterando sobre a propriedade que é lista (porque eu defini)
print(cobra.__dir__()) # retorna atributos e métodos
print('--' * 10)
print(cobra.__dict__) # retorna os atributos com seus valores
print(elefante.__dict__) # retorna os atributos com seus valores