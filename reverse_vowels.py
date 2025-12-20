#to reverse the input string

var_a = input("Enter string : ")
var_a= var_a.split()
reverse = []
for i in var_a:
	temp = ""
	for j in range(len(i)-1,-1,-1):
		temp = temp + i[j]
	reverse.append(temp)	#add the word at reverse list
temp_2 = ""
for j in range(len(reverse)):  # to correct - hello world = world hello prblm
	temp_2 = temp_2 + reverse[j]
	if j != len(reverse)-1:  #for space btw words
		temp_2 = temp_2 + " "
print(temp_2)
