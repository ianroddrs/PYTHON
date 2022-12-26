

class Conta:
    
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        #print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor
        print(f"deposito de {valor}")

    def saca(self, valor):
        self.__saldo -= valor
        print(f"saque de {valor}")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite
    
    def get_titular(self):
        return self.__titular

    def set_limite(self, limite):
        self.__limite = limite




conta1 = Conta(123, "nico", 55.5)
conta2 = Conta(321, "marco", 100.0)
conta3 = Conta(221, "silva", 200.0, 3000.0)

# contas = [conta1, conta2, conta3]

# for conta in contas:
#     conta.extrato()
#     conta.deposita(35)
#     conta.saca(100)
#     conta.extrato()
#     print("¨"*25)

# conta1._Conta__saldo = 20
# print(conta1._Conta__saldo)

# conta1.extrato()

conta2.transfere(10.0, conta1)