class ContactList(list): 

    def search(self, name):
        matching_contacts = ContactList() 
        for contact in self:
            if name in contact.name: 
                matching_contacts.append(contact)
        return matching_contacts

    def __str__(self):
        names = ''
        for c in self:
            names = names + c.name + ' , '

        return names


class Contact():
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __str__(self):
        return self.name

c1 = Contact('Fulano da Silva', 'fulano1@dominio.com') 
c2 = Contact('Fulano Sousa', 'fulano2@dominio.com')
c3 = Contact('Ciclano Pereira', 'ciclano3@dominio.com')

contacts_found = Contact.all_contacts.search('Fulano')

print(contacts_found)