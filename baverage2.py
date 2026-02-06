"""write a py script to select baverage on the basis of temp. where conditions are as follws:
    if tewp is less than 20 then i will have hot coffee
    if temp is btw 20-30  will have tea 
    if temp is 30-40n will have cold cofee  
    if temp is more than 40 will have icelollis"""

x=float(input("enter the value of temp"))
if x<=20:
	print(" have hot coffee")
elif x>20 and x<=30:
	print("have tea")
elif x>30 and x<=40:
	print("have cold coffee")
elif x>=40:
	print("hve icelollies")