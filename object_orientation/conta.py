

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
        # print(f"deposito de {valor}")

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            # print(f"saque de {valor}")
        else:
            print(f"O valor {valor} passou o limite.")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}




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

# conta2.transfere(10.0, conta1)

# print(conta2.limite)

# conta2.limite = 200000.00

# print(conta2.limite)