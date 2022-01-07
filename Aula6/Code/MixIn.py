class Funcionario:

    def __init__(self, nome, cpf, salario,senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self.senha = senha

    def get_bonificacao(self):
        return self._salario * 0.10  

class AutenticavelMixIn:
    def autentica(self, senha):
        # verifica senha
        pass

class AtendimentoMixIn:
    def cadastra_atendimento(self):
        # faz cadastro atendimento
        pass

    def atende_cliente(self):
        # faz atendimento
        pass

class HoraExtraMixIn:

    def calcula_hora_extra(self, horas):
        # calcula horas extras
        pass

class Gerente(Funcionario, AutenticavelMixIn, HoraExtraMixIn):
    pass

class Diretor(Funcionario, AutenticavelMixIn):
    pass

class Cliente(AutenticavelMixIn):
    pass    

class Escriturario(Funcionario, AtendimentoMixIn):
    pass      