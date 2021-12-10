#Codigo adaptado de git@github.com:ifpb/intin-poo.git
from BombaCombustivel import BombaCombustivel as BC
from BombaCombustivel import Veiculo

bomba1 = BC(20, "gasolina", 4.00)
v1 = Veiculo(8, 35, 90000 ,'Fiat Uno','Passeio')

bomba1.alterarValor(20.00)

bomba1.abastecerPorLitro(21,v1)

print(bomba1)
print(repr(bomba1))