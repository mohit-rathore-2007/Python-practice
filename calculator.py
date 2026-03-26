#cal using while loop 
def calculator():
	execution = "yes" or "Yes"
	while execution == True:

		x = int(input("enter 1st digit : "))
		y = int(input("enter 2st digit : "))

		o= input("enter operation to be performed : ")

		if o == "+" :
			print(x+y)
		elif o == "-":
			print(x-y)
		elif o == "*":
			print(x*y)
		elif o == "/":
			print(x/y)

		else:
			print("invalid input")

		execution = input("press yes to continue or no to stop : ")

calculator()





