# 10/01/2025

import random

options = ["rock", "paper", "scissors"]

play = input("Do you want to play? (Y)es or (N)o ").lower()

while play == "y":
    usr_choice = input("Rock, Paper, Scissors SHOOT! ").lower()
    computer_choice = random.choice(options)
    
    if computer_choice == "scissors" and usr_choice == "paper":
        print(f"You lose! I chose {computer_choice}")
    elif computer_choice == "paper" and usr_choice == "rock":
        print(f"You lose! I chose {computer_choice}")
    elif computer_choice == "rock" and usr_choice == "scissors":
        print(f"You lose! I chose {computer_choice}")
    elif computer_choice == usr_choice:
        print(f"Again! I chose {computer_choice}")
    else:
        print(f"You win! I chose {computer_choice}")
    if computer_choice != usr_choice:
        play = input("Do you want to continue playing? (Y)es or (N)o ").lower()
    
    