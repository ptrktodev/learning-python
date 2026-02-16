def saudacao(*args): 
    return sum(args)

saudar = saudacao

def secundaria(funcao, *args):
    return funcao(*args) 

print(secundaria(saudar, 1, 2, 3, 4, 5))