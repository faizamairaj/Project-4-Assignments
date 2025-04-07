import random

def main():
    secret_number = random.randint(1, 99)
    print("I'm thinking of a number between 1 and 99.")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess < secret_number:
                print("Higher.")
            elif guess > secret_number:
                print("Lower.")
            else:
                print(f"Congratulations! The number was: {secret_number}")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

main()


