st1 = set('Patrick') # imprime sem ordem, sem repetição
st2 = {1, 2, 3, 4, 5} # imprime na ordem
st3 = {'str', 1, 'teste', 2, 3, 4} # segue a ordem: int, str
st4 = set([1, 2, 3, 4]) # imprime na ordem
st5 = {1, 2, 2, 2, 7, 8, 8, 10} # imprime na ordem, sem repetição 

print()
for x in st4:
    print(x)


frutas = {'maçã', 'banana'}
frutas.add('laranja')
# {'maçã', 'banana', 'laranja'}

frutas.remove('banana')  # Gera erro se não existir
frutas.discard('uva')    # Não gera erro se não existir

set1 = {1, 2, 3}
set2 = {3, 4, 5}
resultado = set1.union(set2)  # ou set1 | set2
# {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
comum = set1.intersection(set2)  # ou set1 & set2
# {2, 3}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
diferenca = set1.difference(set2)  # ou set1 - set2
# {1, 2}
