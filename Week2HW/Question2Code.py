import random

hand_options = ['rock','paper','scissors']

computer_hand = random.choice(hand_options)
player_hand = input('Please enter either rock, paper, or scissors: ').lower()
while player_hand not in hand_options:
    player_hand = input('Entry not valid. Please re-enter either rock, paper, or scissors: ').lower()
print('Your hand: ',player_hand)
print('Computers hand: ',computer_hand)
if player_hand == 'rock':
    if computer_hand == 'scissors':
        print('You win!')
    elif computer_hand == 'paper':
        print('Computer beats you!')
    else:
        print('It\'s a tie!')

if player_hand == 'paper':
    if computer_hand == 'scissors':
        print('Computer beats you!')
    elif computer_hand == 'paper':
        print('It\'s a tie!')
    else:
        print('You win!')

if player_hand == 'scissors':
    if computer_hand == 'scissors':
        print('It\'s a tie!')
    elif computer_hand == 'paper':
        print('You win!')
    else:
        print('Computer beats you!')


