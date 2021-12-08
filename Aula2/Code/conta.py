class Conta:
    #
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))

    def transfere(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor


c1 = Conta(123,'fulano',1000, 500)
c2 = Conta(456,'ciclano',1200, 100)

print(c1.saldo)
print(c2.saldo)
c1.transfere(c2,100)
print(c1.saldo)
print(c2.saldo)