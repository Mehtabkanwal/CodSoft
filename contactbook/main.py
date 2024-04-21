class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, old_name_or_phone, new_contact):
        for i, contact in enumerate(self.contacts):
            if old_name_or_phone.lower() == contact.name.lower() or old_name_or_phone == contact.phone_number:
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name_or_phone):
        for i, contact in enumerate(self.contacts):
            if name_or_phone.lower() == contact.name.lower() or name_or_phone == contact.phone_number:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("\n--- Search Results ---")
                for contact in found_contacts:
                    print(contact)
            else:
                print("No contacts found.")
        elif choice == '4':
            name_or_phone = input("Enter name or phone number of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone_number, new_email, new_address)
            contact_book.update_contact(name_or_phone, new_contact)
        elif choice == '5':
            name_or_phone = input("Enter name or phone number of the contact to delete: ")
            contact_book.delete_contact(name_or_phone)
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
