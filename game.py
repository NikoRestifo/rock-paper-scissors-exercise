#game.py

import random
import os
from dotenv import load_dotenv

#
# setting up environment vars:
#

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file.

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable

#code that performs the desired functionality:

print("-------------------")
print(f"Welcome {PLAYER_NAME} to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#create a list of options for the computer

options = ['rock', 'paper', 'scissors']

#validate the user selection
#stop the program (not try to determine the winner)
#... if the user choice is invalid
#determining who won

if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
    exit()
print(f"You chose: {user_choice}")

#simulating a computer input

computer_choice = random.choice(options)
print(f"The computer chose: {computer_choice}")

#if statement determining who the winner is

if user_choice == computer_choice:
    print("It is a tie!")
elif user_choice == "rock" and computer_choice == "paper":
    print("The computer won. Better luck next time!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You beat the computer. Congratulations!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("The computer won. Better luck next time!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You beat the computer. Congratulations!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("The computer won. Better luck next time!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You beat the computer. Congratulations!")

#print statement that concludes the program

print("Thanks for playing. Please play again!")