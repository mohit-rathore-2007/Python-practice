#write a py script to convert a string given in special case 
# Input : sunny  # Output : sUNNy
# Input : Codemos # Output : cODEMOs


"""x = "sunny"
print(x)
for i in x:
	y = x[0::4]
	z = y.upper()

print(z)"""


x = input("Enter string : ")
y = ""

for i in range(len(x)):
	if i == 0 or i == len(x) - 1 : 
		j = x[i]
		j = j.lower()
		y = y + j
	else : 
		j = x[i]
		j = j.upper()
		y = y + j

print("Original value : ",x)
print("Converted Value : ",y)
