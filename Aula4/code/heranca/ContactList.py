class ContactList(list): 

    def search(self, name):
        matching_contacts = [] 
        for contact in self:
            if name in contact.name: 
                matching_contacts.append(contact)
        return matching_contacts

class Contact():
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

c1 = Contact('Fulano da Silva', 'fulano1@dominio.com') 
c2 = Contact('Fulano Sousa', 'fulano2@dominio.com')
c3 = Contact('Ciclano Pereira', 'ciclano3@dominio.com')

contacts_found = Contact.all_contacts.search('Fulano')

print(contacts_found)