#!/usr/bin/python3
import random
import subprocess
frames = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |    (×_×;） DEAD!
 /|\  |
 / \  |
      |
=========''']
print("""
       (/) 
       (/)
        (/)
       (/)
        (/)
       (/)
       (/))
      (/)(/)
     (/)'`(/)
    (/)    (/)
    (/)    (/)
    (/)    (/)
    (/)    (/)
     (/)  (/)
      (/)(/)
       `""`

    Welcome to hangman, best of luck!
""")
wordlist = ["moose", "bear", "forest", "raccoon", "beaver", "ant", "hive", "wasp", "bee", "animal", "killerwhale", "sea"]

commands = """

Hangman is a guessing game for two or more players.
One player thinks of a word, phrase, or sentence and
the other tries to guess it by suggesting letters
within a certain number of guesses. 

If you enter a letter it will be checked against the original word

otherwise you can enter:

        help : To display this screen
        quit : To leave the game
        word : To see how much you have uncovered

"""
b = 0
q = 0
answer = input("Do you want to play a) Single player (S) or b) Multiplayer (M)")
if answer.lower() == "s":
    secret = random.choice(wordlist)
elif answer.lower() == "m":
    secret = input("What word will be your secret? ")
    subprocess.run('clear')
else:
    print("Not one of the options, was it...")

name = input("What is your username: ")


def word():
    global secret
    global name
    hidden = ""
    if guessed() == False:
            for letter in secret:
                if letter in guessed_letters:
                    hidden += letter
                else:
                    hidden += " ██"
            print(hidden)

def guessed():
    global q
    global secret
    for letter in secret:
        if letter not in guessed_letters:
            return False
    return True
    

    
guessed_letters = []
print(commands)
while b < 7:
    found = False
    command = input(f"{name}/> ")
    if guessed():
        print(f"Well done {name} the word was, '{secret}!'")
        break
    elif command.lower() == "word":
        word()
    elif command.lower() == "help":
        print(commands)
    elif command.lower() == "secret1243":
        print(secret)
    elif command.lower() == "quit":
        print("Bye, bye...")
        break
    else:
        for i in secret:
            if i == command.lower():
                guessed_letters.append(i)
                found = True
                

        if found:
            word()
        else:
            print(frames[b])
            b += 1
            if b == 7:
                print(f"You lose {name} the word was {secret}, time for hanging...")
            else:
                print(f"Not found...")
