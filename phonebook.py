# phonebook with CRUD operations 
#to run the program see phonebook_main.py all the functions call and runned in it

data_file = "contacts.txt"

def create_contact():
	print("=============================")
	name = input("Enter Contact Name : ")
	email = input("Enter Contact Email : ")
	phone_number = input("Enter Contact Phone Number : ")
	print("Contact Added Successfully")
	print("=============================")
	file=open(data_file,"a")
	file.write("{},{},{}\n".format(name,email,phone_number))
	file.close()

def readfile():
	file = open(data_file,"r")
	contact_records = file.readlines()
	file.close()
	return contact_records

def display_record(contact_item) :
	print("=============================")
	print("Name  : ",contact_item[0])
	print("Email : ",contact_item[1])
	print("Phone : ",contact_item[2])
	print("=============================")

def display_all_contact():
	contact_records = readfile()
	for contact in contact_records : 
		contact = contact.replace("\n","")
		contact_item = contact.split(",")
		display_record(contact_item)
	
def search_contact():
	contact_records = readfile()
	search_term = input("Enter a valid Search Term : ")

	for contact in contact_records : 
		contact = contact.replace("\n","")
		contact_item = contact.split(",")
		if search_term in contact_item : 
			display_record(contact_item)
			return contact_records,contact_item
			break
	else : 
		print("Contact not found")

def write_records(contact_records) :
	file = open(data_file,"w")
	for i in contact_records :
		file.write(i)
	file.close()

def update_contact():
	contact_records,current_contact = search_contact()
	update_contact = current_contact
	current_contact_entry = "{},{},{}\n".format(current_contact[0],current_contact[1],current_contact[2])
	change_choice = int(input("Press 1 to Change Name\nPress 2 to Change Email\nPress 3 to change Phone\nEnter valid change choice : "))
	if change_choice == 1 : 
		update_contact[0] = input("Enter New Name : ")
	elif change_choice == 2 : 
		update_contact[1] = input("Enter New Email : ")
	elif change_choice == 3 : 
		update_contact[2] = input("Enter New Phone : ")
	else : 
		print("Invalid choice")

	update_contact_entry = "{},{},{}\n".format(update_contact[0],update_contact[1],update_contact[2])
	change_index = contact_records.index(current_contact_entry)
	contact_records[change_index] = update_contact_entry

	write_records(contact_records)
	print("Record Updated Successfully")


def delete_contact():
	contact_records = readfile()

	search_term = input("Enter a valid Search Term: ")
	for contact in contact_records:
		contact_item = contact.replace("\n", "").split(",")
		if search_term in contact_item:
			display_record(contact_item)
			current_contact_entry = "{},{},{}\n".format(contact_item[0], contact_item[1], contact_item[2])
			break
		else:
			print("Contact not found")
		return
	contact_records.remove(current_contact_entry)
	records = write_records(contact_records)
	print("Record Deleted Successfully")
 

