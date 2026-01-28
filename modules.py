#direct module for factorial
#time execution of the program in second


from math import factorial,ceil,floor
import time
starting_time = time.perf_counter()

n=int(input("Enter Value : "))
result = ceil(factorial(n))
print ("the factorial of {} is {}".format(n,result))

ending_time = time.perf_counter()
print("Total Execution Time : {} second".format(ending_time - starting_time))


print("======================================")


print("by using for loop")

starting_time = time.perf_counter()

n=int(input("enter value"))
fact=1

for i in range(1,n+1):
	fact=fact*i

print("factorial of ",n,"is",fact)
ending_time = time.perf_counter()

print("Total Execution Time : {} second".format(ending_time - starting_time))

print("======================================")


print("by using while loop")

starting_time = time.perf_counter()

n = int(input("Enter the value :"))
fact=1
i=1

while i<=n:
	fact=fact*i
	i=i+1
print("factorial of {} is {} ".format(n,fact))

ending_time = time.perf_counter()
print("Total Execution Time : {} second".format(ending_time - starting_time))
