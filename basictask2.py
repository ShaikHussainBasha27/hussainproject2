"""A fun guessing game with computer hints for added excitement."""
import random

def guessing_game():
    print("May I ask you for your name?")
    name = input("Name: ")
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")

    while True:
        number_to_guess = random.randint(1, 200)
        attempts = 0
        guessed_correctly = False

        print("Go ahead. Guess!")

        while attempts < 10 and not guessed_correctly:
            guess = input("Guess: ")

            # Allow the user to exit the game
            if guess.lower() == 'exit':
                print("Thanks for playing! Goodbye!")
                return

            # Convert the guess to an integer
            try:
                guess = int(guess)
            except ValueError:
                print("Please enter a valid number.")
                continue

            # Increment the attempt counter
            attempts += 1

            # Provide hints and check if the guess is correct
            if guess < number_to_guess:
                print("The guess of the number that you have entered is too low")
                print("Try Again!")
            elif guess > number_to_guess:
                print("The guess of the number that you have entered is too high")
                print("Try Again!")
            else:
                guessed_correctly = True
                print(f"Congratulations {name}! You've guessed the number in {attempts} attempts.")

        if not guessed_correctly:
            print(f"Nope. The number I was thinking of was {number_to_guess}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
if _name_ == "_main_":
    guessing_game()