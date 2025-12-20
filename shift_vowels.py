#to shift vowels a to e, e to i....

original_string = input("Enter a String: ")
shifted_string = ""


for i in range(len(original_string)):
	word = original_string[i]

	if word =="a":
		shifted_string +="e"
	elif word =="e":
		shifted_string +="i"
	elif word =="i":
		shifted_string +="o"
	elif word =="o":
		shifted_string +="u"
	elif word =="u":
		shifted_string +="a"
	else: 
		shifted_string += word

print("Original: ",original_string)
print("Shifted String: ", shifted_string)






"""
shifted_string +
current_word = 
	original_string = 
	reverse_string =
"""