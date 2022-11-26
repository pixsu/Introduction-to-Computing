print("Rock, Paper, Scissors")

player1 = input("Enter here: ")
player2 = input("Enter here: ")

if player1.lower()=="paper"and player2.lower() == "scissors":
  print("P2 / Scissors wins")
elif player1.lower()=="paper"and player2.lower()=="rock":
  print("P1 / Paper wins")
elif player1.lower()=="paper"and player2.lower()=="paper":
  print("Draw")
elif player1.upper()=="ROCK"and player2.upper()=="SCISSORS":
  print("P1 / Rock wins")
elif player1.upper()=="ROCK"and player2.upper()=="PAPER":
  print("P2 / Paper wins")
elif player1.upper()=="ROCK"and player2.upper()=="ROCK":
  print("Draw")
elif player1.lower()=="scissors"and player2.lower()=="rock":
  print("P2 / Rock wins")
elif player1.lower()=="scissors"and player2.lower()=="paper":
  print("P1 / Scissors wins")
elif player1.lower()=="scissors"and player2.lower()=="scissors":
  print("Draw")
else:
  print("Invalid Input")
  
  
#to make it not case sensitive
#use "(variable).lower()" if value is in lowercase
#use "(variable).upper()" if value is in uppercase
