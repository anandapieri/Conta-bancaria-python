class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.__saldo = saldo
        self.__historico_transacoes = []

    def depositar(self, valor):
        if valor <= 0:
            return False
        
        self.__saldo += valor
        self.__historico_transacoes.append(f'Depósito: +{valor:.2f}')
        return True
    
    def sacar(self, valor):
        if valor <= 0:
            return False
        elif valor > self.__saldo:
            self.__historico_transacoes.append(f'Tentativa de saque no valor de R${valor:.2f} não efetuada, devido a saldo insuficiente.')
            return False
        else:
            self.__saldo -= valor
            self.__historico_transacoes.append(f'Saque: -{valor:.2f}')
            return True
    
    def exibir_saldo(self):
        return f'Seu saldo atual é: R${self.__saldo:.2f}'
    
    def exibir_extrato(self):
        return self.__historico_transacoes

if __name__ == '__main__':
    conta_ananda = ContaBancaria('Ananda', 1000.90)
    conta_ananda.exibir_saldo()
    #conta_ananda.depositar(250)
    #conta_ananda.sacar(2000)
    #conta_ananda.exibir_saldo()
    #conta_ananda.exibir_extrato()