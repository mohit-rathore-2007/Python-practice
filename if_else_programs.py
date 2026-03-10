'''#1.WPS to check whether a person is eligible to vote or not based on their age

age = float(input("Enter your age : "))

if age >= 18:
	print("You are eligible for voting")
else:
	print("You are not eligible for voting")



#2.WPS to display the last digit of a number

num = int(input("Enter a number: "))

if num < 10:
	print(num)
else:
	last = num % 10
	print(last)



#3.Write a Python program that takes two numbers as input from the user and prints the larger of the two numbers

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

if num_1 > num_2:
	print("first number is greater than second")
elif num_1 == num_2:
	print("both are equal")
else:
	print("Second number is greater than first")



#4. rock paper scissor game using logical operators

print("Rock-Paper-Scissor Game")

player1 = input("player 1 : ")
player2 = input("player 2 : ")

if player1 == "rock" and player2 == "scissor":
	print("player1 is winner")
elif player1 == "paper" and player2 == "scissor":
	print("player2 is winner")
elif player1 == "scissor" and player2 == "rock":
	print("player2 is winner")
elif player1 == "scissor" and player2 == "paper":
	print("player1 is winner")
elif player1 == "rock" and player2 == "paper":
	print("player2 is winner")
elif player1 == "paper" and player2 == "rock":
	print("player1 is winner")
elif player1 == "rock" and player2 == "rock":
	print("match tied")
elif player1 == "paper" and player2 == "paper":
	print("match tied")
elif player1 == "scissor" and player2 == "scissor":
	print("match tied")
else:
	print("syntax error")

print("game has ended")


#5. WPSto Check if the first and last number of a list is same or not

l = [1, 6, 2, 52, 7, 12, 1, 15, 5]

if l[0] == l[-1]:
	print("first and last number is same")
else:
	print("They are not same")


'''

#factorial program 

'''n = int(input("Enter the value : "))
for i in range(2,n):
	if n % i == 0:
		print(i,"is factor of ",n)

for i in range(2,n):
	if n % i ==0:
		break
else:
	print(n,"is a prime number")'''

#conditions -
	#identify primility of x
	#find factors of x 
	#find primility of factors



n = int(input("Enter the value : "))
for i in range(2,n):
	if n % i == 0:
		break
else:
	print(n,"is a prime number,there is no factorial of",n)


for i in range(2,n):
	if n % i == 0:
		for j in range(2,i):
			if i % j == 0:
				print(i,"is a composite factor of ",n)
				break
		else:
			print(i,"is a prime factor of ",n)  



'''n = int(input("Enter the value "))

while n % i == 0 :
	print(n,"is a prime number,there is no factorial of",n)
'''





