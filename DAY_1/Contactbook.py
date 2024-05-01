class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'phone_number': phone_number, 'email': email}
        print(f"Contact '{name}' added successfully!")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' removed successfully!")
        else:
            print(f"Contact '{name}' not found in the contact book.")

    def display_contacts(self):
        print("Contacts:")
        if not self.contacts:
            print("Your contact book is empty!")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}")


def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact\n2. Display Contacts\n3. Remove Contact\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to remove: ")
            contact_book.remove_contact(name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
