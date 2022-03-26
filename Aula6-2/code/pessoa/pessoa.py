from sqlite3 import Date


class Pessoa:
    def __init__(self,nome,sexo,data_nasc):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nasc = Date(data_nasc)

class Contrato:
    def __init__(self,salario,fim,inicio):
        self.__nome = salario
        self.__fim = Date(fim)
        self.__inicio = Date(inicio)

class Ator(Pessoa):
    def __init__(self,contrato):
        self.__contrato = contrato

class Aluno(Pessoa):
    pass

class Personagem(Ator):
    pass

class Banco_Contratos:
    contratos = []
    def __init__(self,contrato):
        self.__contrato = contrato
        self.contratos.append(contrato)

p = Pessoa("fulano","M", "2000-11-2")
a = Ator(Contrato(2000,"2022-01-22","2022-10-22"))

c = Contrato(3000,"2022-04-22","2022-12-22")






