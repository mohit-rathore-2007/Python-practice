continue_check =True
while continue_check:
	i=1
	while i<=3:
		player1=input("player1 ")
		player2=input("player2 ")

		if player1=="rock"and player2=="scissor":
			print("player1 is winner")
		elif player1=="paper"and player2=="scissor":
			print("player2 is winner")
		elif player1=="scissor"and player2=="rock":
			print("player2 is winner")
		elif player1=="scissor"and player2=="paper":
			print("player1 is winner")
		elif player1=="rock"and player2=="paper":
			print("player2 is winner")
		elif player1=="paper"and player2=="rock":
			print("player1 is winner")	
		elif player1=="rock"and player2=="rock":
			print("match tied")
		elif player1=="paper"and player2=="paper":
			print("match tied")
		elif player1=="scissor"and player2=="scissor":
			print("match tied")
		else:
			print("syntax error")
		i+=1
	choice=input("enter Y to play again and N to stop the game:")
	if choice=="Y":
		continue_check= True
		print("lets play again ")
	else:
		continue_check= False
		print("game has ended 	")
