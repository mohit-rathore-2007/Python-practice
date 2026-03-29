#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {
	"Name":"Rocky",
	"colour":"white",
	"Breed":"Bulldog",
	"legs":4,
	"age":"2 years",
}
print(dog)

'''Create a student dictionary and add first_name, last_name, gender, age, marital status, 
   skills, country, city and address as keys for the dictionary'''

student_dct = {
	"first_name":"Mohit",
	"last_name":"Rathod",
	"gender":"Male",
	"age":"18",
	"marital_status":"single",
	"skills":["JavaScript", "C++", "Html", "Python"],
	"country":"India",
	"city":"Indore",
	"address":"Bhanwarkua"
}
print(student_dct)

#Get the length of the student dictionary
length = len(student_dct)
print("length of the student_dct: ",length)

#Get the value of skills and check the data type, it should be a list
skill_values = student_dct["skills"]
print("skills: ",skill_values)
print("skill values data type: ",type(skill_values))

#Modify the skills values by adding one or two skills
student_dct["skills"].append("React")
print("Added skills: ",student_dct)

#Get the dictionary keys as a list
keys = student_dct.keys()
print("student_dct keys: ",keys)


#Get the dictionary values as a list
values = student_dct.values()
print("student_dct values: ",values)

#Change the dictionary to a list of tuples using items() method
list_of_tuples = student_dct.items()
print("Changed dct to list of tuples:",list_of_tuples)


#Delete one of the items in the dictionary
student_dct.pop("age")                    #popitem() = removes the last item only
print("Removed one item : ",student_dct)


#Delete one of the dictionaries
del student_dct
print(student_dct)



