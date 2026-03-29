#basics
var_a=[]
print(var_a)
print(type(var_a))

var_a.append("Mohit Rathore")
var_a.append("6260312842")
var_a.append("mohit2007@gmail.com")
var_a.append("18")
var_a.append("60.5 kg")
print(var_a)
#duplicate value
var_a.append("60.5 kg")
print(var_a)

#to add element to a specific
var_a.insert(1,"Indore")
print(var_a)

#for calculating length, Reading a list
for i in range(len(var_a)):
	print(var_a[i])

#another way to use loop (not applicable for range)

var_a=["Mohit,18,Indore,mohit@gmail.com"]
for i in var_a:
	print(i)

#updaing
y = var_a.index("18")
print(y)

var_a[y]="Mohit"
print(var_a)
 



