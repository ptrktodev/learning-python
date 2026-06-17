# Tipagem em Funções

lista: list[str] = ['patrick', 'rafaela', 'pedro', 'julinha']

def remove_duplicate(items: list[str]) -> list[str]:
    items_cap: list[str] = [x.capitalize() for x in items] 
    to_dict = dict.fromkeys(items_cap)
    return  list(to_dict)

print(remove_duplicate(lista))
print('---' * 5)

nome: str = 'patrick'

def end_string(name: str) -> bool:
    ending: tuple[str, ...] = ('ck', 'ela', 'inda')
    return name.lower().endswith(ending)

print(end_string('patrick'))
print('---' * 5)

from collections.abc import Callable

def somar(x: int, y: float, z: bool)-> None:
    print(z, x, y)

def imprimir(x1: int, y2: float, callback: Callable[[int, float, bool], None])-> float:
    soma = x1 + y2
    callback(x1, y2, True)
    return soma

print(imprimir(2, 5, somar))
print('---' * 5)

def with_args_kwargs(*args: str, **kw: int) -> None:
    print(args)
    for key, value in kw.items():
        print(key, value)

print(with_args_kwargs('ptrk', 'stg', idade=23, altura=167))
