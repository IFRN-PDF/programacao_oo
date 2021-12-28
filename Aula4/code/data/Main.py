from Data import Data

data = Data(20, 7, 2018)
print("Data atual = ",data)
data.dia_seguinte()
print("Dia seguinte = ", data)

data = Data() #hoje
print("Data atual = ", data)
data.dia_seguinte()
print("Dia seguinte = ", data)

data1 = Data(28, 2, 2018)
print("Data fim do mês = ", data1)
data1.dia_seguinte()
print("Dia seguinte = ", data1)

data2 = Data(31, 12, 2018)
print("Data no fim do ano = ",data2)
data2.dia_seguinte()
print("Dia seguinte = ", data2)

print("soma das datas",data1 + data2)
print("soma das datas ",Data(20,10,2020) + Data(15,9,2020))