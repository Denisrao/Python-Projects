# Define a class for ContactBook
class ContactBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts

    def add_contact(self, name, number):
        """ Add a new contact """
        self.contacts[name] = number
        print(f"Added contact: {name} - {number}")

    def view_contacts(self):
        """ View all contacts """
        if self.contacts:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("No contacts found.")

    def search_contact(self, name):
        """ Search for a contact by name """
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        """ Delete a contact by name """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print(f"Contact '{name}' not found.")

# Function to display menu
def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

# Main function to run the contact book
def main():
    contact_book = ContactBook()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            contact_book.add_contact(name, number)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
