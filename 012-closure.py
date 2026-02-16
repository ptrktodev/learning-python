# Closure é quando uma função lembra do contexto em que foi criada, mesmo depois desse contexto ter “acabado”.

def multiplicador(n):
    def multiplica(*nums):
        return [numero * n for numero in nums]
    return multiplica

dobro_de_lista = multiplicador(2) # fabrica de comportamentos

print(dobro_de_lista(1, 5, 10))


# Uma função que retorna outra função é chamada de função de ordem superior,
# e a função interna é chamada de função aninhada. O fechamento ocorre quando
# a função aninhada se lembra do ambiente em que foi criada, mesmo depois que 
# a função externa tenha terminado de executar. Isso é Closure.