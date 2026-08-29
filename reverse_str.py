'''Write a program (using functions!) that asks the user for a long string containing multiple words.
 Print back to the user the same string, except with the words in backwards order. For example, 
 say I type the string: my name is  mohit 
output = mohit name is my  '''


def reverse_string(sentence):

	words = sentence.split()

	rev_string = words[::-1]


	return " ".join(rev_string)

sentence = input("Enter a string ")

print(reverse_string(sentence))  