class Livro:

    def __init__(self, livro, total_paginas, pag_atual):
        self.livro = livro
        self.total_paginas = total_paginas
        self.pag_atual = pag_atual

    def passar_pagina(self, qtd = 0):
        if qtd > 0:
            self.pag_atual += qtd
            return f"Você já leu {self.pag_atual} páginas. Falta mais {self.total_paginas - self.pag_atual} páginas para completar o livro inteiro."
        else: 
            return 'Informe quantas páginas você leu.'


livro = Livro('Casa Mágica', 200, 50)

print(livro.passar_pagina(2))
print(livro.passar_pagina(2))
print(livro.passar_pagina(10))
print(livro.passar_pagina(1))
print(livro.passar_pagina(0))
print(livro.passar_pagina())