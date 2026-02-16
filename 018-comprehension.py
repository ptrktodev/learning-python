################# LIST  ######################

valores = 1, 2, 3, 4 # tupla

lista_duplica = [x * 2 for x in valores]
lista_triplica_par = [x * 2 for x in valores if x % 2 == 0]

print(lista_triplica_par)

################# DICT  ######################

valores = 1, 2, 3, 4, 5, 6, 7 # tupla

lista = {x: x * 2 for x in valores}
lista = {x: x * x for x in valores if x % 2 != 0}

print(lista)

# mapeamento de dados com filtro
produtos = [
    {'cor': 'branco', 'preco': 15},
    {'cor': 'rosa', 'preco': 120},
    {'cor': 'branco', 'preco': 4},
    {'cor': 'rosa', 'preco': 145},
    {'cor': 'verde', 'preco': 5}    
]

produtos_desconto = [
    {**produto, 'preco': produto['preco'] * 0.90} 
    if produto['preco'] > 20 else {**produto} # ternário
    for produto in produtos 
    if produto['preco'] > 10 # filtro
]

print(*produtos_desconto, sep='\n')