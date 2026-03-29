#QUESTIONS RELATED TO STRING

#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

str1 = 'Thirty', 'Days', 'Of', 'Python'
result = ' '.join(str1)
print(result)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

str1 = "Coding", "For", "All"
result = " ".join(str1)
print(result)

#3 Print the length of the company string using len() method and print().
company = "coding for all"
print(len(company))

#Change all the characters to uppercase letters
print(company.upper())

#Change all the characters to lowercase letters
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())

print(company.title())

print(company.swapcase()) #Converts all uppercase characters to lowercase and all lowercase characters to uppercase 

#Cut(slice) out the first word of Coding For All string.
word = "Coding For All"
cut = word[:6]
print(cut)
#print(word.strip("Coding"))

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(word.find("Coding"))

#Replace the word coding in the string 'Coding For All' to Python
print(word.replace("Coding","Python"))

#Split the string 'Coding For All' using space as the separator 
print(word.split())

#Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(word.split(", "))

#What is the character at index 0 in the string Coding For All.
print(word[0])

#What is the last index of the string Coding For All.
print(word[-1])

#What character is at index 10 in "Coding For All" string.
print(word[10]) #there is space at index 10

#Create an acronym or an abbreviation for the name 'Python For Everyone'

str_1 = "Python For Everyone"

acronym = str_1[0]+str_1[7]+str_1[11]

print(acronym)

#Use index to determine the position of the first occurrence of C in Coding For All.

print(word.index("C"))

#Use index to determine the position of the first occurrence of F in Coding For All.

print(word.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
word = "Coding For All People"
print(word.rfind("l")) #19

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence
# find and index is used to find first index 
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

#Use rindex to find the position of the last occurrence of the word because in the following sentence
# rfind and rindex is used to find last index 
print(sentence.rfind("because"))

#Slice out the phrase 'because because because' in the following sentence:

sliceing = sentence[31:54]
print(sliceing)

#Does Coding For All' start with a substring Coding?
print(word.startswith("Coding"))

#Does 'Coding For All' end with a substring coding?
print(word.endswith("Coding"))

#The following list contains the names of some of python libraries. Join the list with a hash with space string.
list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = "# ".join(list1)
print(result)

#Use a tab escape sequence to write the following lines
print("Name\tAge\tCity")
print("Mohit\t18\tIndore")


#Use the string formatting method to display the following: (.format method)
'''radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.'''

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square".format(radius, area))



