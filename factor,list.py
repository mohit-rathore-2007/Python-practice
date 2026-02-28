#2 to store various factor of a user defined number in a list
n=int(input("enter value: "))
factor_list=[]

for i in range(2,n):
	if n%i==0:
		factor_list.append(i)
		print(factor_list)
