meu_dict = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

print(len(meu_dict)) # tamanho 
print(tuple(meu_dict.keys())) # chaves
print(tuple(meu_dict.values())) # valores
meu_dict.setdefault("pais", "Brasil") # adiciona se não existir

print()
for chave, valor in meu_dict.items():
    print(f"{chave}: {valor}")

print()

import copy
d2 = copy.deepcopy(meu_dict) # cópia profunda (manipulações na copia nao afeta o dict original)


print(meu_dict.get("cidade")) # obtem o valor da chave


meu_dict.pop("idade") # remove o item pela chave
meu_dict.popitem() # remove o ultimo item adicionado
meu_dict.update({
    "idade": 30,
    "profissão": "Engenheiro"
}) # atualiza ou adiciona itens

print(meu_dict)