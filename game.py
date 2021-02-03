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

if user_choice == computer_choice:
    print("It is a tie!")
elif user_choice == "rock" and computer_choice == "paper":
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")

print("Thanks for playing. Please play again!")