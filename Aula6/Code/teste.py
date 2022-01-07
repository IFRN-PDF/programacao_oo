class funcionario:
    def aut(self,senha):
        return True

class SistemaInterno:
    def login(self, obj,senha):
        if (hasattr(obj, 'autentica')):
            return obj.autentica(senha)            
        else:
            print('{} não é autenticável'.format(self.__class__.__name__))
            return False


f = funcionario()
sis = SistemaInterno()

print(sis.login(f,'1234'))
