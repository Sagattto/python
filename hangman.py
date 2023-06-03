import random

# List of words for the game
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry', 'fig', 'grape']

def select_random_word():
    # Select a random word from the list
    return random.choice(words)

def play_hangman():
    # Select a random word
    word = select_random_word()
    
    # Initialize the game state
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print("Guess the word.")
    
    while attempts > 0:
        # Display the current state of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)
        
        # Get user's guess
        guess = input("Enter a letter: ").lower()
        
        # Check for invalid input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        # Add the letter to the guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1
        
        # Check if the word has been completely guessed
        if set(word) == set(guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break
    
    if attempts == 0:
        print("You ran out of attempts. The word was:", word)
    
    print("Thank you for playing Hangman!")

# Start the game
play_hangman()
