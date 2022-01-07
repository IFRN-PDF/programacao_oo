class A:
    def m1(self):
        print('método de A')

class B(A):

    def m1(self):
        super().m1()

    def m2(self):
        print('método de B')

class C(A):
    def m1(self):
        super().m1()

    def m2(self):
        print('método de C')                

class D(B, C):
    def m1(self):
        super().m1()

    def m2(self):
        super().m2()       

if __name__ == '__main__':
    d = D()
    '''Toda classe tem um atributo __mro__ que retorna uma
    lista de referências das superclasses na ordem MRO - da
    classe atual até a classe object'''
    print(D.mro())
    d.m1()
    d.m2()            