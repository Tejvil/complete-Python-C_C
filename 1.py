import random

# Function to get user and computer choices
def get_choices():
    # Ask user for input
    player_choice = input("Enter your choice (rock // paper // scissors): ").lower()
    
    # Define valid options
    options = ["rock", "paper", "scissors"]
    
    # Validate user input
    while player_choice not in options:
        print("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")
        player_choice = input("Enter your choice (rock // paper // scissors): ").lower()
    
    # Generate computer choice randomly
    computer_choice = random.choice(options)
    
    # Store choices in a dictionary
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# Function to check who wins
def check_win(player, computer):
    # Print user and computer choices
    print(f"You chose {player}, and computer chose {computer}")
    
    # Compare choices and determine the winner
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"

# Get choices from user and computer
choices = get_choices()

# Determine the result
result = check_win(choices["player"], choices["computer"])

# Print the result
print(result)
