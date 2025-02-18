import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            if guess > number_to_guess:
                print("Too high!")
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("You guessed it right!")
                break
        except ValueError:
            print("Please enter a valid number.")
        
        attempts -= 1

    if attempts == 0:
        print("You lost. Want to play again?")
        play_again = input("Enter Y, YES, y, yes, or ok to play again: ").lower()
        if play_again in ['y', 'yes', 'ok']:
            play_game()

play_game()
