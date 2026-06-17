animal = {"nome": "lobo", "patas": 4}
habitat = {"bioma": "floresta", "clima": "frio"}

# unpacking
(chave1, valor1), b = animal.items()
print(chave1, b)

# unpacking
animal_final = {**animal, **habitat}
print(animal_final)

# packing
def funcao1(**kwargs) -> None:
    for chave, valor in kwargs.items(): # unpacking
        print(chave, valor)

funcao1(**animal_final)

# packing
def funcao2(**kwargs) -> None:
    for chave, valor in kwargs.items(): # unpacking
        print(chave, valor)

funcao2(nome='Patrick', idade=23, cidade='Porto Alegre') # argumentos nomeados

# packing
def funcao2(*args, **kwargs) -> None:
    print(sum(args))
    for chave, valor in kwargs.items(): # unpacking
        print(chave, valor)

funcao2(1, 2, 3, nome='Patrick', idade=23, cidade='Porto Alegre') # argumentos nomeados

