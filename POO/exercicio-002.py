from rich.traceback import install
install()

class Churrasco:

    def __init__(self, qtd_pessoas: int, item: list[str], qtd: list[int], medida: list[str], valor: list[float]):
        self.qtd_pessoas = qtd_pessoas
        self.item = item
        self.qtd = qtd
        self.medida = medida
        self.valor = valor

    # custo total de todos os itens
    def custo_total(self):
        valor_total = float()
        for i in range(len(self.qtd)):
            valor_total += self.qtd[i] * self.valor[i]
        return valor_total
    
    # custo total por pessoa
    def custo_pessoa(self):
        return  self.custo_total() / self.qtd_pessoas

festa = Churrasco(
    6, 
    ['Refri', 'Carne', 'Copos'], 
    [2, 2, 6], 
    ['unidade', 'kilo', 'unidade'],
    [10.99, 48.98, 0.54]
)

print(festa.custo_total())
print(festa.custo_pessoa())