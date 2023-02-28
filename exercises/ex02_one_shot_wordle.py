"""EX02 - One Guess Wordle."""
__author__ = "730611114"

SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess = input("What is your " + str(len(SECRET)) + "-letter guess? ")
idx: int = 0
result: str = ""

while len(guess) != len(SECRET):
    print("That was not " + str(len(SECRET)) + " letters! Try again: ")
    guess = input("What is your " + str(len(SECRET)) + "-letter guess? ")

while idx < len(guess):
    # This while loop checks each index of guess.
    if guess[idx] == SECRET[idx]:
        # Checks to add a green box.
        result = result + GREEN_BOX
    else:     
        i: int = 0
        while i < len(SECRET):
            # This while loop checks each character of secret.
            if guess[idx] == SECRET[i]:
                # Checks to add a yellow box.
                result = result + YELLOW_BOX
                i = len(SECRET)
            else:
                if i == len(SECRET) - 1:
                    # Checks to add a white box.
                    result = result + WHITE_BOX
            i = i + 1
    idx = idx + 1
print(result)

if guess == SECRET:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon!")