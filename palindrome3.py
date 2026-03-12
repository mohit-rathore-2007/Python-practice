#write a py script to convert a sentence in each word capital letter
'''x=input("Enter a Sentence")
y=""

z=x.split()
for i in range(len(x)):
	if i == 0 or i == len(x) -1:
		j = x[i]
		j = j[0].upper()
		y = y+j
	else :
		j = x[i]
		j = j[0:].lower()
		y = y+j
print(y)'''


"""org_sent = input("Enter a Sentence : ")
con_sent = ""

temp = org_sent.split(" ")
for i in temp : 
	temp_word = ""
	for j in range(len(i)):
		if j == 0 :
			first = i[j]
			temp_word = temp_word + first.upper()
		else : 
			temp_word = temp_word + i[j].lower()

	if con_sent == "" : 
		con_sent = temp_word
	else : 
		con_sent = con_sent + " " + temp_word

print("Original Sentence :{} ".format(org_sent))
print("Converted Sentence :{} ".format(con_sent))"""


original_string = input("Enter a Sentence : ")
converted_string = ""
word = ""

for i in range(len(original_string)):
	if i == 0 or word == "" : 
		word = word + original_string[i].upper()
	elif word != "" and original_string[i] == " " :
		if converted_string == "":
			converted_string = word
		else : 
			converted_string = converted_string + " " + word
		word = ""
	else : 
		word = word + original_string[i].lower()

converted_string = converted_string + " " + word 

print("Original Sentence :{} ".format(original_string))
print("Converted Sentence :{} ".format(converted_string))



