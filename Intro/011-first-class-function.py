# funcoes que sao tratadas como variaveis

def cumprimenta(nome):
    return f"Olá, {nome}!"

saudacao = cumprimenta  # atribuindo a funcao a uma variavel

print(saudacao("Maria"))  # chamando a funcao via variavel