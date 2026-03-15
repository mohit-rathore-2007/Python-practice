# permutation program 
n = int(input("enter value of n"))
r = int(input("enter value of r"))

a = 1
b = 1

for i in range(1, n+1):
	a = a * i

for j in range(1, n-r+1):
	b = b * j

f = a // b
print(f)