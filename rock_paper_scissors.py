import random

player_win_count = 0

ai_win_count = 0


print "Welcome to rock, paper, scissors. "

print "You can enter r for rock, p for paper, or s for scissors."

for i in range (0,3) :
    print i

    # player makes selection
    player_input = raw_input(" Please enter your choice: ")

    # display player selection
    if player_input == "r":
        print "You typed rock."
    elif player_input == "p":
        print "You typed paper."
    elif player_input == "s":
        print "You typed scissors."
    else:
        print "That is not one of the choices."
        exit()



    # ai makes selection
    moves = ["r", "p", "s"]
    ai_input = random.choice(moves)
    print ai_input


    # display ai selection
    if ai_input == "r":
        print "I picked rock."
    elif ai_input == "p":
        print "I picked paper."
    elif ai_input == "s":
        print "I picked scissors."

    if player_input == "r" and ai_input == "s" :
        print "Good job, you won this round."
        player_win_count = player_win_count + 1
    elif player_input == "p" and ai_input == "r" :
        print "Good job, you won this round. "
        player_win_count = player_win_count + 1
    elif player_input == "s" and ai_input == "p" :
        print "Good job, you won this round. "
        player_win_count = player_win_count + 1
    elif ai_input == "r" and player_input == "s" :
        print "Looks like I won this round. "
        ai_win_count = ai_win_count + 1
    elif ai_input == "p" and player_input == "r" :
        print "Looks like I won this round. "
        ai_win_count = ai_win_count + 1
    elif ai_input == "s" and player_input == "p" :
        print "Looks like I won this round. "
        ai_win_count =ai_win_count + 1
    elif player_input == "r" and ai_input == "r" :
        print "Draw. "
    elif player_input == "p" and ai_input == "p" :
        print "Draw. "
    elif player_input == "s" and ai_input == "s" :
        print "Draw. "

if player_win_count > ai_win_count:
    print "YOU WON!!! "
    print "Good job! "
elif player_win_count == ai_win_count :
    print "Draw. "
else:
    print " AI INPUT WINS!!! "
    print "Better luck next time. "

print "game over"


















