class Pessoa:

    #Atributos: nome, idade, peso e altura
    def __init__(self, nome, idade, peso, altura):
        self.__nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.escolaridade= 'nenhuma'
        self.__historico = []
    
    #Por padrão, a cada ano que a pessoa envelhece, 
    #sendo a idade dela menor que 21 anos, ela deve
    #crescer 0,5 cm.
    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.05
        self.idade+=1

    def engordar(self,kilos):
        self.peso += kilos
    
    def emagrecer(self,kilos):
        self.peso -= kilos
    
    def crescer(self,altura):
        self.altura += altura
    
    def get_nome(self):
        return self.__nome

    def set_nome(self,nome):
        self.__nome = nome  
        self.__historico.append(nome)  

    def get_historico(self):
        return self.__historico

#Objeto pessoa
pessoa = Pessoa('Demetrios',21,85,1.75)
print(pessoa.idade)
print(pessoa.altura)
pessoa.envelhecer()
print(pessoa.idade)
print(pessoa.altura)


print(pessoa.get_nome())
pessoa.set_nome('Aluisio')
pessoa.set_nome('Wender')
pessoa.set_nome('Dorneles')
pessoa.set_nome('Isadora')
print(pessoa.get_historico())