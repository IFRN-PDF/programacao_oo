class Teste:
    def __init__(self, nome):
         self.__nome = nome

    @property
    def nome(self):
         # Este código é executado quando alguém for
         # ler o valor de self.nome
         return self.__nome

    @nome.setter
    def nome(self, value):
         # este código é executado sempre que alguém fizer 
         # self.nome = value
         self.__nome = value

t = Teste('nome1')
n = t.nome
print(n)
n = t.nome = 'nome2'
print(n)