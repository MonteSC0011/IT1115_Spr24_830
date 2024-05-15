# Import random library to use the random.choice function for RPS
import random

# Cut down on some text in body with function for both setting size and hide, and showing
def sizeAndHide(RPS):
    RPS.set_size(0.3)
    RPS.hide()

def moveAndShow(RPS, x):
    RPS.go_to(x, 0)
    RPS.show()

# Declare RPS into an array
choices = ["rock", "paper", "scissors"]
stage.set_background_color("lightsalmon")

# Initialize sprites for both player and computer
computer = codesters.Sprite("dragon",-150,-100)
player = codesters.Sprite("knight1",150,-100)

# Store variable for player's choice for RPS
# Also initialize rock/paper/scissor sprites for use
player_RPS= player.ask("What's your choice? rock, paper, or scissors").lower()
player_rock = codesters.Sprite('rock', 0, 0)
sizeAndHide(player_rock)
player_paper = codesters.Sprite('paper', 0, 0)
sizeAndHide(player_paper)
player_scissors = codesters.Sprite('scissors', 0, 0)
sizeAndHide(player_scissors)

computer_rock = codesters.Sprite('rock', 0, 0)
sizeAndHide(computer_rock)
computer_paper = codesters.Sprite('paper', 0, 0)
sizeAndHide(computer_paper)
computer_scissors = codesters.Sprite('scissors', 0, 0)
sizeAndHide(computer_scissors)

# Do not let user continue until we get a valid input
while player_RPS not in choices:
    player_RPS = player.ask("Not a valid choice... rock, paper, or scissors?").lower()

# # This is where the player sprite would change to their choice, but I opted for a different method
# player.load_image(user_choice)

# Show player's RPS choice next to their sprite, whichever it may be
if player_RPS == 'rock':
    moveAndShow(player_rock, 100)
elif player_RPS == 'paper':
    moveAndShow(player_paper, 100)
elif player_RPS == 'scissors':
    moveAndShow(player_scissors, 100)

# Computer is choosing their RPS choice
comp_RPS = random.choice(choices)
computer.say("I choose...")
stage.wait(1)
computer.say(comp_RPS.title())

# Same functionality as player's RPS except it is near the computer's sprite instead
if comp_RPS == 'rock':
    moveAndShow(computer_rock, -70)
elif comp_RPS == 'paper':
    moveAndShow(computer_paper, -70)
elif comp_RPS == 'scissors':
    moveAndShow(computer_scissors, -70)

# # Iterate for i times, collected from random library imported earlier and load a random RPS for computer
# # I decided to go with a different option without the for loop
# for i in range(random.randint(10,25)):
#     comp_choice = random.choice(choices)
#     computer.load_image(comp_choice)

# Initialize winner element to display the result of RPS between player and computer
winner = codesters.Text("", 0, 150)

# Logic for defining the winner
if player_RPS == comp_RPS:
    winner.set_text("Tie!")
elif player_RPS == 'rock' and comp_RPS == 'scissors' or player_RPS == 'paper' and comp_RPS == 'rock' or player_RPS == 'scissors' and comp_RPS == 'paper':
    winner.set_text("You win!")
else:
    winner.set_text("You lose!")


# ------------  In-Class Section ------------


# # First check if both RPS choices are equal, which is a tie
# if user_choice == comp_choice:
#     winner.set_text("Tie!")


# # If passed tie check, get outcome if player's choice was rock
# elif user_choice == "rock": 
    
#     if comp_choice == "paper":
#         winner.set_text("Computer Wins!")
#     else:
#         winner.set_text("Player Wins!")
    

# # If passed rock check, get outcome if player's choice was paper
# elif user_choice == "paper":
    
#     if comp_choice == "scissors":
#         winner.set_text("Computer Wins!")
#     else:
#         winner.set_text("Player Wins!")
        

# # If none of the previous statements triggered, then the last outcome must be player's choice = scissor
# else:
    
#     if comp_choice == "rock":
#         winner.set_text("Computer Wins!")
#     else:
#         winner.set_text("Player Wins!")



