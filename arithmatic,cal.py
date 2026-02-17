'''ps-1.write a py script to make a calculator where four arithmetic operations 
(+,-,%,/) are implemented through functions for each operation'''

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
def modules(a,b,o):
	result = a%b
	return result
def power(a,b,o):
	result = a**b
	return result
def squareroot(a,b,o):
	result = a**(1/b)
	return result

x = True         # ps-2 to continue a program execution if invalid input is given from the user
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
	elif o=="%":
		mod=modules(a,b,o)
		print(mod)
	elif o=="^":
		power=power(a,b,o)
		print(power)
	elif o=="√":
		sq=squareroot(a,b,o)
		print(sq)
	else:
		print("invalid input")
	
	m=input("Enter Y to continue N to exit")
	if m == "N" or m == "n":
		x = False


'''types of error-
1) one time error
2) compile time error'''							