print("Hello brave knight! I am your spiritual guide, Hecate. After great struggle, you have finally reached the Lost Island of Pluto. However, the real quest begins now! As you follow the path ahead, you will come across many challenges. Every right choice will bring you one step closer to the treasure you seek. But, beware! one wrong choice could lead to your ultimate demise! Good luck! \n")
choice1 = input("Your journay begins at the crossroads! Which way do you want to go, left, right or straight?\n").lower()
if choice1 == 'left' or choice1 == 'l':  #through the forest of jewels
  print("Looks like you have entered the forest of jewels that belongs to the evil witch Hera! Continue walking down the path.\n")
  choice2 = input("Oh, look! There is the legendary tree of invincibility! It is said that if you can succesfully pluck a diamond from that tree unnoticed, you become invincible and cannot be defeated by anyone. However, stealth is of utmost importance! If you are caught by Hera, she will place a curse on you and turn you into her minion! Do you wish to pluck the diamond?\n").lower()
  if choice2 == 'yes' or choice2 == 'y':
    print("\nAlas, Your greed has cost you your life! You were cursed by Hera and now must spend eternity serving her.\n")
    ahead = False
  elif choice2 == 'no' or choice2 == 'n':
    print("A wise decision! It is prudent to let sleeping snakes be. Speaking of snakes, looks like you have reached the giant rattlesnake's lair")
    choice3 = input("Do you want to Fight it?\n").lower()
    if choice3 == 'yes' or choice2 == 'y':
      print("Turns out you weren't strong enough to take down the rattlesnake. You are dead!")
      ahead = False
    elif choice3 == 'no' or choice2 == 'n':
      print("The rattlesnake doesn't think of you as much of a threat, continue forward!")
      ahead = True  
  golden_shield = False    
  if ahead == False:
    won = False

if choice1 == 'straight' or choice1 == 's': #through the troll bridge
  print("You have reached the troll bridge! If you have been keeping up to date with the legends, you would know that now your wisdom is to be tested by the grumpy old troll. Solve the puzzle correctly and you will be allowed passage!\n")
  choice2 = int(input("If you buy a rooster for the purpose of laying eggs and you expect to get three eggs each day for breakfast, how many eggs will you have after three weeks?\n"))
  if choice2 == 0:
    print("That is the right answer! You certainly know your way around riddles. Continue forward!")
    ahead = True
  else:
    print("Turns out you weren't smart enough to answer the puzzle. Roosters are males, they don't lay eggs! But fear not, you do have your sward and your fighting skills! ")
    choice3 = input("Do you want to fight the troll?\n").lower()
    if choice3 == 'y' or choice3 == 'yes':
      print("You won! Turns out trolls aren't as scary as they are said to be, this one ran away at the sight of your sword! Continue forward!")
      ahead = True
    elif choice3 == 'n' or choice3 == 'no':
      print("Unfortunately, you couldn't cross the troll bridge to reach the treasure!")  
      ahead = False
  golden_shield = False  
  if ahead == False:
    won = False

if choice1 == 'right' or choice1 == 'r': #reached the river of misery
  print("Behold! You have arrived at the shore of the River of Misery, where the souls of the worst criminals are tormented for eternity. Anyone who swims through the river is reminded of all their pain and misery until they lose their will and drown! However, if you look over the horizon, you can see a vessel coming towards you. ")
  choice2 = input("Do you want to wait for the boat or swim across the river yourself? ").lower()
  if choice2 == 'wait' or choice2 == 'wait for boat' or choice2 == 'boat' or choice2 == 'w' or choice2 == 'b' or choice2 == 'wait for the boat':
    print("\nAlas! the vessel was owned by the infamour pirate, Captain Cook! You are now his prisioner! They have taken your sword and all your resources, and are planning to feed you to their monstorous pet alligators. Now is the opportunity to fight back! ")
    choice3 = input("Do you want to fight the pirates?\n").lower()
    if choice3 == 'y' or choice3 == 'yes':
      print("Without your sword, you were no match to the fleet of criminals in the vessel! You died fighting like a brave knight!")
      ahead = False
    else:
      print("The pirates went ahead with their plan and you became alligator fooder!")
      ahead = False
  elif choice2 == 'swim' or choice2 == 's':
    print("As you hit the freezing water of the river, your ears start ringing with the shrieks of the dead in pain. You try to swim forward with all your might, but are almost about to give up, when you come across a magnificent golden shield floating unharmed on the surface of the river. You climb up on the shield and row your way safely to the shore! You are now closer to your destination and have a fancy new shield which might help you ahead! Continue forward! \n")
    ahead = True
    golden_shield = True
  if ahead != True:
    won = False  

#final quest - through the great hill of pluto!
if ahead == True:
  print("\nGreat job, Brave knight! You intelligence and perseverance has now led you to the gates of the Great hill of Pluto, home of the treasure you seek and the three-headed dog, Cebrus, who guards it. You once again stand at the crossroads. On you right is a white corridor dressed with banners and royal motifs, while on your left is a makeshift tunnel which looks like it might fall on itself any minute now. ")
  final_choice1 = input("Which path will you take, Right or left? \n").lower()
  if final_choice1 == 'right' or final_choice1 == 'r':
    print("You have now reached the final door, behind which lies the treasure. Before that door stands the beloved pet of Pluto, his three-headed dog Cebrus, guarding the door! There is no hope in fighting him, but you can try and distract him. One option would be to use your golden shield as a frisbee, but you may have to get innovative if you don't have one. ")
    final_choice2 = input("Would you like to distract Cebrus?\n").lower()
    if final_choice2 == 'no' or final_choice2 == 'n':
      print("Unfortunately, you could not reach the treasure and came back like a sore loser.")
      won = False
    elif final_choice2 == 'yes' or final_choice2 == 'y':
      if golden_shield == True:
        won = True
      else:
        print("You tried to do a silly dance for Cebrus to distract him. Needless to say, he did not appreciate your wonderful dance skills and killed you!\n")
        won = False    
  elif final_choice1 == 'left' or final_choice1 == 'l':
    print("You walk through the tunnel carefully, and reach the end! Turns out it was a secret passageway to the treasure. You have reached the treasure without alerting Cebrus!\n")  
    won = True

if won == True:
  print("Congrats! You have found the treasure! Now just take it back through the path you came and you will go back a legendary, and most importantly, a wealthy knight!")
else:
  print("You lost! Start over!")  
