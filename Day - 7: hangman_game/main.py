#final hangman project
#import all required modules
import random
import hangman_art
import hangman_words


#get input for type of list
type_of_list = input("What word list would you like? \n-> For Classic Novels - press 'N'\n-> For YA Novels - press 'YA'\n-> For Random Words - press 'W'\nInput:- ").lower()

#get random word from selected list
if type_of_list == 'w':
    word_list = hangman_words.word_list
elif type_of_list == 'n':
    word_list = hangman_words.classic_novel_list    
elif type_of_list == 'ya':
    word_list = hangman_words.ya_novel_list

word = (random.choice(word_list)).lower()
word_length = len(word) 


#print logo
print(f"{hangman_art.logo}\n")

#testing code
#print(word)

#define lives
end_of_game = False
lives = 6

#create blanks 
display = []
blank = "_"
for _ in word:
    if _ == " ":
        display += " "
    else:
        display += blank
print(f"{' '.join(display)}\n")
while not end_of_game:
    
    guess = input("Guess a letter: ").lower() #user input - convert to lower case

    #print logo
    print(f"{hangman_art.logo}\n") 

    #to check if letter already guessed
    if guess in display:
        print(f"You have already guessed {guess}, chose another letter.")
    
    #to check guess in word
    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = guess

    #to check if letter not in chosen word and decrease lives
    if guess not in word:
        print(f"{guess} is not in the word, you lose a life.")
        lives -= 1

    #to display word and lives
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
    
    #end of game
    if lives == 0:
        end_of_game = True
        print(f"The word was {word}")
        print(f"{hangman_art.you_lose}")
    elif blank not in display:
        end_of_game = True
        print(f"{hangman_art.you_win}")    
    
