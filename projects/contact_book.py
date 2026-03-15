# Contact Book
class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, contact):
        self.contacts[contact.name.lower()] = contact

    def find(self, name):
        return self.contacts.get(name.lower())

    def delete(self, name):
        return self.contacts.pop(name.lower(), None)

    def list_all(self):
        for c in sorted(self.contacts.values(), key=lambda x: x.name):
            print(c)

book = ContactBook()
book.add(Contact("Habtamu", "+251911000000", "habtamu@example.com"))
book.add(Contact("Alice",   "+1234567890",   "alice@example.com"))
book.add(Contact("Bob",     "+0987654321"))
book.list_all()
print("\nSearch:", book.find("alice"))
