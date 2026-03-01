from typing import Any

nome: str = 'peixe'
idade: int = 23
altura: float = 1.67
is_masc: bool = True
 
# Constantes
# Essa constante não costuma ser reatribuída, então a tipagem é redundante.
# O próprio valor já deixa claro que é uma string.
CONSTANTE = "valor constante"

# Coleções
hobb1: list[str] = ['assisitr esportes', 'aulas de ingles', 'ficar com a namorada', 'jogar video game']
hobb2: list[Any] = ['correr', 123, ['str', 'int'], True] # pra definir qualquer tipo dentro da lista
hobb3: list[str | int | bool] = ['correr', 123, True] # pra definir quais tipos são permitidos
tupla1: tuple[str, int] = 'patrick', 23
tupla2: tuple[str, ...] = 'patrick', '23', 'teste'
set_int: set[int] = {2, 4, 5, 7}
dict_hobbie: dict[str, int] = {'chave1': 1, 'chave2': 2}
range: range = range(10)

# Outros tipos
nada: None = None  # Representa ausência de valor
qualquer_coisa: object = 123  # Pode ser qualquer objeto
tipo: type[str] = str  # Referência ao tipo 'str' em si (não uma string)