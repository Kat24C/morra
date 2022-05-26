import random


def game_choice():
    """
    Get users choice, numbers 1 and 3.
    """
    while True:
        comp_score = 0
        try:
            user_choice = int(input("Choose a number between 1 and 3: "))
        except ValueError:
            print("Please enter a valid number between 1 and 3")
            user_choice = int(input("Choose a number between 1 and 3: "))
        if user_choice not in {1, 2, 3}:
            print("Please enter a number between 1 and 3:")
        else:
            computer_guess = random.randint(1, 3)
            print(f"The computer guessed: {computer_guess}")
            computer_choosing()
            pc_finalscore(comp_score, user_choice, computer_guess)


def computer_choosing():
    """
    Computer generates a random number between 1 and 3
    User inputs a number guess between 1 and 3
    """
    try:
        user_guess = int(input("Guess the computers number between 1 and 3: "))
    except ValueError:
        print("Please enter a valid number between 1 and 3")
        user_guess = int(input("Guess the computers number between 1 and 3: "))
    if user_guess not in {1, 2, 3}:
        print("Please enter a number between 1 and 3:")
    else:
        computer_choice = random.randint(1, 3)
        print(f"The computer chose: {computer_choice}\n")
        final_score(user_guess, computer_choice)     
            

def final_score(user_guess, computer_choice):
    """
    Compares the user choice and the computers guess.
    """
    player_score = 0
    if user_guess == computer_choice:
        user_score = user_guess + computer_choice
        print(f"Well done, You got {user_score}")
        player_score = player_score + user_score
        print(f"Your total is {player_score}\n")
    else:
        print("Oh dear, try again you got 0")
        print(f"You total is {player_score}\n")
        

def pc_finalscore(comp_score, user_choice, computer_guess):
    """
    Compare the user choice to the computer guess
    """
    if user_choice == computer_guess:
        computer_score = user_choice + computer_guess
        print(f"The computer got {computer_score}")
        comp_score = comp_score + computer_score
        print(f"The computer's total is {comp_score}\n")
    else:
        print("The computer got 0")
        print(f"The computer's total is {comp_score}\n")


def finalgame(player_score, comp_score):
    """
    This will decide if the game continues
    """
    if player_score > 20:
        print("Congratulations you win")
        return False
    elif comp_score > 20:
        print("Sorry the computer won :(")
        return False
    else:
        return True


def game_play():
    """
    Brings the game play together
    """
    game_choice()


game_play()
