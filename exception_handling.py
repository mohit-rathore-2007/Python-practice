def division(a,b):
	try:
		result = a/b
		print(result)
	except ZeroDivisionError:
		print("division should not be zero")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

division(a,b)