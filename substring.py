#write a py script to replace multiple exictence of user given substring in a universal string
paragraph=input("Type your Paragraph :")
replacing_word=input("Type the word you want to replace :")
replaced_word=input("Type the word you want to replace with :")

z=paragraph.split()
word=""

for i in range(len(word)):
	if word[i] == replacing_word:
		print()