import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Initialize the number of attempts
attempts = 0

# Start the game loop
while True:
    # Get user's guess
    guess = int(input("Take a guess: "))

    # Increase the number of attempts
    attempts += 1

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

print("Thank you for playing Guess the Number!")
