class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'Phone': phone_number, 'Email': email, 'Address': address}
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

    def search_contact(self, search_term):
        found_contacts = [(name, details) for name, details in self.contacts.items() if
                          search_term.lower() in name.lower() or search_term in details['Phone']]
        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for name, details in found_contacts:
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['Phone'] = new_phone_number
            self.contacts[name]['Email'] = new_email
            self.contacts[name]['Address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter the number corresponding to your choice (1-6): ")

        if choice == "1":
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_manager.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter the name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter the new phone number: ")
            new_email = input("Enter the new email address: ")
            new_address = input("Enter the new address: ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    print("Welcome to Contact Manager!")
    main()
