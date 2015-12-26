print "Welcome to rock, paper, scissors. "

print "You can enter r for rock, p for paper, or s for scissors."

# player makes selection
player_input = raw_input(" Please enter your choise: ")

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
if player_input == "r":
     ai_input = "p"
elif player_input == "p":
    ai_input = "s"
elif player_input == "s":
    ai_input = "r"


# display ai selection
if ai_input == "r":
    print "I picked rock."
elif ai_input == "p":
    print "I picked paper."
elif ai_input == "s":
    print "I picked scissors."



# show who won. 

#if input == "p":
    #print "You typed paper."

#if input == "s":
    #print "You typed scissors"

#print "1) enter rock paper or scissors: "
#input = raw_input("2)enter rock paper or scissors: ")

print "game over"

#rock = int(raw_input("r"))
#paper = int(raw_input("p"))
#scissors = int(raw_input("s"))
#options = ["Chose:", "rock", "paper", "scissors"]

#for choices in options:
#    print choices










