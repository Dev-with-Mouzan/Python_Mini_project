contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Phone number: {contacts[name]}")
    else:
        print("Contact not found.")

def list_contacts():
    if not contacts:
        print("Address book is empty.")
    else:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def contact_book():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List All Contacts")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            list_contacts()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    contact_book()
