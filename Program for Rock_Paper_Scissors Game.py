#Program for Rock_Paper_Scissors Game
    
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "User"
    else:
        return "Computer"

# Score Tracking
user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    user_choice = input("\nChoose rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user_choice == "exit":
        print("\nFinal Scores:")
        print(f"User: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "Tie":
        print("It's a tie!")
    elif result == "User":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Current Score - You: {user_score} | Computer: {computer_score}")