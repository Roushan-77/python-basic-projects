contacts = [] 

def new_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip().lower()

    if not name:
        print("Name is required. Contact not added.\n")
        return

    while True:
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Phone number is required.")
        elif not phone.isdigit():
            print("Invalid phone number. It should only contain digits.")
        elif any(contact['phone'] == phone for contact in contacts):
            print("This phone number is already in your contacts.")
            return
        else:
            break 

    email = input("Enter email (optional): ").strip()
    address = input("Enter address (optional): ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(f"\nContact for {name} added successfully!\n")




def view_contact():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.\n")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"""{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}""")
        print()


def search_contact():
    print("\n--- Search Contacts ---")
    if not contacts:
        print("No contacts found.\n")
        return
    
    search = input("Please enter the name/contact to search: ").strip().lower()
    
    found = False 
    
    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone'].lower():
            print("\nFound Contact:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
 
    
    if not found:
        print(f"No contact found with the name '{search}'.\n")


def update_contact():
    print("\n--- Update Contact ---")
    if not contacts:
        print("No contacts available to update.\n")
        return

    search = input("Enter the name or phone number of the contact you want to update: ").strip().lower()

    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone'].lower():
            print(f"\nFound Contact:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")

            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            print("4. Address")
            print("5. Update All Fields")

            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 1:
                    new_name = input("Enter new name: ").strip()
                    
                    if any(c['name'].lower() == new_name.lower() and c != contact for c in contacts):
                        print("A contact with this name already exists.\n")
                        return
                    contact['name'] = new_name

                elif choice == 2:
                    new_phone = input("Enter new phone number: ").strip()
                    if any(c['phone'] == new_phone and c != contact for c in contacts):
                        print("A contact with this phone number already exists.\n")
                        return
                    contact['phone'] = new_phone

                elif choice == 3:
                    contact['email'] = input("Enter new email: ").strip()
                elif choice == 4:
                    contact['address'] = input("Enter new address: ").strip()
                elif choice == 5:
                    new_name = input("Enter new name: ").strip()
                    new_phone = input("Enter new phone number: ").strip()
                    if any((c['name'].lower() == new_name.lower() or c['phone'] == new_phone) and c != contact for c in contacts):
                        print("A contact with this name or phone number already exists.\n")
                        return
                    contact['name'] = new_name
                    contact['phone'] = new_phone
                    contact['email'] = input("Enter new email: ").strip()
                    contact['address'] = input("Enter new address: ").strip()
                else:
                    print("Invalid option. Update canceled.\n")
                    return

                print("\nContact updated successfully!\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
            return

    print("No contact found matching your input.\n")



def delete_contact():
    print("\n--- Delete Contact ---")
    if not contacts:
        print("No contacts available to delete.\n")
        return

    search = input("Enter the name or phone number of the contact to delete: ").strip().lower()

    for i, contact in enumerate(contacts):
        if search in contact['name'].lower() or search in contact['phone'].lower():
            print(f"\nFound Contact:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            confirm = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
            if confirm in ('yes', 'y'):
                contacts.pop(i)
                print("Contact deleted successfully!\n")
            else:
                print("Deletion canceled.\n")
            return

    print("No contact found matching your input.\n")


def menu():
    print("welcome to your contact book ")
    print("please select what you want to do")
    print("1. Add new contact")
    print("2. View all contact")
    print("3. search a contact")
    print("4. update the contach")
    print("5. Delete a contact")
    print("6. Exit the app")
    


def main():
    while True:
        menu()
        try:
            user_choice = int(input("Please choose an option from above (1 to 6): "))
            if user_choice == 1:
                new_contact()
            elif user_choice == 2:
                view_contact()
            elif user_choice == 3:
                search_contact()
            elif user_choice == 4:
                update_contact()
            elif user_choice == 5:
                delete_contact()
            elif user_choice == 6:
                print("Exiting the app... Have a nice day!")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


if __name__ == "__main__":
    main()