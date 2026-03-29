#Declare an empty list
empty_lst = []

#Declare a list with more than 5 items
lst = ["apple", "banana", "grapes", "mango", "orange"]
print(lst)

#Find the length of your list
print(len(lst))

#Get the first item, the middle item and the last item of the list
first_item = lst[0]
middle_item = lst[2]
third_item = lst[4]

print("First item =",first_item)
print("Middle item =",middle_item)
print("Third item =	",third_item)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = [{"Name":"Mohit","Age":"18","Height":"6","marital status":"single","Address":"Indore"}]
print("Data",mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("IT Companies = ",it_companies)

#Print the number of companies in the list
print("No of companies : ",len(it_companies))

#Print the first, middle and last company

first_company = it_companies[0]
middle_company = it_companies[3]
third_company = it_companies[6]

print("First company =",first_company)
print("Middle company =",middle_company)
print("Third company =	",third_company)

#Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

#Add an IT company to it_companies
it_companies.append("Deloitte")
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(3,"TCS")
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)

#print(it_companies[1].upper()) ("this will capitalise outside the list")
it_companies[1] = it_companies[1].upper()
print(it_companies)

#Join the it_companies with a string '#; '
print("#; ".join(it_companies))

#Check if a certain company exists in the it_companies list.
is_present = "IBM"
print(is_present in it_companies)

#Sort the list using sort() method
it_companies.sort()
print("Sorted list: ",it_companies)

#Reverse the list in descending order using reverse() method

it_companies.reverse()
print("In descending order : ",it_companies)

#Slice out the first 3 companies from the list
first_three = it_companies[0:3]
print("sliced first 3 companies: ",first_three) 

#Slice out the last 3 companies from the list
last_three = it_companies[6:9]
print("sliced last 3 companies : ",last_three) 

#Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies)//2]
print("Scliced the middle company: ",middle_company)

#Remove the first IT company from the list
it_companies.pop(0)   #.pop() remove the given index and if not given removes the last one 
print("Removed first company: ",it_companies)

#Remove the middle IT company or companies from the list
del it_companies[3]
print("removed middle company : ",it_companies)


#Remove the last IT company from the list
it_companies.pop()
print("Without last company : ",it_companies)

#Remove all IT companies from the list
del it_companies[0:6]
print("Empty list = ", it_companies)

#Destroy the IT companies list (# This should give: NameError: name 'fruits' is not defined if the list is deleted)
'''del it_companies
print(it_companies)   
'''

#Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print("front_end + back_end = ",front_end)

#After joining the lists. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

front_end.insert(5,"Python")
front_end.insert(6, "SQL")

full_stack = front_end
print("FULL STACK = ",full_stack)

