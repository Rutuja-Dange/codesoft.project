def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contacts = {}

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print(f"Contact '{name}' added.")

        elif choice == '2':
            if contacts:
                print("\nContact List:")
                for name, phone in contacts.items():
                    print(f"Name: {name}, Phone: {phone}")
            else:
                print("No contacts available.")

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found = {name: phone for name, phone in contacts.items() if search_term in name or search_term in phone}
            if found:
                print("\nSearch Results:")
                for name, phone in found.items():
                    print(f"Name: {name}, Phone: {phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            if name in contacts:
                phone = input("Enter new phone number: ")
                contacts[name] = phone
                print(f"Contact '{name}' updated.")
            else:
                print("Contact not found.")

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print("Contact not found.")

        elif choice == '6':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
