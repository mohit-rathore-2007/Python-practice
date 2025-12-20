'''write a py...... calculate avg of n user given integer'''


'''x=float(input("enter the value"))
t=int(input("enter the total numbers")) 
for
avg=(x/t)'''

n=int(input("enter value"))
sum=0
for i in range(n):
	x=int(input("enter value"))
	sum = sum+x
	print("sum",sum)
avg=sum/n
print("avg",avg)