try:
    # nome = 'patricik' + 123 # type error
    lista = [0, 1, 2] # IndexError
    #print(lista[4])
    number = int('abc') # ValueError
    print(somatorio) # NameError
    texto = "python".append('!') # AttributeError
except (TypeError, ValueError) as error: # tratando erros individuais
    print('Operação incompatível ou tipo incorreto.')
    print(f"Mensagem do erro: {error}")
    print(f"Nome do erro: {error.__class__.__name__}")
except IndexError:
    print('Índice fora do limite da lista/tupla.')
except (NameError, AttributeError):
    print('Variável ou métodod não existente')
except Exception: # tratando outros erros
    print('Estou tratando todos os tipos de erro ao mesmo tempo')
else:
    print('Execução quando Tr   y for bem sucedido.')
finally:
    print('Isso será executado de qualquer jeito.')