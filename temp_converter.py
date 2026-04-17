#Que-4 temprature converter from celcius to  fahrenheit
c=float(input("enter the temperature in celsius"))
def temp(c):
	f = (c*9/5) + 32
	print("result",f,"°F")
temp(c)