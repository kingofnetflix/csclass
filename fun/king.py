import random

class GamblingGame:
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def place_bet(self, amount):
        if amount > self.balance:
            print("You don't have enough balance to place this bet.")
            return False
        self.balance -= amount
        return True

    def play_round(self, bet_amount):
        if not self.place_bet(bet_amount):
            return

        outcome = random.choice(['win', 'lose'])
        if outcome == 'win':
            winnings = bet_amount * 2
            self.balance += winnings
            print(f"You won! Your new balance is: ${self.balance}")
        else:
            print(f"You lost! Your new balance is: ${self.balance}")

    def play_game(self):
        print("Welcome to the Gambling Game!")
        while self.balance > 0:
            print(f"Your current balance is: ${self.balance}")
            try:
                bet_amount = int(input("Enter your bet amount (or 0 to quit): "))
                if bet_amount == 0:
                    break
                self.play_round(bet_amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print(f"Game over! Your final balance is: ${self.balance}")
        self.show_warning()

    def show_warning(self):
        print("\nGambling can be addictive and lead to financial ruin. Always gamble responsibly and be aware of the risks involved.")

if __name__ == "__main__":
    starting_balance = 100  # Starting balance for the player
    game = GamblingGame(starting_balance)
    game.play_game()