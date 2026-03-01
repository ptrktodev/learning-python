import sys

iterator = [n for n in range(999)]
generator = (n for n in range(999))

print(f'tamanho em bytes na memoria: {sys.getsizeof(iterator)}') 
print(f'tamanho em bytes na memoria: {sys.getsizeof(generator)}') 

print(iterator[-1]) # vc pode iterar sobre ele

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

def generator_fun():
    yield 1 # stop na funcao
    yield 2
    yield 3
    yield 4

funcao = generator_fun()

print(f'Funcao geradora: {next(funcao)}')
print(f'Funcao geradora: {next(funcao)}')


for x in funcao:
    print(x)


def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6

g = gen2(gen1)

print(next(g)) # 1
print(next(g)) # 2

for x in g:
    print(x)
