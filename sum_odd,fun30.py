#Que-14
def sum_of_odds(n):
	total = 0
	for i in range (n+1):
		if i % 2 != 0:
			total += i
	print("result",total)
n=int(input("enter the values"))
sum_of_odds(n)
