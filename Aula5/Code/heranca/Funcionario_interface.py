import abc

'''Uma classe abstrata não pode ser instanciada 
e deve conter pelo menos um método abstrato.'''
class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    '''Um método abstrato pode ter implementação, mas 
    não faz sentido em nosso sistema, 
    portanto vamos deixá-lo sem implementação.'''
    @abc.abstractmethod
    def get_bonificacao(self):
        pass 

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

    def get_bonificacao(self):
        return self._salario * 0.15 + 1000

'''Vamos criar a classe Diretor que herda de Fucionario sem o método get_bonificacao():'''
class Diretor:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario   
        
    def get_bonificacao(self):
        return self._salario * 0.5 + 1000           

if __name__ == '__main__':
    #f = Funcionario() #erro

    '''conseguimos instanciar suas filhas que são objetos que 
    realmente existem em nosso sistema (objetos concretos):'''
    gerente = Gerente('jose', '222222222-22', 5000.0, '1234', 0)
    print(gerente.get_bonificacao())
    
    Funcionario.register(Diretor)
    '''Não conseguimos instanciar uma subclasse de Funcionario 
    sem implementar o método abstrato get_bonificacao().'''
    diretor = Diretor('joao', '111111111-11', 4000.0) #erro
    print(isinstance(diretor,Funcionario))
    print(issubclass(Diretor,Funcionario))
    print(diretor.get_bonificacao())
    