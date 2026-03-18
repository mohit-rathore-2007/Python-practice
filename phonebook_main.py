from phonebook import create_contact, display_all_contact, search_contact, update_contact, delete_contact

while True:
    print("=======================")
    print("1. Create contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")

    choice = int(input("Enter your choice : "))

    if choice ==1:
        create_contact()
    elif choice ==2:
        display_all_contact()
    elif choice ==3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()

    else:
        print("Invalid choice")



