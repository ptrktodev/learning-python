class ContaBancaria:
    '''
    Classe que representa uma conta bancária simples.

    Atributos:
        titular (str): nome do titular da conta.
        saldo (float): saldo atual da conta.

    Métodos:
        consultar_saldo(): retorna o saldo atual formatado.
        sacar_valor(valor): realiza um saque, se houver saldo suficiente.
        transferir(valor, destinatario): transfere um valor para outra conta.
    '''
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = float(saldo)

    def consultar_saldo(self) -> str:
        return f'O saldo atual é de R$ {self.saldo:.2f}'
    
    def sacar(self, valor: float | int) -> str:
        if valor < 0:
            return f"Valor inserido é negativo."
        else: 
            if self.saldo > 0 and self.saldo >= valor:
                self.saldo -= valor
                return f"{self.titular} sacou R$ {valor:.2f} e o saldo atual é de R$ {self.saldo:.2f}"
            else:
                return f"Saldo insuficiente para sacar R$ {valor:.2f}"
    
    def transferir(self, valor: float | int, destinatario: str) -> str:
        
        if self.saldo > 0 and self.saldo >= valor:
            self.saldo -= valor
            return f"O valor de R$ {valor:.2f} foi transferido para {destinatario}. O seu saldo atual é de R$ {self.saldo:.2f}"
        else: 
            return f"Saldo insuficiente para a transferência de R$ {valor:.2f}"
    
    def depositar(self, valor: float | int) -> str:
        self.saldo += valor
        return f'O valor de R$ {valor:.2f} foi depositado e o saldo atual é de R$ {self.saldo:.2f}'
        

conta01 = ContaBancaria('Patrick', 500)

print(conta01.__dict__)
print(conta01.consultar_saldo())
print(conta01.sacar(-50))
print(conta01.sacar(460))
print(conta01.transferir(300, 'Pedro'))
print(conta01.depositar(100))

        