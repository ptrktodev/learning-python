# *args é uma tupla que aceita quantos argumentos forem passados para a função. 

def duplica(*args):
    return sum(args) * 2

print(duplica(1, 2, 4, 7))

def hobbies(*args):
    my_hobbies = ', '.join(args)
    return f'Eu gosto de {my_hobbies}.'

print(hobbies('futebol', 'música', 'filmes'))