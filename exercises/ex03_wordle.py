"""EX03 - Structured Wordle"""
__author__ = "730611114"


"""This function searches for a character in a string."""
def contains_char(secret: str, char: str) -> bool:
    assert len(char) == 1
    idx: int = 0
    while idx < len(secret):
        # This while loop checks each index of guess.
        if secret[idx] == char:
            return True
        idx = idx + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis representing the correctness of guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    idx: int = 0
    while idx < len(guess):
        # This while loop assigns the appropriate emoji to each index of guess.
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX
        else: 
            if contains_char(secret, guess[idx]):
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        idx = idx + 1
    return result

def input_guess(guesslen: int) -> str:
    """prompt the user for a guess of the expected length"""
    guess = input(f"Enter a {guesslen} character word: ")
    while len(guess) != guesslen:
        # This while loop checks to see if the user's guess is the right length and prompts them if it is not.
        guess = input(f"That wasn't {guesslen} chars! Try again: ")
    return guess

def main() -> None:
    """The entry point of the program and main game loop."""
    SECRET: str = "codes"
    turn: int = 1
    while turn <= 6:
        # This while loop checks to see if the user's guess is correct and keeps track of the user's turns.
        guess = input_guess(len(SECRET))
        print(f"=== Turn {turn}/6 ===")
        print(emojified(guess, SECRET))
        if guess == SECRET:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()