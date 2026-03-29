#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
	return a+b
result = add_two_numbers(5,7)
print(result)



'''Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
Write a function which converts °C to °F, convert_celsius_to-fahrenheit.'''
c =float(input("Enter Temperature in celsius : "))
def celcius_to_fahrenheit(c):
	f = (c*9/5) + 32
	print("result: ",f)
celcius_to_fahrenheit(c)

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer
def check_season():
