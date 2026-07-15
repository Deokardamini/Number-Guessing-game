import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number
secret_number = random.randint(1, 100)

# Count the number of attempts
attempts = 0

while True:
    try:
        # Take user input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("📉 Too low! Try again.\n")

        elif guess > secret_number:
            print("📈 Too high! Try again.\n")

        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number}.")
            print(f"You took {attempts} attempt(s).")
            break

    except ValueError:
        print("❌ Please enter a valid number.")
