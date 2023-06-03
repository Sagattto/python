import random

# Define the possible choices
choices = ['rock', 'paper', 'scissors']

print("Welcome to Rock, Paper, Scissors!")
print("Let's play!")

# Start the game loop
while True:
    # Get user's choice
    user_choice = input("Choose your move (rock, paper, scissors): ").lower()

    # Generate computer's choice
    computer_choice = random.choice(choices)

    # Check for valid user input
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Display the choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thank you for playing Rock, Paper, Scissors!")
