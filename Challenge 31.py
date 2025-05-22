import random #Import random to let the computer make random choices
#asking the user their name
playerName= input("What is your name?")
print(f'Welcome to rock paper sissors {playerName}')
#Define the choices
choices = ("rock" , "paper", "sissors")
#Start the game
while True:
#ask the user for their choice
    playerChoice= input("Please enter rock, paper or sissors")
#If the user puts in something different
    if playerChoice not in choices:
        print("That is an invalid choice please type in rock, paper or sissors")
        continue
#The computer makes their choice
    computerChoice = random.choice (choices)
    print(f"The computer chose {computerChoice}")
#Make the outcomes
    if playerChoice==computerChoice:
        print("Its a draw!")
    elif (computerChoice=="rock" and playerChoice=="sissors") or \
         (computerChoice=="paper" and playerChoice=="rock") or \
         (computerChoice=="sissors" and playerChoice=="paper"):
        print("The computer wins!")
    else:
        print(" Congratulations! You won!")