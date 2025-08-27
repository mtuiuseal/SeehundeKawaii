# 1. Guess The Number Game:
# -we will generate a random number with the help of randint() function from 1 to 100 and ask the user to guess it.
# -After every guess, the user will be told if the number is above or below the randomly generated number.
# -The user will win if they guess the number maximum five attempts.
# -Ask the user to stop or continue playing again.
# ***
# Add another situations like:
# level of game (hard (guess 3 times), medium (6 times), easy (10 times)
# assume that you have 100$, each game you spent 5$. Play game until you choose stop, report the game you win/lost and amount you have.
import random

def play_game(difficulty, money):
    if difficulty == "hard":
        max_attempts = 3
    elif difficulty == "medium":
        max_attempts = 6
    else:
        max_attempts = 10

    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"\nYou have {max_attempts} attempts to guess the number between 1 and 100.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts + 1} attempts!")
            return True

        attempts += 1

    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
    return False

def main():
    money = 100
    games_played = 0
    games_won = 0

    print("Welcome to the Guess The Number Game!")
    print("You start with $100. Each game costs $5 to play.")

    while money >= 5:
        print(f"\nCurrent balance: ${money}")
        play_again = input("Would you like to play a game? (y/n): ").lower( )

        if play_again not in ['yes', 'y', 'ýe']:
            break

        money -= 5
        games_played += 1

        print("\nSelect difficulty:")
        print("1. Easy (10 attempts)")
        print("2. Medium (6 attempts)")
        print("3. Hard (3 attempts)")

        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice in [1, 2, 3]:
                    break
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Please enter a valid number.")

        if choice == 1:
            difficulty = "easy"
        elif choice == 2:
            difficulty = "medium"
        else:
            difficulty = "hard"

        won = play_game(difficulty, money)

        if won:
            games_won += 1
            money += 10
            print("You won $10!")
        else:
            print("Better luck next time!")

    print("\n" + "=" * 40)
    print("GAME OVER")
    print("=" * 40)
    print(f"Games played: {games_played}")
    print(f"Games won: {games_won}")
    print(f"Games lost: {games_played - games_won}")
    print(f"Final balance: ${money}")

    if games_played > 0:
        win_percentage = (games_won / games_played) * 100
        print(f"Win percentage: {win_percentage:.1f}%")

if __name__ == "__main__":
    main( )
