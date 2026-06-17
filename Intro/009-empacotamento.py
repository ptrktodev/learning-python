x, y, *resto = 1, 2, 3, 4, 5, 6, 7

def soma(*nums):
    print(nums)
    total = 0
    for numero in nums:
        total += numero
    return total

print(sum(resto))
# print(soma(resto)) # errado, soma recebe uma tupla como único argumento
print(soma(*resto)) # correto, desempacota a tupla em vários argumentos
print(soma(1, 3, 4, 5))

# print(sum(1, 2, 3, 4, 5, 6, 7)) # errado, sum recebe um iterável como único argumento
print(sum((1, 2, 3))) # correto, um iteravel (tupla, lista, conjunto, etc)


def multiplica(*valores):
    total = 1
    for numero in valores:
        total *= numero
    return total

print("-----" * 3)
valores_aqui = [1, 2, 3, 4, 5]
print(multiplica(*valores_aqui))