'''
**Programming Task: Email Obfuscation**

You are provided with two files:
	1.File A: A large text file containing various email addresses interspersed within the text.
	2.File B: A file listing specific email addresses that need to be obfuscated.

##Objective:

Your task is to write a Python program that obfuscates all occurrences of the email addresses listed in File B within File A. 
The result should be written to a new file, (File C).
Additionally, you should provide a function to revert the changes in File C back to the original text of File A using an additional storage mechanism if needed.

'''
file1 = open("file_b.txt","r")
fileB = file1.read()
emails = fileB.split("\n")
file1.close()

file2 = open("file_a.txt","r")
fileA = file2.read()


codes = []
count = 1

for line in emails:
	codes.append("CODE" + str(count))
	count = count +1


for index in range(len(emails)):
	email = emails[index]
	code = codes[index]
	if email in fileA:
		fileA = fileA.replace(email, code)
file2.close()


fileC = open("file_c.txt","w")
fileC.write(fileA)
fileC.close()
print("Completed check : file_c.txt")


secret_file = open("secret_code.txt","w")

for index in range(len(emails)):
	email = emails[index]
	code = codes[index]
	secret_file.write(email + "  =  " + code +"\n")

secret_file.close()
print("Completed cheak secret_code.txt")


file3 = open("file_c.txt","r")
obfs_file = file3.read()
file3.close()


reverse_dict = {}

for index in range(len(emails)):
	email = emails[index]
	code = codes[index]
	reverse_dict[code] = email

for code in reverse_dict.keys():
	original_email = reverse_dict[code]
	if code in obfs_file:
		obfs_file = obfs_file.replace(code,original_email)

fileD = open("reversed_file.txt","w")
fileD.write(obfs_file)
fileD.close()

print("Completed : reversed_file.txt ")






