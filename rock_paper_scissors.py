import random

# initialize variables
counter = 0
player_win_count = 0
ai_win_count = 0
moves = ['r', 'p', 's']
choices = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
}

# introduction
print 'Welcome to rock, paper, scissors. '
print 'You can enter r for rock, p for paper, or s for scissors.'

while True:
    if counter >= 3:
        break

    # player makes selection
    player_input = raw_input(' Please enter your choice: ')
    if player_input in choices:
        print 'You typed', choices[player_input]
    else:
        print 'That is not one of the choices.'
        continue

    # ai makes selection
    ai_input = random.choice(moves)

    # display ai selection
    print 'I picked', choices[ai_input]

    if player_input == 'r' and ai_input == 's' or player_input == 'p' and ai_input == 'r' or player_input == 's' and ai_input == 'p':
        print 'Good job, you won this round. '
        player_win_count += 1
    elif ai_input == 'r' and player_input == 's' or ai_input == 'p' and player_input == 'r' or ai_input == 's' and player_input == 'p':
        print 'Looks like I won this round. '
        ai_win_count += 1
    elif player_input == ai_input:
        print 'Draw. '

    counter += 1

if player_win_count > ai_win_count:
    print 'YOU WON!!!, Good job!'
elif player_win_count == ai_win_count:
    print 'Draw'
else:
    print ' AI INPUT WINS!!!, Better luck next time.'

print 'Good bye'
