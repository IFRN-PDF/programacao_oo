from datetime import datetime
from datetime import date
from datetime import timedelta
from calendar import isleap

class Data:

    def __init__(self, dia=None, mes=None, ano=None):
        if dia == None:
            dia = date.today().day
        if mes == None:
            mes = date.today().month
        if ano == None:
            ano = date.today().year

        self.__mes = mes
        self.__dia = dia
        self.__ano = ano

        self.__monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
 
    def __str__(self):
        return '{}/{}/{}'.format(self.__dia,self.__mes,self.__ano)

    def dia_seguinte(self):
        self.__add_dias()

    def ano_bissexto(self):
        if isleap(self.__ano):
            return True
        else:
            return False

    def get_dia(self):
        return self.__dia
    
    def set_dia(self, dia):
        self.__dia = dia

    def get_mes(self):
        return self.__mes

    def set_mes(self, mes):
        self.__mes = mes

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def __add_data(self, other):
        d = self.__dia + other.__dia
        m = self.__mes + other.__mes
        a = self.__ano + other.__ano

        diff_mes = d - self.__monthDays[m-1 if m < 12 else m-12]

        """testando se precisa virar o mes"""
        if diff_mes > 0:
            d = diff_mes
            m += 1
        """testando se precisa virar o ano"""
        if m > 12:
            m -= 12
            a += 1       

        return Data(d,m,a)

    def __add_dias(self, d = None):
        if d == None:
            d = datetime(self.__ano, self.__mes, self.__dia, 0, 0, 0) + timedelta(days=1)
        else:
            d = datetime(self.__ano, self.__mes, self.__dia, 0, 0, 0) + timedelta(days=d)

        self.__dia = d.day
        self.__mes = d.month
        self.__ano = d.year
     
    def __add__(self,other):
        if isinstance(other, Data):
            return self.__add_data(other)
        else:
            return self.__add_dias(other) #inteiro

    def __radd__(self, other):
        return self.__add__(other)

