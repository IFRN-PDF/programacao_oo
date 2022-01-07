import abc

class Autenticavel(abc.ABC):
    """Classe abstrata que contém operações de um objeto autenticável.

    As subclasses concretas devem sobrescrever o método autentica
    """
    @abc.abstractmethod
    def m1():
        print()     

    @abc.abstractmethod
    def autentica(self, senha):
        """ Método abstrato que faz verificação da senha.
        Devolve True se a senha confere, e False caso contrário.
        """
class Funcionario:

    def __init__(self, nome, cpf, salario,senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self.senha = senha

    def get_bonificacao(self):
        return self._salario * 0.10     
      
class Diretor(Funcionario):  
    def autentica(self, senha):
        if self.senha == senha:
            return True
        else:
            return False

    def m1(self):
        pass

class SistemaInterno:
    def login(self, obj,senha):
        if (isinstance(obj, Autenticavel)):
            return obj.autentica(senha)            
        else:
            print('{} não é autenticável'.format(self.__class__.__name__))
            return False
 
 
if __name__ == '__main__':

    Autenticavel.register(Diretor)

    d = Diretor('José', '22222222-22', 3000.0,'1234')

    sistema = SistemaInterno()
    print(sistema.login(d,'1234'))