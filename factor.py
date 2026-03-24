'''n=int(input("enter value"))
for i in range (2,n+1):
	if n%i==0:
		print(i,"is a factor of",n)
	else:
		print(i,"is not a factor of",n)

for i in range (2,n):
	if n%i==0:
		print("composite")
		break
else:
		print("prime")'''




'''type break to break the command or 
pull else command to dirtectly break the command
means to print prime or composite one time'''


'''n=int(input("enter value"))
for i in range(1,n+1):
	if n%i==0:
		a=i
		for j in range(2,i):
			if a%j==0:
				print(i,"is composite factor of",n)
				break
		else:
			print(i,"is prime factor of",n)'''

n=int(input("enter value"))
for i in range(2,n):
	if n%i==0:
		for j in range(2,i):
			if i%j==0:
				print("{} is composite factor of {}".format(i,n))
				break
		else:
			print("{} is prime factor of {}".format(i,n))





			