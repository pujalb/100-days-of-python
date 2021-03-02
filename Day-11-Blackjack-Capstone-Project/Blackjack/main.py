############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

from replit import clear
import art
from random import choice

def draw_cards(lst):
    ''' Draws a random card from deck of cards and appends it to lst'''

    # Ace is counted either as 1 or 11 
    # Cards 2 to 10 are evaluated on their face value
    # Cards K, Q, J are counted as 10
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    # Pick a random card using random.choice(seq) function
    card = choice(cards)
    lst.append(card)

def calculate_score(lst):
    ''' Takes in a list of numbers and returns their sum'''
    lst_copy = lst.copy()
    for letter in lst_copy:
        if letter == 'J' or letter == 'Q' or letter == 'K':
            lst_copy[lst_copy.index(letter)] = 10
        elif letter == 'A':
            lst_copy[lst_copy.index(letter)] = 11
    
    if sum(lst_copy) > 21:
        # Replace the value of Ace from 11 to 1
        for _ in range(len(lst)):
            if 11 in lst_copy:
                lst_copy[lst_copy.index(11)] = 1
    return sum(lst_copy)


def print_player_hand(user_cards, computer_cards):
    print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")

def winner(score1, score2):
    if score1 > 21:
        print("\n\tBUST! You went over!")
        print(art.lose)
    elif score2 > 21:
        print("\n\tBUST! Computer went over!")
        print(art.win)
    elif score2 == 21:
        print("\n\tBlackjack! Computer wins!")
        print(art.lose)
    elif score1 == 21:
        print("\n\tBlackjack! You win!")
        print(art.win)
    elif score1 == score2:
        print(art.draw)
    else:
        if score2 > score1:
            print("\n\tComputer wins!")
            print(art.lose)
        else:
            print("\n\tYou win!")
            print(art.win)

def play_game():
    '''Main Function'''    
    
    print(art.logo)

    user = []
    computer = []

    # Draw 2 cards each for the user and the computer
    for _ in range(2):
        draw_cards(user)
        draw_cards(computer)
    
    # Check if after drawing 2 cards computer or user has a blackjack. (Ace + 10 value card)
    if (calculate_score(computer) == 21):        
        print(f"\tComputer scored a perfect hand of {computer} with a score of {calculate_score(computer)}")
        print(f"\tYour final hand: {user}, final score: {calculate_score(user)}")
        print("\tBlackjack! The computer wins")
        print(art.lose)
        return
    elif (calculate_score(user) == 21):
        print(f"\tYou scored a perfect hand of {user} with a score of {calculate_score(user)}")
        print(f"\tComputer's final hand: {computer}, final score: {calculate_score(computer)}")
        print("\tBlackjack! You win")
        print(art.win)
        return

    print_player_hand(user, computer)

    # Let the user draw cards until the sum is less than 21
    while (input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y'):
        draw_cards(user)
        user_score = calculate_score(user)
        if user_score >= 21:
            break
        print_player_hand(user, computer)    
    user_score = calculate_score(user)
    print(f"\tYour final hand: {user}, final score: {user_score}")
    
    # Let the computer draw cards
    computer_score = calculate_score(computer)
    while (computer_score <= 16 and user_score <= 21):
        draw_cards(computer)
        computer_score = calculate_score(computer)
    print(f"\tComputer's final hand: {computer}, final score: {computer_score}")

    winner(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play_game()
    