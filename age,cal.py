'''dob =int(input("enter your date of birth: "))
cd =int(input("enter today's date"))
age = (cd-dob)
print("your age is:", age)'''


def date():
	a=int(input("enter your birth date"))
	return a

def month():
	b=int(input("enter your birth month"))
	return b

def year():
	c=int(input("enter your birth year"))
	return c

def age(c,b,a):
	current_year,current_month,current_date = 2025,8,6  #change the current date before using 
	if current_date < a:
		current_month -= 1
		current_date += 30 
	if current_month < b:
		current_year -= 1
		current_month += 12
	years = (current_year-c)
	month = (current_month-b)
	date = (current_date-a)
	
	print("your current age is",years,"years",month,"month",date,"days")

def main():
	b=month()
	c=year()
	a=date()
	age(c,b,a)

if __name__ == '__main__':
	main()
