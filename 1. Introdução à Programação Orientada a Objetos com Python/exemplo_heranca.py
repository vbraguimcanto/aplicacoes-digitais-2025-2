

class Conta:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.saldo -= valor
        print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
    
    def extrato(self):
        print(f"Titular: {self.titular}, Saldo: R${self.saldo}")


class ContaPoupanca(Conta):

    def __init__(self, titular, saldo=0, taxa_juros=0.01):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.depositar(juros)
        print(f"Juros de R${juros} aplicados. Saldo atual: R${self.saldo}")

class ContaCorrente(Conta):

    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)


if __name__ == "__main__":
    conta_poupanca = ContaPoupanca("Carlos", 1000, 0.02)
    conta_corrente = ContaCorrente("Ana", 500)

    conta_poupanca.extrato()
    conta_poupanca.aplicar_juros()
    conta_poupanca.sacar(200)
    conta_poupanca.extrato()

    conta_corrente.extrato()
    conta_corrente.depositar(300)
    conta_corrente.sacar(100)
    conta_corrente.extrato()    