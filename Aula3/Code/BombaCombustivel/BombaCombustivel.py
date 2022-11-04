'''''
Codigo adaptado de git@github.com:ifpb/intin-poo.git
pip install playsound
'''
from playsound import playsound


class BombaCombustivel:

    def __init__(self, quantidadeCombustivel, tipo, preco):
        self.__quantidadeCombustivel = quantidadeCombustivel
        self.__tipoCombustivel = tipo
        self.__valorLitro = preco

    def abastecerPorValor(self, valor,veiculo):
        # Existe gasolina suficiente na bomba?
        litros = valor / self.__valorLitro
        print("Abastecendo litros: %s" % litros)
        if (self.__quantidadeCombustivel >= litros):
            self.__diminuirQuantidade(litros)
            veiculo.abastecer(litros)
            print("Abastecimento por valor concluído")
        else:
            print("Não há combustivel suficiente na bomba")

    def abastecerPorLitro(self, litros,veiculo):
        if (self.__quantidadeCombustivel >= litros):
            valor = litros * self.__valorLitro
            print("Valor a pagar: %f" % valor)
            '''Diminuir combustivel na bomba'''
            self.__diminuirQuantidade(litros)
            '''Acrescentar combustivel no veiculo'''
            veiculo.abastecer(litros)
            print("Abastecimento por valor concluído")
        else:
            print("Não há combustivel suficiente na bomba")

    def alterarValor(self, novoPreco):
        self.__valorLitro = novoPreco

    def alterarCombustivel(self, tipo):
        self.__tipoCombustivel = tipo

    def alterarQuantidadeCombustivel(self, quantidade):
        self.__quantidadeCombustivel = quantidade

    def getTipoCombustivel(self):
        return self.__tipoCombustivel

    def getquantidadeCombustivel(self):
        return self.__quantidadeCombustivel

    def getValorLitro(self):
        return self.__valorLitro
    #método privado
    def __diminuirQuantidade(self, quantidade):
        self.__quantidadeCombustivel -= quantidade

    ## Representação formal do objeto (usado para debug)
    def __repr__(self):
        return "Bomba de Combustivel, tipo: %s, quantidade: %d e preço: %f" % (self.__tipoCombustivel, self.__quantidadeCombustivel, self.__valorLitro)

    '''***Sobrecarga de operadores***
    - __str__ é um método especial, como __init__, 
    usado para retornar uma representação de string de um objeto.'''
    def __str__(self): 
        return "Bomba de %s" % self.__tipoCombustivel

#Classe Veiculo
class Veiculo:
    
    def __init__(self,consumo, tanqueLitrosMax,odometro,marca,tipo):
        self.__tanqueLitrosMax = tanqueLitrosMax
        self.__quantidade_combustivel = tanqueLitrosMax
        self.__consumoPorLitro = consumo
        self.__odometro = odometro
        
        self.marca = marca
        self.tipoCarro = tipo
        
    def abastecer(self,litros):
        self.__quantidade_combustivel += litros

        if self.__quantidade_combustivel >= self.__tanqueLitrosMax:
            self.__quantidade_combustivel = self.__tanqueLitrosMax
            print('Combustivel vazando do tanque')
    
    def acelerar(self,tempo):
        pass

    def freiar(self):
        pass

    def dirigir(self,tempo,velocidade):
        #assumindo km/h e h
        distancia = velocidade * tempo
        #assumindo  km/l
        litrosConsumidos = distancia / self.__consumoPorLitro

        self.__quantidade_combustivel -= litrosConsumidos

        if(self.__quantidade_combustivel <= 0 ):
            self.__quantidade_combustivel = 0
            print('Tanque vazio. Vai levar multa :P')

    def getQuantidadeCombustivel(self):
        return self.__quantidade_combustivel

    '''Fazer sair um som de buzina'''
    def buzinar(self):
        playsound("horn.wav")


# Testes
'''
v1 = Veiculo(8, 35, 90000 ,'Fiat Uno','Passeio')
v1.buzinar()

bomba1 = BombaCombustivel(10000,'Gasolina Aditivada', 7.30 )
v1 = Veiculo(8, 35, 90000 ,'Fiat Uno','Passeio')

bomba1.abastecerPorLitro(10,v1)
print(bomba1.getTipoCombustivel())
print(bomba1.getquantidadeCombustivel())
print(bomba1.getValorLitro())

print('\n Carro dirigindo')
print(v1.getQuantidadeCombustivel())
v1.dirigir(120,1)
print(v1.getQuantidadeCombustivel())

print('\n')
bomba1.abastecerPorValor(100,v1)
print(bomba1.getquantidadeCombustivel())
print(bomba1.getValorLitro())
'''
#print('\nstr:')
#print(bomba1)

#print('\nrepresentaçāo do objeto:')
#print(repr(bomba1))