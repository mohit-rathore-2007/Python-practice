'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old '''

name = input("Enter your name : ")
age = int(input("Enter your age : "))

current_year = 2026 

century_year = 100  

rem_age = century_year - age 


resultend_year = current_year + rem_age


print(name + "You will become 100 years old in :" + str(resultend_year))



'''
clean solution 
name = input("Enter your name : ")
age = int(input("Enter your age : "))

year = 2026 - age + 100

print(name + "You will become 100 years old in :" + str(year))'''