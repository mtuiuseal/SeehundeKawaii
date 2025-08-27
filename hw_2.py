# 2.Write a game that simulate rolling a pair of dice:
# -If the sum of two faces is greater than 5 “Tài”
# -Otherwise “Xỉu”
# -User ask for guessing “Tài” or “Xỉu”
# -Match the results
# -After one turn, ask user for continue playing game.
# -**** Extend the game by asking the user to enter an amount of money, then continue playing until the user runs out of money or the user stops playing. Statistics of results.
import random

def main():
    print("Welcome to the Tài Xỉu Game!")
    print("Rules:")
    print("- If the sum of two dice is greater than 5: Tài")
    print("- If the sum is 5 or less: Xỉu")
    print("- You'll guess whether the result will be Tài or Xỉu")
    print( )

    while True:
        try:
            money = float(input("Enter the amount of money you want to play with: $"))
            if money <= 0:
                print("Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    initial_money = money
    games_played = 0
    games_won = 0

    while money > 0:
        print(f"\nCurrent balance: ${money:.2f}")

        while True:
            try:
                bet = float(input("Enter your bet amount (or 0 to quit): $"))
                if bet < 0:
                    print("Bet amount cannot be negative.")
                    continue
                if bet > money:
                    print(f"You don't have enough money. Maximum bet: ${money:.2f}")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        if bet == 0:
            break

        while True:
            guess = input("Enter your guess (Tài/Xỉu): ").strip( ).lower( )
            if guess in ['tài', 'tai', 't']:
                guess = 'tài'
                break
            elif guess in ['xỉu', 'xiu', 'x']:
                guess = 'xỉu'
                break
            else:
                print("Please enter either 'Tài' or 'Xỉu'.")

        input("Press Enter to roll the dice...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        result = 'tài' if total > 5 else 'xỉu'

        print(f"\nDice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        print(f"Total: {total} → {result.upper( )}")
        print(f"Your guess: {guess.upper( )}")

        if guess == result:
            print("Congratulations! You won!")
            money += bet
            games_won += 1
        else:
            print("Sorry, you lost this round.")
            money -= bet

        games_played += 1

        if money <= 0:
            print("\nYou've run out of money!")
            break

        continue_playing = input("\nDo you want to play again? (y/n): ").strip( ).lower( )
        if continue_playing not in ['yes', 'y', 'ýe']:
            break

    print("\n" + "=" * 50)
    print("GAME OVER - FINAL STATISTICS")
    print("=" * 50)
    print(f"Initial money: ${initial_money:.2f}")
    print(f"Final money: ${money:.2f}")

    if initial_money > 0:
        profit_loss = money - initial_money
        if profit_loss > 0:
            print(f"Profit: ${profit_loss:.2f} (+{(profit_loss / initial_money) * 100:.1f}%)")
        else:
            print(f"Loss: ${abs(profit_loss):.2f} (-{(abs(profit_loss) / initial_money) * 100:.1f}%)")

    print(f"Games played: {games_played}")
    if games_played > 0:
        print(f"Games won: {games_won} ({(games_won / games_played) * 100:.1f}%)")
        print(f"Games lost: {games_played - games_won} ({((games_played - games_won) / games_played) * 100:.1f}%)")

if __name__ == "__main__":
    main( )
