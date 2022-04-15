#rock, paper, scissors, lizard, spock
import random
print("RULES:- \n-> Scissors cuts Paper\n-> Paper covers Rock\n-> Rock crushes Lizard\n-> Lizard poisons Spock\n-> Spock smashes Scissors\n-> Scissors decapitates Lizard\n-> Lizard eats Paper\n-> Paper disproves Spock\n-> Spock vaporizes Rock\n-> (and as it always has) Rock crushes Scissors\n")
outcomes = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
user = int(input("Enter 0 for rock, 1 for paper, 2 for scissors, 3 for lizard and 4 for spock.\n"))
print(f"You chose: {outcomes[user]}")
index_outcome = random.randint(0,4)
computer = outcomes[index_outcome]
print(f"Computer chose: {computer}")

if user == 0:
  if index_outcome == 3: #Rock crushes Lizard
    user_win = 1
  elif index_outcome == 2: #Rock crushes Scissors
    user_win = 1
  elif index_outcome == 0: #draw
    user_win = 0  
  else:
    user_win = -1   

if user == 1:
  if index_outcome == 0: #Paper covers Rock
    user_win = 1
  elif index_outcome == 4: #Paper disproves Spock
    user_win = 1
  elif index_outcome == 1: #draw
    user_win = 0   
  else:
    user_win = -1     

if user == 2:
  if index_outcome == 1: #Scissors cuts Paper
    user_win = 1
  elif index_outcome == 3: #Scissors decapitates Lizard
    user_win = 1
  elif index_outcome == 2: #draw
    user_win = 0    
  else:
    user_win = -1 

if user == 3:
  if index_outcome == 4: #Lizard poisons Spock
    user_win = 1
  elif index_outcome == 1: #Lizard eats Paper
    user_win = 1
  elif index_outcome == 3: #draw
    user_win = 0    
  else:
    user_win = -1 

if user == 4:
  if index_outcome == 2: #Spock smashes Scissors
    user_win = 1
  elif index_outcome == 0: #Spock vaporizes Rock
    user_win = 1
  elif index_outcome == 4: #draw
    user_win = 0    
  else:
    user_win = -1

if user_win == 1:
  print("You win!")
elif user_win == -1:
  print("You lose!")  
elif user_win == 0:
  print("It's a draw!")
