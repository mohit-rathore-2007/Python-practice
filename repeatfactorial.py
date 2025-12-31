n=int(input("enter value"))
fact=1
for i in range(n,0,-1):
	fact=fact*i
	print(fact)
	print("factorial of ",n,"=",fact)


'''n= int(input("Enter the value"))

if n * 3:
	print("Fizz")

elif n * 5:
	print("Buzz")

elif n * 3, n *5:
	print("FIZZBUZZ")

else:
	print("Invalid Input")'''