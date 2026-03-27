'''write a py script to convert a given string of multiple words in capitalise each word form
without using upper and lower pre defined functions 

'''

string = "mohit rathod"

result= ""

for i in range(len(string)):
	if i == 0 and "a" <= string[i] <= "z":
		result+= chr(ord(string[i])-32)

print(result)


