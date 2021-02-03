import random
# game.py

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print(f"You chose: {user_choice}")

#simulating a computer input

options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)
print(f"The computer chose: {computer_choice}")


#determining who won

exit()

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")