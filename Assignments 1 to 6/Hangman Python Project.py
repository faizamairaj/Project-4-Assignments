import random

words_list = ["programming", "python", "hangman", "challenge", "code"]

def display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)

def hangman():
    word = random.choice(words_list)  
    guessed_letters = set()
    attempts = 6

    print("-" * 20)
    print("Welcome to Hangman Game")

    while attempts > 0:
        print("-" * 20)
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        print(f"Remaining Attempts: {attempts}")

        guess = input("Enter a Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter! Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good Guess!")
        else:
            print("Wrong Guess!")
            attempts -= 1

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You won!")
            print(f"The word was: {word}")
            break

    else:
        print("You failed!")
        print(f"The word was: {word}")

hangman()
