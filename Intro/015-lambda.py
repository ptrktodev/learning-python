# list comprehension

triplica = lambda x: x * 3 # funcao 1
ox = lambda x: 'par' if x % 2 == 0 else 'impar' # funcao 2

print(triplica(10))
print(ox(5))

valores = 12, 30, 50 # tupla
print(list(map(lambda x: x / 2, valores)))