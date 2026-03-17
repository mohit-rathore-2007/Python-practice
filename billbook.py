#Billing system for Tea Stall

master_data = {"Poha" : 10, "Chai" : 6, "Jalebi": 20,"Samosa" : 10}
cart = {}

def select_menu():
	read_menu()
	item = input("Enter Item Name : ")
	if item in master_data : 
		quantity = int(input("Enter Quantity : "))
		price = master_data[item] * quantity
		cart[item] = price # add item


def read_menu() : 
	print("Menu-list")
	print("==================")
	counter = 1 
	for m,n in master_data.items():
		print("{}. {} = {} inr".format(counter,m,n))
		counter+=1
	print("==================")


print("Welcome to Mohit's Kitchen")
item_con = True
while item_con :
	select_menu()
	next_item = input("Enter y to add next item or n to stop : ")
	if next_item == "Y" or next_item == "y" :
		item_con = True
	else : 
		item_con = False

print("Bill Details")
counter = 1
totalamount=0
for x,y in cart.items() : 
	print("{}. {} = {} ".format(counter,x,y))
	counter+= 1
	totalamount=totalamount+y
print("Amount without gst", totalamount)
a=totalamount*(18/100)
cost=a+totalamount
print("TOTAl",cost)

