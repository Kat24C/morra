import random


def game_choice():
    """
    Get users choice, numbers 1 and 3.
    """
    while True:
        try:
            user_choice = int(input("Choose a number between 1 and 3: "))
        except ValueError:
            print("Please enter a valid number between 1 and 3")
            user_choice = int(input("Choose a number between 1 and 3: "))
        if user_choice not in {1, 2, 3}:
            print("Please enter a number between 1 and 3:")
            user_choice = int(input("Choose a number between 1 and 3: "))
        else:
            computer_guess = random.randint(1, 3)
            print(f"The computer guessed: {computer_guess}")


def computer_choosing():
    """
    Computer generates a random number between 1 and 3
    User inputs a number guess between 1 and 3
    """


def game_play():
    """
    Brings the game play together
    """
    game_choice()
    computer_choosing()


game_play()
