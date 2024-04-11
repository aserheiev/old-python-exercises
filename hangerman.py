import random
import string

greeting = "H A N G M A N\n"
keywords = ["python", "java", "swift", "javascript"]
input_prompt = "Input a letter: "
alphabet = set(string.ascii_lowercase)
menu_prompt = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
winrars = 0
losrars = 0

def menu():
    print(menu_prompt)
    choice = input()
    if choice == "play":
        hangerman()
        menu()
    elif choice == "results":
        print(f'You won: {winrars} times')
        print(f'You lost: {losrars} times')
        menu()
    elif choice == "exit":
        pass

def guessing(current_word):
    init_check = False
    while init_check is False:
        print("\n" + current_word)
        print(input_prompt)
        word = input()
        if checks(word) is True:
            init_check == True
            return word

def checks(word):
    if len(word) > 1 or len(word) < 1:
        print("Please, input a single letter.")
        return False
    elif word not in alphabet:
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    else:
        return True

def hangerman():

    global winrars, losrars
    keyword = random.choice(keywords)
    current_word = "-" * len(keyword)
    counter = 0
    guess_set = set()

    while "-" in current_word and counter < 8:
        guess = guessing(current_word)

        if guess in keyword:
            if guess not in guess_set:
                for i in range(len(current_word)):
                    if guess == keyword[i]:
                        current_word = current_word[:i] + guess + current_word[i + 1:]
                guess_set.add(guess)
                print("")
            else:
                print("You've already guessed this letter.\n")
        else:
            if guess in guess_set:
                print("You've already guessed this letter.")
            else:
                print("That letter doesn't appear in the word.\n")
                guess_set.add(guess)
                counter += 1

    if current_word == keyword:
        print(f'You guessed the word {keyword}!')
        print("You survived!")
        winrars += 1
    else:
        print("\nYou lost!")
        losrars += 1

menu()