'''Practice Problem: Write a program to find the largest and smallest digit within a given integer 
(e.g., in 75869, the largest is 9 and the smallest is 5'''


num = 75869

digits = []

for d in str(num):
	digits.append(int(d))

largest = digits[0]
smallest = digits[0]

for i in digits:
	if i > largest:
		largest = i

	if i < smallest:
		smallest = i

print("largest", largest)
print("Smallest", smallest)
