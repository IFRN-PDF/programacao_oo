class Contact: 
    all_contacts = []
    def __init__(self, name, email): 
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    '''str para imprimir objeto'''
    def __str__(self):
        return self.name
    
    def print_allcontacts(self):
        for c in Contact.all_contacts:
            print(c)

class Supplier(Contact): 
    def order(self, pedido):
        print("Pedido para '{}': "
            "'{}'".format(self.name, pedido))

c1 = Contact('Filipe', 'filipe@gmail.com')
f1 = Supplier('Amazon', 'amazon@gmail.com')

print(c1.name, c1.email)
print(f1.name, f1.email)

f1.order('Preciso de 2 camisas do palmeiras')

'''Vai gerar erro'''
c1.order('Preciso de 2 camisas do palmeiras')


'''all_contacts é compartilhado por ambos objetos.
Como ele é um atributo de classe, você pode acessá-lo 
diretamente pela classe.'''
print(c1.all_contacts)
print(f1.all_contacts)

c1.print_allcontacts()
#Contact.all_contacts
