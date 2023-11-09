# white a minigame of rock paper scissors

import random

win_count = 0

while True:
    # get user input
    user_action = input("Enter a choice (rock, paper, scissors): ")
    #make user input lowercase
    user_action = user_action.lower()

    #check if user input is valid
    if user_action not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        continue
    
    #computer choice
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    #determine winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            win_count += 1

        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            win_count += 1

        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            win_count += 1

        else:
            print("Rock smashes scissors! You lose.")

    #ask user if they want to play again
    play_again = input("Play again? (y/n): ")

    if play_again.lower() != "y":

        print(f"You won {win_count} times!")
        break

    