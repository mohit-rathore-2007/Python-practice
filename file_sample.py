#write py script to calculate factorial of no 1 to 100 


for i in range(1,11):
	result = 1 
	for j in range(1,i+1) : 
		result *= j
	data_entry = "{}! = {}".format(j,result)
	print(data_entry)
	file1 = open("sample.txt","a")
	file1.write(data_entry + "\n" + "\n")
	file1.close()

file2 = open("sample.txt","r")
#data = file2.read()
data = file2.readlines()
file2.close()

print(data)
