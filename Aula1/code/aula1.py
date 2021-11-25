class Cadeira:

    def __init__(self, fabricante, preco, peso, modelo, azimute = 0):
        self.fabricante = fabricante
        self.preco = preco
        self.peso = peso
        self.modelo = modelo
        self.azimute = azimute

    #isso vai girar mais que 360?
    #o que vai acontecer se uma cadeira que nao gira, usar esse metodo?
    def girar(self, grau):
        self.azimute += grau
        self.azimute = (self.azimute % 360)

    

c1 = Cadeira("x",200,100,'mo')

c1.fabricante = 'x'

print(c1)
#c1.girar(180)
#print(c1.azimute)

