#3 to make a phone book 

def create_contact():
	name = input("Enter Contact Name : ")
	email = input("Enter Contact Email : ")
	phone_number = input("Enter Contact Phone Number : ")
	print("Contact Added Successfully")
	file1 = open("contactbook.txt","a")
	file1.write("{},{},{}\n".format(name,email,phone_number))
	file1.close()

file2 = open("contactbook.txt","r")
data = file2.readlines()
file2.close()


def display_all_contact():
	file=open("contactbook.txt","r")
	x=file.readlines()
	file.close()
	print(x)


def search_contact():
	search_term = input("Enter a search term : ")
	file = open("contactbook.txt","r")
	x = file.readlines()
	file.close()
	print(x)

'''def update_contact():
	current_contact = search_contact()
	old_contact = current_contact
	change_choice = int(input("Press 1 for updating the name\nPress 2 for updating the email\nPress 3 for updating the Contact No.\nEnter a valid choice : "))
	changed_term = input("Enter Replacing Term : ")
	if change_choice == 1 :--
		current_contact[0] = changed_term
	elif change_choice == 2 :
		current_contact[1] = changed_term
	elif change_choice == 3 :
		current_contact[2] = changed_term
	else :
		print("Invalid Input")
	change_index = master_list.index(old_contact)
	master_list[change_index] = current_contact
	print("Contact Updated Successfuly")
	print(master_list)'''

			
def delete_contact():
	delete_term = search_contact()
	#master_list.remove(delete_term)
	#print(master_list)
	file1 = open("contactbook.txt","a")
	file1.write(name+ "\n")
	file1.write(email+ "\n")
	file1.write(phone_number+ "\n") 
	file1.close()

file2 = open("contactbook.txt","r")
data = file2.readlines()
file2.close()

print("Welcome to My Phonebook")
opt_choice = input("Press 1 for Creating a Contact\nPress 2 for Searching a Contact\nPress 3 for Display all contact\nPress 4 for Updating a Contact\nPress 5 for Deleting a Contact\nEnter a Valid Choice : ")
if opt_choice == "1":
	create_contact()
elif opt_choice == "2":
	search_contact()
elif opt_choice == "3":
	display_all_contact()
elif opt_choice == "4":
	update_contact()
elif opt_choice == "5":
	delete_contact()
else : 
	print("Invalid Choice. Please restart the program") 
















	record_file = "contactbook.txt"

def create_contact():
	print("=============================")
	name = input("Enter Contact Name : ")
	email = input("Enter Contact Email : ")
	phone_number = input("Enter Contact Phone Number : ")
	print("Contact Added Successfully")
	print("=============================")
	file=open(record_file,"a")
	file.write("{},{},{}\n".format(name,email,phone_number))
	file.close()

def display_all_contact():
	file = open(record_file,"r")
	contact_records = file.readlines()
	#print(contact_records)
	file.close()

	for contact in contact_records : 
		#print(contact)
		contact = contact.replace("\n","")
		#print(contact)
		contact_item = contact.split(",")
		#print(contact_item)
		print("=============================")
		print("Name  : ",contact_item[0])
		print("Email : ",contact_item[1])
		print("Phone : ",contact_item[2])
		print("=============================")

		
def search_contact():
	file = open(record_file,"r")
	contact_records = file.readlines()
	file.close()

	search_term = input("Enter a valid Search Term : ")
	for contact in contact_records : 
		contact = contact.replace("\n","")
		contact_item = contact.split(",")
		if search_term in contact_item : 
			print("=============================")
			print("Name  : ",contact_item[0])
			print("Email : ",contact_item[1])
			print("Phone : ",contact_item[2])
			print("=============================")
			break
	else : 
		print("Contact not found")


def update_contact():
	file = open(record_file,"r")
	contact_records = file.readlines()
	file.close()  

	search_term = input("Enter a valid search term")
	change_choice = int(input("Press 1 for updating the name\nPress 2 for updating the email\nPress 3 for updating the Contact No.\nEnter a valid choice : "))





			
def delete_contact():
	pass



def delete_contact():
	delete_term = search_contact()
	#master_list.remove(delete_term)
	#print(master_list)
	file1 = open("contactbook.txt","a")
	file1.write(name+ "\n")
	file1.write(email+ "\n")
	file1.write(phone_number+ "\n") 
	file1.close()

file2 = open("contactbook.txt","r")
data = file2.readlines()
file2.close()


