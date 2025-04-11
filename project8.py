#Rock paper scissors game
import random
game_options = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
print("You chose: ", user_choice)

computer_choice = random.randint(0, 2)
print("Computer Chose: ", game_options[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == computer_choice:
    print("its a Tie, try aagain")
else:
    print("You Lose, Womp Womp")