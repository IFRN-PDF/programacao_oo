class Autenticavel:
    def autentica(self, senha):
        if self.senha == senha:
            return True
        else:
            return False

class Funcionario:

    def __init__(self, nome, cpf, salario,senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self.senha = senha

    def get_bonificacao(self):
        return self._salario * 0.10     

class Gerente(Funcionario, Autenticavel):

    def __init__(self, nome, cpf, salario, senha,qtd_gerenciaveis):
        super().__init__(nome, cpf, salario,senha)
        self._qtd_gerenciaveis = qtd_gerenciaveis

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000
      
class Diretor(Funcionario, Autenticavel):  
    pass

class Cliente(Autenticavel):   
    def __init__(self,nome, cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

class SistemaInterno:
    def login(self, obj,senha):
        if (hasattr(obj, 'autentica')):
            return obj.autentica(senha)            
        else:
            print('{} não é autenticável'.format(self.__class__.__name__))
            return False
 
 
if __name__ == '__main__':
    
    diretor = Diretor('João', '111111111-11', 3000.0,'1234')
    gerente = Gerente('José', '222222222-22', 5000.0,'1234',4)
    cliente = Cliente('Maria', '333333333-33','1234')
    
    sistema = SistemaInterno()
    print(sistema.login(diretor,'1234'))
    print(sistema.login(gerente,'12354'))
    print(sistema.login(cliente,'12'))