"""EX01 - Chardle - A cute step toward Wordle"""
__author__ = "730611114"

match_count = 0
instances = "instances"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)

if character == word[0]:
    print(character + " found at index 0")
    match_count = match_count + 1
if character == word[1]:
    print(character + " found at index 1")
    match_count = match_count + 1
if character == word[2]:
    print(character + " found at index 2")
    match_count = match_count + 1
if character == word[3]:
    print(character + " found at index 3")
    match_count = match_count + 1
if character == word[4]:
    print(character + " found at index 4")
    match_count = match_count + 1

if match_count == 0:
    match_count = "No"
if match_count == 1:
    instances = "instance"

print (str(match_count) + " " + instances + " of " + character + " found in " + word)
                        
