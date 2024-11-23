#Screencast Overview - https://youtu.be/BqPvJ1zR_Fo
#https://www.nytimes.com/games/wordle/index.html 

#https://pypi.org/project/termcolor/

import random
#pip install termcolor
from termcolor import colored 
import os

def evaluate_guess(guess, word):    #guess and word are strings (an array of characters)
    str = ""
    for i in range(5):              # 5 letter word
        if guess[i] == word[i]:     #correct letter in correct space is green
            str += colored(guess[i], "white", "on_green")
        else:                       #correct letter in incorrect space is yellow
            if guess[i] in word:
                str += colored(guess[i], "white", "on_yellow")
            else:
                str += guess[i]
    return str 

def print_guesses(guessed_letters, guessed_words):
    print("-".join(sorted(guessed_letters))) #join method takes a list and converts to a string
    for bad_guesses in guessed_words:
        print(bad_guesses)
    return

guesses = [] #list of potential guesses (collection of about 5000 words)
with open("guesses.txt") as f:
    for line in f:
        guesses.append(line.strip())


#answers contains potential Wordle answers
with open('answers.txt') as f: 
    answers = [line.strip() for line in f] #Create a list

secret_word = random.choice(answers).lower()
attempts = 1
max_attempts = 6
guessed_letters = set() #Sets don't store duplicate values
guessed_words = [] #list contains guessed words

os.system('cls')
print("Welcome to Wordle! Get 6 chances to guess a 5-letter word. " + secret_word)
while attempts <= max_attempts:
    print_guesses(guessed_letters, guessed_words)
    guess = input("Enter Guess: ").lower()
    os.system('cls')
    if not guess in guesses:
        print("Invalid guess. Please enter an English word with 5 letters.")
        continue
    feedback = evaluate_guess(guess, secret_word)
    guessed_words.append(feedback)
    if guess == secret_word:
        break
    for letter in guess:
        guessed_letters.add(letter) #add each of our guessed letters to 'guessed_letters'
    attempts += 1

#We are either out of guesses or our last guess was correct!
print_guesses(guessed_letters, guessed_words)
if attempts > max_attempts:
    print("Game over. The secret word was:", secret_word)
else:
    print("Congratulations! You guessed the word!!")
