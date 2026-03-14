'''n=int(input("enter value of n"))
r=int(input("enter value of r"))
a=1
b=1
for i in range(1,n+1):
	a=a*i
for j in range(1,n-r+1):
	b=b*j
for k in range(1,r+1):
	k=k*r
f=a/(b*r)
print(f)'''


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