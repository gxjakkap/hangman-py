import os
import random

from lib.game import Hangman

word = ""

with open(f"{os.path.dirname(os.path.realpath(__file__))}/lib/words.txt") as f:
    l = f.readlines()
    word = l[random.randint(0, len(l) - 1)]
    word = word.strip().lower()

game = Hangman(word)

del word

print("Welcome to Hangman!")
print("Goal: guess a letter (or a word when you're confident) before the man got hang. You got 6 tries.")
print(f"I'm thinking of a word that is {game.wlen} letters long")

game.setBeginTime()

while not game.end:
    if game.wrong == 5:
        game.setEnd()
        break

    if game.slw == 0: game.printHang()
    game.printCws()
    
    if game.checkCurrFinish():
        break

    usrInp = input("guess: ")
    usrInp = usrInp.lower()

    if len(usrInp) < 1 or (not usrInp.isascii()) or (not usrInp.isalpha()):
        print("Invalid Input! Try again.")
        continue

    if game.checkAlreadyExist(usrInp):
        print(f"You already guessed {usrInp}! Try other letters.")
        continue

    if len(usrInp) > 1:
        # guess word
        if game.checkWord(usrInp):
            break
        else:
            print("Not yet!")
            game.wrongIncr()
    else:
        game.checkChar(usrInp)

if not game.end: game.setEnd()

gameTime = game.getPlayTime()

if game.win:
    print(f"You win! the word was indeed {game.word}!")
    print(f"Time used: {gameTime} second{'s' if gameTime > 1 else ''}")
else:
    game.printHang()
    print(f"The word was {game.word}")
    print(f"Time used: {gameTime} second{'s' if gameTime > 1 else ''}")



