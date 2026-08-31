import random

secret_number = random.randint(1, 10)

print("Guess the number between 1 and 10.")

while True:

    try:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Correct! You guessed the number.")
            break

        elif guess < secret_number:
            print("Too low. Try again.")

        else:
            print("Too high. Try again.")

    except ValueError:
        print("Please enter a valid number.")