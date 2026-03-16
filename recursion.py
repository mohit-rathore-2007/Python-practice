#write a py script to solve an user defined arithmatic equation containing additon, sub, div and multiplication , make recursion function also

def addition(a,b,o):
	result = a+b
	return result
def substraction(a,b,o):
	result = a-b
	return result
def multiplication(a,b,o):
	result = a*b
	return result
def divison(a,b,o):
	result = a/b
	return result

x = True
while x == True:
	a=int(input("enter 1st value:"))
	b=int(input("enter 2nd value:"))
	o=input("enter the operator:")
	if o=="+":
		add=addition(a,b,o)
		print(add)
	elif o=="-":
		sub=substraction(a,b,o)
		print(sub)
	elif o=="*":
		multi=multiplication(a,b,o)
		print(multi)
	elif o=="/":
		div=divison(a,b,o)
		print(div)
	else:
		print("invalid input")
	
	m=input("Enter Y to continue N to exit")
	if m == "N" or m == "n":
		x = False



