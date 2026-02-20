#Write a py script to display the last digit of a number

num = int(input("Enter a number: "))

if num < 10:
	print(num)
else:
	last = num % 10
	print(last)