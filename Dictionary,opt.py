#CRUD

#Create

var_a = {1: "Mohit",2: "Rohit", 3: "456"}

'''
for i in var_a:
	print(i)     # for keys
	print(var_a[i]) # for values


for j in var_a.values():
	print(j)  #values'''

for m,n in var_a.items():
	print(m) #keys
	print(n)  #values


#update
#adding an item

var_a["Rohit"] = "Mango"
print(var_a)

#change an item (for values only)

var_a[2] = "Naman"
print(var_a)

#Delete (key)
var_a.pop(1)
print(var_a)