#fibonacci series 
 #next number(c) = previous(a) + current(b)
 #previus = current 
 #current = next 


num_terms = int(input("enter how many terms you want to run : "))

a = 0
b = 1

for i in range(num_terms):
	print(a)
	c = a + b
	a = b
	b = c
