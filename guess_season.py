#Que-5
def check_season(m):
	if m=="March" or m=="April" or m=="May":
		print("Spring season")
	elif m =="June" or m=="July" or m=="August":
		print("Summer season")
	elif m == "September" or m=="October" or m== "November":
		print("Autumn season")
	elif m == "December" or m=="January" or m=="February":
		print("Winter season")
	else:
		print("Invalid month name")
m=input("enter the month")		
check_season(m)
