#write a program that prints out all the elements of the list that are less than 5 or less than user choice


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

choice = int(input("choose a number: "))

result = []

for num in a:
	if num < choice:
		result.append(num)
print(result)