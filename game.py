# game.py

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

x = input("Please choose either 'rock', 'paper', or 'scissors':")

#print(x)
#print("You chose: ", x, "another string", "something else", x)
print("You chose:", x)

#string concat
#print("You chose: " + "other string here")
print("You chose: " + x)

#  string interpolation / format string usage
print(f"You chose: {x}")

#simulating a computer input

exit()

print("The computer chose: 'paper'")


#determining who won

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")