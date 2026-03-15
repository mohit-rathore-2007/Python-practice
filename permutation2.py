#combination program 

def fact(n):
	result = 1
	for i in range(1,n+1):
		result = result*i
	return result
a=int(input("enter a :"))
b=int(input("enter b :"))
result_a = fact(a)
result_b = fact(a-b)
result_c = fact(b)
apb=result_a/(result_b*result_c)
print("{}p{}={}".format(a,b,apb))