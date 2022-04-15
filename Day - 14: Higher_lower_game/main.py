#project - higher lower game
import random
import art
from game_data import data
data_range = len(data) - 1
from replit import clear

#compare followers
def main_game(first_person, second_person):
    """Higher lower game main code"""
    def follower_check(person_1, person_2):
        """check follower count and find higher one"""
        first_count = person_1['follower_count']
        second_count = person_2['follower_count']
        if first_count > second_count:
            return person_1
        elif second_count > first_count:
            return person_2    

    def ans_tracking(user_guess, high_follow):
        """Check winner"""
        if user_guess == high_follow:
            win = True
        else:
            win = False 
        return win

    #display name and from
    print(f"Compare A: {first_person['name']}, {first_person['description']}, from {first_person['country']}")

    print(art.vs)

    print(f"\nAgainst B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")

    #take user input and check
    user_answer = input("\nGuess who has more followers? 'A' or 'B': ").lower()
    if user_answer == 'a':
        user_answer = first_person
    else:
        user_answer = second_person
    higher_count = follower_check(first_person, second_person)

    if ans_tracking(user_answer, higher_count) == True:
        win = True   
    else: 
        win = False
    return win


#correct add 1 - take previous 2nd one and new entry
win = True
score = 0
#randomly select two people from data list
first_person = random.choice(data)
#print(first_person)
while win == True:
    second_person = random.choice(data)
    clear()
    print(art.logo)
    print(f"\nYou Current score is: {score}")
    win = main_game(first_person, second_person)
    if win == True:
        score += 1
        print(f"\nYou guess is correct!")
    else:
        print(f"\nYou guess is wrong!")    
    first_person = second_person
#wrong stop game
