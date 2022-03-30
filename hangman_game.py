import os
import random
from files.hangman_ascci import man_pics


def valid_game_required(chosen):
    try:
        if chosen.isdigit() is False:
            raise ValueError("Please type a digit")
        return True
    except ValueError as ve:
        os.system("clear")
        print(ve)
        return False


def guess_the_number():
    pass


def checking_user_input_hangman_game(character):
    str(character)
    try:
        if len(character) > 1:
            raise ValueError("Please type just one character")
        if ord(character) < 97 | ord(character) > 122:
            raise ValueError("Characters out of range of [a-z] (only lowercase characters) and numbers are not allowed")
        return True
    except ValueError as ve:
        os.system("clear")
        print(ve)
        return False


def hangman_game():
    user_lives = len(man_pics)-1
    user_word = list()
    string_user_word = str()

    with open("files/data.txt", "r") as f:
        words = [i.rstrip() for i in f]
    random_word_index = random.randint(0, len(words)-1)
    random_word = words[random_word_index]

    for i in range(len(random_word)):
        user_word.append("_")
        string_user_word = string_user_word + "_"
    os.system("clear")
    while True:
        print(man_pics[user_lives])
        print(string_user_word)
        print("You have ", user_lives, "lives")
        matches = False
        character = input("Type a letter to match: ")
        if checking_user_input_hangman_game(character) is False: continue
        os.system("clear")
        for index in range(len(random_word)):
            if character == random_word[index]:
                user_word[index] = random_word[index]
                string_user_word = string_user_word + user_word[index]
                matches = True
        if matches is False:
            user_lives = user_lives - 1
        string_user_word = ""
        for i in range(len(user_word)):
            string_user_word = string_user_word + user_word[i]
        if string_user_word == random_word:
            os.system("clear")
            print(man_pics[user_lives])
            print(string_user_word)
            print("You win!")
            break
        if user_lives == 0:
            os.system("clear")
            print(man_pics[user_lives])
            print("You lose!")
            print("The word is:", random_word)
            break
        os.system("clear")


def run():
    while True:
        game = input("""
         _     _  _______  ___      _______  _______  __   __  _______ 
        | | _ | ||       ||   |    |       ||       ||  |_|  ||       |
        | || || ||    ___||   |    |       ||   _   ||       ||    ___|
        |       ||   |___ |   |    |       ||  | |  ||       ||   |___ 
        |       ||    ___||   |___ |      _||  |_|  ||       ||    ___|
        |   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___ 
        |__| |__||_______||_______||_______||_______||_|   |_||_______|
    
        Select a game (type his number on the prompt):
            1.- The hangman game
            2.- Guess the number
            0.- To exit""")
        if valid_game_required(game) is False: continue
        if int(game) == 0: break
        if int(game) == 1:
            hangman_game()
        elif int(game) == 2:
            guess_the_number()


if __name__ == "__main__":
    run()
