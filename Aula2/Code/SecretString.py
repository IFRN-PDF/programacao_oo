class SecretString:
    '''Uma maneira nada segura de armazenar uma string que
    contém um segredo.'''
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase 

    def decrypt(self, pass_phrase):
        '''Só mostra o segredo se o senha estiver certa.'''
        if pass_phrase == self.__pass_phrase: 
            return self.__plain_string
        else:
            return ''

ss = SecretString('O SEGREDO','qwerty')

#sintaxe : objeto._NOMEDACLASSE_NOMEDOTRIBUTO
print(ss._SecretString__plain_string)