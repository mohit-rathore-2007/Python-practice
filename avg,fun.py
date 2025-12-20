# write a py script to calculate avg of "n" user defined integer where the values are user defined.

n=int(input("enter the range of times"))
def average(n):
	sum=0
	for i in range(n):
		x=int(input("enter value"))
		sum = sum+x
		print("sum",sum)
	avg=sum/n
average(n)
