nome = 'Patrick silva'

print('a' in nome)  # Verifica se a letra 'a' está presente na string
print('z' not in nome)  # Verifica se a letra 'z' está presente na string

# string iteravel e fatiamento

print(nome[-1])  # Acessa o último caractere da string
print(nome[0:8])  # Acessa os caracteres do índice 0 ao 7
print(nome[0:8:2])  # Acessa os caracteres do índice 0 ao 7, pulando de 2 em 2
print(nome[:8])  # Acessa os caracteres do início até o índice 7
print(nome[8:])  # Acessa os caracteres do índice 8 até o final
print(nome[::1])  # Acessa todos os caracteres, pulando de 1 em 1
print(nome[::2])  # Acessa todos os caracteres, pulando de 1 em 1
print(nome[::-1])  # Acessa todos os caracteres de trás para frente

print(len(nome) - 1)