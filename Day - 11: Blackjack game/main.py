import random
import art

class clear:
 def __call__(self):
  import os
  if os.name==('ce','nt','dos'): os.system('cls')
  elif os.name=='posix': os.system('clear')
  else: print('\n'*120)
 def __neg__(self): self()
 def __repr__(self):
  self();return ''

clear=clear()

#deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def house_rules(rules):
    if rules == 'y':
        print("1. The deck is unlimited in size.\n2. You can draw as many times as you want\n3. The goal is to get the sum of cards close as you can to 21. If you go over 21, you lose.\n4. There are no jokers.\n5. The Jack/Queen/King all count as 10.\n6. The the Ace can count as 11 or 1.\n7. The cards in the list have equal probability of being drawn.\n8. Cards are not removed from the deck as they are drawn.")

#returns a random cards
def deal_cards(cards):
    cards = [random.choice(cards),random.choice(cards)]
    return cards

def ace(input_deck):
    """ Assigns appropraite value to ace"""
    input_score = sum(input_deck)
    if input_score > 21:
        for card in input_deck:
            if card == cards[0]:
                input_score -= 10  
                card = 1            
    return input_score

def blackjack(user_sum,dealer_sum):
    """ Check for blackjack """
    if dealer_sum == 21 and user_sum == 21:
        blackjack = 'draw'
    elif dealer_sum == 21:
        blackjack = 'computer'
        print(f"Dealer's total score = {dealer_sum}\n")
    elif user_sum == 21:
        blackjack = 'user'
        print(f"\nYour total score = {user_sum}")
    else:
        blackjack = 'not'
    return blackjack

def compare_score(user_cards, dealer_cards):
    """ Compare scores to check if closer to 21 """
    user_score = ace(user_cards)
    print(f"\nYour total score = {user_score}")
    dealer_score = ace(dealer_cards)   
    print(f"Dealer's total score = {dealer_score}\n")
    user_diff = 21 - user_score
    dealer_diff = 21 - dealer_score
    if user_diff < 0:
        score = 'computer'
    elif dealer_diff < 0:
        score = 'user'
    else:
        if user_diff > dealer_diff:
            score = 'computer'
        elif user_diff == dealer_diff:
            score = 'draw'
        else:
            score = 'user'
    return score          

def main_game():
    """ main blackjack game """
    clear()
    print(f"{art.logo}\n")
    rules = input("Would you like to read the house rules? 'y' or 'n': ")
    house_rules(rules)
    game = input("\nDo you want to start a game? 'y' or 'n'? ").lower()
    if game == 'y':
        user_cards = deal_cards(cards)
        dealer_cards = deal_cards(cards)
        user_sum = sum(user_cards)
        dealer_sum = sum(dealer_cards)
        # Reveal computer's first card to the user.
        print(f"\nYour cards are: {user_cards}")
        print(f"Dealer's first card: {dealer_cards[0]}")           
        # Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
        is_blackjack = blackjack(user_sum,dealer_sum)
        if is_blackjack != 'not':
            winner = is_blackjack
        else: 
            draw_again = True
            while draw_again == True:
                draw = input("\nDo you want to draw another card? 'y' or 'n': ").lower()
                if draw == 'y' :
                    draw_again = True
                    user_cards.append(random.choice(cards))
                elif draw == 'n':
                    draw_again = False
                print(user_cards)
            
            while dealer_sum < 17:
                dealer_cards.append(random.choice(cards))
                dealer_sum = sum(dealer_cards)
            
            winner = compare_score(user_cards, dealer_cards)

        if winner == 'draw':
            print("\nIt was a draw.")
        elif winner == 'user':
            print(f"Congratulations! You won this round!")
        else:
            print(f"Hard luck! You lost this round!")

        

game_again = 'y'
while game_again == 'y':
    main_game()
    game_again = input("\nWould like to play another round? 'y' or 'n'? ").lower()

