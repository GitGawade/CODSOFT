class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Store Name: {contact.store_name}, Phone Number: {contact.phone_number}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.store_name == name:
                return contact
        return None

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.store_name == name:
                self.contacts[i] = new_contact
                return True
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.store_name == name:
                del self.contacts[i]
                return True
        return False

manager = ContactManager()

while True:
    print("1: Add contact, 2: View contacts, 3: Search contact, 4: Update contact, 5: Delete contact, 6: Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        store_name = input("Enter store name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(store_name, phone_number, email, address)
        manager.add_contact(contact)
    elif choice == 2:
        manager.view_contacts()
    elif choice == 3:
        name = input("Enter store name to search: ")
        contact = manager.search_contact(name)
        if contact:
            print(f"Store Name: {contact.store_name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("Contact not found")
    elif choice == 4:
        name = input("Enter store name to update: ")
        store_name = input("Enter new store name: ")
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        new_contact = Contact(store_name, phone_number, email, address)
        if manager.update_contact(name, new_contact):
            print("Contact updated successfully")
        else:
            print("Contact not found")
    elif choice == 5:
        name = input("Enter store name to delete: ")
        if manager.delete_contact(name):
            print("Contact deleted successfully")
        else:
            print("Contact not found")
    elif choice == 6:
        break
