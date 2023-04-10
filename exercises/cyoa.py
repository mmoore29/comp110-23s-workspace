"""EX06 - Choose Your Own Adventure."""
__author__ = "730611114"

from random import randint

GREEN_CHECK: str = "\U00002705"
RED_X: str = "\U0000274C"
player: str = ""
points: int


def main() -> None:
    """Main function that greets the player and presents the player with at least three options of where to go next and ask them to choose one."""
    global points
    points = 0
    option: int = 1

    greet()

    while option != 3:
        option = int(input("Would you like to play Coins(1), Die(2), or quit the game(3)? "))
        if option == 1:
            points += coins(points)
        elif option == 2:
            dice()
        elif option == 3:
            print(f"Thanks for playing, {player}!")
        else:
            print("Sorry, that is not an option. Please select either 1, 2, or 3")
        print(f"You currently have {points} total adventure points!")


def greet() -> None:
    """Procedure that greets the player and asks them their name."""
    global player
    print("Hello and welcome to the Gameroom! The goal of the Gameroom is to get as many adventure points as possible.")
    player = input("What is your name? ")


def coins(points: int) -> int:
    """Custom function that chooses a random integer between 1 and 2, asks the user for a guess between 1 and 2, and then awards a point if the guess matches the random integer."""
    print(f"Thanks for choosing to play coins, {player}. I am going to flip a coin, but first you must guess whether the coin will land on heads or tails. If you guess incorrectly you get only 1 adventure point, but if you guess correctly you get 3 adventure points! You get 10 turns to guess as many right as you can!")
    turn: int = 1
    coin: int = 0

    while turn <= 10:
        print(f"Turn {turn}/10.")
        user_guess = int(input("heads(1) or tails(2)? "))
        coin = randint(1, 2)
        if user_guess == coin:
            print(f"{GREEN_CHECK} Correct!")
            points += 3
            turn += 1
        else:
            print(f"{RED_X} Incorect. The correct guess was {coin}.")
            points += 1
            turn += 1
    print("Sorry, you ran out of turns.")
    return points


def dice() -> None:
    """Custom function that chooses a random integer between 1 and 6, asks the user for a guess between 1 and 6, and then awards a point if the guess matches the random integer."""    
    print(f"Thanks for choosing to play Dice, {player}. I am going to roll a six sided die, but first you must guess what number the die will land on. If you guess incorrectly you only get 1 adventure point, but if you guess correctly you get 3 adventure points! You get 10 turns to guess as many right as you can!")
    turn: int = 1
    die: int = 0
    global points 

    while turn <= 10:
        print(f"Turn {turn}/10.")        
        user_guess = int(input("What number will the die land on? "))
        die = randint(1, 6)
        if user_guess == die:
            print(f"{GREEN_CHECK} Correct!")
            points += 3
            turn += 1
        else:
            print(f"{RED_X} Incorrect. The correct guess was {die}.")
            points += 1
            turn += 1
    print("Sorry, you ran out of turns.")


if __name__ == "__main__":
    main()