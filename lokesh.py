import random

# List of predefined words
words = ["python", "hangman", "programming", "developer", "software"]

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_length = len(chosen_word)
display = ["_"] * word_length

# Variables for tracking guesses
incorrect_guesses = 0
max_incorrect_guesses = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")

while incorrect_guesses < max_incorrect_guesses:
    print("\nCurrent word: " + " ".join(display))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You've already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"Good job! '{guess}' is in the word.")
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

    # Check if the word is completely guessed
    if "_" not in display:
        print("\nCongratulations! You've guessed the word: " + chosen_word)
        break
else:
    print("\nGame over! The word was: " + chosen_word)