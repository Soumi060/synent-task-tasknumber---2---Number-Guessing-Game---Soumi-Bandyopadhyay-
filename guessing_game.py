# Number Guessing Game (CLI)
# Beginner Friendly Python Project

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    try:
        # Take user input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess > secret_number:
            print("📈 Too high! Try again.")

        elif guess < secret_number:
            print("📉 Too low! Try again.")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the correct number: {secret_number}")
            print(f"Total attempts: {attempts}")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
