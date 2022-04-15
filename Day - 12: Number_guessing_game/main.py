#project - number guessing game
import random
import art

#choose a random number
def choose_number():
    return random.randint(1,100)

#select level - define attempts
def levels():
    level = input("Choose a difficulty: 'Easy' or 'Hard': ").lower()
    if level == 'easy':
        attempts = 10
    elif level == 'hard':
        attempts = 5
    return attempts

#user input
def number_guess_game():
    #greeting
    print(f"{art.logo}\nWelcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\n")
    number = choose_number()
    attempts = levels()
    for a in range (attempts):
        guess = int(input(f"You have {attempts} attempts left to guess the number.\nMake a guess: "))
        #check if less or greater - give reply
        if guess == number:
            print(f"You got it!")
            return
        else: 
            #repeat and decrease lives accordingly
            attempts -= 1   
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
    print(f"{number} is the correct answer.")

number_guess_game()      

