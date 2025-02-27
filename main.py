import random
import time

print("# Welcome to the Ultimate Guess the Number Game! 🎉\n")

while True:
    # Select difficulty level
    print("Select difficulty level:\n1. Easy (1-10)\n2. Medium (1-50)\n3. Hard (1-100)")
    difficulty = input("Enter 1, 2, or 3: ")

    if difficulty == "1":
        max_number = 10
    elif difficulty == "2":
        max_number = 50
    elif difficulty == "3":
        max_number = 100
    else:
        print("Invalid choice! Please select 1, 2, or 3.\n")
        continue  # Restart difficulty selection

    a = random.randint(1, max_number)  # Generate the random number
    attempts = 0  # Track number of guesses
    start_time = time.time()  # Start timer

    while True:
        b = input(f"Enter a number between 1 and {max_number}: ")

        if not b.isdigit():
            print("Invalid input! Please enter a valid number.\n")
            continue

        b = int(b)
        attempts += 1  # Increment attempts

        if b > a:
            print("Too high!")
        elif b < a:
            print("Too low!")
        else:  # Correct guess
            end_time = time.time()  # Stop timer
            time_taken = round(end_time - start_time, 2)

            print(f"Correct! You guessed the number in {attempts} attempts and {time_taken} seconds.\n")
            break  # Exit the guessing loop
        
        # Hint system: If guess is close (within 3 numbers)
        if abs(b - a) <= 3:
            print("You're very close!")

    while True:
        x = input("Do you want to play again? (yes/no): ").strip().lower()
        if x == "no":
            print("\nThanks for playing! Goodbye!")
            exit()  # Exit the game
        elif x == "yes":
            print("\nStarting a new game...\n")
            break  # Restart the game
        else:
            print('Invalid choice! Please type "yes" or "no".\n')
