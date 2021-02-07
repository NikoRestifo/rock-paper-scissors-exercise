import random
# game.py

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")



options = ['rock', 'paper', 'scissors']

if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
    exit()
print(f"You chose: {user_choice}")


#simulating a computer input


computer_choice = random.choice(options)
print(f"The computer chose: {computer_choice}")

#validate the user selection
#stop the program (not try to determine the winner)
#... if the user choice is invalid
#determining who won

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
elif user_choice == "paper" and computer_choice == "rock":
    print("You beat the computer. Congratulations!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("The computer won. Better luck next time!")
print("Thanks for playing. Please play again!")