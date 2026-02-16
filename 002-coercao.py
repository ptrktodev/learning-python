# Também conhecido como: Typecasting, Conversão de dados

# string to int / float
number01 = '1'

number02 = int(number01)
number03 = float(number01)

print(type(number02))
print(type(number03))

# verificar se uma string tem conteudo (mesmo que seja vazio)
print(bool('')) # false
print(bool(' ')) # true

# int to str:
print(str(11) + ' avos')