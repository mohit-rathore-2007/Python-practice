'''upgrade the py script to identify factors of a given number and 
find the prime and composite of it using a function prime'''

def factor(n):
	for i in range(1,n+1):
		if n%i==0:

			for j in range(2,i):
				if i%j==0:
					print("{} is composite factor of {}".format(i,n))
					break
			else:
				print("{} is prime factor of {}".format(i,n))
n=int(input("enter value: "))
factor(n)