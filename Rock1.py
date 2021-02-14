#Rock, Paper, Scissors game
from random import randint      #for random numbers

#Create a list of rock, paper and scissors
items = ['rock', 'paper', 'scissor']

#Assigning value to computer
computer= items[randint(0,2)]

#to get the player input value
player = False

while player == False:
    player = input("rock,paper,scissor ? ")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("You lose!")
        elif computer == "scissors":
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("You win!")
        else:
            print("You win!")
    else:
        print("That\'s not a valid play.")
    player = False      #make player false to continue the loop
    computer= items[randint(0,2)]

    
    
    
    #done game
    
