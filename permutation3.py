def fact(n):
	result = 1
	for i in range(1,x+1):
		result = result*i
	print(result)
a=int(input("enter a :"))
b=int(input("enter b :"))
fact_a = fact(a)
fact_b = fact(a-b)
fact_c=fact_a/fact_b
print("answer:",fact_c)